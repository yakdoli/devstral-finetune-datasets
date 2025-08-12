```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_185.jpeg
document_name: pdf
page_number: 185
page_id: pdf#page_185
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:36Z
fidelity: lossless
-->

# Essential PDF

## Content

### Code Example

```vb
[VB.NET]

Dim fileStream As IO.FileStream = New IO.FileStream("..\..\Images\jpg\image.jpg", FileMode.Open)
Dim streamAttachment As Syncfusion.Pdf.Interactive.PdfAttachment = New Syncfusion.Pdf.Interactive.PdfAttachment("mouse.jpg", fileStream)
streamAttachment.MimeType = "application/jpeg"
document.Attachments.Add(streamAttachment)

Dim disp As IDisposable = fileStream
disp.Dispose()
```

### 4.1.3.4 Portfolio

**Overview:**
- Essential PDF Portfolio provides support to add multiple files of different formats, created in different applications.
- This feature enables you to enhance the presentation of files stored in the PDF by providing support to define your own fields for attachments.

**Use Case Scenarios:**
- You can add any number of documents into PDF Portfolio.
- You can attach files and add custom file fields and attributes to provide your own file description.

## Notes and Additional Information

This section of the document details the functionality of adding attachments to a PDF using the Portfolio feature in Essential PDF. It provides code examples in VB.NET to demonstrate how to attach a file and define its properties, such as the MIME type. The use case scenarios highlight the versatility of the Portfolio feature, allowing users to enhance and organize their PDF documents effectively.

<!-- tags: [Essential PDF, Portfolio, VB.NET] keywords: [attachments, multiple files, MIME type, document enhancement, custom file fields, file description] -->
```