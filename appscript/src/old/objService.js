/**
 * ObjService
 * @author James Ferriera
 * @documentation http://goo.gl/JdEHW
 *
 * Changes an object like e.parameter into a 2D array useful in
 * writting to a spreadsheet with using the .setValues method
 *
 * @param   {Array}   headers    [header, header, ...]
 * @param   {Array}   objValues  [{key:value, ...}, ...]
 * @returns {Array}              [[value, value, ...], ...]
 */
function objectToArray(headers, objValues){
  var values = [];
  var headers = camelArray(headers);
  for (var j=0; j < objValues.length; j++){
    var rowValues = [];
    for (var i=0; i < headers.length; i++){
      rowValues.push(objValues[j][headers[i]]);
    }
    values.push(rowValues);
  }
  return values;
}

/**
 * Changes a range array often returned from .getValues() into an
 * array of objects with key value pairs.
 * The first element in the array is used as the keys (headers)
 *
 * @param   {Array}   range   [[key, key, ...],[value, value, ...]]
 * @returns {Array}           [{key:value, ...}, ...]
 */
function rangeToObjects(range){
  var headers = range[0];
   var values = range;
  var rowObjects = [];
  for (var i = 1; i < values.length; ++i) {
    var row = new Object();
    row.rowNum = i;
    for (var j in headers){
      row[camelString(headers[j])] = values[i][j];
    }
   rowObjects.push(row);
  }
  return rowObjects;
}

/**
 * Changes a range array into an array of objects with key value pairs
 *
 * @params  {array}    headers  [key, key, ...]
 * @params  {array}    values    [[value, value, ...], ...]
 * @returns {array}    [{key:value, ...}, ...]
 */
function splitRangesToObjects(headers, values){
  var rowObjects = [];
  for (var i = 0; i < values.length; ++i) {
    var row = new Object();
    row.rowNum = i;
    for (var j in headers){
      row[camelString(headers[j])] = values[i][j];
    }
   rowObjects.push(row);
  }
  return rowObjects;
}

/**
 * Removes special characters from strings in an array
 * Commonly know as a camelCase,
 * Examples:
 *   "First Name" -> "firstName"
 *   "Market Cap (millions) -> "marketCapMillions
 *   "1 number at the beginning is ignored" -> "numberAtTheBeginningIsIgnored"
 * @params  {array} headers   [string, string, ...]
 * @returns {array}           camelCase
 */
function camelArray(headers) {
  var keys = [];
  for (var i = 0; i < headers.length; ++i) {
    var key = camelString(headers[i]);
    if (key.length > 0) {
      keys.push(key);
    }
  }
  return keys;
}

/**
 * Removes special characters from a string
 * Commonly know as a camelCase,
 * Examples:
 *   "First Name" -> "firstName"
 *   "Market Cap (millions) -> "marketCapMillions
 *   "1 number at the beginning is ignored" -> "numberAtTheBeginningIsIgnored"
 * @params  {string}  header   string
 * @returns {string}           camelCase
 */
function camelString(header) {
  var key = "";
  var upperCase = false;
  for (var i = 0; i < header.length; ++i) {
    var letter = header[i];
    if (letter == "ş") {
      letter = "s";
    }
    if (letter == "ţ") {
      letter = "t";
    }
    if (letter == "Ţ") {
      letter = "T";
    }
    if (letter == "ă") {
      letter = "a";
    }
    if (letter == "Ă") {
      letter = "A";
    }
    if (letter == "Î") {
      letter = "I";
    }
    if (letter == "î") {
      letter = "i";
    }
    if (letter == " " && key.length > 0) {
      upperCase = true;
      continue;
    }
    if (!isAlnum_(letter)) {
      continue;
    }
    if (key.length == 0 && isDigit_(letter)) {
      continue; // first character must be a letter
    }
    if (upperCase) {
      upperCase = false;
      key += letter.toUpperCase();
    } else {
      key += letter.toLowerCase();
    }
  }
  return key;
}

// Returns true if the cell where cellData was read from is empty.
// Arguments:
//   - cellData: string
function isCellEmpty_(cellData) {
  return typeof(cellData) == "string" && cellData == "";
}

// Returns true if the character char is alphabetical, false otherwise.
function isAlnum_(char) {
  return char >= 'A' && char <= 'Z' ||
    char >= 'a' && char <= 'z' ||
    isDigit_(char);
}

// Returns true if the character char is a digit, false otherwise.
function isDigit_(char) {
  return char >= '0' && char <= '9';
}
