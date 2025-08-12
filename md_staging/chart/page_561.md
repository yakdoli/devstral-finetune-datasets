```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_561.jpeg
document_name: chart
page_number: 561
page_id: chart#page_561
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:10Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
series.Type = ChartSeriesType.Spline
series.Text = series.Name
Me.ChartControl1.Series.Add(series)
```

## 4.12.2.10 Inverse Error Function

The Inverse Error function, which is a rational approximation of the error function, gives the element-by-element inverse of the error function. The absolute value of the relative error is less than \(1.15 \times 10^{-9}\) in the entire region.

### Using the formula

The below table describes this function in detail.

| **Method Name**       | **Parameters**             | **Return Value**                              |
|------------------------|----------------------------|-----------------------------------------------|
| InverseErrorFunction   | \(x\) must be less than \(1.15 \times 10^{-9}\) | A double that gives the inverse of error function. |

### Example

Here is a code snippet that shows a sample usage.

#### C#

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
int double = UtilityFunctions.InverseErf(x);
```

#### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim double as result = UtilityFunctions.InverseErf(x)
```

## 4.12.2.11 Inverse F Cumulative Distribution

This formula returns the inverse of the F cumulative distribution.

### Using the Formula
```