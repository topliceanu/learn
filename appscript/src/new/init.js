function onInstall (e) {
  onOpen(e);
}

function onOpen (e) {
  addMenus();
  addTriggers();
}

function addMenus () {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  spreadsheet.addMenu('Precompletare tabele', [
    { name: 'Setaţi datele necesare', functionName: 'billDate' }
  ]);
  // [todo] remove this menu and the createRegister/saveRegister functions.
  spreadsheet.addMenu('Registru casă', [
    { name: 'Creaţi registru casă', functionName: 'createRegister'},
    null,
    {name: 'Salvaţi registru casă', functionName: 'saveRegister'}
  ]);
  // [todo] remove this menu and the closeLog function.
  spreadsheet.addMenu('Registru jurnal', [
    {name: 'Închideţi registru jurnal', functionName: 'closeLog' }
  ]);
}

function addTriggers () {
  ScriptApp.newTrigger('fillBalance').forSpreadsheet(ss).onEdit().create();
  ScriptApp.newTrigger('addEmptyRows').forSpreadsheet(ss).onEdit().create();
}
