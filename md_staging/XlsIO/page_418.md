```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_418.jpeg
document_name: XlsIO
page_number: 418
page_id: XlsIO#page_418
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:23Z
fidelity: lossless
-->

# Essixial XlsIO

## Content

### Code Examples

#### C#

```csharp
// Decryption:
// Opening the encrypted workbook.
IWorkbook workbook = application.Workbooks.Open("FileName.xls", 
ExcelParseOptions.Default, true, "password");
```

#### VB.NET

```vb
' Decryption:
' Opening the encrypted workbook.
Dim workbook As Syncfusion.XlsIO.IWorkbook = 
Application.Workbooks.Open("FileName.xls", ExcelParseOptions.Default, True, 
"password")
```

### Figure: Decrypting the Document

![](https://i.imgur.com/XlsIO_Decrypt.png)

**Figure 158: Decrypting the Document**

### Explanation

The provided code examples show how to decrypt an encrypted Excel workbook using both C# and VB.NET. The password required to decrypt the document is `"password"`. The `application.Workbooks.Open` method is used with the appropriate parameters to open the encrypted workbook.

### Image Description

The image depicts a Microsoft Excel interface showing the options for decrypting a document. The security settings prompt indicates that the document has been decrypted, and the user is advised to check the security settings at `Tools > Options > Security`.

## API Reference

### Method: `Workbooks.Open`

- **Parameters:**
  - `FileName`: The path to the encrypted Excel file.
  - `ExcelParseOptions`: The options for parsing the Excel file. Here, `Default` is used.
  - `ReadOnly`: A boolean indicating whether the file should be opened read-only. Here, `true` is used.
  - `Password`: The password required to decrypt the file.

### Return Type: `IWorkbook`

An interface for handling the workbook after it has been successfully opened and decrypted.

## Code Examples

### Example 1: Decrypting an Excel Workbook

#### C#

```csharp
using Syncfusion.XlsIO;
using System;

class Program
{
    static void Main()
    {
        // Create a new Excel engine instance
        ExcelEngine excelEngine = new ExcelEngine();
        IApplication application = excelEngine.Excel;

        // Open the encrypted workbook
        IWorkbook workbook = application.Workbooks.Open("FileName.xls", 
        ExcelParseOptions.Default, true, "password");

        // Process the workbook as needed
        // Example: Access a sheet
        IWorksheet sheet = workbook.Worksheets[0];
        Console.WriteLine($"Sheet name: {sheet.Name}");

        // Save and dispose of resources
        workbook.Close();
        application.Quit();
        excelEngine.Dispose();
    }
}
```

#### VB.NET

```vb
Imports Syncfusion.XlsIO
Imports System

Module Module1
    Sub Main()
        ' Create a new Excel engine instance
        Dim excelEngine As New ExcelEngine()
        Dim application As IApplication = excelEngine.Excel

        ' Open the encrypted workbook
        Dim workbook As IWorkbook = application.Workbooks.Open("FileName.xls", 
        ExcelParseOptions.Default, True, "password")

        ' Process the workbook as needed
        ' Example: Access a sheet
        Dim sheet As IWorksheet = workbook.Worksheets(0)
        Console.WriteLine($"Sheet name: {sheet.Name}")

        ' Save and dispose of resources
        workbook.Close()
        application.Quit()
        excelEngine.Dispose()
    End Sub
End Module
```

### Example 2: Handling Decryption Errors

#### C#

```csharp
using Syncfusion.XlsIO;
using System;

class Program
{
    static void Main()
    {
        try
        {
            ExcelEngine excelEngine = new ExcelEngine();
            IApplication application = excelEngine.Excel;

            // Attempt to open an encrypted workbook
            IWorkbook workbook = application.Workbooks.Open("FileName.xls", 
            ExcelParseOptions.Default, true, "password");

            // Process the workbook
            IWorksheet sheet = workbook.Worksheets[0];
            Console.WriteLine($"Sheet name: {sheet.Name}");

            workbook.Close();
            application.Quit();
            excelEngine.Dispose();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
```

### Example 3: Advanced Decryption Options

#### C#

```csharp
using Syncfusion.XlsIO;
using System;

class Program
{
    static void Main()
    {
        ExcelEngine excelEngine = new ExcelEngine();
        IApplication application = excelEngine.Excel;

        // Set advanced decryption options
        ExcelParseOptions options = new ExcelParseOptions()
        {
            // Configure additional settings as needed
        };

        // Open the encrypted workbook with advanced options
        IWorkbook workbook = application.Workbooks.Open("FileName.xls", 
        options, true, "password");

        // Process the workbook
        IWorksheet sheet = workbook.Worksheets[0];
        Console.WriteLine($"Sheet name: {sheet.Name}");

        workbook.Close();
        application.Quit();
        excelEngine.Dispose();
    }
}
```

### Tags and Keywords
<!-- tags: [Excel, decryption, Syncfusion, XlsIO] keywords: [decrypt, workbook, password, C#, VB.NET, API, encryption] -->
```