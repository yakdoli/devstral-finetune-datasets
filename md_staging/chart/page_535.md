```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_535.jpeg
document_name: chart
page_number: 535
page_id: chart#page_535
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:46:19Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- A section focused on performing an F-Test using the `BasicStatisticalFormulas` class in Syncfusion Winforms.
- Explains the hypothesis testing procedure for comparing the variances of two data series.
- Provides details on the `FTest` method with parameters and return values, along with an example usage.

## Content

### 4.12.1.4 F-Test

The F-Test is a statistical test used to determine whether two series have the same standard deviation at a specified confidence level. This is achieved by comparing the variances of the series values and, consequently, their standard deviations. The null hypothesis assumes that the two variances are equal. All hypothesis testing is conducted under the assumption that the null hypothesis is true.

#### Steps to perform F-Test

1. Calculate the variances of both the series.
2. Calculate the F Ratio as given below.

\[
F \, \text{Value} = \frac{\text{firstSeriesVariance}}{\text{secondSeriesVariance}}
\]

The F-Test can be easily performed using the `FTest` method of the `BasicStatisticalFormulas` class, which returns the results as an object of type `FTestResult`. The `FTestResult` class is designed to save the F test result, including the FValue and other computational results such as series means, series variances, FRatio, and FCriticalValue of the test. Below is a detailed table for the `FTest` method.

| Method Name      | Parameters                                                  | Returns                                                                 |
|-------------------|-------------------------------------------------------------|-------------------------------------------------------------------------|
| FTest            | 1. **Probability**: Probability that gives the confidence level. <br> 2. **FirstInputSeries**: Type of ChartSeries object that represents the first group of data. <br> 3. **SecondInputSeries**: Type of ChartSeries object that represents the second group of data. | An `FTestResult` has the following members: <br> - FirstSeriesMean <br> - SecondSeriesMean <br> - FirstSeriesVariance <br> - SecondSeriesVariance <br> - FValue <br> - ProbabilityFOneTail <br> - F CriticalValueOneTail |

#### Example

Here is a code snippet that shows a sample usage.

```csharp
FTestResult ttr =
Syncfusion.Windows.Forms.Chart.Statistics.BasicStatisticalFormulas.FTest
```

### WinForms-specific conventions
- Precise usage of `Syncfusion.Windows.Forms.Chart.Statistics.BasicStatisticalFormulas` namespace for statistical operations.
- Emphasis on performing F-Tests and interpreting results using the `FTest` method.
- Highlighted support for handling statistical data series through the `ChartSeries` objects.

### API Reference

#### FTest Method
- **Namespace**: Syncfusion.Windows.Forms.Chart.Statistics
- **Class**: BasicStatisticalFormulas
- **Parameters**:
  - **Probability**: Type
  - **FirstInputSeries**: ChartSeries
  - **SecondInputSeries**: ChartSeries
- **Returns**: FTestResult

### Code Examples

```csharp
using Syncfusion.Windows.Forms.Chart;
using Syncfusion.Windows.Forms.Chart.Statistics.BasicStatisticalFormulas;

// Example usage of FTest method
public void PerformFTest()
{
    // Assume the existence of two data series
    ChartSeries series1 = new ChartSeries();
    ChartSeries series2 = new ChartSeries();

    // Populate the series with data
    // ... populate series here ...

    // Perform the F-Test
    FTestResult ttr = BasicStatisticalFormulas.FTest(0.05, series1, series2);

    // Access the results
    Console.WriteLine($"FValue: {ttr.FValue}");
    Console.WriteLine($"Probability One Tail: {ttr.ProbabilityFOneTail}");
    Console.WriteLine($"FCriticalValue One Tail: {ttr.FCriticalValueOneTail}");
}
```

<!-- tags: [Syncfusion Winforms, F-Test, Statistical Analysis, Hypothesis Testing, variance comparison, BasicStatisticalFormulas, FTestResult, Probability, ChartSeries, C#] keywords: [F-Test, Statistical test, Hypothesis testing, variance comparison, probability level, Statistical formulas, ChartSeries, FValue, ProbabilityFOneTail, FCriticalValueOneTail] -->
```