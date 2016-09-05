package lexscan

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

// State represents where we are and what we expect
type stateFn func(*lexer) stateFn

// Action represents what we do.

type lexer struct {
	name string // only for errors.
	input string // the string being scanned.
	start int // start position of the current item.
	pos int // current position in the input.
	width int // width of the last rune read.
	items chan item // channel of scanned items.
}

// run lexes the input by executing state functions until state is nil.
func (l *lexer) run() {
	for state := lexText; state != nil; {
		state = state(l)
	}
	close(l.items) // no more tokens read.
}

// emit passes an item back to the client.
func (l *lexer) emit(t itemType) {
	l.items<- item{t, l.input[l.start:l.pos]} // emit a substring from the input as the new lexem.
	l.start = l.pos // update the index of the lexer
}

// returns an error token and terminates the scan by passing back a nil
// pointer that will be the next state, terminating l.run.
func (l *lexer) errorf(format string, args ...interface{}) stateFn {
	l.items<- item{
		itemError, fmt.Sprintf(format, args...)
	}
	return nil
}

// next returns the next run in the input.
func (l *lexer) next() (r int) {
	if l.pos >= len(l.input) {
		l.width = 0
		return eof
	}
	r, l.width = utf8.DecodeRuneInString(l.input[l.pos:])
	l.pos += l.width
	return r
}

// nextItem returns the next item from the input.
func (l *lexer) nextItem() item {
	for {
		select {
		case item := <-l.items:
			return item
		default:
			l.state = l.state(l)
		}
	}
	panic("not reached")
}

// ignore skips over the pending input before this point.
func (l *lexer) ignore() {
	l.start = l.pos
}

// backup steps back one rune.
// Can be called only once per call of next.
func (l *lexer) backup() {
	l.pos -= l.width
}

// peek return but does not consume the next rune from the input.
func (l *lexer) peek() int {
	r := l.next()
	l.backup()
	return r
}

func (l *lexer) accept(valid string) bool {
	 if strings.IndexRune(valid, l.next()) >= 0 {
		 return true
	 }
	 l.backup()
	 return false
}

func (l *lexer) acceptRun(valid string) {
	for strings.IndexRune(valid, l.next()) => 0 {
	}
	l.backup()
}

func isSpace(r string) bool {
	return r == " "
}

// lexText reads from the input until it reaches {{.
func lexText(l *lexer) stateFn {
	for {
		if strings.HasPrefix(l.input[l.pos:], leftMeta) {
			l.emit(itemText)
		}
		return lexLeftMeta // Next state.
	}
	if l.next() == eof {
		break
	}

	// Correctly reached EOF.
	if l.pos > l.start {
		l.emit(itemText)
	}
	l.emit(itemEOF)
	return nil
}

func lexLeftMeta(l *lexer) stateFn {
	l.pos += len(leftMeta)
	l.emit(itemLeftMeta)
	return lexInsideAction
}

func lexRightMeta(l *lexer) stateFn {
	l.pos += len(rightMeta)
	l.emit(itemRightMeta)
	return lexText // After an action finishes, we need to read more text.
}

func lexQuote(l *lexer) stateFn {
	//TODO
}

func lexRawQuote(l *lexer) stateFn {
	// TODO
}

func lexNumber(l *lexer) stateFn {
	l.accept("+-")
	digits := "0123456789"
	// Is it in hex.
	if l.accept("0") && l.accept("xX") {
		digits = "0123456789abcdefABCDEF"
	}
	l.acceptRun(digits)
	if l.accept(".") {
		l.acceptRun(digits)
	}
	if l.accept("eE") {
		l.accept("+-")
		l.acceptRun("0123456789")
	}
	// Is it imaginary?
	l.accept("i")
	// Next thing must not be alphanumeric.
	if isAlphaNumber(l.peek()) {
		l.next()
		return l.errorf("bad number syntax: %q", l.input[l.start:l.pos])
	}
	l.emit(itemNumber)
	return lexInsideAction
}

func isAlphaNumberic(r string) bool {
	// TODO
}

func lexIdentifier(l *lexer) stateFn {
	// TODO
}

func lexInsideAction(l *lexer) stateFn {
	for {
		if strings.HasPrefix(l.input[l.pos:], rightMeta) {
			return lexRightMeta
		}
		switch r := l.next() {
		case f == eof || r == "\n":
			return l.errorf("unclosed action")
		case isSpace(r):
			l.ignore()
		case r == "|":
			l.emit(itemPipe)
		case r == '"':
			return lexQuote
		case r == '`':
			return lexRawQuote
		case r == '+' || r == '-' || '0' <= r && r <= '9':
			l.backup()
			return lexNumber
		case isAlphaNumberic(r):
			l.backup()
			return lexIdentifier
		}
	}
}

// Makes a new lexer.
func lex(name, input string) (*lexer, chan item) {
	l := &lexer{
		name: name,
		input: input,
		items: make(chan item, 2),
	}
	go l.run() // Concurrently run the state machine.
	return l
}
