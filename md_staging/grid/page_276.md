```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_276.jpeg
document_name: grid
page_number: 276
page_id: grid#page_276
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:07:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## 4.1.4.6.6.57 DAVERAGE

The DAVERAGE function finds the average values in a column of a list or database that matches the conditions that have been specified.

### Syntax

```plaintext
DAVERAGE(database, field, criteria)
```

- **database** is the range of cells that makes up the list or database.
- **field** indicates which column is used in the function.
- **criteria** is the range of cells that contains the conditions that you specify.

## 4.1.4.6.6.58 DAY

Returns the day of a date, represented by a serial number. The day is given as an integer ranging from 1 to 31.

### Syntax

```plaintext
DAY(serial_number)
```

- **serial_number** is the date of the day you are trying to find. Dates should be entered by using the DATE function or as results of other formulas or functions. For example, use `DATE(2002,4,23)` for the 23rd day of April, 2002.

## 4.1.4.6.6.59 DAYS360

Returns the number of days between two dates based on a 360-day year (twelve 30-day months) which, is used in some accounting calculations.

### Syntax

```plaintext
DAYS360(start_date, end_date, method)
```

- **start_date** and **end_date** are the two dates between which you want to know the number of days. If start_date occurs after end_date, DAYS360 returns a negative number. Dates should be entered by using the DATE function or as results of other formulas or functions.
- **method** is a logical value that specifies whether to use the U.S. or European method in the calculation.

<!-- tags: [DAVERAGE, DAY, DAYS360, date functions, Essential Grid, Windows Forms, Grid, average values, cell range, date calculations, date representation, accounting calculations, 360-day year, start_date, end_date, method, U.S. method, European method] -->
```