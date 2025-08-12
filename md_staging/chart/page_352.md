```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_352.jpeg
document_name: chart
page_number: 352
page_id: chart#page_352
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:59Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to customize text orientation and color in chart series styles using C# and VB.NET.
- Highlights the use of properties like `TextOrientation` and `TextColor` to enhance visual presentation.
- Includes `See Also` references for additional chart-related topics.

## Content

### Code Examples

#### C#

```csharp
this.chartControl1.Series[1].Styles[0].TextOrientation = ChartTextOrientation.RegionDown;
this.chartControl1.Series[0].Styles[0].TextOrientation = ChartTextOrientation.Up;
this.chartControl1.Series[0].Styles[0].TextColor = Color.Blue;
this.chartControl1.Series[1].Styles[0].TextColor = Color.Red;

this.chartControl1.Series[1].Styles[1].TextOrientation = ChartTextOrientation.Smart;
this.chartControl1.Series[0].Styles[1].TextOrientation = ChartTextOrientation.UpRight;
this.chartControl1.Series[0].Styles[1].TextColor = Color.Green;
this.chartControl1.Series[1].Styles[1].TextColor = Color.Yellow;
```

#### VB.NET

```vb
Private Me.chartControl1.Series(1).Styles(0).TextOrientation = ChartTextOrientation.RegionDown
Private Me.chartControl1.Series(0).Styles(0).TextOrientation = ChartTextOrientation.Up
Private Me.chartControl1.Series(0).Styles(0).TextColor = Color.Blue
Private Me.chartControl1.Series(1).Styles(0).TextColor = Color.Red

Private Me.chartControl1.Series(1).Styles(1).TextOrientation = ChartTextOrientation.Smart
Private Me.chartControl1.Series(0).Styles(1).TextOrientation = ChartTextOrientation.UpRight
Private Me.chartControl1.Series(0).Styles(1).TextColor = Color.Green
Private Me.chartControl1.Series(1).Styles(1).TextColor = Color.Yellow
```

### See Also
- [Chart Types](Chart Types)

## Tooltip Configuration

### 4.5.1.87 Tooltip

Sets the tooltip of the style object associated with the series.

#### Details
The tooltip property can be used to display additional information when the user hovers over specific elements in the chart series.

---

<!-- tags: [chart, textorientation, textcolor, winforms, syncfusion] keywords: [chartcontrol, series, styles, tooltip, textorientation, textcolor] -->
```