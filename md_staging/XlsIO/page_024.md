```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: XlsIO
page_number: 024
page_id: XlsIO#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:49:43Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates the features of the ASP.NET MVC sample browser for XlsIO.
- High performance server-side .NET library that can read and write Microsoft Excel files.

## Content

### XlsIO Overview
- **High performance server side .NET library** that can read and write Microsoft Excel files.
- Full-fledged object model just like the Microsoft Office COM libraries.
- Built entirely in C# and can be used on systems that do not have Microsoft Excel installed, making it an excellent reporting engine for tabular data.

#### Featured Samples
- **Product Show Case**: Displays various functionalities like charts, data management, and settings.
- **Pie Chart**: Example of a pie chart showing budget allocation in percentages.
- **Tabular Report**: Example of a tabular report showcasing data in a structured format.
- **Template Marker**: Demonstrates the use of template markers with example data.
- **Sparklines**: Visualizes data trends using sparklines.
- **Invoice**: Sample invoice creation.
- **Pivot Table**: Example of a pivot table summarizing and analyzing data.

### Selecting Samples
1. **Select any sample and browse through the features.**

### Source Code Location

#### Default Locations for Source Code
The default locations of the source code for Essential XlsIO corresponding to each platform are given below:

- **Windows**
  - **Location**: The source code for the Windows platform is located at:
    ```
    [System Drive]:\Program Files\Syncfusion\Essential Studio[Version Number]\Base\XlsIO.Windows\Src
    ```

- **WPF**
  - **Location**: The source code for the WPF platform is located at the following location.

#### Code Snippet Example
```csharp
// Example code snippet demonstrating creation of a chart
using Syncfusion.XlsIO;
using (ExcelEngine engine = new ExcelEngine())
{
    IApplication application = engine.Excel;
    IWorkbook workbook = application.Workbooks.Create();

    IWorksheet sheet = workbook.Worksheets[0];
    sheet.Range["A1:D4"].Text = "Budget Allocation in %";
    sheet.Rows[1].InsertChart(Syncfusion.Chart.ChartType.Pie,
        sheet.Range["F1:G4"], 100, 100);
    sheet.Cells[1, 1].Format.Number.NumberFormat = "@"; // To Label

    workbook.SaveAs("Budget Allocation.xlsx");
}
```

## API Reference (if applicable)
- **Namespace**: `Syncfusion.XlsIO`
- **Class**: `ExcelEngine`
- **Properties**:
  - `Range`
  - `Rows`
  - `Range.Number.NumberFormat`
- **Methods**:
  - `InsertChart(ChartType, Range, int, int)`
  - `SaveAs(string)`

### Code Examples
- Demonstrates the creation and manipulation of Excel files programmatically using the XlsIO library.

## RAG Annotations
<!-- tags: [XlsIO, ASP.NET MVC, Windows, WPF, source code, sample browser, tabular data, pie chart, tabular report, template marker, sparklines, invoice, pivot table] keywords: [Essential XlsIO, features, .NET library, Microsoft Excel files, tabular data, reporting engine, Windows, WPF, source code locations] -->
```