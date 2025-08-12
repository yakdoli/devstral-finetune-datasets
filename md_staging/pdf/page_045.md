```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: pdf
page_number: 045
page_id: pdf#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:33Z
fidelity: lossless
-->

# Essential PDF

## Content

### Saving PDF Documents

The following code snippets demonstrate how to save a PDF document to disk and update a loaded document.

#### Saving to Disk

```csharp
pdfDoc.Save("Sample.pdf");
```

```vb
' Save the PDF document to disk.
pdfDoc.Save("Sample.pdf")
```

#### Updating a Loaded Document

You can also save the changes to the loaded document as follows.

```csharp
// Save the document with same name
pdfDoc.Save();
```

```vb
' Save the document with same name
pdfDoc.Save()
```

The created pdf document is saved to the disk using the above code.

### Closing the PDF Document

Finally, close the PDF Document using the following code, so that the objects are released.

#### C#

```csharp
// Release the common resources.
pdfDoc.Close();

// (or)

// Releases document stream. This releases entire document
PdfDoc.Close(true);
```

#### VB.NET

```vb
' Release the common resources.
pdfDoc.Close()

' (or)

' Releases document stream. This releases entire document
PdfDoc.Close(True)
```

## Footer

© 2013 Syncfusion. All rights reserved. | Page 45

<!-- tags: [Syncfusion, Winforms, PDF, document, save, close, C#, VB.NET] keywords: [PDF, save, close, document management, resource release] -->
```