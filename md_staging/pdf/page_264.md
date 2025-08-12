```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_264.jpeg
document_name: pdf
page_number: 264
page_id: pdf#page_264
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:01Z
fidelity: lossless
-->

## Essential PDF

### Code Example (C#)

```csharp
PdfLoadedDocument doc1 = new PdfLoadedDocument(@"..\..\Data\Sample.pdf");

if (doc1.Attachments == null)
    doc1.CreateAttachment();

PdfAttachment attachment = new PdfAttachment(@"..\..\Data\Manual.txt");
attachment.ModificationDate = DateTime.Now;
attachment.Description = @"..\..\Data\Manual.txt";
attachment.MimeType = "application/txt";

doc1.Attachments.Add(attachment);
```

### Code Example (VB.NET)

```vb
Dim doc1 As New PdfLoadedDocument("...\Data\Sample.pdf")

If doc1.Attachments Is Nothing Then
    doc1.CreateAttachment()
End If

Dim attachment As New PdfAttachment("...\Data\Manual.txt")
attachment.ModificationDate = DateTime.Now
attachment.Description = "...\Data\Manual.txt"
attachment.MimeType = "application/txt"

doc1.Attachments.Add(attachment)
```
```