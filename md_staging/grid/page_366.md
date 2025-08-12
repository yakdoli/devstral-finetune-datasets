```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_366.jpeg
document_name: grid
page_number: 366
page_id: grid#page_366
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

value is a numeric value a formula that evaluates to a numeric value or a reference to a cell containing a numeric value.

**format_text** is a number format in text form in the Category box on the Number tab in the Format Cells dialog box.

## 4.1.4.6.244 TIME

Returns the decimal number for a particular time.

The decimal number returned by TIME is a value ranging from 0 (zero) to 0.99999999, representing the times from 0:00:00 (12:00:00 A.M.) to 23:59:59 (11:59:59 P.M.).

### Syntax

**TIME(hour, minute, second)**, where:

* **hour** is a number from 0 (zero) to 23 representing the hour.
* **minute** is a number from 0 to 59 representing the minute.
* **second** is a number from 0 to 59 representing the second.

## 4.1.4.6.245 TIMEVALUE

Returns the decimal number of the time represented by a text string. The decimal number is a value ranging from 0 (zero) to 0.99999999, representing the times from 0:00:00 (12:00:00 A.M.) to 23:59:59 (11:59:59 P.M.).

### Syntax

**TIMEVALUE(time_text)**, where:

* **time_text** is a text string that represents a time as a formatted string; for example, "6:45 PM" and "18:45" text strings within quotation marks that represent time.

### Remarks

* Date information in time_text is ignored.
<!-- tags: [syncfusion, windows forms, essential grid, numeric value, format, time, syntax, timevalue] keywords: [time, decimal number, hour, minute, second, text string, ignored, date] -->
```