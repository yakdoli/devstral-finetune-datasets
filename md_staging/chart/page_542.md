```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_542.jpeg
document_name: chart
page_number: 542
page_id: chart#page_542
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:25Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

| 2. Probability: A double value that gives the confidence level.                                                                                                              | - FirstSeriesMean                                                                                                      |
| 3. FirstInputSeries: A ChartSeries object that stores the first group of data.                                                                                 | - SecondSeriesMean                                                                                                     |
| 4. SecondInputSeries: A ChartSeries object that stores the second group of data. .                                                           | - FirstSeriesVariance                                                                                                   |
|                                                                                                                                         | - SecondSeriesVariance                                                                                                  |
|                                                                                                                                         | - Tvalue                                                                                                               |
|                                                                                                                                         | - DegreeOfFreedom                                                                                                       |
|                                                                                                                                         | - ProbabilityTOneTail                                                                                                   |
|                                                                                                                                         | - TCriticalValueOneTail                                                                                                 |
|                                                                                                                                         | - ProbabilityTTwoTail                                                                                                   |
|                                                                                                                                         | - TCriticalValueTwoTail                                                                                                 |

## Example

Here is a code snippet that shows a sample usage.

### C#

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
TTestResult ttr = BasicStatisticalFormulas.TTestEqualVariances (0.2, 0.05, series1, series2);
```

### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim ttr As TTestResult = BasicStatisticalFormulas.TTestEqualVariances (0.2, 0.05, series1, series2)
```

### 4.12.1.8.2 T-Test with UnEqual Variance

If the assumption of 'equal variances' is violated, then we have to compute the test statistic using the individual sample's standard deviation instead of pooled standard deviation. Like the TTestEqualVariances formula, the TTestUnequalVariances formula also will be carried out on two independent samples. The only difference with unequal variances test is that the sample should be of different sizes.

#### Steps to perform the test

1. Specify the null hypothesis and alternate hypothesis.

## API Reference

### Methods
- TTestEqualVariances(Double Probability, Double ConfidenceLevel, ChartSeries FirstInputSeries, ChartSeries SecondInputSeries)
  - **Parameters**
    - Probability: A double value that gives the confidence level.
    - FirstInputSeries: A ChartSeries object that stores the first group of data.
    - SecondInputSeries: A ChartSeries object that stores the second group of data.

  - **Returns**
    - TTestResult object containing the following properties:
      - FirstSeriesMean
      - SecondSeriesMean
      - FirstSeriesVariance
      - SecondSeriesVariance
      - Tvalue
      - DegreeOfFreedom
      - ProbabilityTOneTail
      - TCriticalValueOneTail
      - ProbabilityTTwoTail
      - TCriticalValueTwoTail

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
TTestResult ttr = BasicStatisticalFormulas.TTestEqualVariances (0.2, 0.05, series1, series2);
```

### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim ttr As TTestResult = BasicStatisticalFormulas.TTestEqualVariances (0.2, 0.05, series1, series2)
```

## Conclusion

This section covers the usage of T-Tests with both equal and unequal variances in the Syncfusion Chart for Windows Forms. The examples and methods provided demonstrate how to perform such statistical tests in a practical manner.

## Related Information
- Refer to the Syncfusion documentation for more detailed examples and explanations of the T-Test formulas.
- Ensure proper handling of statistical assumptions and validation of data.

<!-- tags: [syncfusion-sdk, winforms, chart, statistical-analysis, t-test, unequal-variances, api] keywords: [ttest, statistics, confidence level, chartseries, degree of freedom, probability] -->
```