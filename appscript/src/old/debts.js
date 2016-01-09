// Custom function to fill in the data of the `restante` column.
// [todo] improve this functionality !!!
function restantUpkeep(){
  var date = sheet(0).getRange("A1").getValue().split(' ');
  var initialMonth = date[0],
      year = parseInt(date[1]);
  var monthsObj = months(year);
  // [todo] replace with Object.keys(months(year))
  var monthsArray = [];
  for (month in monthsObj) {
    monthsArray.push(month);
  }
  // [todo] duplicate code with billDate() function.
  var position = monthsArray.indexOf(initialMonth);
  var billMonth = monthsArray[(position + 2) % 12];

  var localYear = year;
  if (billMonth == 'IANUARIE' || billMonth == 'FEBRUARIE') {
    localYear += 1;
  }
  var localMonths = months(localYear);
  var dueDate = new Date(localYear,
                         localMonths[initialMonth][0]+1,
                         1);
  var lateDate = Math.round((new Date() - dueDate)/(1000*60*60*24)),
      sumPenalties = [],
      sumBoxe = [];

  // The spreadsheet `evidenta chitante` has a sheet with all generated sheets and their IDs sorted by month and year.
  var sheetIds = SpreadsheetApp.openById('0ApG54gFt9Qs9dGNSRGY0Zm5ONDZrZUY4SXJlbWEzNFE').getSheetByName('sheet ids'),
      lastSheetId = sheetIds.getRange("B"+(firstRow(sheetIds,1)-2)).getValue(),
      lastSheet = SpreadsheetApp.openById(lastSheetId);

  if (lateDate >= 0) {
    var lastRestRentRange = sheet(10,lastSheet).getRange(2,16,10,1).getValues(),   // 'rest plată' last month
        restantRange = sheet(10).getRange(2,15,10,1), // 'restanțe' current month
        restantRangeValues = restantRange.getValues(),
        lastBalanceRangeA = sheet(8,lastSheet).getRange('C10:C11').getValues(),
        //lastBalanceRangeP = sheet(8,lastSheet).getRange('F10:F13').getValues(),
        balanceRangeA = sheet(8).getRange('C10:C11'),
        //balanceRangeP = sheet(8).getRange('F10:F13'),
        balanceValuesA = balanceRangeA.getValues(),
        //balanceValuesP = balanceRangeP.getValues(),
        lastBankSold = sheet(7,lastSheet).getRange('F'+(firstRow(sheet(7,lastSheet),3)-1)).getValue(),
        lastBoxaSold = sheet(9,lastSheet).getRange('F'+(firstRow(sheet(9,lastSheet),12)-1)).getValue(),
        lastRentSold = sheet(10,lastSheet).getRange('H'+(firstRow(sheet(10,lastSheet),18)-1)).getValue(),
        lastInterestSold = sheet(12,lastSheet).getRange('F'+(firstRow(sheet(12,lastSheet),3)-1)).getValue(),
        lastFactSold = sheet(13,lastSheet).getRange('F'+(firstRow(sheet(13,lastSheet),3)-1)).getValue(),
        lastPenaltiesSold = sheet(14,lastSheet).getRange('F'+(firstRow(sheet(14,lastSheet),12)-1)).getValue(),
        lastSalSold = sheet(17,lastSheet).getRange('F'+(firstRow(sheet(17,lastSheet),17)-1)).getValue();

    // Set current rents
    for (var k = 0; k < 10; k++) {
      if (lastRestRentRange[k][0] > 0 && lastRestRentRange[k][0] < 0.01)
        lastRestRentRange[k][0] = 0;
      restantRangeValues[k][0] = lastRestRentRange[k][0];
    }
    restantRange.setValues(restantRangeValues);

    // Set current 'balance' solds
    for (var l = 0; l < 2; l++) {
      balanceValuesA[l][0] = lastBalanceRangeA[l][0];
      //balanceValuesP[l][0] = lastBalanceRangeP[l][0];
    }
    balanceRangeA.setValues(balanceValuesA);
    //balanceRangeP.setValues(balanceValuesP);

    // Set initial solds in fonds
    sheet(7).getRange('F2').setValue(lastBankSold);
    sheet(9).getRange('F11').setValue(lastBoxaSold);
    sheet(10).getRange('H17').setValue(lastRentSold);
    sheet(12).getRange('F2').setValue(lastInterestSold);
    sheet(13).getRange('F2').setValue(lastFactSold);
    sheet(14).getRange('F11').setValue(lastPenaltiesSold);
    sheet(17).getRange('F16').setValue(lastSalSold);

    // Set 'taxă boxă' cashings
    var boxaRange = sheet(9).getRange('A12:D17'),
        taxaRange = sheet(9).getRange('B2:B7').getValues(),
        date = '12.' + (position + 2) % 12 + '.' + localYear;
    boxaRange.setValues([
      [date,initialMonth,'Taxă boxă - sc. A',taxaRange[0]],
      [date,initialMonth,'Taxă boxă - sc. B',taxaRange[1]],
      [date,initialMonth,'Taxă boxă - sc. C',taxaRange[2]],
      [date,initialMonth,'Taxă boxă - sc. D',taxaRange[3]],
      [date,initialMonth,'Taxă boxă - sc. E',taxaRange[4]],
      [date,initialMonth,'Taxă boxă - sc. F',taxaRange[5]]
    ]);

    // Set current fond, restant upkeep, penalties
    for (var i = 1; i < 7; i++) {
      var lastRange = sheet(i,lastSheet).getRange(9,getColumnIndexByName(sheet(i,lastSheet), 'restTotalIntretinere')+1,44,4).getValues(), //last 4 'rest' columns
          lastRestantUpkeep,
          restantUpkeepRange = sheet(i).getRange(9,getColumnIndexByName(sheet(i), 'intretinere')+1,44,1), //current 'rest intretinere' column
          lastRestPenaltiesRange = sheet(i,lastSheet).getRange(9,getColumnIndexByName(sheet(i,lastSheet), 'restPenalitati')+1,44,1).getValues(), //last 'rest penalitati' column
          penaltiesRange = sheet(i).getRange(9,getColumnIndexByName(sheet(i), 'penalitati01zi')+1,44,1), //current 'penalties' column
          penalties = [];
      if (initialMonth == 'APRILIE' || initialMonth == 'MAI' || initialMonth == 'IUNIE')
        var fondRange = sheet(i).getRange(9,getColumnIndexByName(sheet(i), 'fondRulment')+1,44,1), //current 'fond rulment'
            fondRangeValues = fondRange.getValues();
      if (initialMonth == 'MAI' || initialMonth == 'IUNIE' || initialMonth == 'IULIE')
        var lastRestFondRange = sheet(i,lastSheet).getRange(9,getColumnIndexByName(sheet(i,lastSheet), 'restRulment')+1,44,1).getValues(); //last 'rest rulment'

      for (var j = 0; j < lastRange.length; j++) {
        // set sums from last month between 0 and 0.01 to 0
        if( (lastRange[j][0] > 0 && lastRange[j][0] < 0.01) || (lastRange[j][1] > 0 && lastRange[j][1] < 0.01) || (lastRange[j][2] > 0 && lastRange[j][2] < 0.01)) {
          lastRange[j][0] = 0;
          lastRange[j][1] = 0;
          lastRange[j][2] = 0;
        }
        switch(initialMonth) {
          case 'APRILIE':
            lastRange[j][1] = 0;
            lastRange[j][0] = lastRange[j][0] + lastRange[j][2];
            lastRange[j][2] = lastRange[j][2];
            fondRangeValues[j][0] = 0;
            break;
          case 'MAI':
          case 'IUNIE':
            if (lastRange[j][3] > 0 && lastRange[j][3] < 0.01)
              lastRange[j][3] = 0;
            lastRange[j][0] = lastRange[j][0] + lastRange[j][3];
            lastRange[j][2] = lastRange[j][3];
            fondRangeValues[j][0] = lastRestFondRange[j][0];
            break;
          case'IULIE':
            if (lastRange[j][3] > 0 && lastRange[j][3] < 0.01)
              lastRange[j][3] = 0;
            lastRange[j][0] = lastRange[j][0] + lastRange[j][1] + lastRange[j][3];
            lastRange[j][2] = lastRange[j][3];
            break;
          default:
            lastRange[j][0] = lastRange[j][0] + lastRange[j][2];
            lastRange[j][2] = lastRange[j][2];
        }
        lastRestantUpkeep = lastRange[j][2];
        lastRange[j].splice(1,3);
        lastRange[j][0] = lastRange[j][0].toFixed(2);
        var clone = lastRange[j].slice(0);
        penalties.push(clone);
        if (lastRestantUpkeep > 0)
          penalties[j][0] = (lastRestPenaltiesRange[j][0] + lastRestantUpkeep*0.03).toFixed(2);
        else
          penalties[j][0] = lastRestPenaltiesRange[j][0];
      }
      restantUpkeepRange.setValues(lastRange);
      penaltiesRange.setValues(penalties);
      if (fondRange)
        fondRange.setValues(lastRestFondRange);
      sumPenalties.push((sheet(i,lastSheet).getRange(53,getColumnIndexByName(sheet(i,lastSheet), 'penalitati01zi')+1,1,1).getValue()
                        -sheet(i,lastSheet).getRange(53,getColumnIndexByName(sheet(i,lastSheet), 'restPenalitati')+1,1,1).getValue()).toFixed(2));
      sumBoxe.push(sheet(i,lastSheet).getRange(53,getColumnIndexByName(sheet(i,lastSheet), 'taxaBoxe')+1,1,1).getValue());
    }
  }
  var values = [
    [sumPenalties[0]],
    [sumPenalties[1]],
    [sumPenalties[2]],
    [sumPenalties[3]],
    [sumPenalties[4]],
    [sumPenalties[5]]
  ];
  sheet(0).getRange('P2').setValue(sheet(0,lastSheet).getRange('P2').getValue());
  sheet(14).getRange('B2:B7').setValues(values);
}
