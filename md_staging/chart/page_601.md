```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_601.jpeg
document_name: chart
page_number: 601
page_id: chart#page_601
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:32Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Chart displaying Coordinate value at a Client Point.
- Methods to get Chart value or client coordinates.

## Content

### Chart displaying Coordinate value at a Client Point

#### Code snippet for the above sample

[C#]

```csharp
// Chartcontrol mouse move event.
private void chartControl_MouseMove(object sender, System.Windows.Forms.MouseEventArgs e)
{
    ChartPoint chpt = this.chartControl.ChartArea.GetValueByPoint(new Point(e.X, e.Y));
    string text = "Result of method GetValueByPoint - {" + chpt.X.ToString() + "," + chpt.YValues[0].ToString() + "}";
    toolTip.SetToolTip(chartControl, text);
}
```

[VB.NET]

```vb
' ChartControl mouse move event.
Private Sub chartControl_MouseMove(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventArgs)
    Dim chpt As ChartPoint = Me.chartControl.ChartArea.GetValueByPoint(New Point(e.X, e.Y))
    Dim [text] As String = "Result of method GetValueByPoint - {" + chpt.X.ToString() + "," + chpt.YValues(0).ToString() + "}"
    toolTip.SetToolTip(chartControl, text)
End Sub
```

#### GetPointByValue()

The GetPointByValue method does the opposite of the above—given a chart coordinate it returns the client co-ordinate corresponding to that chart point.

### 4.18.2 LegendItem By Point

#### Get LegendItem By Point

The Legend.GetLegendItemBy method will let you get the reference to a legend item at a specific point. Implementing the below code sample will display a tooltip with the legend item name, on which the user mouse hovers.

```csharp
```

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Chart] keywords: [MouseMove, ChartPoint, GetValueByPoint, GetPointByValue, Legend, GetLegendItemBy, Tooltip] -->
```
