```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: XlsIO
page_number: 048
page_id: XlsIO#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:23Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
// New instance of XlsIO is created. [Equivalent to launching MS Excel with
no workbooks open].
// The instantiation process consists of two steps.

// Step 1: Instantiate the spreadsheet creation engine.
ExcelEngine excelEngine = new ExcelEngine();
```

```vbnet
' New instance of XlsIO is created. [Equivalent to launching MS Excel with
' no workbooks open].
' The instantiation process consists of two steps.

' Step 1: Instantiate the spreadsheet creation engine.
Dim excelEngine As ExcelEngine = New ExcelEngine()
```

4. Instantiate the Excel application through the `IApplication` interface which represents an Excel application.

```csharp
// Step 2: Instantiate the excel application object.
IApplication application = excelEngine.Excel;
```

```vbnet
' Step 2: Instantiate the excel application object.
Dim application As IApplication = excelEngine.Excel
```

An Excel document is created.

5. Create a workbook. A newly created workbook has three worksheets by default. You can change the count of the worksheets by using the `Create` method of `IWorkbook`.

```csharp
// A new workbook is created. [Equivalent to creating a new workbook in MS Excel].
// The new workbook will have 5 worksheets.
IWorkbook workbook = application.Workbooks.Create(5);
```

### WinForms-Specific Conventions

- All code samples are presented in both C# and VB.NET formats to cater to different developer preferences.
- The `ExcelEngine` is the entry point for all operations, providing an engine for creating and manipulating Excel documents programmatically.

#### Example in VB.NET

```vbnet
Dim excelEngine As ExcelEngine = New ExcelEngine()
Dim application As IApplication = excelEngine.Excel
Dim workbook As IWorkbook = application.Workbooks.Create(5)
```

## Page-level Navigation/TOC

- **1. Instantiating the XlsIO Engine**
- **2. Creating an Excel Application**
- **3. Creating a Workbook**
- **4. Working with Worksheets**

## Cross References

For more details on specific API calls and properties, refer to the API reference section at the end of this document.

## API Reference

### Namespace: Syncfusion.XlsIO

#### Class: ExcelEngine
- **Property**: `Excel` - Returns the `IApplication` interface representing the Excel application.

#### Interface: IApplication
- **Property**: `Workbooks` - Provides access to a collection of workbooks.
- **Method**: `Create(int)` - Creates a new workbook with the specified number of worksheets.

## Code Examples

Below are additional code examples to illustrate key functionalities:

### Creating and Manipulating a Workbook in C#

```csharp
using Syncfusion.XlsIO;
using System;

class Program
{
    static void Main(string[] args)
    {
        // Instantiate the XlsIO engine
        ExcelEngine excelEngine = new ExcelEngine();
        
        // Create an Excel application instance
        IApplication application = excelEngine.Excel;
        
        // Create a new workbook with 3 sheets
        IWorkbook workbook = application.Workbooks.Create(3);
        
        // Access the first worksheet
        IWorksheet worksheet = workbook.Worksheets[0];
        
        // Add data to the first cell
        worksheet[0, 0].Text = "Hello, World!";
        
        // Save the workbook
        workbook.SaveAs("Output.xlsx");
        
        // Dispose of resources
        excelEngine.Dispose();
    }
}
```

### Saving and Disposing of Resources

It is crucial to dispose of the `ExcelEngine` resources after use to avoid memory leaks. Always call `Dispose` on the `ExcelEngine` when you are done with it.

## Conclusion

This section provides a comprehensive guide on how to instantiate the XlsIO engine, create an Excel application, and generate workbooks with custom settings. These foundational steps are essential for leveraging the full capabilities of the Syncfusion XlsIO library in WinForms applications.

<!-- tags: [XlsIO, Syncfusion, Winforms, Excel, workbook creation, worksheet manipulation] keywords: [ExcelEngine, IApplication, IWorkbook, IWorksheet, instantiation, workbook, worksheet, data manipulation] -->
```