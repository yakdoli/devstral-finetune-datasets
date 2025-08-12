```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_377.jpeg
document_name: grid
page_number: 377
page_id: grid#page_377
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:12Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section explains how to use the `serial_number` to specify dates for calculations and discusses the `ZTEST` function for statistical analysis.

## Content

### Dates and Serial Numbers

**serial_number** is the date of the year you want to find. Dates should be entered by using the DATE function or as results of other formulas or functions. For example, use `DATE(2002,11,12)` for the 12th day of November 2002.

#### Remarks
- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900, is serial number 1 and January 1, 2008, is serial number 39448 because it is 39,448 days after January 1, 1900.

### ZTEST Function

#### Function Overview
4.1.4.6.6.265 **ZTEST**

Returns the one-tailed probability-value of a z-test.

#### Syntax
```markdown
ZTEST(array, u0, sigma)
```

- **array**: is the array or range of data against which to test `u0`.
- **u0**: is the value to test.
- **sigma**: is the population (known) standard deviation. If omitted, the sample standard deviation is used.

#### Remarks
- When `sigma` is not omitted, ZTEST is calculated as:
  ```
  ZTEST(array, u0) = 1 - NORMSDIST((x - u0) * sqrt(n) / sigma)
  ```
- When `sigma` is omitted, ZTEST is calculated as:
  ```
  ZTEST(array, u0) = 1 - NORMSDIST((x - u0) * sqrt(n) / s)
  ```
 where:
 - **x**: is the sample mean `AVERAGE(array)`.
 - **s**: is the sample standard deviation `STDEV(array)`.
 - **n**: is the number of observations in the sample `COUNT(array)`.

## API Reference
- **Namespace**: `System.Windows.Forms` (or related namespace if applicable)
- **Class**: `GridControl`
- **Method**: `ZTEST(array, u0, sigma)`
- **Parameters**:
  - **array**: Array of data to test.
  - **u0**: Value to test.
  - **sigma**: Known standard deviation (optional).

## Code Examples
### C#
```csharp
double[] data = { 2.5, 9.0, 7.6, 8.3, 5.4 };
double u0 = 7.5;
double sigma = 2.5;
double ztestValue = ZTEST(data, u0, sigma);
```

### VB.NET
```vbnet
Dim data As Double() = {2.5, 9.0, 7.6, 8.3, 5.4}
Dim u0 As Double = 7.5
Dim sigma As Double = 2.5
Dim ztestValue As Double = ZTEST(data, u0, sigma)
```

## Cross References
- For more information on date calculations, refer to the section on `DATE` function.

<!-- tags: date calculations, z-test, probability-value, standard deviation, dates, serial numbers, windows forms, gridcontrol, syncfusion -->
```