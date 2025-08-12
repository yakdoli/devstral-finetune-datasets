```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_161.jpeg
document_name: calculate
page_number: 161
page_id: calculate#page_161
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:42Z
fidelity: lossless
-->

# Essential Calculate

## Syntax

### DATEVALUE(date_text)

where:  

**date_text** is the text that represents a date as a formatted string. For example, "11/12/2002" or "12-Nov-2002" are text strings within quotation marks that represent dates. If the year portion of the date_text is omitted, DATEVALUE uses the current year from your computer’s built-in clock. The time information in the date_text is ignored.

### Remarks

- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1, and November 12, 2002 is serial number 37572 because it is 37572 days after January 1, 1900.
- Most functions automatically convert date values to serial numbers.

## 4.7.36 DAY

Returns the day of a date, represented by a serial number. The day is given as an integer ranging from 1 to 31.

### Syntax

**DAY(serial_number)**  

where:  

**serial_number** is the date of the day you are trying to find. Dates should be entered by using the DATE function or as results of other formulas or functions. For example, use DATE(2002,4,23) for the 23rd day of April, 2002.

## 4.7.37 DAYS360

Returns the number of days between two dates based on a 360-day year (twelve 30-day months) which, is used in some accounting calculations.

<!--
tags: [syncfusion, sdk, calculate, datevalue, day, days360, winforms, syntax, remarks, date, serial number, accounting calculations] keywords: [datevalue, day, days360, serial number, date, accounting, calculate, winforms]
-->
```