```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_228.jpeg
document_name: XlsIO
page_number: 228
page_id: XlsIO#page_228
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:23Z
fidelity: lossless
-->

## XlsIO

### Overview
- Demonstrates setting font styles for chart data labels and titles.
- Highlights techniques for creating rich-text formatting with variable font styles.
- Illustrates how to open, modify, and save Excel workbooks programmatically.

### Content

#### Setting Font Styles for Chart Data Labels

The following C# code snippet demonstrates how to apply italic, blue, size 10 Calibri font to a specific range of text within a chart's data label.

```csharp
blueFont.Italic = true;
blueFont.Size = 10;
blueFont.FontName = "Calibri";
blueFont.Color = ExcelKnownColors.Blue;
//SetFont(int startIndex, int endIndex, IFont font)
chart.Series[0].DataPoints[0].DataLabels.RichText.SetFont(1, 2, blueFont);
//Save workbook
workbook.Version = ExcelVersion.Excel2007;
string fileName = @"../../Output/SampleOutput.xlsx";
workbook.SaveAs(fileName);
workbook.Close();
excelEngine.Dispose();
```

#### Rich-text Formatting in Chart Titles

The following VB.NET code snippet demonstrates how to apply bold and red font to a specific range of text within a chart title.

```vb
[VB]
'Step 1: Instantiate the spreadsheet creation engine.
Dim excelEngine As ExcelEngine = New ExcelEngine()
'Step 2: Instantiate the excel application object.
Dim application As IApplication = excelEngine.Excel
Dim workbook As IWorkbook = application.Workbooks.Open("../../Data/Sample.xlsx", ExcelOpenType.Automatic)
Dim worksheet As IWorksheet = workbook.Worksheets(0)
Dim chart As IChart = worksheet.Charts(0)
chart.ChartTitle = "Title with a variable font style"
'Rich-text in chart title
'Create a new font with the following properties
Dim redFont As IFont = workbook.CreateFont()
redFont.Bold = True
redFont.Italic = False
redFont.Size = 18
redFont.FontName = "Georgia"
redFont.Color = ExcelKnownColors.Red
Dim chartRTS As IChartRichTextString = chart.ChartTitleArea.RichText
'SetFont(int startIndex, int endIndex, IFont font)
chartRTS.SetFont(0, 12, redFont)
```

---

### API Reference

#### Classes and Methods
- **ExcelEngine**: Provides the core functionality for creating and manipulating Excel documents.
- **IApplication**: Represents the Excel application object that manages workbooks.
- **IWorkbook**: Represents an Excel workbook, allowing access to its components.
- **IWorksheet**: Represents an individual worksheet within a workbook.
- **IChart**: Represents a chart object within a worksheet, allowing modification of its properties.
- **RichText**: Provides functionality for applying rich-text formatting to chart titles and data labels.
- **SetFont(int startIndex, int endIndex, IFont font)**: Applies the specified font to a range of text.

#### Properties
- **Bold**: Boolean indicating whether the font is bold.
- **Italic**: Boolean indicating whether the font is italic.
- **Size**: Integer specifying the font size.
- **FontName**: String specifying the font name.
- **Color**: Enum specifying the font color.

### Code Examples

#### C# Example: Setting Rich Text in Data Labels
The C# example demonstrates assigning a specific font style to a portion of text in a chart's data label.

```csharp
using Syncfusion.XlsIO;
using System;

class Program
{
    static void Main(string[] args)
    {
        // Instantiate the Excel engine
        ExcelEngine excelEngine = new ExcelEngine();
        IApplication application = excelEngine.Excel;
        IWorkbook workbook = application.Workbooks.Open("../../Data/Sample.xlsx", ExcelOpenType.Automatic);
        IWorksheet worksheet = workbook.Worksheets[0];
        IChart chart = worksheet.Charts[0];

        // Create a new font with specific properties
        IFont blueFont = workbook.CreateFont();
        blueFont.Italic = true;
        blueFont.Size = 10;
        blueFont.FontName = "Calibri";
        blueFont.Color = ExcelKnownColors.Blue;

        // Apply the font to a specific range in the data label
        chart.Series[0].DataPoints[0].DataLabels.RichText.SetFont(1, 2, blueFont);

        // Save the workbook
        workbook.Version = ExcelVersion.Excel2007;
        string fileName = @"../../Output/SampleOutput.xlsx";
        workbook.SaveAs(fileName);
        workbook.Close();
        excelEngine.Dispose();
    }
}
```

#### VB.NET Example: Setting Rich Text in Chart Titles
The VB.NET example demonstrates applying different font styles to portions of a chart title.

```vb
Imports Syncfusion.XlsIO
Imports System

Module Module1
    Sub Main()
        ' Instantiate the Excel engine
        Dim excelEngine As New ExcelEngine()
        Dim application As IApplication = excelEngine.Excel
        Dim workbook As IWorkbook = application.Workbooks.Open("../../Data/Sample.xlsx", ExcelOpenType.Automatic)
        Dim worksheet As IWorksheet = workbook.Worksheets(0)
        Dim chart As IChart = worksheet.Charts(0)

        ' Create a new font with specific properties
        Dim redFont As IFont = workbook.CreateFont()
        redFont.Bold = True
        redFont.Italic = False
        redFont.Size = 18
        redFont.FontName = "Georgia"
        redFont.Color = ExcelKnownColors.Red

        ' Apply the font to a specific range in the chart title
        Dim chartRTS As IChartRichTextString = chart.ChartTitleArea.RichText
        chartRTS.SetFont(0, 12, redFont)

        ' Save the workbook
        workbook.Version = ExcelVersion.Excel2007
        Dim fileName As String = @"../../Output/SampleOutput.xlsx"
        workbook.SaveAs(fileName)
        workbook.Close()
        excelEngine.Dispose()
    End Sub
End Module
```

---

### Cross References
- For more information on Excel formatting and styles, refer to the [Excel Formatting and Styles](#) documentation.
- For detailed instructions on working with charts in Excel, see the [Working with Charts](#) guide.

<!-- tags: XlsIO, ExcelDocument, Font, RichText, Chart, DataLabels, VB.NET, C#, WinForms keywords: ExcelEngine, IWorkbook, IWorksheet, IChart, RichText, SetFont, FontColor, FontStyle -->
```