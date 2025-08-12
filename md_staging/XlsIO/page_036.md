```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: XlsIO
page_number: 036
page_id: XlsIO#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:50:29Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- This section demonstrates how to insert text into a cell in an Excel workbook using C# and VB.NET.
- It illustrates saving, closing, and disposing of the workbook and Excel engine.

## Content

### Inserting Sample Text

The string `"Hello World"` is written to the cell **A1** of the document.

```csharp
// Inserting sample text into the first cell of the first worksheet.
sheet.Range("A1").Text = "Hello World"
```

#### Save and Close the Workbook

```csharp
[C#]
// Saving the workbook to disk.
workbook.SaveAs("Sample.xls");

// Closing the workbook.
workbook.Close();
```

```vb.net
[VB.NET]
' Saving the workbook to disk.
workbook.SaveAs("Sample.xls")

' Closing the workbook.
workbook.Close()
```

The Workbook is saved and closed.

> **Note:** To know more about saving the workbook, see **Save**.

#### Dispose the Excel Engine

Dispose the Excel engine. Note that the engine should be disposed after completing workbook operations.

```csharp
[C#]
// Dispose the Excel engine.
excelEngine.Dispose();
```

```vb.net
[VB.NET]
' Dispose the Excel engine.
excelEngine.Dispose()
```

The Excel engine is disposed.

## API Reference (if applicable)

- **workbook.SaveAs("Sample.xls")**: Saves the workbook to disk.
- **workbook.Close()**: Closes the workbook.
- **excelEngine.Dispose()**: Properly disposes the Excel engine.

## Code Examples (multi-language supported)

```csharp
// Example: Saving and closing the workbook using C#
[C#]
workbook.SaveAs("Sample.xls");
workbook.Close();
excelEngine.Dispose();
```

```vb.net
' Example: Saving and closing the workbook using VB.NET
[VB.NET]
workbook.SaveAs("Sample.xls")
workbook.Close()
excelEngine.Dispose()
```

## RAG Annotations

<!-- tags: [XlsIO, Essential XlsIO, Syncfusion Winforms, Excel Engine, workbook save and close] keywords: [workbook.SaveAs, workbook.Close, excelEngine.Dispose, VB.NET, C#, workbook operations, dispose engine] -->
```