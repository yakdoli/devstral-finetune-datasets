```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: pdf
page_number: 041
page_id: pdf#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:24Z
fidelity: lossless
-->

# Essential PDF

Create PDF graphics for the page.

```csharp
PdfGraphics g = page.Graphics;
// Create a solid brush
PdfBrush brush = new PdfSolidBrush(Color.Black);
float fontSize = 20f;
// Set the font
PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, fontSize);
// Draw the text
g.DrawString("Hello world!", font, brush, new PointF(20, 20));

// Stream the output to the browser.
if (this.CheckBox1.Checked)
{
    doc.Save("Sample.pdf", Response, HttpReadType.Open);
}
else
{
    doc.Save("Sample.pdf", Response, HttpReadType.Save);
}
```

The sample PDF document created through the above procedure is shown below.

<!-- tags: [pdf, graphics, font, brush, drawstring, essentialpdf] keywords: [pdf, essentialpdf, drawstring, font, brush, response] -->
```