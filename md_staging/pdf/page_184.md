```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_184.jpeg
document_name: pdf
page_number: 184
page_id: pdf#page_184
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:03Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Demonstrates how to add attachments to a PDF document.
- Provides code examples in C# and VB.NET for adding attachments.
- Explains additional parameters for specifying attachment details.

## Content

### Adding Attachments to a PDF Document

The following code example illustrates how to add an attachment to the document.

```csharp
[C#]

PdfAttachment attachment = new PdfAttachment(@"..\..\Images\jpg\logo.jpg");
attachment.ModificationDate = DateTime.Now;
attachment.Description = "Syncfusion Logo";
attachment.MimeType = "application/jpeg";
document.Attachments.Add(attachment);
```

```vbnet
[VB.NET]

Dim attachment As PdfAttachment = New PdfAttachment("..\..\Images\jpg\logo.jpg")
attachment.ModificationDate = DateTime.Now
attachment.Description = "Syncfusion Logo"
attachment.MimeType = "application/jpeg"
document.Attachments.Add( attachment )
```

#### Important Notes
- Ensure the attachment is added to the attachment collection of the document.
- Additional parameters such as `ModificationDate`, `MimeType`, and `Description` can be specified for the attachment.

### Creating Attachments from Data Streams

It is possible to create attachments from data contained in a stream or data array. In this case, the file name passed to the constructor will determine the title of the attachment displayed on the attachments panel.

The following code example illustrates how to attach stream data to the PDF document.

```csharp
[C#]

using (FileStream fileStream = new FileStream(@"..\..\Images\jpg\image.jpg", FileMode.Open))
{
    PdfAttachment streamAttachment = new PdfAttachment("mouse.jpg", fileStream);
    streamAttachment.MimeType = "application/jpeg";
    document.Attachments.Add(streamAttachment);
}
```

## API Reference

- **Namespace**: Pdf
- **Class**: PdfAttachment
- **Methods/Properties**:
  - `PdfAttachment(string fileName)`
  - `PdfAttachment(string fileName, Stream stream)`
  - `ModificationDate`: Sets the modification date of the attachment.
  - `Description`: Sets the description of the attachment.
  - `MimeType`: Sets the MIME type of the attachment.

## Code Examples

- **Adding attachments using file paths**:
  - C# and VB.NET examples are provided in the document body.
- **Adding attachments from stream data**:
  - A C# example is provided in the document body.

## Cross References

- For more information on PDF features, see the official Syncfusion documentation.

<!-- tags: [pdf, attachment, document, c#, vb.net, stream, mime type] keywords: [PdfAttachment, modification date, description, MIME type, document.Attachments, stream attachment, C#, VB.NET] -->
```