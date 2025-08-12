```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_217.jpeg
document_name: calculate
page_number: 217
page_id: calculate#page_217
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:49Z
fidelity: lossless
-->

## Remarks

The equation for the Pearson product moment correlation coefficient, \( r \), is:

\[
r = \frac{\sum(x - \overline{x})(y - \overline{y})}{\sqrt{\sum(x - \overline{x})^2 \sum(y - \overline{y})^2}}
\]

where:

- \(\overline{x}\) and \(\overline{y}\) are the sample means AVERAGE(known_x's) and AVERAGE(known_y's).

RSQ returns \( r^2 \), which is the square of this correlation coefficient.

### 4.7.142 SECOND

Returns the seconds of a time value. The second is given as an integer in the range 0 (zero) to 59.

#### Syntax

SECOND(serial_number)

where:

- serial_number is the time that contains the seconds you want to find.

#### Remarks

- Time values are a portion of a date value and are represented by a decimal number (for example, 12:00 PM is represented as 0.5 because it is half of a day).

### 4.7.143 SIGN

<!-- tags: [pearson correlation coefficient, rsq, second, serial_number, correlation, time values, Syncfusion Winforms, 11.4.0.26] keywords: [pearson product moment correlation coefficient, rsq, second function, serial_number, time values, syncfusion winforms, version 11.4.0.26] -->
```