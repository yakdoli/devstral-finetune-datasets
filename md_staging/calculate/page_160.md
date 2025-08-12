```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_160.jpeg
document_name: calculate
page_number: 160
page_id: calculate#page_160
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:31Z
fidelity: lossless
-->

## Essential Calculate

### Overview
- probability_s is the probability of a success on each trial.
- alpha is the criterion value.

### Remarks
- Trials must be >= 0.
- Probability_s must be >= 0 and <= 1.
- Alpha must be >= 0 and <= 1.

## 4.7.34 DATE

### Overview
- Returns the sequential serial number that represents a particular date.

### Syntax
- **DATE(year, month, day)**

#### Where:
- **year** can be one to four digits. Year is interpreted based on 1900.
  - If a year is between 0 (zero) and 1899 (inclusive), the value is added to 1900 to calculate the year. For example, DATE(102,11,12) returns November 12, 2002 (1900+102).
  - If a year is between 1900 and 9999 (inclusive), the value is used as is, for example, DATE(2002,11,12) returns November 12, 2002.
- **month** is a number representing the month of the year.
- **day** is a number representing the day of the month.

### Remarks
- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1 and November 12, 2002 is serial number 37572 because it is 37572 days after January 1, 1900.

## 4.7.35 DATEVALUE

### Overview
- Returns the serial number of the date represented by the date_text.

<!-- tags: [probability, alpha, trials, DATE, DATEVALUE, serial number, date calculation, Syncfusion Winforms, version 11.4.0.26] keywords: [probability_s, alpha, trials, date, date_serial, datevalue, date_text, 1900, 37572] -->
```