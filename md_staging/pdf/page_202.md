```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_202.jpeg
document_name: pdf
page_number: 202
page_id: pdf#page_202
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:17Z
fidelity: lossless
--> 

## Essential PDF

### Overview
- Demonstrates creating a PDF document with text and rendering it.
- Uses a solid brush and font styles for rendering.

### Content

```cs
//Add a page.
PdfPage page = doc.Pages.Add();

//Create Pdf graphics for the page.
PdfGraphics g = page.Graphics;

//Create a solid brush.
PdfBrush brush = new PdfSolidBrush(Color.Black);
float fontSize = 20f;
Font f = new Font("Helvetica", fontSize, FontStyle.Regular);

//Set the font.
PdfFont font = new PdfTrueTypeFont(f, true);

//Draw the text.
g.DrawString("Hello world!", font, brush, new PointF(20, 20));
doc.Save("Sample.pdf");
```

```vb
'Create a new document with PDF/A standard.
Dim doc As PdfDocument = New PdfDocument(PdfConformanceLevel.Pdf_A1B)

'Add a page.
Dim page As PdfPage = doc.Pages.Add()

'Create Pdf graphics for the page.
Dim g As PdfGraphics = page.Graphics

'Create a solid brush.
Dim brush As PdfBrush = New PdfSolidBrush(Color.Black)
Dim fontSize As Single = 20f
Dim f As Font = New Font("Helvetica", fontSize, FontStyle.Regular)

'Set the font.
Dim font As PdfFont = New PdfTrueTypeFont(f, True)

'Draw the text.
g.DrawString("Hello world!", font, brush, New PointF(20, 20))
doc.Save("Sample.pdf")
```

## Page-level Navigation/TOC (if applicable)
- None present in this section.

## Cross References
- None present in this section.

<!-- tags: [Syncfusion, Essential PDF, PDF document, text rendering] keywords: [pdf, graphics, font, brush, text rendering, hello world] -->
```