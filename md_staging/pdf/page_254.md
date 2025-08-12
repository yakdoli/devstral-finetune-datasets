```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_254.jpeg
document_name: pdf
page_number: 254
page_id: pdf#page_254
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:33Z
fidelity: lossless
-->

# Essential PDF

An existing PDF document can be loaded and customized. To open an existing PDF document for further manipulations, use the `PdfLoadedDocument` class. Its constructor allows you to specify the file name, stream, or byte array as the source of the document data and the password for encrypted documents.

```csharp
[C#]

PdfLoadedDocument ldDoc = new PdfLoadedDocument(filename);
PdfLoadedDocument ldDoc = new PdfLoadedDocument(memoryStream);
PdfLoadedDocument ldDoc = new PdfLoadedDocument(byte);
PdfLoadedDocument ldDoc = new PdfLoadedDocument(filename, password);
PdfLoadedDocument ldDoc = new PdfLoadedDocument(memoryStream, password);
PdfLoadedDocument ldDoc = new PdfLoadedDocument(byte, password);
```

```vb
[VB.NET]

Dim ldDoc As PdfLoadedDocument = New PdfLoadedDocument(filename)
Dim ldDoc As PdfLoadedDocument = New PdfLoadedDocument(memoryStream)
Dim ldDoc As PdfLoadedDocument = New PdfLoadedDocument(byte)
Dim ldDoc As PdfLoadedDocument = New PdfLoadedDocument(filename, password)
Dim ldDoc As PdfLoadedDocument = New PdfLoadedDocument(memoryStream, password)
Dim ldDoc As PdfLoadedDocument = New PdfLoadedDocument(byte, password)
```

**Note:** You must add the `Syncfusion.Pdf.Parsing` namespace to work with the loaded documents.

In the loaded document, you can do the following:

- Access the bookmarks
- Add a new page
- Add an Attachment
- Load dynamic fields

Go to the above individual links for detailed information.

## Public Members

The following table lists the public members of the `PdfLoadedDocument` class.

## Methods
```


<!-- tags: [syncfusion winforms, Essential PDF, PdfLoadedDocument, document manipulation] keywords: [loaded document, document manipulation, bookmarks, new page, attachment, dynamic fields, memory stream, byte array, password, namespace, parsing, public members, methods] -->
```