```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_529.jpeg
document_name: chart
page_number: 529
page_id: chart#page_529
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:26Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Calculate F Ratio and compare with F Critical Value to make a decision on the null hypothesis.
- Essential Chart provides support to perform Anova Test using the Anova method in the `BasicStatisticalFormulas` class.
- The AnovaResult class stores the test results, including various statistical metrics like `FRatio` and `FCriticalValue`.

## Content

### Anova Test Calculation
4. Finally, calculate F Ratio as below and get the F Critical Value.

\[ MS_{\text{within}} = \frac{SS_{\text{within}}}{df_{\text{within}}} \]

\[ F = \frac{MS_{\text{among}}}{MS_{\text{within}}} \]

5. Make your decision as below.

- If the between variance is smaller than the within variance, then the means are really close to each other and you will fail to reject the null hypothesis.
- If the F ratio is greater than the F critical value, then the decision will be to reject the null hypothesis and thereby conclude that at least one of the means is different.

### APIs Used

**Essential Chart** provides support to perform Anova Test by implementing a method named `Anova` in the `BasicStatisticalFormulas` class. This method performs the above described calculations and returns the test results as an instance of the `AnovaResult` class. The `AnovaResult` is a class implemented to store the anova test results such as sum of squares, degrees of freedom, and mean squares for different variations, and also stores the `FRatio` and `FCriticalValue` of the test.

Below is a detailed table for the Anova method.

### Anova Method Details

| Method Name   | Parameters                                                                 | Return Values                                                                                                                 |
|---------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Anova         | 1. Probability: the alpha value (probability).                          | An Anova has the following members:                                                                                          |
|               | 2. InputSeries: references to two or more input series. Each series must |                                                                                                                               |
|               | exist in the series collection at the time of the method call, and have  | • DegreeOfFreedomBetweenGroups                                                                                               |
|               | the same number of data points.                                          | • DegreeOfFreedomTotal                                                                                                       |
|               |                                                                           | • DegreeOfFreedomWithinGroups                                                                                               |
|               |                                                                           | • FCriticalValue                                                                                                             |
|               |                                                                           | • FRatio                                                                                                                    |
|               |                                                                           | • MeanSquareVarianceBetweenGroups                                                                                          |
|               |                                                                           | • MeanSquareVarianceWithinGroups                                                                                            |
|               |                                                                           | • SumOfSquaresBetweenGroups                                                                                                 |

## API Reference

### Namespace
- `BasicStatisticalFormulas`

### Class
- `AnovaResult`

#### Members
- `DegreeOfFreedomBetweenGroups`: Degree of freedom between groups.
- `DegreeOfFreedomTotal`: Total degree of freedom.
- `DegreeOfFreedomWithinGroups`: Degree of freedom within groups.
- `FCriticalValue`: Critical value of F-test.
- `FRatio`: F Ratio calculated from the test.
- `MeanSquareVarianceBetweenGroups`: Mean square variance between groups.
- `MeanSquareVarianceWithinGroups`: Mean square variance within groups.
- `SumOfSquaresBetweenGroups`: Sum of squares between groups.
- `Probability`: The alpha value (probability).

### Parameters
1. **Probability**: The alpha value (probability).
2. **InputSeries**: References to two or more input series. Each series must exist in the series collection at the time of the method call, and have the same number of data points.

### Return Values
- An instance of the `AnovaResult` class, containing the above members.

### Summary
The `Anova` method in the `BasicStatisticalFormulas` class enables performing an Analysis of Variance (ANOVA) test, returning comprehensive statistical results that can be used to make informed decisions regarding the null hypothesis.

<!-- tags: [Essential Chart, Anova Test, BasicStatisticalFormulas, AnovaResult, F Critical Value, FRatio, Syncfusion Winforms, version 11.4.0.26] keywords: [Anova, Statistical Formulas, Degrees of Freedom, Null Hypothesis, F Ratio, Mean Square Variance, Probability, Input Series] -->
```