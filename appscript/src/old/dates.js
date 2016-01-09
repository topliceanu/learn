// Calculates the number of days in February
// @param {Number} year
// @return {Number}
function daysInFebruary (year) {
  return year % 4 == 0 ? 29 : 28;
}

// Returns a hash of months with month index and number of days.
// @param {Number} year - given the year it will correctly calculate the number of days in February.
// @return {Object}
function months (year) {
  return {
    'IANUARIE':[1,31],
    'FEBRUARIE':[2, daysInFebruary(year)],
    'MARTIE':[3,31],
    'APRILIE':[4,30],
    'MAI':[5,31],
    'IUNIE':[6,30],
    'IULIE':[7,31],
    'AUGUST':[8,31],
    'SEPTEMBRIE':[9,30],
    'OCTOMBRIE':[10,31],
    'NOIEMBRIE':[11,30],
    'DECEMBRIE':[12,31]
  };
};

// Function updates the date header for all `plata` sheets: A, B, C, D, E, F.
// [todo] turn this into a custom function that will be called on line 4 of each `plata` sheets.
// [todo] remove deleteColumns() and restantUpkeep() function calls.
function billDate() {
  var a4 = sheet(1).getRange("A4");

  // Read the initial month and year (the date for which we display the table)
  var date = sheet(0).getRange("A1").getValue().split(' ');
  var initialMonth = date[0],
      year = parseInt(date[1]);

  // Build an array of month names
  // [todo] replace with Object.keys(months(year))
  var monthsObj = months(year);
  var monthsArray = [];
  for (month in monthsObj) {
    monthsArray.push(month);  // [IANUARIE, FEBRUARIE, MARTIE, APRILIE, MAI, IUNIE, IULIE, AUGUST, SEPTEMBRIE, OCTOMBRIE, NOIEMBRIE, DECEMBRIE]
  }

  // Calculate the billing month. Billing is done 2 months after the actual month.
  var position = monthsArray.indexOf(initialMonth);
  var billMonth = monthsArray[(position + 2) % 12];

  var localYear = year;
  if (billMonth == 'IANUARIE' || billMonth == 'FEBRUARIE') {
    localYear += 1;
  }
  var localMonths = months(localYear);

  // Calculate month index, prefixed with 0 if needed.
  var billMonthNumber = localMonths[billMonth][0];
  if (billMonthNumber < 10) {
    billMonthNumber = "0" + localMonths[billMonth][0];
  }

  // Update all sheets headers with the date value.
  if (initialMonth == "" || year == ""){
    a4.setValue("");
  } else {
    var diff = localMonths[billMonth][1]-12+1,
      term = diff < 20 ? diff + ' ZILE' : diff + ' DE ZILE';
    a4.setValue(initialMonth +", DATA DE AFIŞARE: 12."+billMonthNumber+"."+localYear+", DATA SCADENTĂ: "+localMonths[billMonth][1]+'.'+billMonthNumber+"."+localYear+", TERMEN DE PLATĂ: "+term);
  }

  // Delete 'termoficare' or 'fondRulment' if needed
  deleteColumns();
  // Calculate and display the penalties for last month
  restantUpkeep();
  Browser.msgBox('Datele au fost adăugate','',Browser.Buttons.OK);
}

// Formats the date in the romanian style
// @param {Date} date
// @return {String} dd.mm.yyyy
function formatDate(date) {
  var dd = date.getDate(),
      mm = date.getMonth()+1, //January is 0!
      yyyy = date.getFullYear();

  if (dd < 10) dd = '0' + dd;
  if (mm < 10) mm = '0' + mm;
  var formattedDate = dd + '.' + mm + '.' + yyyy;

  return formattedDate;
}
