// Set names for numbers in receipt.
// [todo] remove this file, only needed for the invoices.
var ones = ['','unu','doi','trei','patru','cinci','şase','şapte','opt','nouă'];
var tens = ['','','douăzeci','treizeci','patruzeci','cincizeci',
            'şaizeci','şaptezeci','optzeci','nouăzeci'];
var teens = ['zece','unsprezece','doisprezece','treisprezece','paisprezece',
             'cincisprezece','şaisprezece','şaptesprezece','optsprezece','nouăsprezece'];

function toWords (number) {
  // Converts numbers to words
  var integer = (number > 1) ? convertThousands(number) + ' lei' : '';
  var floating = float(number);
  var output = '';
  if (integer !== '') output += integer;
  if (output !== '' && floating !== '') output += ' şi ';
  if (floating !== '') output += floating + ' bani';
  return (output != 0) ? " adică " + output : '';
}

function float(num) {
  // Converts float number to decimal
  var decimal = Math.round((num - parseInt(num, 10))*100);
  return convertTens(decimal);
}

function convertThousands(num){
  if (num >= 1000)
    return (convertHundreds(Math.floor(num / 1000)) == 'unu')
                             ? "una mie " + convertHundreds(Math.floor(num % 1000))
                             : convertHundreds(Math.floor(num / 1000)) + " mii " + convertHundreds(Math.floor(num % 1000));
  else
    return convertHundreds(num);
}

function convertHundreds(num) {
  if (num > 99)
    return (ones[Math.floor(num / 100)] == 'unu')
                            ? "una sută " + convertTens(Math.floor(num % 100))
                            : ones[Math.floor(num / 100)] + " sute " + convertTens(Math.floor(num % 100));
  else
    return convertTens(num);
}

function convertTens(num) {
  if (num < 10)
    return ones[Math.floor(num)] ;
  else if (num >= 10 && num < 20)
    return teens[parseInt(num) - 10];
  else
    return (ones[Math.floor(num % 10)] == "") ? tens[Math.floor(num / 10)]
                                              : tens[Math.floor(num / 10)] + " şi " + ones[Math.floor(num % 10)];
}
