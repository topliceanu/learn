// The input stream.
var InputStream = function (input) {
  var pos = 0, line = 1, col = 0;
  var next = function() {
    var ch = input.charAt(pos++);
    if (ch == "\n") line++, col = 0; else col++;
    return ch;
  };
  var peek = function() {
    return input.charAt(pos);
  };
  var eof = function() {
    return peek() == "";
  };
  var croak = function(msg) {
    throw new Error(msg + " (" + line + ":" + col + ")");
  };
  return {
    next  : next,
    peek  : peek,
    eof   : eof,
    croak : croak,
  };
};

// The tokenizer or lexer.
// Maintains the same interface as the InputStream, except it does not expose.
// individual characters but tokens.
// Tokens are objects with format {type, value}, where type is one of ["punc", "num", "str", "kw", "var", "op"].
// The big deal is that it treats the input one character at a time, not the whole input at once.
var TokenStream = function() {
  var current = null; // current read token.
  var keywords = " if then else lambda λ true false "; // list of reserved tokens for keywords.

  var is_keyword = function(x) {
    return keywords.indexOf(" " + x + " ") >= 0;
  };
  var is_digit = function(ch) {
    return /[0-9]/i.test(ch);
  };
  var is_id_start = function(ch) {
    return /[a-zλ_]/i.test(ch);
  };
  var is_id = function(ch) {
    return is_id_start(ch) || "?!-<>=0123456789".indexOf(ch) >= 0;
  };
  var is_op_char = function(ch) {
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
      return is_digit(ch);
    });
    return { type: "num", value: parseFloat(number) };
  };
  // identifiers are either keywords or variables.
  var read_ident = function() {
    var id = read_while(is_id);
    return {
      type  : is_keyword(id) ? "kw" : "var",
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
    if (is_digit(ch)) return read_number();
    if (is_id_start(ch)) return read_ident();
    if (is_punc(ch)) return {
      type  : "punc",
      value : input.next()
    };
    if (is_op_char(ch)) return {
      type  : "op",
      value : read_while(is_op_char)
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

// The parser. Transforms the token input into an AST.

var FALSE = { type: "bool", value: false };
var PRECEDENCE = {
  "=": 1,
  "||": 2,
  "&&": 3,
  "<": 7, ">": 7, "<=": 7, ">=": 7, "==": 7, "!=": 7,
  "+": 10, "-": 10,
  "*": 20, "/": 20, "%": 20,
};

function parse(input) {
  return parse_toplevel();
  var is_punc = function(ch) {
    var tok = input.peek();
    return tok && tok.type == "punc" && (!ch || tok.value == ch) && tok;
  };
  var is_kw = function(kw) {
    var tok = input.peek();
    return tok && tok.type == "kw" && (!kw || tok.value == kw) && tok;
  };
  var is_op = function(op) {
    var tok = input.peek();
    return tok && tok.type == "op" && (!op || tok.value == op) && tok;
  };
  var skip_punc = function(ch) {
    if (is_punc(ch)) input.next();
    else input.croak("Expecting punctuation: \"" + ch + "\"");
  };
  var skip_kw = function(kw) {
    if (is_kw(kw)) input.next();
    else input.croak("Expecting keyword: \"" + kw + "\"");
  }
  var skip_op = function(op) {
    if (is_op(op)) input.next();
    else input.croak("Expecting operator: \"" + op + "\"");
  }
  var unexpected = function() {
    input.croak("Unexpected token: " + JSON.stringify(input.peek()));
  }
  var maybe_binary = function(left, my_prec) {
    var tok = is_op();
    if (tok) {
      var his_prec = PRECEDENCE[tok.value];
      if (his_prec > my_prec) {
        input.next();
        return maybe_binary({
          type     : tok.value == "=" ? "assign" : "binary",
          operator : tok.value,
          left     : left,
          right    : maybe_binary(parse_atom(), his_prec)
        }, my_prec);
      }
    }
    return left;
  }
  function delimited(start, stop, separator, parser) {
    var a = [], first = true;
    skip_punc(start);
    while (!input.eof()) {
      if (is_punc(stop)) break;
      if (first) first = false; else skip_punc(separator);
      if (is_punc(stop)) break;
      a.push(parser());
    }
    skip_punc(stop);
    return a;
  }
  function parse_call(func) {
    return {
      type: "call",
      func: func,
      args: delimited("(", ")", ",", parse_expression),
    };
  }
  function parse_varname() {
    var name = input.next();
    if (name.type != "var") input.croak("Expecting variable name");
    return name.value;
  }
  function parse_if() {
    skip_kw("if");
    var cond = parse_expression();
    if (!is_punc("{")) skip_kw("then");
    var then = parse_expression();
    var ret = {
      type: "if",
      cond: cond,
      then: then,
    };
    if (is_kw("else")) {
      input.next();
      ret.else = parse_expression();
    }
    return ret;
  }
  function parse_lambda() {
    return {
      type: "lambda",
      vars: delimited("(", ")", ",", parse_varname),
      body: parse_expression()
    };
  }
  function parse_bool() {
    return {
      type  : "bool",
      value : input.next().value == "true"
    };
  }
  function maybe_call(expr) {
    expr = expr();
    return is_punc("(") ? parse_call(expr) : expr;
  }
  function parse_atom() {
    return maybe_call(function(){
      if (is_punc("(")) {
        input.next();
        var exp = parse_expression();
        skip_punc(")");
        return exp;
      }
      if (is_punc("{")) return parse_prog();
      if (is_kw("if")) return parse_if();
      if (is_kw("true") || is_kw("false")) return parse_bool();
      if (is_kw("lambda") || is_kw("λ")) {
        input.next();
        return parse_lambda();
      }
      var tok = input.next();
      if (tok.type == "var" || tok.type == "num" || tok.type == "str")
        return tok;
      unexpected();
    });
  }
  function parse_toplevel() {
    var prog = [];
    while (!input.eof()) {
      prog.push(parse_expression());
      if (!input.eof()) skip_punc(";");
    }
    return { type: "prog", prog: prog };
  }
  function parse_prog() {
    var prog = delimited("{", "}", ";", parse_expression);
    if (prog.length == 0) return FALSE;
    if (prog.length == 1) return prog[0];
    return { type: "prog", prog: prog };
  }
  function parse_expression() {
    return maybe_call(function(){
      return maybe_binary(parse_atom(), 0);
    });
  }
}
