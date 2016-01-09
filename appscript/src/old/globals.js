// Returns one sheet from spreadsheet by it's index.
// @param {Number} index
// @param {Spreadsheet} ss - narrows the scope of the search.
// @return {Sheet}
// [todo] remove ss param
// [todo] instead of getSheetByName() use getSheets()[index]
function sheet (index, ss) {
  if (!ss) {
    ss = SpreadsheetApp.getActiveSpreadsheet();
  }
  var names = [
    'consum',
    'A', 'B', 'C', 'D', 'E', 'F',
    'bancă',
    'bilanţ',
    'boxă',
    'chirii',
    'chitanţă',
    'dobândă',
    'furnizori',
    'penalităţi',
    'reg.casă',
    'reg.jurnal',
    'salarii'
  ];
  return ss.getSheetByName(names[index]);
}

// Return the index of a column by name
// @param {Sheet} sheet
// @param {String} name
// @return {Number}
// [todo] memoize the headersRange var, it's querying the sheet for no reason all the time.
function getColumnIndexByName(sheet, name) {
  var headersRange = camelArray(sheet.getRange(7, 1, 1, sheet.getLastColumn()).getValues()[0]),
      index = headersRange.indexOf(name);
  return index;
}

// Iterates row by row in the input range and returns an array of objects.
// Each object contains all the data for a given row, indexed by its normalized column name.
// @param {Sheet} sheet - the sheet object that contains the data to be processed
// @param {Range} range - the exact range of cells where the data is stored
// @param {Number} columnHeadersRowIndex - specifies the row number where the column names are stored.
// @return {Array<Object>}
function getRowsData(sheet, range, columnHeadersRowIndex, numColumns) {
  var columnHeadersRowIndex = columnHeadersRowIndex || range.getRowIndex() - 2;
  var numColumns = numColumns || range.getLastColumn() - range.getColumn() + 1;
  var headersRange = sheet.getRange(columnHeadersRowIndex, range.getColumn(), 1, numColumns);
  var headers = headersRange.getValues()[0];
  return splitRangesToObjects(headers, range.getValues());
}

// Returns the object of data for the owner where the mouse is.
// @return {Object}
// [todo] check where this is used, should not be required anymore.
function ownerData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet(),
      currentSheet = ss.getActiveSheet(),
      ownerDataRange = currentSheet.getRange("A9:T52"),
      ownerObjects = getRowsData(currentSheet, ownerDataRange),
      // Get row where the cursor is
      // Get the owner object for 'row'
      row = currentSheet.getActiveCell().getRow(),
      lastColumn = currentSheet.getLastColumn()-1,
      ownerObject = ownerObjects[row-9],
      name = ownerObject.numeSiPrenume,
      apt = ownerObject.nrApt,
      totalUpkeep = ownerObject.totalIntretiNere,
      fond = ownerObject.fondRulment,
      penalties = ownerObject.penalitati01zi,
      restantUpkeep = ownerObject.intretinere,
      restTotalUpkeep = ownerObject.restTotalIntretinere,
      restFond = ownerObject.restRulment,
      restPenalties = ownerObject.restPenalitati,
      restUpkeep = ownerObject.restIntretinere;

  return {
    row: row,
    lastColumn: lastColumn,
    name: name,
    apt: apt,
    totalUpkeep: totalUpkeep,
    fond: fond,
    penalties: penalties,
    restantUpkeep: restantUpkeep,
    restTotalUpkeep: restTotalUpkeep,
    restFond: restFond,
    restPenalties: restPenalties,
    restUpkeep: restUpkeep
  };
}

// ???
function renterData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet(),
      currentSheet = ss.getActiveSheet(),
      renterDataRange = currentSheet.getRange("B2:P11"),
      renterObjects = getRowsData(currentSheet, renterDataRange, 1, 15),
      row = currentSheet.getActiveCell().getRow(),
      renterObject = renterObjects[row-2],
      stair = renterObject.scara,
      name = renterObject.nume,
      utilities = renterObject.totalPlataUtilitati,
      rent = renterObject.sumaChirie,
      restante = renterObject.restante,
      rest = renterObject.restPlata;

  return {
    row: row,
    stair: stair,
    name: name,
    rent: rent,
    utilities: utilities,
    restante: restante,
    rest: rest
  };
}

// Returns the first empty row in a given sheet.
// @param {Sheet} sheet
// @param {Number} startingRow - optimization, where to start looking.
// [todo] find usages and replace with Sheet.appendRow(row:Array). Remove this method.
function firstRow(sheet,startingRow) {

  var len = sheet.getMaxRows(),
      range = sheet.getRange(startingRow,3,len,1).getValues();

  for (var i = 0, n = range.length; i < n; i ++) {
    var _row = range[i];
    if (_row[0] === '') {
      return startingRow + i;
    }
  }
}
