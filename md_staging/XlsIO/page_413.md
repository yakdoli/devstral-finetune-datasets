```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_413.jpeg
document_name: XlsIO
page_number: 413
page_id: XlsIO#page_413
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:41Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates setting built-in and custom document properties using XlsIO.
- Includes examples in C# and VB.NET.

## Content

### Setting Built-in Document Properties
The following code snippet sets built-in document properties such as `Author`, `Comments`, `ByteCount`, `LastSaveDate`, and `Manager`.

#### C#
```csharp
ICustomDocumentProperties customProperites = workbook.CustomDocumentProperties;
customProperites[ "Author" ].Text = ""Essential XlsIO"";
customProperites[ "Comments" ].Text = "XlsIO support Custom document properties";
customProperites[ "Double" ].Double = 120.2;
```

#### VB.NET
```vb
' Setting Built-in Document Properties.
Dim builtInProperites As IBuiltInDocumentProperties = book.BuiltInDocumentProperties
builtInProperites.Author = "Essential XlsIO"
builtInProperites.Comments = "This document was generated using Essential XlsIO"
builtInProperites.ByteCount = 120
builtInProperites.LastSaveDate = New DateTime(1950, 1, 2, 3, 4, 5, 6)
builtInProperites.Manager = "Manager"

' Setting Custom Properties.
Dim customProperites As ICustomDocumentProperties = workbook.CustomDocumentProperties
customProperites( "Author" ).Text = "Essential XlsIO"
customProperites( "Comments" ).Text = "XlsIO support Custom document properties"
customProperites( "Double" ).Double = 120.2
```

## API Reference

### Namespaces and Classes
- **Syncfusion.XlsIO**
  - `IBuiltInDocumentProperties`
  - `ICustomDocumentProperties`
  - `Workbook`

### Methods and Properties
- `IBuiltInDocumentProperties.Author`
- `IBuiltInDocumentProperties.Comments`
- `IBuiltInDocumentProperties.ByteCount`
- `IBuiltInDocumentProperties.LastSaveDate`
- `IBuiltInDocumentProperties.Manager`
- `ICustomDocumentProperties[...]`

## Code Examples

### Built-in Document Properties Example
#### C#
```csharp
using Syncfusion.XlsIO;
using System;

class Program
{
    static void Main(string[] args)
    {
        // Create a new workbook.
        using (ExcelEngine excelEngine = new ExcelEngine())
        {
            IApplication application = excelEngine.Excel;
            application.DefaultVersion = ExcelVersion.Excel2010;
            IWorkbook workbook = application.Workbooks.Create(1);
            IWorksheet worksheet = workbook.Worksheets[0];

            // Set built-in document properties.
            IBuiltInDocumentProperties builtInProperites = workbook.BuiltInDocumentProperties;
            builtInProperites.Author = "Essential XlsIO";
            builtInProperites.Comments = "This document was generated using Essential XlsIO";
            builtInProperites.ByteCount = 120;
            builtInProperites.LastSaveDate = new DateTime(1950, 1, 2, 3, 4, 5, 6);
            builtInProperites.Manager = "Manager";

            // Save the workbook.
            workbook.SaveAs("BuiltInProperties.xlsx");
        }
    }
}
```

### Custom Document Properties Example
#### C#
```csharp
using Syncfusion.XlsIO;
using System;

class Program
{
    static void Main(string[] args)
    {
        // Create a new workbook.
        using (ExcelEngine excelEngine = new ExcelEngine())
        {
            IApplication application = excelEngine.Excel;
            application.DefaultVersion = ExcelVersion.Excel2010;
            IWorkbook workbook = application.Workbooks.Create(1);
            IWorksheet worksheet = workbook.Worksheets[0];

            // Set custom document properties.
            ICustomDocumentProperties customProperites = workbook.CustomDocumentProperties;
            customProperites["Author"].Text = "Essential XlsIO";
            customProperites["Comments"].Text = "XlsIO support Custom document properties";
            customProperites["Double"].Double = 120.2;

            // Save the workbook.
            workbook.SaveAs("CustomProperties.xlsx");
        }
    }
}
```

## Page-level Navigation/TOC
- [Setting Built-in Document Properties]
- [Setting Custom Document Properties]
- [Code Examples]

## Cross References
- Refer to the XlsIO documentation for more details on document properties.

<!-- tags: [XlsIO, document properties, built-in properties, custom properties, C#, VB.NET, version:11.4.0.26] keywords: [Essential XlsIO, built-in document properties, custom document properties, author, comments, byte count, last save date, manager, custom properties, C# example, VB.NET example] -->
```