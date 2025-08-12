<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: pdf
page_number: 036
page_id: pdf#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:25:30Z
fidelity: lossless
-->

# Essential PDF

```csharp
// Use the predefined fonts to draw the text.
PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, fontSize, fontStyle);

// Draw the string at the specified coordinates.
firstPage.Graphics.DrawString("Hello World", pdfFont, PdfBrushes.Black, 0, 0);
```

### [VB.NET]

```vbnet
' Use the predefined fonts to draw the text.
Dim font As Syncfusion.Pdf.Graphics.PdfFont = New Syncfusion.Pdf.Graphics.PdfStandardFont(PdfFontFamily.Helvetica, fontSize, FontStyle)

' Draw the string at the specified coordinates.
firstPage.Graphics.DrawString("Hello World", pdfFont, PdfBrushes.Black, 0, 0)
```

The string "Hello World" is written to the document.

### Then write the PDF document we have created to the disk. This is achieved by using the Save method of the PDF document.

#### [C#]

```csharp
// Save the PDF document to disk.
pdfDoc.Save("Sample.pdf");
```

#### [VB.NET]

```vbnet
' Save the PDF document to disk.
pdfDoc.Save("Sample.pdf")
```

You can also save the changes to the loaded document as follows.

### [C#]

```csharp
// Save the document with the same name
pdfDoc.Save();
```

### [VB.NET]

```vbnet
pdfDoc.Save()
```

<!-- tags: [Essential PDF, Syncfusion Winforms, pdf, drawing text, saving PDF] keywords: [pdfdocument, pdfpage, pdffont, predefined fonts, drawstring, save to disk, FB.NET, C#] -->