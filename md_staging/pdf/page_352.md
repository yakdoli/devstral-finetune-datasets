```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_352.jpeg
document_name: pdf
page_number: 352
page_id: pdf#page_352
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:38Z
fidelity: lossless
-->

## 5.1.1.11 How To Dispose The Pdf document Object?

You can dispose the Pdf object by using the `Close` method. Note that without closing this object, it is not possible to use the same document again for any other manipulation.

**Close** method releases the commonly used memory. Its overload with its parameter set to `true` (`Close(true)`), releases the entire document stream, enabling it to be reused.

```csharp
[C#]

// Release the common resources.
pdfDoc.Close();

// (or)

// Releases document stream. This releases the entire document.
PdfDoc.Close(true);
```

```vbnet
[VB.NET]

' Release the common resources.
pdfDoc.Close()

' (or)

' Releases document stream. This releases the entire document.
PdfDoc.Close(True)
```

## 5.1.1.12 How to open the generated PDF document into the browser instead of displaying the Open/Save dialog in browser?

You can open the PDF document directly in the browser with the help of the Response object. Follow the below steps to generate the PDF document inline:

1. Save the PDF document as Stream object.
2. Write the stream in the Response object.

```csharp
[C#]

//Save the PDFDocument as a Stream.
MemoryStream stream = new MemoryStream();
```

## API Reference

### Namespaces

- Syncfusion.Windows.Forms.Tools
- Syncfusion.Windows.Forms.Grid

### Members

- `Close()`: Releases the common resources.
- `Close(bool)`: Releases the common resources and disconnects some of the resources that are not in use.
- `MemoryStream`: Class used for creating streams to write or read the PDF.

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.Tools;
using Syncfusion.Windows.Forms.Grid;

// Create a PDF document.
PdfDoc pdfDoc = new PdfDoc();
// Save the PDF document as a stream.
MemoryStream stream = new MemoryStream();
pdfDoc.Save(stream);
// Write the stream in the Response object.
Response.ContentType = "application/pdf";
Response.AddHeader("Content-Disposition", "inline; filename=document.pdf");
Response.BinaryWrite(stream.ToArray());
Response.End();
```

### VB.NET

```vbnet
Imports Syncfusion.Windows.Forms.Tools
Imports Syncfusion.Windows.Forms.Grid

' Create a PDF document.
Dim pdfDoc As New PdfDoc()
' Save the PDF document as a stream.
Dim stream As New MemoryStream()
pdfDoc.Save(stream)
' Write the stream in the Response object.
Response.ContentType = "application/pdf"
Response.AddHeader("Content-Disposition", "inline; filename=document.pdf")
Response.BinaryWrite(stream.ToArray())
Response.End()
```

<!-- tags: [Syncfusion, WinForms, PDF, API, version 11.4.0.26] keywords: [PDF, document, dispose, stream, open, browser, inline, memory stream, WinForms, tools, grid, close method, generated PDF, open dialog, document stream, release resources] -->
```