```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_234.jpeg
document_name: XlsIO
page_number: 234
page_id: XlsIO#page_234
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:03Z
fidelity: lossless
-->

## Example Code for Chart Customization

### Chart Styling and Configuration

The following code snippet demonstrates how to customize various aspects of a chart in XlsIO, including the color of the side wall, fill type and pattern of the floor, data labels, chart positions, and legends.

```csharp
// Set border line color of the side wall
chart.SideWall.Border.LineColor = System.Drawing.Color.Beige

// Set fill type of floor
chart.Floor.Fill.FillType = ExcelFillType.Pattern

// Set pattern type of the floor
chart.Floor.Fill.Pattern = ExcelGradientPattern.Pat_Divot

// Set foreground and background color of the floor
chart.Floor.Fill.ForeColor = System.Drawing.Color.Blue
chart.Floor.Fill.BackColor = System.Drawing.Color.White

// Set thickness of the floor
chart.Floor.Thickness = 3

// Show value as data labels
serieOne.DataPoints.DefaultDataPoint.DataLabels.IsValue = True
serieTwo.DataPoints.DefaultDataPoint.DataLabels.IsValue = True

// Set embedded chart positions
chart.TopRow = 2
chart.BottomRow = 30
chart.LeftColumn = 5
chart.RightColumn = 18
serieTwo.Name = "Temperature,deg.F"

// Set chart legends
chart.Legend.Position = ExcelLegendPosition.Right
chart.Legend.IsVerticalLegend = False
```

This code provides a comprehensive guide to styling and positioning elements within a chart, ensuring readability and visual appeal. Each section addresses specific customization options for charts in XlsIO.
```