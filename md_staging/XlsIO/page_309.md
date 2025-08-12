```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_309.jpeg
document_name: XlsIO
page_number: 309
page_id: XlsIO#page_309
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:00Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- Page Setup functionality in xlsx documents.
- Setting Orientation through the `Orientation` property of `IPageSetup`.
- Examples in C# and VB.NET for setting page orientation.

## Content

### Page Setup

Figure 109 illustrates the `Page Setup` dialog, where you can adjust various page settings, including the orientation, margins, header/footer, and sheet options.

#### Setting Orientation

XlsIO allows you to define the orientation through the `Orientation` property of the `IPageSetup` interface.

- **Orientation Options:**
  - **Portrait:** The default orientation for printing, where the page is taller than it is wide.
  - **Landscape:** The page is wider than it is tall, useful for spreadsheets with wide data.

#### Code Example: Setting Page Orientation

The following code examples demonstrate how to set the page orientation using C# and VB.NET.

#### C#

```csharp
// Setting the Page Orientation as Portrait or Landscape.
sheet.PageSetup.Orientation = ExcelPageOrientation.Landscape;
```

#### VB.NET

```vb
' Setting the Page Orientation as Portrait or Landscape.
sheet.PageSetup.Orientation = ExcelPageOrientation.Landscape
```

## API Reference

### Properties

- **Orientation:** 
  - **Type:** `ExcelPageOrientation`
  - **Description:** Specifies the orientation of the printed page.
  - **Possible Values:**
    - `ExcelPageOrientation.Portrait`
    - `ExcelPageOrientation.Landscape`
  - **Default:** `ExcelPageOrientation.Portrait`
  - **Required:** No

## Code Examples

### Setting Page Orientation in C#

```csharp
// Example: Setting the Page Orientation to Landscape
using Syncfusion.XlsIO;
using System;

class Program
{
    static void Main()
    {
        // Create a new workbook
        ExcelEngine excelEngine = new ExcelEngine();
        IApplication application = excelEngine.Excel;
        application.DefaultVersion = ExcelVersion.Excel2013;
        IWorkbook workbook = application.Workbooks.Create(1);
        IWorksheet sheet = workbook.Worksheets[0];

        // Set the page orientation to Landscape
        sheet.PageSetup.Orientation = ExcelPageOrientation.Landscape;

        // Save and close
        workbook.Version = ExcelVersion.Excel2013;
        workbook.SaveAs("PageOrientation.xlsx");
        excelEngine.Dispose();
    }
}
```

### Setting Page Orientation in VB.NET

```vb
' Example: Setting the Page Orientation to Landscape
Imports Syncfusion.XlsIO
Imports System

Module Program
    Sub Main()
        ' Create a new workbook
        Dim excelEngine As New ExcelEngine()
        Dim application As IApplication = excelEngine.Excel
        application.DefaultVersion = ExcelVersion.Excel2013
        Dim workbook As IWorkbook = application.Workbooks.Create(1)
        Dim sheet As IWorksheet = workbook.Worksheets(0)

        ' Set the page orientation to Landscape
        sheet.PageSetup.Orientation = ExcelPageOrientation.Landscape

        ' Save and close
        workbook.Version = ExcelVersion.Excel2013
        workbook.SaveAs("PageOrientation.xlsx")
        excelEngine.Dispose()
    End Sub
End Module
```

## RAG Annotations

<!-- tags: [xlsio, page setup, orientation, ipagesetup, c#, vb.net] keywords: [xlsio, excel, page setup, orientation, landscape, portrait, csharp, vb.net, api, code example] -->
```