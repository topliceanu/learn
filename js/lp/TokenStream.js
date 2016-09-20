// The tokenizer or lexer.
// Maintains the same interface as the InputStream, except it does not expose.
// individual characters but tokens.
// Tokens are objects with format {type, value}, where type is one of ["punc", "num", "str", "kw", "var", "op"].
// The big deal is that it treats the input one character at a time, not the whole input at once.
//
// @param {InputStream} input
var TokenStream = function(input) {
  var current = null; // current read token.
  var keywords = " if then else lambda λ true false "; // list of reserved tokens for keywords.

  // @return {Boolean} whether the read token is a reserved keyword.
  var isKeyword = function(token) {
    return keywords.indexOf(" " + token + " ") >= 0;
  };

  // @return {Boolean} whether the read character is a digit.
  var isDigit = function(ch) {
    return /[0-9]/i.test(ch);
  };

  // Identifiers can only start with letters, λ or underscore.
  // @return {Boolean}
  var isIdStart = function(ch) {
    return /[a-zλ_]/i.test(ch);
  };

  // @return {Boolean} whether the caracter can be part of an identifier.
  var isId = function(ch) {
    return isIdStart(ch) || "?!-<>=0123456789".indexOf(ch) >= 0;
  };

  // @return {Boolean} whether character is an operator.
  var isOpChar = function(ch) {
    return "+-*/%=&|<>!".indexOf(ch) >= 0;
  };

  // @return {Boolean} recognizes punctuation marks.
  var isPunc = function(ch) {
    return ",;(){}[]".indexOf(ch) >= 0;
  };

  // @return {Boolean} true for newline, tabs and white-spaces.
  var isWhitespace = function(ch) {
    return " \t\n".indexOf(ch) >= 0;
  };

  // Reads the input stream as long as read characters match the predicate or
  // until EOF is reached.
  // @return {String} returns a token and also consumes it from the input stream.
  var readWhile = function(predicate) {
    var str = "";
    while (!input.eof() && predicate(input.peek()))
      str += input.next();
    return str;
  };

  // Reads a number from the input stream.
  // Numbers are allowed to have one dot.
  var readNumber = function() {
    var has_dot = false;
    var number = readWhile(function(ch){
      if (ch == ".") {
        if (has_dot) return false;
        has_dot = true;
        return true;
      }
      return isDigit(ch);
    });
    return { type: "num", value: parseFloat(number) };
  };

  // Identifiers are either keywords or variables.
  // @return {String} a token representing an identifier.
  var readId = function() {
    var id = readWhile(isId);
    return {
      type  : isKeyword(id) ? "kw" : "var",
      value : id
    };
  };

  // @return {String} returns a string which can have escaped characters.
  var readEscaped = function(end) {
    var escaped = false, str = "";
    input.next();
    while (!input.eof()) {
      var ch = input.next();
      if (escaped) {
        str += ch;
        escaped = false;
      } else if (ch == "\\") {
        escaped = true;
      } else if (ch == end) {
        break;
      } else {
        str += ch;
      }
    }
    return str;
  };

  var read_string = function() {
    return { type: "str", value: readEscaped('"') };
  };
  var skip_comment = function() {
    readWhile(function(ch) {
      return ch != "\n";
    });
    input.next();
  };
  var read_next = function() {
    readWhile(isWhitespace);
    if (input.eof()) return null;
    var ch = input.peek();
    if (ch == "#") {
      skip_comment();
      return read_next();
    }
    if (ch == '"') return read_string();
    if (isDigit(ch)) return readNumber();
    if (isIdStart(ch)) return readId();
    if (isPunc(ch)) return {
      type  : "punc",
      value : input.next()
    };
    if (isOpChar(ch)) return {
      type  : "op",
      value : readWhile(isOpChar)
    };
    input.croak("Can't handle character: " + ch);
  };
  var peek = function() {
    return current || (current = read_next());
  };
  var next = function() {
    var tok = current;
    current = null;
    return tok || read_next();
  };
  var eof = function() {
    return peek() == null;
  };

  return {
    next  : next,
    peek  : peek,
    eof   : eof,
    croak : input.croak
  };
};

