```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_237.jpeg
document_name: XlsIO
page_number: 237
page_id: XlsIO#page_237
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:14Z
fidelity: lossless
-->

### Code Example for Creating a 3D Column Chart

The following example demonstrates how to create a 3D clustered column chart in a spreadsheet using Syncfusion's XlsIO library. 

```csharp
sheet.Range["E3"].Number = 44;
sheet.Range["E4"].Number = 23;
sheet.Range["E5"].Number = 53;
sheet.Range["E6"].Number = 55;

//Chart is added in sheet-1.
IChartShape chart = sheet.Charts.Add();

//Setting the chart DataRange.
chart.DataRange = sheet.Range["A1:E6"];

//Change the chart seriesInRows.
chart.IsSeriesInRows = false;

//Setting the Chart Type.
chart.ChartType = ExcelChartType.Column_Clustered_3D;

//Get the series and categories from the chart.
IChartSeries series = chart.Series;
IChartCategories categories = chart.Categories;

//Set the Backwall fill option.
chart.BackWall.Fill.FillType = ExcelFillType.Gradient;
chart.BackWall.Fill.GradientColorType = ExcelGradientColor.TwoColor;
chart.BackWall.Fill.GradientStyle = ExcelGradientStyle.Diagonal_Down;
chart.BackWall.Fill.ForeColor = System.Drawing.Color.WhiteSmoke;
chart.BackWall.Fill.BackColor = System.Drawing.Color.LightBlue;
chart.BackWall.Thickness = 10;

//Set the sidewall foreground and backcolor.
chart.SideWall.Fill.FillType = ExcelFillType.SolidColor;
chart.SideWall.Fill.BackColor = System.Drawing.Color.White;
chart.SideWall.Fill.ForeColor = System.Drawing.Color.White;
```

---

## API Reference

### Properties Used

#### `Range.Number`
- **Type**: `double`
- **Description**: Sets the numeric value of the specified range.

#### `Charts.Add()`
- **Return Type**: `IChartShape`
- **Description**: Adds a new chart to the spreadsheet and returns the chart object.

#### `Chart.DataRange`
- **Type**: `Range`
- **Description**: Sets the data range for the chart.

#### `Chart.IsSeriesInRows`
- **Type**: `bool`
- **Description**: Determines whether the chart data is in rows or columns.

#### `Chart.ChartType`
- **Type**: `ExcelChartType`
- **Description**: Sets the type of the chart.

#### `Chart.Series`
- **Type**: `IChartSeries`
- **Description**: Represents the series in the chart.

#### `Chart.Categories`
- **Type**: `IChartCategories`
- **Description**: Represents the categories in the chart.

#### `Chart.BackWall.Fill.FillType`
- **Type**: `ExcelFillType`
- **Description**: Sets the fill type for the back wall of the chart.

#### `Chart.BackWall.Fill.GradientColorType`
- **Type**: `ExcelGradientColor`
- **Description**: Sets the gradient color type for the back wall.

#### `Chart.BackWall.Fill.GradientStyle`
- **Type**: `ExcelGradientStyle`
- **Description**: Sets the gradient style for the back wall.

#### `Chart.BackWall.Fill.ForeColor`
- **Type**: `Color`
- **Description**: Sets the foreground color for the back wall.

#### `Chart.BackWall.Fill.BackColor`
- **Type**: `Color`
- **Description**: Sets the background color for the back wall.

#### `Chart.BackWall.Thickness`
- **Type**: `int`
- **Description**: Sets the thickness of the back wall.

#### `Chart.SideWall.Fill.FillType`
- **Type**: `ExcelFillType`
- **Description**: Sets the fill type for the side wall of the chart.

#### `Chart.SideWall.Fill.BackColor`
- **Type**: `Color`
- **Description**: Sets the background color for the side wall.

#### `Chart.SideWall.Fill.ForeColor`
- **Type**: `Color`
- **Description**: Sets the foreground color for the side wall.

---

### Description

This example shows how to create a 3D clustered column chart in a spreadsheet. It involves setting the data range, configuring the chart properties, and customizing the visual appearance of the chart's back wall and side wall.

---

### See also

- [`Range`](#range)
- [`IChartShape`](#ichartshape)
- [`ExcelChartType`](#excelcharttype)
- [`ExcelFillType`](#excelfilltype)
- [`ExcelGradientColor`](#excelgradientcolor)
- [`ExcelGradientStyle`](#excelgradientstyle)

<!-- tags: [Syncfusion, XlsIO, Chart, 3D Column Chart, WinForms, API Reference] keywords: [range, chart, fill type, gradient style, chart series, chart categories, back wall, side wall, visual appearance] -->
```