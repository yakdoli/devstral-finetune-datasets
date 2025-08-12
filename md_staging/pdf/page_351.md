```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_351.jpeg
document_name: pdf
page_number: 351
page_id: pdf#page_351
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:43Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Adds a CJK font to the font collection for rendering text.
- Demonstrates reading and displaying text from a file using a specified font.
- Explains how to set graphic units for resizing elements in a PDF document.

## Content

### [VB.NET]

```vb
'Add CJK font to the font collection
string font = "gulim.ttf";
PrivateFontCollection fcol = new PrivateFontCollection();
fcol.AddFontFile(font);
Font f = new Font(fcol.Families[0], 14);
PdfFont font = new PdfTrueTypeFont(f, true);
string koreanText = "korean.txt";

'Read the text from text file
StreamReader reader = new StreamReader(koreanText, Encoding.Unicode);
string text = reader.ReadToEnd();
reader.Close();

page.Graphics.DrawString(text, font, brush, PointF.Empty);
```

#### 5.1.1.10 How To Set Graphic Units?

Essential PDF sets the size of an element in terms of points [1/72 inch]. It has a utility class, `PdfUnitConverter`, which enables to convert different measure units and use them for resizing pages.

### [C#]

```csharp
// Setting Page size after converting units to points
PdfUnitConverter con = new PdfUnitConverter();
doc.PageSettings.Width = con.ConvertUnits(100f, PdfGraphicsUnit.Millimeter, PdfGraphicsUnit.Point);
```

### [VB.NET]

```vb
' Setting Page size after converting units to points
Dim con As New PdfUnitConverter()
doc.PageSettings.Width = con.ConvertUnits(100F, PdfGraphicsUnit.Millimeter, PdfGraphicsUnit.Point)
```

#### Note: 
The width or height property of the document is always represented by using Points [1/72 inch]. However, the helper method enables you to set page sizes in the desired unit.
```

<!-- tags: [pdf, graphic units, font handling, resizing, text rendering] keywords: [Syncfusion, PDF, CJK font, graphic units, FontCollection, PdfTrueTypeFont, StreamReader, PdfUnitConverter] -->
```