```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_552.jpeg
document_name: chart
page_number: 552
page_id: chart#page_552
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:05Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Introduces the cumulative beta distribution formula and its use in chart controls.
- Explains the BetaCumulativeDistribution method and its parameters.
- Provides examples in C# and VB.NET for plotting the cumulative beta distribution.

## Content

### Mathematical Formula
The cumulative beta distribution $ F(x; \alpha, \beta) $ is defined as:

\[
F(x; \alpha, \beta) = \frac{\text{B}_x(\alpha, \beta)}{\text{B}(\alpha, \beta)}
\]

where $\text{B}_x(\alpha, \beta)$ is the incomplete beta function and $\text{I}_x(\alpha, \beta)$ is the regularized incomplete beta function.

### Using the Formula

#### The BetaCumulativeDistribution Method
- The BetaCumulativeDistribution method of the UtilityFunctions class returns the cumulative beta distribution for $ x >= 0 $, $ \alpha > 0 $, and $ \beta > 0 $.

#### Parameters and Return Value
| Method Name                         | Parameters                                                  | Return Value                                          |
|-------------------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| BetaCumulativeDistribution         | 1. $\alpha$: The lower limit.                              | A double that represents the cumulative beta distribution. |
|                                     | 2. $\beta$: The upper limit.                               |                                                       |
|                                     | 3. $x$: The value for which the distribution has to be calculated. |                                                       |

### Example

#### Sample Usage
Here is a code snippet that shows how to use the BetaCumulativeDistribution method:

#### C#
```csharp
ChartSeries series = this.ChartControl1.Model.NewSeries("a=b=0.5");
for(double i=0;i<=1;i=i+0.1)
{
    // Calculate Beta cumulative function for a points and plot the points in chart control.
    series.Points.Add(i, Syncfusion.Windows.Forms.Chart.Statistics.UtilityFunctions.BetaCumulativeDistribution(0.5,0.5,i));
}
series.Type = ChartSeriesType.Spline;
series.Text = series.Name;
this.ChartControl1.Series.Add(series);
```

#### VB.NET
```vb
' Calculate Beta cumulative function for a points and plot the points in chart control.
Dim series As ChartSeries = Me.ChartControl1.Model.NewSeries("a=b=0.5")
For i As Double = 0 To 1 Step 0.1
End For
series.Type = ChartSeriesType.Spline
series.Text = series.Name
Me.ChartControl1.Series.Add(series)
```

## API Reference

### UtilityFunctions Class

#### BetaCumulativeDistribution Method
##### Parameters
- $\alpha$: The lower limit.
- $\beta$: The upper limit.
- $x$: The value for which the distribution has to be calculated.

##### Return Type
- `double`: Represents the cumulative beta distribution for the given parameters.

## Code Examples
The examples demonstrate the usage of the BetaCumulativeDistribution method in both C# and VB.NET, plotting the distribution in a chart control.

### C# Example
The example shows how to use the BetaCumulativeDistribution method to plot the cumulative beta distribution for a range of values in a chart.

### VB.NET Example
Similar to the C# example, the VB.NET example demonstrates the same functionality in a different language.

## Page-level Navigation/TOC
- [Using the Formula](#using-the-formula)
- [Example](#example)

## Cross References
See also: Cumulative Distribution Functions, Chart Controls, Statistical Functions.

<!-- tags: [syncfusion, winforms, chart, cumulative-distribution, utilityfunctions, betacumulativedistribution] keywords: [beta distribution, cumulative distribution, chart control, statistical functions, code examples] -->
```