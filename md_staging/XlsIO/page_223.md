```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_223.jpeg
document_name: XlsIO
page_number: 223
page_id: XlsIO#page_223
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:00Z
fidelity: lossless
-->

## XlsIO

### Overview
- Demonstrates how to edit an existing Excel chart using VB.NET code.
- explains modifying chart titles, axis labels, and series names.
- Describes setting text formatting for the title area.
- Illustrates adjusting the chart's dimensions and axis range.
- Includes saving and closing the workbook.

## Content

### Opening and Editing an Existing Excel Chart

The following VB.NET code snippet shows how to open an Excel workbook, access an existing chart, and modify its properties.

```vb
' Opening the Existing Worksheet from a Workbook.
Dim workbook As IWorkbook =
application.Workbooks.Open("...\\...\\...\\Data\\EditChartsTemplate.xls")

' The first worksheet object in the worksheets collection is accessed.
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Editing the Existing Chart.
Dim chart As IChart = sheet.Charts(0)
chart.ChartTitle = "Texas Books Unit Sales"
chart.PrimaryCategoryAxis.Title = "City"
chart.PrimaryValueAxis.Title = "Sales (in Dollars)"
chart.Legend.Position = ExcelLegendPosition.Top

' Setting the Series Names in a Legend.
Dim serieOne As IChartSerie = chart.Series(0)
serieOne.Name = "Jan"
Dim serieTwo As IChartSerie = chart.Series(1)
serieTwo.Name = "Feb"
Dim serieThree As IChartSerie = chart.Series(2)
serieThree.Name = "March"

' Setting the Title Area text.
Dim Area As IChartTextArea = chart.ChartTitleArea
Area.Bold = True
Area.Underline = ExcelUnderline.Single

' Setting the Minimum and Maximum Value for the Value Axis.
chart.PrimaryValueAxis.MinimumValue = 10
chart.PrimaryValueAxis.MaximumValue = 100

' Setting the Height of the chart.
chart.Height = 1 / 10

' Setting the Width of the chart.
chart.Width = 1 / 72

' Saving the workbook to disk.
workbook.SaveAs("Sample.xls")

' Closing the workbook.
workbook.Close()
```

### Explanation

1. **Opening the Workbook**:
   - The `application.Workbooks.Open` method is used to open an existing Excel file located at a specified path.

2. **Accessing the Worksheet**:
   - The first worksheet (`Worksheets(0)`) is accessed to manipulate its contents.

3. **Editing the Chart**:
   - The `chart.ChartTitle` property is used to set the title of the chart.
   - The `chart.PrimaryCategoryAxis.Title` and `chart.PrimaryValueAxis.Title` properties are used to set the axis labels.
   - The `chart.Legend.Position` is set to place the legend at the top of the chart.

4. **Setting Series Names**:
   - Individual series are accessed using `chart.Series(index)`, and their names are updated to reflect different months.

5. **Formatting the Title Area**:
   - The `chart.ChartTitleArea` is used to apply bold and underline formatting to the chart title.

6. **Adjusting Axis Range**:
   - The `MinimumValue` and `MaximumValue` properties of the `PrimaryValueAxis` are set to define the axis range.

7. **Setting Chart Dimensions**:
   - The `chart.Height` and `chart.Width` properties are used to specify the dimensions of the chart.

8. **Saving and Closing the Workbook**:
   - The `workbook.SaveAs` method saves the modified workbook to disk.
   - The `workbook.Close` method is used to close the workbook after modifications.

## API Reference

### Namespaces and Types Used
- `IWorkbook`
- `IWorksheet`
- `IChart`
- `IChartSerie`
- `IChartTextArea`
- `ExcelLegendPosition`
- `ExcelUnderline`

### Parameters and Returns
- **Parameters**:
  - `application`: The Excel application object.
  - `workbook`: The opened workbook object.
  - `sheet`: The worksheet object.
  - `chart`: The chart object.
  - `serieOne`, `serieTwo`, `serieThree`: The series objects.
  - `Area`: The title area object.

- **Returns**: The modified workbook is saved to disk with the specified name.

## Code Examples

The provided code snippet demonstrates how to perform various operations on an existing Excel chart programmatically using the XlsIO library in VB.NET.

## Page-level Navigation/TOC
- Opening and Editing an Existing Excel Chart
- Explanation of the Code
- API Reference
- Code Examples

<!-- tags: [XlsIO, Excel, Chart, VB.NET, Syncfusion, Winforms] keywords: [IWorkbook, IWorksheet, IChart, ChartTitle, PrimaryCategoryAxis, PrimaryValueAxis, ExcelLegendPosition, ExcelUnderline, SeriesNames, ChartTitleArea, ChartHeight, ChartWidth, SaveAs, Close] -->
```