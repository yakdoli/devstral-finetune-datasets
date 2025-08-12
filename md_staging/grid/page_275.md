```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_275.jpeg
document_name: grid
page_number: 275
page_id: grid#page_275
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:51Z
fidelity: lossless
-->

## DATE(year, month, day)

**Syntax:**
DATE(year, month, day)

### Parameters:

- **year:** A number representing the year. It can be one to four digits. The year is interpreted based on 1900.
  - If the year is between 0 (zero) and 1899 (inclusive), the value is added to 1900 to calculate the year. For example, DATE(102, 11, 12) returns November 12, 2002 (1900 + 102).
  - If the year is between 1900 and 9999 (inclusive), the value is used as is. For example, DATE(2002, 11, 12) returns November 12, 2002.
  
- **month:** A number representing the month of the year.
  
- **day:** A number representing the day of the month.

### Remark:
Dates are stored as sequential serial numbers so that they can be used in calculations. By default:
- January 1, 1900, is serial number 1.
- November 12, 2002, is serial number 37572 because it is 37572 days after January 1, 1900.

## 4.1.4.6.6.56 DATEVALUE

### Overview
Returns the serial number of the date represented by the `date_text`.

### Syntax:
DATEVALUE(date_text)

#### Parameters:
- **date_text:** The text that represents a date as a formatted string. For example, "11/12/2002" or "12-Nov-2002" are text strings within quotation marks that represent dates. If the year portion of the `date_text` is omitted, DATEVALUE uses the current year from your computer's built-in clock. The time information in the `date_text` is ignored.

### Remarks:
- Dates are stored as sequential serial numbers so that they can be used in calculations. By default:
  - January 1, 1900, is serial number 1.
  - November 12, 2002, is serial number 37572 because it is 37572 days after January 1, 1900.
- Most functions automatically convert date values to serial numbers.

<!-- tags: [winforms, date, datevalue, serialnumber, timestamp] keywords: [DATE, DATEVALUE, year, month, day, serialnumber, timeinformation] -->
```