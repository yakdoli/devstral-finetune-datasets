```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_205.jpeg
document_name: pdf
page_number: 205
page_id: pdf#page_205
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:41Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Document properties of Adobe can be set using either the XMP's PDF schema or the `DocumentInformation` method of `PdfDocument`.
- Properties that can be set include: Author, CreationDate, Keywords, Producer, Subject, and Title.

## Content

The document properties of Adobe are set by using either the **XMP's PDF** schema or the `DocumentInformation` method of the `PdfDocument`. The properties that can be set are as follows:

- **Author**
- **CreationDate**
- **Keywords**
- **Producer**
- **Subject**
- **Title**

The following code snippet illustrates setting the document properties such as **Title**, **Author**, and **Keywords**.

### Code Examples

#### C#

```csharp
[C#]

// Setting various Document Properties.
pdfDoc.DocumentInformation.Title = "Document Properties Information";
pdfDoc.DocumentInformation.Author = "Syncfusion";
pdfDoc.DocumentInformation.Keywords = "PDF";

// XMP Basic Schema.
BasicSchema basic = xmp.BasicSchema;
basic.Advisory.Add("advisory");
basic.BaseURL = new Uri("http://google.com");
```

#### VB.NET

```vb
[Vb.Net]

' Setting various Document Properties.
pdfDoc.DocumentInformation.Title = "Document Properties Information"
pdfDoc.DocumentInformation.Author = "Syncfusion"
pdfDoc.DocumentInformation.Keywords = "PDF"

' XMP Basic Schema.
Dim basic As Syncfusion.Pdf.Xmp.BasicSchema = xmp.BasicSchema
basic.Advisory.Add("advisory")
basic.BaseURL = New Uri("http://google.com")
```

## Page-level Navigation/TOC
- Document properties can be set using the `DocumentInformation` method or the XMP's PDF schema.
- List of properties that can be set (Author, CreationDate, Keywords, Producer, Subject, Title).
- `DocumentInformation` method used to set properties (Title, Author, Keywords).

## API Reference
- `PdfDocument`
  - `DocumentInformation`
    - `.Title`
    - `.Author`
    - `.Keywords`
- `Xmp`
  - `BasicSchema`
    - `.Advisory`
    - `.BaseURL`

## Code Examples
- C# code snippet for setting document properties.
- VB.NET code snippet for setting document properties.

<!-- tags: [pdfdocument, documentinformation, xmppsdfschema, csharp, vb.net, adobe, documentproperties, syncfusion, winforms] keywords: [document information, xmp schema, pdfdocument, creationdate, keywords, producer, subject, title, csharp, vb.net, syncfusion, essential pdf] -->
```