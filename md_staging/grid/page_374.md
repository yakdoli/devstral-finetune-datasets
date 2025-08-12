```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_374.jpeg
document_name: grid
page_number: 374
page_id: grid#page_374
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:29Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- WEEKDAY function used for determining the day of the week based on a given date.
- WEIBULL function for calculating the Weibull distribution.
- Explanation of serial_number representation and return_type parameters in WEEKDAY function.
- WEIBULL function syntax and parameters including x, alpha, beta, and cumulative.

## Content

### WEEKDAY(serial_number, return_type)

- **serial_number**: A sequential number representing the date you are trying to find. Dates should be entered using the DATE function or as results of other formulas or functions. For example, `DATE(2008,5,23)` for the 23rd day of May 2008.
- **return_type**: A number that determines the type of return value.

| Return_type is | Number Returned |
|-----------------|-----------------|
| 1 or omitted    | Numbers 1 (Sunday) through 7 (Saturday). |
| 2               | Numbers 1 (Monday) through 7 (Sunday). |
| 3               | Numbers 0 (Monday) through 6 (Sunday). |

#### Remarks
- Dates are stored as sequential serial numbers for calculations.
- By default, January 1, 1900, is serial number 1, and January 1, 2008, is serial number 39448 because it is 39,448 days after January 1, 1900.

### WEIBULL

#### Syntax
- `WEIBULL(x, alpha, beta, cumulative)`, where:
  - **x**: The value at which to evaluate the function.
  - **alpha**: A parameter to the distribution.
  - **beta**: A parameter to the distribution.
  - **cumulative**: Determines the form of the function.

#### Remarks
- **X must be >= 0.**
- **Alpha and beta must > 0.**

## API Reference

### Parameters for WEIBULL Function
| Name        | Description                                      |
|-------------|--------------------------------------------------|
| x           | The value to evaluate the function.             |
| alpha       | A parameter to the distribution.                |
| beta        | A parameter to the distribution.                |
| cumulative  | Determines the form of the function.            |

## Code Examples

### Example for WEIBULL Function
```csharp
// Example usage of WEIBULL function
double x = 8;
double alpha = 2;
double beta = 2;
bool cumulative = true;

double result = WEIBULL(x, alpha, beta, cumulative);
```

## Page-level Navigation/TOC

- WEEKDAY(serial_number, return_type)
- WEIBULL(x, alpha, beta, cumulative)

<!-- tags: [syncfusion-winforms, essential-grid, date-functions, weibull-distribution] keywords: [WEEKDAY, WEIBULL, serial_number, return_type, alpha, beta, cumulative] -->
```