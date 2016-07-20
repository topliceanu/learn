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
  var is_punc = function(ch) {
    return ",;(){}[]".indexOf(ch) >= 0;
  };
  var is_whitespace = function(ch) {
    return " \t\n".indexOf(ch) >= 0;
  };
  var read_while = function(predicate) {
    var str = "";
    while (!input.eof() && predicate(input.peek()))
      str += input.next();
    return str;
  };
  // Reads a number from the input stream.
  // Numbers can have only one dot.
  var read_number = function() {
    var has_dot = false;
    var number = read_while(function(ch){
      if (ch == ".") {
        if (has_dot) return false;
        has_dot = true;
        return true;
      }
      return isDigit(ch);
    });
    return { type: "num", value: parseFloat(number) };
  };
  // identifiers are either keywords or variables.
  var read_ident = function() {
    var id = read_while(isId);
    return {
      type  : isKeyword(id) ? "kw" : "var",
      value : id
    };
  };
  var read_escaped = function(end) {
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
    return { type: "str", value: read_escaped('"') };
  };
  var skip_comment = function() {
    read_while(function(ch) {
      return ch != "\n";
    });
    input.next();
  };
  var read_next = function() {
    read_while(is_whitespace);
    if (input.eof()) return null;
    var ch = input.peek();
    if (ch == "#") {
      skip_comment();
      return read_next();
    }
    if (ch == '"') return read_string();
    if (isDigit(ch)) return read_number();
    if (isIdStart(ch)) return read_ident();
    if (is_punc(ch)) return {
      type  : "punc",
      value : input.next()
    };
    if (isOpChar(ch)) return {
      type  : "op",
      value : read_while(isOpChar)
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

