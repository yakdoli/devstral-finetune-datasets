```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_225.jpeg
document_name: XlsIO
page_number: 225
page_id: XlsIO#page_225
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:33Z
fidelity: lossless
-->


# Essential XlsIO

## Adjusting Chart Layout and Legend Properties

### Code Example: C#

```csharp
chart.PlotArea.Layout.Width = 300;
chart.PlotArea.Layout.Height = 200;

// Manually positioning and resizing chart legend
chart.Legend.Layout.LeftMode = LayoutModes.edge;
chart.Legend.Layout.TopMode = LayoutModes.edge;
chart.Legend.Layout.Left = 400;
chart.Legend.Layout.Top = 150;
chart.Legend.Layout.Width = 50;
chart.Legend.Layout.Height = 100;

// Saving workbook
workbook.Version = ExcelVersion.Excel2007;
string fileName = @"../../Output/SampleOutput.xlsx";
workbook.SaveAs(fileName);
workbook.Close();
excelEngine.Dispose();
```

### Code Example: VB

```vb
' Step 1: Instantiate the spreadsheet creation engine
Dim excelEngine As ExcelEngine = New ExcelEngine()

' Step 2: Instantiate the excel application object
Dim application As IApplication = excelEngine.Excel
Dim workbook As IWorkbook = application.Workbooks.Open("../../Data/Sample.xlsx", ExcelOpenType.Automatic)
Dim worksheet As IWorksheet = workbook.Worksheets(0)
Dim chart As IChart = worksheet.Charts(0)

' Manually positioning chart title
//Edge: Specifies that the Width or Height will be interpreted as the right
//or bottom of the chart element
//Factor: Specifies that the Width or Height will be interpreted as the
//width or height of the chart element

chart.PlotArea.Layout.LeftMode = LayoutModes.edge
chart.PlotArea.Layout.TopMode = LayoutModes.edge

'Value in points should not be negative value if LayoutMode is Edge
'//It can be a negative value if LayoutMode is Factor.
```

## Explanation

This section demonstrates how to adjust the layout of a chart and its legend within an Excel document using the XlsIO library in both C# and VB. The code examples show how to set the dimensions of the chart's plotting area and manually position and resize the legend. Additionally, the examples include saving the workbook in Excel 2007 format and properly disposing of the Excel engine once operations are complete.

## Page-level Navigation/TOC (if applicable)
- **Adjusting Chart Layout and Legend Properties**
  - **C# Code Example**
  - **VB Code Example**

## Cross References
See also:
- For more information on chart properties, refer to the documentation on [chart customization](#).
- Detailed instructions on working with Excel documents can be found in the [XlsIO Overview](#).

<!-- tags: [Excel, XlsIO, Chart, Legend, LayoutModes, Workbook, Save, Dispose] keywords: [chart, legend, layout, positioning, resizing, workbook, excel2007, dispose] -->
```