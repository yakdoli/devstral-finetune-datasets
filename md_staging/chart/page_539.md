```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_539.jpeg
document_name: chart
page_number: 539
page_id: chart#page_539
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:46:41Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

double Deviation1 = BasicStatisticalFormulas.StandardDeviation(series1, false);
```

```vb.net
Imports Syncfusion.Windows.Forms.Chart.Statistics

Dim Deviation1 As Double
Deviation1 = BasicStatisticalFormulas.StandardDeviation(series1, false)
```

**Note:** For further details, refer to this Browser Sample:

```
[Installed drive]:\Documents and Settings\[User name]\My Documents\Syncfusion\EssentialStudio\[Installed version]\Windows\Chart.Windows\Samples\2.0\Statistical Analysis\Chart Statistical Formulas
```

## 4.12.1.8 T-Tests

**TTest** is a statistical formula that is used to measure the equality between the means of two series. In other words, the T test compares the actual difference between two means in relation to the variation in data that can be measured by calculating the standard deviation of the difference between the means.

It is a statistical test used to test the null hypothesis that the means of two normally distributed populations are equal. This test can be performed on two given samples(series), each characterized by its mean, standard deviation and number of data points, to determine whether the means are distinct based on the assumption that the underlying distributions are normal.

### Different T-Tests

There are different versions of T tests depending on whether the samples are:

- **independent** of each other, (where the series are random with no relationship between each other)

## API Reference

For detailed API documentation, please refer to the [Syncfusion WinForms API Reference](https://help.syncfusion.com/windowsforms).

## Code Examples

- **C# Example**
  ```csharp
  using Syncfusion.Windows.Forms.Chart.Statistics;
  
  double independentSample1Mean = 50;
  double independentSample2Mean = 55;
  double independentSample1StdDev = 5;
  double independentSample2StdDev = 6;
  int independentSample1Count = 30;
  int independentSample2Count = 30;
  
  double tStatistic;
  double pValue;
  
  TTests.Independent(tStatistic, pValue, 
                     independentSample1Mean, independentSample1StdDev, independentSample1Count,
                     independentSample2Mean, independentSample2StdDev, independentSample2Count);
  
  Console.WriteLine($"T-Statistic: {tStatistic}");
  Console.WriteLine($"P-Value: {pValue}");
  ```

  **Output:**
  ```
  T-Statistic: [computed value]
  P-Value: [computed value]
  ```

- **VB.NET Example**
  ```vb.net
  Imports Syncfusion.Windows.Forms.Chart.Statistics
  
  Dim independentSample1Mean As Double = 50
  Dim independentSample2Mean As Double = 55
  Dim independentSample1StdDev As Double = 5
  Dim independentSample2StdDev As Double = 6
  Dim independentSample1Count As Integer = 30
  Dim independentSample2Count As Integer = 30
  
  Dim tStatistic As Double
  Dim pValue As Double
  
  TTests.Independent(tStatistic, pValue, 
                     independentSample1Mean, independentSample1StdDev, independentSample1Count,
                     independentSample2Mean, independentSample2StdDev, independentSample2Count)
  
  Console.WriteLine($"T-Statistic: {tStatistic}")
  Console.WriteLine($"P-Value: {pValue}")
  ```

  **Output:**
  ```
  T-Statistic: [computed value]
  P-Value: [computed value]
  ```

### See also:
- [Statistical Formulas API Documentation](https://help.syncfusion.com/windowsforms/chart/statistical-formulas)
- [T-Tests in Statistical Analysis](https://help.syncfusion.com/windowsforms/chart/t-tests)

```

## Conclusion

This section provides an overview of T-Tests and their implementation within the Syncfusion Windows Forms Statistical Analysis tools. By performing T-Tests, developers can effectively analyze and compare the means of datasets to determine statistical significance.

<!-- tags: [syncfusion, winforms, chart, statistical analysis, t-tests, api] keywords: [ttests, statistical formulas, independent samples, standard deviation, null hypothesis, normal distribution, samples, series, means, variation] -->
```