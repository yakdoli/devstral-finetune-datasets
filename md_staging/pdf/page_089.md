```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_089.jpeg
document_name: pdf
page_number: 089
page_id: pdf#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:07Z
fidelity: lossless
-->

# Essential PDF

```csharp
PdfPage page = document.Pages.Add();
page.Graphics.DrawPdfTemplate(template, new Point(50, 50));
}
```

### [VB.NET]

```vb
Dim document As PdfDocument = New PdfDocument()
Dim page As PdfPage = document.Pages.Add()

Dim font As PdfFont = New PdfStandardFont(PdfFontFamily.Helvetica, 12.0F)
Dim brush As PdfBrush = PdfBrushes.Black

Dim template As PdfTemplate = New PdfTemplate(15, 15)

Dim dateField As PdfDateTimeField = New PdfDateTimeField(font, brush)
Dim dateField.DateFormatString = "dd/MMM/yyyy"

dateField.Draw(template.Graphics)

For i As Integer = 0 To 49
    Dim page As PdfPage = document.Pages.Add()
    page.Graphics.DrawPdfTemplate(template, New Point(50, 50))
Next i
```

## 4.1.2.1.4 Links

A hyperlink, which is more commonly called a link, is an electronic connection between one web page and other web pages on the same web site, or web pages located on another web site. More specifically, a hyperlink is a connection between one page of a hypertext document to another.

You can create hyperlinks in a PDF document by using the `PdfTextWebLink` class. The `DrawTextWebLink` method is used to draw hyperlinks in PDF pages.

The following code example illustrates how to draw hyperlinks.

### [C#]

```csharp
// Create the Text Web Link
PdfTextWebLink textLink = new PdfTextWebLink();
textLink.Url = "http://www.google.com";
```

```html
<!-- tags: [pdf, hyperlink, pdfdatetimefield, pdftemplate, synfusion, winforms, hyperlink creation, pdftextweblink, drawtextweblink, dateformatstring] keywords: [pdf, hyperlink, datefield, template, brush, font, web link, url] -->
```