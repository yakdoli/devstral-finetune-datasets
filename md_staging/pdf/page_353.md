```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_353.jpeg
document_name: pdf
page_number: 353
page_id: pdf#page_353
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:43Z
fidelity: lossless
-->

## Essential PDF

```csharp
doc.Save(stream);

// Stream the output to the browser.
Response.ContentType = "application/pdf";
Response.AddHeader("content-disposition", "inline; filename=MyPDF.PDF");
Response.AddHeader("content-length", stream.Length.ToString());
Response.BinaryWrite(stream.ToArray());
Response.End();
```

### [VB]

1. **Save the PDFDocument as a Stream.**

    ```vb
    Dim stream As New MemoryStream()
    doc.Save(stream)
    ```

2. **Stream the output to the browser.**

    ```vb
    Response.ContentType = "application/pdf"
    Response.AddHeader("content-disposition", "inline; filename=MyPDF.PDF")
    Response.AddHeader("content-length", stream.Length.ToString())
    Response.BinaryWrite(stream.ToArray())
    Response.End()
    ```

---

## 5.1.1.13 How to set the default view of Navigation Pane in Viewer?

When a PDF document is opened in Adobe, by default, any one of the tabs in the Navigation pane can be expanded. It can be set using the PdfPageMode enumeration in Essential PDF. The following code snippet, when executed, makes Attachments as a default view.

### Code Example

```csharp
// [C#]
```

## API Reference

### Methods
- `doc.Save(stream)`: Saves the PDF document to the specified stream.
- `Response.ContentType`: Sets the content type of the response as "application/pdf".
- `Response.AddHeader(key, value)`: Adds a header with the given key and value to the response.
- `Response.BinaryWrite(data)`: Writes binary data to the response stream.
- `Response.End()`: Ends the response.

## Code Examples

### Example in C#

```csharp
doc.Save(stream);

// Stream the output to the browser.
Response.ContentType = "application/pdf";
Response.AddHeader("content-disposition", "inline; filename=MyPDF.PDF");
Response.AddHeader("content-length", stream.Length.ToString());
Response.BinaryWrite(stream.ToArray());
Response.End();
```

### Example in VB

```vb
Dim stream As New MemoryStream()
doc.Save(stream)

' Stream the output to the browser.
Response.ContentType = "application/pdf"
Response.AddHeader("content-disposition", "inline; filename=MyPDF.PDF")
Response.AddHeader("content-length", stream.Length.ToString())
Response.BinaryWrite(stream.ToArray())
Response.End()
```

## See also
- [Handling PDF Navigation Pane](#handling-pdf-navigation-pane)
- [PDF Document Viewer Settings](#pdf-document-viewer-settings)

<!-- tags: pdf, navigation, viewer, document, essentialpdf, adobe, winforms, syncfusion version: 11.4.0.26 -->
```