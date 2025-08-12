```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_240.jpeg
document_name: XlsIO
page_number: 240
page_id: XlsIO#page_240
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:28Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
sheet.Range("D5").Number = 89
sheet.Range("D6").Number = 64
sheet.Range("E2").Number = 67
sheet.Range("E3").Number = 44
sheet.Range("E4").Number = 23
sheet.Range("E5").Number = 53
sheet.Range("E6").Number = 55

'Chart is added in sheet-1.
Dim chart As IChartShape = sheet.Charts.Add()

' Setting the chart DataRange.
chart.DataRange = sheet.Range("A1:E6")
' Change the chart seriesInRows.
chart.IsSeriesInRows = False

' Setting the chart type.
chart.ChartType = ExcelChartType.Column_Clustered_3D

' Get the series and categories from the chart.
Dim series As IChartSeries = chart.Series
Dim categories As IChartCategories = chart.Categories

' Set the Backwall fill option.
chart.BackWall.Fill.FillType = ExcelFillType.Gradient
chart.BackWall.Fill.GradientColorType = ExcelGradientColor.TwoColor
chart.BackWall.Fill.GradientStyle = ExcelGradientStyle.Diagonal_Down
chart.BackWall.Fill.ForeColor = System.Drawing.Color.WhiteSmoke
chart.BackWall.Fill.BackColor = System.Drawing.Color.LightBlue
chart.BackWall.Thickness = 10

' Set the sidewall foreground and backcolor.
chart.SideWall.Fill.FillType = ExcelFillType.SolidColor
chart.SideWall.Fill.BackColor = System.Drawing.Color.White
```

## Page-level Navigation/TOC (if applicable)

### WinForms-specific conventions

- The code snippet demonstrates how to create and customize a 3D clustered column chart in an Excel sheet using Syncfusion's XlsIO library.

## API Reference (if applicable)

### Namespace: Syncfusion.XlsIO.Excel

#### Class: IChartShape

##### Properties:
- **DataRange**: Defines the range of data used in the chart.
- **IsSeriesInRows**: Determines whether the chart data is arranged in rows.
- **ChartType**: Specifies the type of chart to be created.
- **BackWall.Fill.FillType**: Defines the fill type for the back wall.
- **BackWall.Fill.GradientColorType**: Specifies the type of gradient for the back wall.
- **BackWall.Fill.GradientStyle**: Determines the gradient style for the back wall.
- **BackWall.Fill.ForeColor**: Sets the foreground color for the back wall.
- **BackWall.Fill.BackColor**: Sets the background color for the back wall.
- **BackWall.Thickness**: Sets the thickness of the back wall.
- **SideWall.Fill.FillType**: Defines the fill type for the side wall.
- **SideWall.Fill.BackColor**: Sets the background color for the side wall.

## Code Examples (multi-language supported)

```csharp
// Example of creating a 3D clustered column chart
sheet.Range("D5").Number = 89
sheet.Range("D6").Number = 64
sheet.Range("E2").Number = 67
sheet.Range("E3").Number = 44
sheet.Range("E4").Number = 23
sheet.Range("E5").Number = 53
sheet.Range("E6").Number = 55

Dim chart As IChartShape = sheet.Charts.Add()
chart.DataRange = sheet.Range("A1:E6")
chart.IsSeriesInRows = False
chart.ChartType = ExcelChartType.Column_Clustered_3D
Dim series As IChartSeries = chart.Series
Dim categories As IChartCategories = chart.Categories
chart.BackWall.Fill.FillType = ExcelFillType.Gradient
chart.BackWall.Fill.GradientColorType = ExcelGradientColor.TwoColor
chart.BackWall.Fill.GradientStyle = ExcelGradientStyle.Diagonal_Down
chart.BackWall.Fill.ForeColor = System.Drawing.Color.WhiteSmoke
chart.BackWall.Fill.BackColor = System.Drawing.Color.LightBlue
chart.BackWall.Thickness = 10
chart.SideWall.Fill.FillType = ExcelFillType.SolidColor
chart.SideWall.Fill.BackColor = System.Drawing.Color.White
```

## Tags and Keywords

<!-- tags: [Syncfusion, XlsIO, WinForms, Chart, 3D, Column, Gradient, Fill, Backwall, SideWall] keywords: [ExcelChartType, IChartShape, DataRange, IsSeriesInRows, BackWall, SideWall, FillType, GradientColorType, GradientStyle, ForeColor, BackColor, Thickness] -->
```