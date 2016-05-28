### Functions List

- triggers()
  - menus()
    - billDate() - fils in the tables with data
      - restantUpkeep()
      - deleteColumns() - deleteColumns.js
    - receiptBox() - nu exista!
    - createRegister() - both in receipts.js and register.js
      - sheet() - returns a sheed by index.
    - saveRegister() - both in receipts.js and register.js
      - copyLines() - copies lines from registru casa into registru jurnal
        - sheet()
        - getRowsData()
        - getLastRow()
        - firstRow()
      - fillBalance()
    - closeLog()
      - sheet()
  - fillBalance() - balance.js TODO remove
  - addEmptyRows() - receipts.js/register.js TODO remove

- extra (to be removes)
  - addEmptyRows() - not used in the script.

### Improve performance:
- improve performance by batching and memoization.
- reduce the number of calls to the spreadsheets.
- reduce redundant code.

### Extra functions
- objServer.js
  - objectToArray() - not used!
  - rangeToObjects() - not used!
  - splitRangesToObjects() - used in globals.js
  - camelArray() - used in objectsToArray()
  - camelString() - used in camelArray() and splitRangesToObjects()
  - isCellEmpty\_()
  - isAlnum\_()
  - isDigit\_()
- globals.js
  - getColumnIndexByName() - used in deleteColumns.js, debts.js, and balance.js
  - getRowsData() - receipts.js and register.js
