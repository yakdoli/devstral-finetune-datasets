```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_332.jpeg
document_name: grid
page_number: 332
page_id: grid#page_332
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:24Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Pearson product moment correlation coefficient and Percentile calculations explained.
- Details on how to use `PEARSON` and `PERCENTILE` functions in the context of data analysis.

## Content

### PEARSON Function

#### Syntax
`PEARSON(array1, array2)`, where:

- `array1` is a set of independent values.
- `array2` is a set of dependent values.

#### Remarks
- The arguments must be either numbers or names, array constants, or references that contain numbers.
- The formula for the Pearson product moment correlation coefficient, r, is:

\[
r = \frac{\sum (x - \overline{x})(y - \overline{y})}{\sqrt{\sum (x - \overline{x})^2 \sum (y - \overline{y})^2}}
\]

where x-bar and y-bar are the sample means `AVERAGE(array1)` and `AVERAGE(array2)`.

---

### PERCENTILE Function

#### Syntax
`PERCENTILE(array, k)`, where:

- `array` is the array or range of data that defines relative standing.
- `k` is the percentile value in the range 0..1, inclusive.

#### Remarks
- `k` must be >=10 and <= 1.
- If `k` is not a multiple of 1/(n - 1), `PERCENTILE` interpolates to determine the value at the k-th percentile.

## API Reference (if applicable)
For more detailed information on these functions, refer to the documentation provided by Syncfusion for Essential Grid for Windows Forms. These functions are generally available in the context of data manipulation and statistical analysis.

## Code Examples (multi-language supported)
This section includes examples of how to use the `PEARSON` and `PERCENTILE` functions in your code.

```csharp
// Example: Calculating Pearson correlation coefficient
double[] array1 = {1.0, 2.0, 3.0, 4.0};
double[] array2 = {2.0, 4.0, 6.0, 8.0};
double pearsonCorrelation = Pearson(array1, array2);
Console.WriteLine($"Pearson Correlation: {pearsonCorrelation}");

// Example: Calculating Percentile
double[] dataArray = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0};
double percentileValue = Percentile(dataArray, 0.25);
Console.WriteLine($"25th Percentile: {percentileValue}");
```

## Page-level Navigation/TOC (if applicable)
- [Pearson Function](#pearson-function)
- [Percentile Function](#percentile-function)

## Cross References
See also:
- [Statistical Functions Overview](#statistical-functions-overview)

<!-- tags: [syncfusion-sdk, syncfusion-winforms, statistical-functions, pearson, percentile] keywords: [pearson, percentile, statistical functions, essential grid] -->
```