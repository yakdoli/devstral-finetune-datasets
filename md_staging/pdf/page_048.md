```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: pdf
page_number: 048
page_id: pdf#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:11Z
fidelity: lossless
-->

# Essential PDF

A PDF page is added to the document (doc).

## Content

3. Write the string "Hello World" on the first page in the PDF document. This task is further subdivided into the following tasks.

- **Create the font object to be used for writing the "Hello World" string. You can set the font size and style in the same statement.**
- **Write the text using the DrawString method of the Graphics object.**

### Sample Code: C#

```csharp
// Use the predefined fonts to draw the text.
PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, fontSize, fontStyle);

// Draw the string at the specified coordinates.
firstPage.Graphics.DrawString("Hello World", pdfFont, PdfBrushes.Black, 0, 0);
```

### Sample Code: VB.NET

```vb
' Use the predefined fonts to draw the text.
Dim font As Syncfusion.Pdf.Graphics.PdfFont = New Syncfusion.Pdf.Graphics.PdfStandardFont(PdfFontFamily.Helvetica, fontSize, FontStyle)

' Draw the string at the specified coordinates.
firstPage.Graphics.DrawString("Hello World", pdfFont, PdfBrushes.Black, 0, 0)
```

The string "Hello World" is written to the document.

4. **User can save the generated PDF document to their specified locations with the help of the SaveFileDialog class by streaming the generated PDF document.**

### Sample Code: C#

```csharp
// Create instance for SaveFileDialog
SaveFileDialog sfd = new SaveFileDialog()
{
    DefaultExt = "pdf",
    Filter = "Text files (*.pdf)|*.pdf|All files (*.*)|*.*",
    FilterIndex = 1
};
```

<!-- tags: [pdf, document, savefiledialog, syncfusion, winforms, 11.4.0.26] keywords: [Hello World, PdfFont, PdfStandardFont, DrawString, SaveFileDialog, pdf, document, font, text] -->
```