```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_534.jpeg
document_name: chart
page_number: 534
page_id: chart#page_534
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:52Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains how to calculate covariance using the `Covariance` method in the `BasicStatisticalFormulas` class.
- Provides a table detailing the method parameters and return value.
- Includes code examples in both C# and VB.NET for demonstrating the usage of the `Covariance` method.
- Recommends further exploration of samples for additional insights.

## Content

### Using the Formula

#### Overview of the Covariance Method

The Covariance can easily be calculated by using the `Covariance` method available with the `BasicStatisticalFormulas` class. The following table describes the details of this method.

| **Method Name** | **Parameters** | **Return Value** |
|------------------|----------------|------------------|
| **Covariance**   |  - 1. `FirstInputSeriesName`: A ChartSeries object that stores the first group's data. <br> - 2. `SecondInputSeriesName`: A ChartSeries object that stores the second group's data. An exception will be raised if the input series do not have the same number of data points. | A `double` value that represents the covariance value between the two groups of data. |

#### Example

Here is the code snippet that demonstrates the usage of this method.

##### C# Example

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
............
double Covariance1 =
Statistics.BasicStatisticalFormulas.Covariance(series1, series2);
```

##### VB.NET Example

```vb.net
Imports Syncfusion.Windows.Forms.Chart.Statistics
............
Dim Covariance1 As Double
Covariance1 = BasicStatisticalFormulas.Covariance(series, series1)
```

#### Additional Notes

> **Note:** For further details, refer to this Browser Sample:  
>  
> ```
> [Installed drive]:\Documents and Settings\[User name]\My Documents\Syncfusion\EssentialStudio\[Installed version]\WindowsChart.Windows\Samples\2.0\Statistical Analysis\Chart Statistical Formulas
> ```

## Page-level Navigation/TOC (if applicable)
- **Using the Formula**
  - Overview of the Covariance Method
  - Example
    - C# Example
    - VB.NET Example
  - Additional Notes

## Cross References
- **Covariance**
- **BasicStatisticalFormulas**
- **ChartSeries**
- **Data Points**
- **Statistical Analysis**

<!-- tags: [Windows Forms, Chart, Covariance, BasicStatisticalFormulas, ChartSeries, Data Points, Statistical Analysis] keywords: [Covariance, BasicStatisticalFormulas, ChartSeries, Data Points, Statistical Analysis, Syncfusion, Windows Forms] -->
```