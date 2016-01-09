// [todo] remove this script.
function fillBalance() {
  var sheetIds = SpreadsheetApp.openById('0ApG54gFt9Qs9dGNSRGY0Zm5ONDZrZUY4SXJlbWEzNFE').getSheetByName('sheet ids'),
      lastSheetId = sheetIds.getRange("B"+(firstRow(sheetIds,1)-2)).getValue(),
      lastSheet = SpreadsheetApp.openById(lastSheetId),
      today = new Date(),
      currentSoldRC = sheet(15).getRange(sheet(15).getLastRow()-1,6).getValue(),
      bankSold = sheet(7).getRange(firstRow(sheet(7),3)-1,6).getValue(),
      upkeepSold = 0,
      restantSold = 0;

  // Set date of 'bilanţ'
  sheet(8).getRange('D6').setValue(formatDate(today));

  for (var k=1; k<7; k++) {
    var upkeepUnpaid = Number(sheet(k).getRange(53,getColumnIndexByName(sheet(k),'restTotalIntretinere')+1,1,1).getValue()).toFixed(2),
        restantUnpaid = Number(sheet(k).getRange(53,getColumnIndexByName(sheet(k),'restIntretinere')+1,1,1).getValue()).toFixed(2);
    upkeepSold += Number(upkeepUnpaid);
    restantSold += Number(restantUnpaid);
  }

  var lastBalanceRangeA = sheet(8,lastSheet).getRange('C10:C13').getValues(),
      //lastBalanceRangeP = sheet(8,lastSheet).getRange('F10:F13').getValues(),
      balanceRangeA = sheet(8).getRange('C10:C13');
      //balanceRangeP = sheet(8).getRange('F10:F13'),

  balanceRangeA.setValues([ [currentSoldRC],
                            [bankSold],
                            [upkeepSold],
                            [restantSold] ]);
//  balanceRangeP.setValues([ [''],
//                            [''],
//                            [specialSold+factBoxa+factDob+salBoxa+salDob],
//                            [otherSold+factCh+factPen+salCh+salPen],
//                            [lastUnpayed+factUnpayed],
//                            [''],
//                            [''] ]);
  saveBalance();
}

function saveBalance() {
  // Copy current balance in 'bilanţ'+date spreadsheet
  var sheetIds = SpreadsheetApp.openById('0ApG54gFt9Qs9dGNSRGY0Zm5ONDZrZUY4SXJlbWEzNFE').getSheetByName('sheet ids'),
      lastRow = sheetIds.getLastRow(),
      d6 = sheet(8).getRange('D6').getValue(),
      balanceId = sheetIds.getRange("D"+(lastRow)).getValue(),
      destination = SpreadsheetApp.openById(balanceId),
      foaie1 = destination.getSheetByName('Foaie1'),
      copy = sheet(8).copyTo(destination),
      lastSheet = destination.getSheetByName(d6.substring(0,5));

  // Copy sheet if one with same name doesn't exist, else replace it
  if (lastSheet == null)
    copy.setName(d6.substring(0,5));
  else {
    destination.deleteSheet(lastSheet);
    copy.setName(d6.substring(0,5));
  }

  // Move sheet to the end
  var destLength = destination.getSheets().length;
  destination.setActiveSheet(copy);
  destination.moveActiveSheet(destLength);

  // Delete default sheet
  if (foaie1 != null) {
    destination.deleteSheet(foaie1);
  }
}
