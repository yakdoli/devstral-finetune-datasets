```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_155.jpeg
document_name: calculate
page_number: 155
page_id: calculate#page_155
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:20Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- The section explains the use of `alpha` for calculating confidence levels, `standard_dev` for population standard deviation, and the `size` for sample size in calculations.
- It also introduces the `CORREL` function to calculate the correlation coefficient between two cell ranges.

---

### Primary Explanation
#### Parameters for Confidence Level Calculation

**alpha**
- Represents the significance level used to compute the confidence level.
- The confidence level equals 100 * (1 - alpha)%.
- For example, an alpha of 0.05 indicates a 95 percent confidence level.

**standard_dev**
- Denotes the population standard deviation for the data range.
- It is assumed to be known.

**size**
- Represents the sample size.

#### Remarks
- All arguments must be non-numeric.
- Alpha must be between 0 and 1.
- Standard_dev must be greater than 0.
- Size must be greater than or equal to 1.

---

## 4.7.25 CORREL

### Description
- The `CORREL` function returns the correlation coefficient of the `array1` and `array2` cell ranges.

#### Syntax
```plaintext
CORREL(array1, array2)
```

- `array1`: A cell range of values.
- `array2`: The second cell range of values.

#### Remarks
- `array1` and `array2` must have the same number of data points.
- The equation for the correlation coefficient is:
```plaintext
Correl(X,Y) = \frac{\sum(x-\overline{x})(y-\overline{y})}{\sqrt{\sum(x-\overline{x})^2\sum(y-\overline{y})^2}}
```

---

## API Reference

### Method: CORREL
#### Parameters
- `array1`: The first cell range of values.
- `array2`: The second cell range of values.

#### Returns
- The correlation coefficient as a numeric value.

#### Exceptions
- Throws an error if `array1` and `array2` do not have the same number of data points.

---

### Code Examples

#### C#
```csharp
double correlation = CORREL(range1, range2);
```

---

## Page-level Navigation/TOC (if applicable)
- Possible navigation or reference to related sections like "Confidence Level Calculations" or "Statistical Functions".

---

## Cross References
See also:
- Documentation on Confidence Interval functions.
- Usage of standard deviation and sample size in statistical analysis.

---

<!-- tags: [Syncfusion Winforms, statistics, confidence intervals, correlation, alpha, standard_deviation, sample_size] keywords: [alpha, standard_deviation, sample_size, CORREL, correlation_coefficient, confidence_level, statistical_functions, array1, array2] -->
```