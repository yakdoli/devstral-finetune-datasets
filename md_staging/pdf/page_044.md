```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: pdf
page_number: 044
page_id: pdf#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:25:58Z
fidelity: lossless
-->

## Essential PDF

### Adding a Page to the Document

A PDF page is added to the document (`doc`).

```vbnet
' Add a page to the document
Dim firstPage As Syncfusion.Pdf.PdfPage = doc.Pages.Add()
```

### Writing the String "Hello World" on the First Page

Write the string "Hello World" on the first page in the PDF document. This task is further subdivided into the following tasks:

- **Create the font object**: Define the font object to be used for writing the "Hello World" string. You can set the font size and style in the same statement.
- **Write the text**: Use the `DrawString` method of the `Graphics` object to write the text.

#### C#

```csharp
// Use the predefined fonts to draw the text.
PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, fontSize, fontStyle);

// Draw the string at the specified coordinates.
firstPage.Graphics.DrawString("Hello World", pdfFont, PdfBrushes.Black, 0, 0);
```

#### VB.NET

```vbnet
' Use the predefined fonts to draw the text.
Dim font As Syncfusion.Pdf.Graphics.PdfFont = New Syncfusion.Pdf.Graphics.PdfStandardFont(PdfFontFamily.Helvetica, fontSize, FontStyle)

' Draw the string at the specified coordinates.
firstPage.Graphics.DrawString("Hello World", pdfFont, PdfBrushes.Black, 0, 0)
```

The string "Hello World" is written to the document.

### Saving the PDF Document to Disk

#### Step 5: Save the PDF Document to Disk

Save the PDF document that has been created to the disk using the `Save` method of the PDF document.

```csharp
// Save the PDF document to disk.
```

<!-- tags: [pdf, document, page, font, drawstring, save] keywords: [pdf, document, page, font, drawstring, save, helloworld] -->
```