// Contains constants and utility functions.

// Id of the spreadsheet used as a database to store other sheet ids.
var STORAGE_SPREADSHEET_ID = "1WBDJR1056EzSeth1LfTNFdPC-YDGn9pdGiy17XH7cLM";

// Caches and returns the storage spreasheet.
var storageSpreadsheetSingleton = null;
function getStorageSpreadsheet_ () {
  if (storageSpreadsheetSingleton === null) {
    storageSpreadsheetSingleton = SpreadsheetApp.openById(STORAGE_SPREADSHEET_ID).getSheetByName('sheet ids')
  }
  return storageSpreadsheetSingleton
};
