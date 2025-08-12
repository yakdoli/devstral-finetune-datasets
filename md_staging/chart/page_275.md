```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_275.jpeg
document_name: chart
page_number: 275
page_id: chart#page_275
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:03Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Properties Overview

| Details |
| --- |
| **Possible Values** | - Open - Points only the opening value of that period.<br/> - Close - Points out the closing value of that period.<br/> - Both - Points out both the opening and the closing values of that period. |
| **Default Value** | Both |
| **2D / 3D Limitations** | No |
| **Applies to Chart Element** | Any Series points |
| **Applies to Chart Types** | HiLoOpenClose Chart |

## Code Snippet for OpenCloseDrawMode

Here is the code snippet using OpenCloseDrawMode.

### C#

```csharp
ChartSeries CS1 = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.HiLoOpenClose);
CS1.Points.Add(date, 456, 214, 364, 386);
CS1.Points.Add(date.AddDays(1), 491, 234, 321, 378);
CS1.Points.Add(date.AddDays(2), 482, 193, 302, 352);
CS1.Points.Add(date.AddDays(3), 437, 243, 354, 391);
CS1.Points.Add(date.AddDays(4), 421, 223, 317, 367);
CS1.Points.Add(date.AddDays(5), 434, 263, 339, 385);
this.chartControl1.Series.Add(CS1);
this.chartControl1.Series[0].OpenCloseDrawMode = ChartOpenCloseDrawMode.Open;
```

### VB.NET

```vb
Dim CS1 As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.HiLoOpenClose)
CS1.Points.Add(date, 456, 214, 364, 386)
CS1.Points.Add(date.AddDays(1), 491, 234, 321, 378)
CS1.Points.Add(date.AddDays(2), 482, 193, 302, 352)
CS1.Points.Add(date.AddDays(3), 437, 243, 354, 391)
CS1.Points.Add(date.AddDays(4), 421, 223, 317, 367)
CS1.Points.Add(date.AddDays(5), 434, 263, 339, 385)
```

## References

- © 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion Winforms, Chart, HiLoOpenClose Chart, OpenCloseDrawMode, C#, VB.NET] keywords: [chart, hi-lo-open-close, open-close-draw-mode, csharp, vb.net, series, chart series type, chart series properties] -->
```