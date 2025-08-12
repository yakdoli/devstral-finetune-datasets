```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_533.jpeg
document_name: chart
page_number: 533
page_id: chart#page_533
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:51Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to calculate the correlation coefficient and covariance between two groups of data using built-in formulas in `Syncfusion.Windows.Forms.Chart`.
- Includes examples of code snippets for C# and VB.NET.

## Content

### Example

The below code snippet demonstrates how to get the correlation coefficient between two groups of data (Series1 and Series2) using the in-built formula.

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
............
double Correlation1 =
BasicStatisticalFormulas.Correlation(series1, series2);
```

```vbnet
Imports Syncfusion.Windows.Forms.Chart.Statistics
............
Dim Correlation1 As Double
Correlation1 = BasicStatisticalFormulas.Correlation(series, series1)
```

**Note:** For further details, refer to this Browser Sample:

\[Installed drive]:\Documents and Settings\[User name]\My Documents\Syncfusion\EssentialStudio\[Installed version]\Windows\ Chart.Windows\Samples\2.0\Statistical Analysis\Chart Statistical Formulas

### 4.12.1.3 Covariance

**Covariance** is a statistical formula that measures the extent to which the \( y \) values of two series vary together. It is basically used to measure the fluctuations between two quantities. For a given pairs of series \( y \) values, the covariance can be calculated by taking their differences from their mean values and multiplying these differences together. That is,

\[
\text{Cov}(x,y) = \Sigma\{[x - \Sigma(x)]\, [ y - \Sigma(y) ]\}
\]

If this product is **positive**, then the values would be varying in the same direction; if it is **negative**, then the values would be varying in opposite directions. If the product is **zero**, then we can conclude that there is no linear relationship between the series values. The above formula can be simplified as below.

\[
\text{Cov}(x,y) = \Sigma\{xy\} - \Sigma\{x\} \Sigma\{y\}
\]

### Summary
- Covariance measures the joint variability of two random variables.
- The simplified formula shows how the covariance is computed using sums of products and individual sums.
- A positive covariance indicates a positive linear relationship, a negative covariance indicates a negative linear relationship, and a zero covariance indicates no linear relationship.

## API Reference

### Methods
- `BasicStatisticalFormulas.Correlation`: Calculates the correlation coefficient between two series.
- `BasicStatisticalFormulas.Covariance`: Calculates the covariance between two series.

### Parameters
- `series1`: The first series of data.
- `series2`: The second series of data.

### Returns
- A `double` representing the correlation coefficient or covariance.

### Exceptions
- ArgumentNullException: If the provided series are null.

## Code Examples

### C# Example

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

double Correlation1 = BasicStatisticalFormulas.Correlation(series1, series2);
double Covariance1 = BasicStatisticalFormulas.Covariance(series1, series2);
```

### VB.NET Example

```vbnet
Imports Syncfusion.Windows.Forms.Chart.Statistics

Dim Correlation1 As Double
Correlation1 = BasicStatisticalFormulas.Correlation(series, series1)

Dim Covariance1 As Double
Covariance1 = BasicStatisticalFormulas.Covariance(series1, series2)
```

### See also
- [Syncfusion Documentation](https://www.syncfusion.com/documentation)
- [Statistical Analysis](https://www.syncfusion.com/products/windowsforms/chart/statistics)

## RAG Annotations
<!-- tags: [chart, covariance, correlation, essential studio, windows forms] keywords: [covariance formula, correlation coefficient, statistical formulas, Syncfusion.Windows.Forms.Chart, statistical analysis, built-in formulas] -->
```