```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_233.jpeg
document_name: XlsIO
page_number: 233
page_id: XlsIO#page_233
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:04Z
fidelity: lossless
-->

# Essential XlsIO

```vb
'Add a new chart to the existing worksheet
Dim chart As IChartShape = workbook.Worksheets(0).Charts(0)

'Set chart series
Dim serieOne As IChartSerie = chart.Series(0)
Dim serieTwo As IChartSerie = chart.Series(1)

'Set fill type of back wall
chart.BackWall.Fill.FillType = ExcelFillType.Gradient

'Set fill options for the back wall
chart.BackWall.Fill.GradientColorType = ExcelGradientColor.TwoColor
chart.BackWall.Fill.GradientStyle = ExcelGradientStyle.Diagonl_Down

'set the foreground and background color of the back wall
chart.BackWall.Fill.ForeColor = System.Drawing.Color.WhiteSmoke
chart.BackWall.Fill.BackColor = System.Drawing.Color.LightBlue

'Set border line color of the back wall
chart.BackWall.Border.LineColor = System.Drawing.Color.Wheat

'Set thickness of the back wall
chart.BackWall.Thickness = 10

'Set fill type of side wall
chart.SideWall.Fill.FillType = ExcelFillType.SolidColor

'Set foreground and backcolor of the side wall
chart.SideWall.Fill.BackColor = System.Drawing.Color.White
chart.SideWall.Fill.ForeColor = System.Drawing.Color.White
```
