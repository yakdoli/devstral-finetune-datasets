```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_326.jpeg
document_name: grid
page_number: 326
page_id: grid#page_326
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Optional argument specifying an array of dates not to be counted as working days.
- The NETWORKDAYS function returns the #VALUE! error value if any argument is not a valid date.
- The example demonstrates calculating working days between two dates using NETWORKDAYS.

## Content

### Optional Argument Example

`[holidays]`: An optional argument, which specifies an array of dates that are not to be counted as working days.

#### Notes
- If any argument is not a valid date, NETWORKDAYS returns the #VALUE! error value.

#### Example

| FORMULA                                                                 | RESULT |
|-------------------------------------------------------------------------|--------|
| =NETWORKDAYS(DATE(2012,10,1),DATE(2013,3,1))                            | 110    |

### NORMDIST

#### Syntax
```plaintext
Returns the normal distribution for the specified mean and standard deviation.
```

#### NORMDIST(x, mean, standard_dev, cumulative), where:
- `x` is the value for which you want the distribution.
- `mean` is the arithmetic mean of the distribution.
- `standard_dev` is the standard deviation of the distribution.
- `cumulative` is a logical value that determines the form of the function. If cumulative is True, NORMDIST returns the cumulative distribution function; if False, it returns the probability mass function.

#### Remarks
- Standard_dev must be > 0.
- The equation for the normal density function (cumulative = False) is:
  \[
  f(x, \mu, \sigma) = \frac{e^{-\left(\frac{(x-\mu)^2}{2\sigma^2}\right)}}{\sqrt{2\pi}\sigma}
  \]

## Code Examples
```csharp
// Example of using NETWORKDAYS
int workingDays = NETWORKDAYS(DATE(2012, 10, 1), DATE(2013, 3, 1));

// Example of using NORMDIST
double normalDistribution = NORMDIST(x, mean, standard_dev, cumulative);
```

## Cross References
- See also: NETWORKDAYS, DATE, NORMDIST

<!-- tags: [product, module, control, api, version?] keywords: [NETWORKDAYS, NORMDIST, DATE, working days, normal distribution, mean, standard deviation, cumulative, error value] -->
```