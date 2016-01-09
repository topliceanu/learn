// [todo] remove this function, it's a duplicate of receipts.gs#createRegister()
function createRegister() {
  // Set date and initial sold for new register and clear content from old register
  var sheetIds = SpreadsheetApp.openById('0ApG54gFt9Qs9dGNSRGY0Zm5ONDZrZUY4SXJlbWEzNFE').getSheetByName('sheet ids'),
      lastSheetId = sheetIds.getRange("B"+(firstRow(sheetIds,1)-2)).getValue(),
      lastSheet = SpreadsheetApp.openById(lastSheetId),
      lastRow = sheetIds.getLastRow(),
      curRegId = sheetIds.getRange("C"+(lastRow)).getValue(),
      curReg = SpreadsheetApp.openById(curRegId),
      foaie1 = curReg.getSheetByName('Foaie1'),
      total = foaie1 != null ? sheet(15,lastSheet).getRange(sheet(15,lastSheet).getLastRow()-1,6)
                             : sheet(15).getRange(sheet(15).getLastRow()-1,6);
//      lastTotal = foaie1 != null ? sheet(15,lastSheet).getRange('F7')
//                                 : sheet(15).getRange('F7');

  sheet(15).getRange('F5').setValue(formatDate(new Date()));
  sheet(15).getRange('F7').setValue(total.getValue());
  sheet(15).getRange(8,1,sheet(15).getLastRow()-9,6).clearContent();
}

// [todo] remove this function, its a duplicate of receipts.gs#saveRegister()
function saveRegister() {
  // Copy current register in 'registru casă'+date spreadsheet
  var sheetIds = SpreadsheetApp.openById('0ApG54gFt9Qs9dGNSRGY0Zm5ONDZrZUY4SXJlbWEzNFE').getSheetByName('sheet ids'),
      lastRow = sheetIds.getLastRow(),
      f5 = sheet(15).getRange('F5').getValue(),
      registerId = sheetIds.getRange("C"+(lastRow)).getValue(),
      destination = SpreadsheetApp.openById(registerId),
      foaie1 = destination.getSheetByName('Foaie1'),
      copy = sheet(15).copyTo(destination),
      lastSheet = destination.getSheetByName(f5.substring(0,5));

  // Delete default sheet
  if (foaie1 != null) {
    destination.deleteSheet(foaie1);
  }

  // Copy sheet if one with same name doesn't exist, else replace it
  if (lastSheet == null)
    copy.setName(f5.substring(0,5));
  else {
    destination.deleteSheet(lastSheet);
    copy.setName(f5.substring(0,5));
  }

  // Move sheet to the end
  var destLength = destination.getSheets().length;
  destination.setActiveSheet(copy);
  destination.moveActiveSheet(destLength);

  copyLines();
  fillBalance();
  Browser.msgBox('Registrul a fost salvat','',Browser.Buttons.OK);
}

function copyLines() {
  // Copy the lines from 'reg.casă' in 'reg.jurnal'
  // registerObjects is an array of all data that needs to be copied in RJ
  var registerDataRange = sheet(15).getRange("A8:F" + parseInt(sheet(15).getLastRow()-2)),
      registerObjects = getRowsData(sheet(15), registerDataRange, 6, 7),
      len = registerObjects.length,
      date = sheet(15).getRange('F5').getValue();

  var firstRowRJ = sheet(16).getLastRow()+1, // Get first empty row at the bottom of RJ
      numberRJ = firstRowRJ - 8, // The index of the next line to be written in RJ
      // Get first empty rows from 'bancă', 'chirii', 'furnizori', 'salarii'
      firstRowBank = firstRow(sheet(7),3),
      firstRowRent = firstRow(sheet(10),18),
      firstRowFact = firstRow(sheet(13),3),
      firstRowSal = firstRow(sheet(17),17);

  for (var i=0; i < len; i++) {
    var registerObject = registerObjects[i],
        act = registerObject.nrActCasa,
        anexa = registerObject.nrAnexa,
        explicatii = registerObject.explicatii,
        incasari = registerObject.incasari,
        plati = registerObject.plati;

    if (explicatii == "")
      break;

    // Copy line in 'reg.jurnal'
    sheet(16).getRange("A"+firstRowRJ+":H"+firstRowRJ).setValues([[numberRJ,date,act+' '+anexa,explicatii,incasari,'',plati,'']]);
    firstRowRJ++;
    numberRJ++;

    // Copy line in fonds' sheets
    switch(act) {
      case 'CH':
        // Copy line in 'chirii'
        if (explicatii.indexOf(' - sc. ') != -1 ) {
          sheet(10).getRange("A"+firstRowRent+":G"+firstRowRent).setValues([[date,act + ' ' + anexa,explicatii,incasari,'',plati,'']]);
          firstRowRent++;
        }
        break;
      case 'FACT':
        // Copy line in 'furnizori'
        sheet(13).getRange("A"+firstRowFact+":E"+firstRowFact).setValues([[date,act + ' ' + anexa,explicatii,incasari,plati]]);
        firstRowFact++;
        break;
      case 'FV':
        // Copy line in 'bancă' or 'salarii'
        if (explicatii.toLowerCase().indexOf('dob'.toLowerCase()) != -1) {
          sheet(7).getRange("A"+firstRowBank+":E"+firstRowBank).setValues([[date,act+' '+anexa,explicatii,plati,incasari]]);
          firstRowBank++;
        } else {
          sheet(17).getRange("A"+firstRowSal+":E"+firstRowSal).setValues([[date,
                                                                   explicatii.substring(explicatii.lastIndexOf(' ')+1),
                                                                   act+' '+explicatii.substring(0,explicatii.lastIndexOf(' ')),
                                                                   incasari,
                                                                   plati]]);
          firstRowSal++;
        }
          break;
      case 'STAT':
        // Copy line in 'salarii'
        sheet(17).getRange("A"+firstRowSal+":E"+firstRowSal).setValues([[date,abrMonths()[anexa],explicatii,incasari,plati]]);
        firstRowSal++;
        break;
    }
  }

//  var bankDataRange = sheet(7).getRange("A3:F" + firstRow(sheet(7),3)),
//      bankObjects = getRowsData(sheet(7), bankDataRange, 1, 6),
//      bankLen = bankObjects.length;
//  for (var j=0; j<bankLen; j++) {
//    var bankObject = bankObjects[j],
//        bankDate = bankObject.dataNregistrarii,
//        doc = bankObject.documentulFelulNr,
//        explicatie = bankObject.explicatie,
//        bankIncasari = bankObject.incasari,
//        bankPlati = bankObject.plati,
//        sold = bankObject.sold,
//        firstRowRC = sheet(15).getLastRow()+1,
//        numberRC = sheet(15).getRange("A"+(firstRowRC-1)).getValue() + 1;
//    sheet(15).getRange("A"+firstRowRC+":H"+firstRowRC).setValues([[numberRC,bankDate,doc,explicatie,'',bankIncasari,'',bankPlati]]);
//  }
}

