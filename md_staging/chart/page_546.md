```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_546.jpeg
document_name: chart
page_number: 546
page_id: chart#page_546
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:45Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Paired t-Test Properties

- ProbabilityTOneTail
- TCriticalValueOneTail
- ProbabilityTTwoTail
- TCriticalValueTwoTail

#### Example

Here is a code snippet that shows a sample usage.

**C#**

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

TTestResult ttr = BasicStatisticalFormulas.TTestPaired(0.2, 0.05, series1, series2);
```

**VB.NET**

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics

Dim ttr As TTestResult = BasicStatisticalFormulas.TTestPaired(0.2, 0.05, series1, series2)
```

### 4.12.1.9 Variance

#### Overview

Variance is a statistical formula that calculates the variance of series y values. A Variance can be defined as the square of the standard deviation of a sample.

#### Using the Formula

The variance can be computed for any series by using the method `Variance` of `BasicStatisticalFormulas` class. Below table shows the details of this method.

## API Reference (if applicable)
- **Namespace**: `Syncfusion.Windows.Forms.Chart.Statistics`
- **Class**: `BasicStatisticalFormulas`
- **Method**: `Variance`

### Parameters

| Name | Type | Description |
|------|------|-------------|
| yValues | double[] | The series y values for which the variance is to be computed. |

### Returns

| Type | Description |
|------|-------------|
| double | The computed variance of the series y values. |

### Code Examples

**C#**

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

double[] yValues = { 1.0, 2.0, 3.0, 4.0, 5.0 };
double variance = BasicStatisticalFormulas.Variance(yValues);
```

**VB.NET**

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics

Dim yValues As Double() = {1.0, 2.0, 3.0, 4.0, 5.0}
Dim variance As Double = BasicStatisticalFormulas.Variance(yValues)
```

<!-- tags: [syncfusion, winforms, chart, statistics, variance, ttest, C# examples, VB.NET examples] -->
```