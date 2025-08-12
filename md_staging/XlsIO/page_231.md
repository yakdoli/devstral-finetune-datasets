```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_231.jpeg
document_name: XlsIO
page_number: 231
page_id: XlsIO#page_231
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:41Z
fidelity: lossless
-->

# Chart Customization in XlsIO

## Overview
- Configures the appearance of a chart in XlsIO, including the back wall, side wall, floor, and data labels.
- Details include setting the border line color, thickness, fill type, pattern, and colors.
- Demonstrates how to display data labels for chart series.

## Content

```csharp
chart.BackWall.Border.LineColor = System.Drawing.Color.Wheat;

//Set thickness of the back wall
chart.BackWall.Thickness = 10;

//Set fill type of side wall
chart.SideWall.Fill.FillType = ExcelFillType.SolidColor;

//Set the foreground and background colors of the side wall
chart.SideWall.Fill.BackColor = System.Drawing.Color.White;
chart.SideWall.Fill.ForeColor = System.Drawing.Color.White;

//Set border line color of the side wall
chart.SideWall.Border.LineColor = System.Drawing.Color.Beige;

//Set fill type of floor
chart.Floor.Fill.FillType = ExcelFillType.Pattern;

//Set pattern type of the floor
chart.Floor.Fill.Pattern = ExcelGradientPattern.Pat_Divot;

//Set the foreground and background color of the floor
chart.Floor.Fill.ForeColor = System.Drawing.Color.Blue;
chart.Floor.Fill.BackColor = System.Drawing.Color.White;

//Set thickness of the floor
chart.Floor.Thickness = 3;

//Show value as data labels
serieOne.DataPoints.DefaultDataPoint.DataLabels.IsValue = true;
serieTwo.DataPoints.DefaultDataPoint.DataLabels.IsValue = true;
```

## RAG Annotations
<!-- tags: [XlsIO, chart customization, side wall, floor, data labels, Syncfusion Winforms, version: 11.4.0.26] keywords: [chart appearance, fill type, pattern, foreground, background, thickness, line color] -->
```