function addEmptyRows(){
  // Add another 10 rows to RC when there are no empty rows
  var lastRowRC = sheet(15).getLastRow();
  if (sheet(15).getRange("D"+(lastRowRC-2)).getValue() !== "") {
    sheet(15).insertRows(lastRowRC-1, 10);
  }

  var lastRowRC = sheet(15).getLastRow(),
      sumRC = sheet(15).getRange("F"+(lastRowRC-1)),
      formula = "=SUM(E8:E"+(lastRowRC-2)+")-SUM(F8:F"+(lastRowRC-2)+")+F7",
      rangeB = sheet(15).getRange("B"+(lastRowRC-11)+":B"+(lastRowRC-2)),
      rangeC = sheet(15).getRange("C"+(lastRowRC-11)+":C"+(lastRowRC-2)),
      rangeEF = sheet(15).getRange("E"+(lastRowRC-11)+":F"+(lastRowRC-2)),
      horizontalAlignments = [["center"],["center"],["center"],["center"],["center"],["center"],["center"],["center"],["center"],["center"]],
      formats = [["0.00","0.00"],["0.00","0.00"],["0.00","0.00"],["0.00","0.00"],["0.00","0.00"],["0.00","0.00"],["0.00","0.00"],["0.00","0.00"],["0.00","0.00"],["0.00","0.00"]];
      rule = SpreadsheetApp.newDataValidation().requireValueInList(['CH', 'FACT', 'STAT', 'FV'], true).build(),
      rules = rangeB.getDataValidations();

  if (sheet(15).getRange("D"+(lastRowRC-2)).getValue() === "") {
    for (var i = 0, m = rules.length; i < m; i++) {
      for (var j = 0, n = rules[i].length; j < n; j++) {
        rules[i][j] = rule;
      }
    }
    rangeB.setDataValidations(rules);
    rangeB.setHorizontalAlignments(horizontalAlignments);
    rangeC.setHorizontalAlignments(horizontalAlignments);
    rangeEF.setNumberFormats(formats);
  }
  if (sumRC.getFormula() !== formula)
    sumRC.setFormula(formula);
}

function closeLog() {
  // Close 'reg.jurnal' at the end of month
  var initialMonth = sheet(0).getRange("A1").getValue().split(' ')[0];
  var firstRowRJ = sheet(16).getLastRow() + 1;
  sheet(15).getRange("A" + firstRowRJ + ":C" + firstRowRJ).merge().setValue('TOTAL luna ' + initialMonth);
  var values = sheet(16).getRange("E9:H" + (firstRowRJ-1)).getValues(),
      len = values.length,
      sumE = 0, sumF = 0, sumG = 0, sumH = 0;

  for (var i=0; i < len; i++) {
    sumE += Number(values[i][0]) || 0;
    sumF += Number(values[i][1]) || 0;
    sumG += Number(values[i][2]) || 0;
    sumH += Number(values[i][3]) || 0;
  }
  sheet(16).getRange("E"+firstRowRJ+":H"+firstRowRJ).setValues([[sumE,sumF,sumG,sumH]]);
  sheet(16).getRange(firstRowRJ,1,1,8).setFontSize(11).setFontWeight('bold');
  sheet(16).getRange("A"+(firstRowRJ+1)+":H").setBorder(true, false, false, false, false, false);
}
