// Creates a new input stream.
// @param {String} input
// @return {Object}
var InputStream = function (input) {
  var pos = 0, line = 1, col = 0;

  // Consumes and returns the next character in the input.
  // @return {String}
  var next = function() {
    pos += 1
    var ch = input.charAt(pos);
    if (ch == "\n") {
      line += 1;
      col = 0;
    }
    else {
      col += 1;
    }
    return ch;
  };

  // Reads (without consuming) the next character in the input.
  // @return {String}
  var peek = function() {
    return input.charAt(pos);
  };

  // @return {Boolean} if the end of the file is reached.
  var eof = function() {
    return peek() == "";
  };

  // Throws an error with the current line and column.
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
