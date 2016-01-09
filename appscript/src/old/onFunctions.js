
// Adds trigger functions to the current sheet for open and edit.
// [todo] Trebuie rulat de fiecare data ca sa apara meniurile! Acum putem folosi direct onInstall(e)/onOpen(e);
function triggers() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  ScriptApp.newTrigger('menus').forSpreadsheet(ss).onOpen().create();
  ScriptApp.newTrigger('fillBalance').forSpreadsheet(ss).onEdit().create();
  ScriptApp.newTrigger('addEmptyRows').forSpreadsheet(ss).onEdit().create();
  Browser.msgBox('Meniu adăugat. Reîncărcaţi pagina');
}

// Adds the UI menus for the main sheet.
// [todo] replace with onOpen() with https://developers.google.com/apps-script/reference/base/ui#createMenu%28String%29
function menus() {
  // Adds a dropdown to the menu.
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  ss.addMenu('Precompletare tabele', [{ name: 'Setaţi datele necesare', functionName: 'billDate' }]);
  ss.addMenu('Chitanţe', [{ name: 'Creaţi chitanţă', functionName: 'receiptBox' }]);
  ss.addMenu('Registru casă', [{ name: 'Creaţi registru casă', functionName: 'createRegister'},
                               null,
                               {name: 'Salvaţi registru casă', functionName: 'saveRegister'}]);
  ss.addMenu('Registru jurnal', [{name: 'Închideţi registru jurnal', functionName: 'closeLog' }]);
}

// [todo] move complex function from the sheet into custom function in the script, use arrays.
// [todo] add the new column and make sure all functionality still works.
