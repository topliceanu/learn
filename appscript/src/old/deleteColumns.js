// Delete 'termoficare' column and rearrange columns' numbers,
// [todo] column numbers on `plata` sheets are generated dynamically, replace with usage of COLUMN() function.
// [todo] move this into globals.gs
function deleteColumns() {
  var initialMonth = sheet(0).getRange("A1").getValue().split(' ')[0];

  if (initialMonth != 'NOIEMBRIE' && initialMonth != 'DECEMBRIE' && initialMonth != 'IANUARIE' && initialMonth != 'FEBRUARIE' && initialMonth != 'MARTIE') {
    for (var i = 1; i < 7; i++ ) {
      if (getColumnIndexByName(sheet(i), 'termoFicare') != -1) {
        var termCol = getColumnIndexByName(sheet(i), 'termoFicare') + 1;
        sheet(i).deleteColumn(termCol);
        sheet(i).getRange(8,termCol).setValue(termCol);
        sheet(i).getRange('Q57').setValue('0');
      }
    }
  }

// Delete 'fondRulment' and rearrange columns' numbers. - fond rulment is now no longer removed.
//  if(initialMonth != 'APRILIE' && initialMonth != 'MAI' && initialMonth != 'IUNIE') {
//    for (var i = 1; i < 7; i++ ) {
//      if (getColumnIndexByName(sheet(i), 'fondRulment') != -1) {
//        var fondCol = getColumnIndexByName(sheet(i), 'fondRulment') + 1,
//            restCol = getColumnIndexByName(sheet(i), 'restRulment');
//        sheet(i).deleteColumn(fondCol);
//        sheet(i).deleteColumn(restCol);
//        sheet(i).getRange(8,fondCol).setValue(fondCol);
//        sheet(i).getRange(8,restCol).setValue(restCol);
//      }
//    }
//  }
}
