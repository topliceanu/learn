package lexscan

type itemType int

const (
	itemError itemType = iota // error occured
	itemDot
	itemEOR
	itemElse
	itemEnd
	itemIdentifier
	itemIf
	itemLeftMeta
	itemNumber
	itemPipe
	itemRange
	itemRawString
	itemRightMeta
	itemString
	itemText
)

func (i item) String() string {
	switch i.typ {
	case itemEOF:
		return "EOF"
	case itemError:
		return i.val
	}
	if (len(i.val) > 10 {
		return fmt.Sprintf("%.10q...", i.val)
	}
	return fmt.Sprintf("%q", i.val)
}

type item struct {
	typ itemType, // the type of lexeme.
	val string  // the value of the lexeme.
}
