```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: pdf
page_number: 037
page_id: pdf#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:16Z
fidelity: lossless
-->

# Essential PDF

```csharp
' Save the document with the same name
pdfDoc.Save()
```

The created PDF document is saved to the disk using the above code.

## Finally close the PDF Document so that the objects are released.

### C#

```csharp
// Release the common resources.
pdfDoc.Close();

//(or)

// Releases document stream. This releases the entire document
PdfDoc.Close(true);
```

### VB.NET

```vbnet
' Release the common resources.
pdfDoc.Close()

'(or)

' Releases document stream. This releases entire document
PdfDoc.Close(True)
```

**PDF document will be closed after saving.**

**The sample pdf document created through the above procedure is shown below.**

<!-- tags: [pdf, document saving, document closing] keywords: [pdf document, save, close, resources, stream, document stream, file management] -->
```