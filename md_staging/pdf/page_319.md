```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_319.jpeg
document_name: pdf
page_number: 319
page_id: pdf#page_319
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:32Z
fidelity: lossless
-->

# Essential PDF

```vb
Dim pdfImage As PdfImage = pdfImage.FromImage(result)
pdfImage.Draw(pdfPage, PointF.Empty, format)
```

**Note:** Both `ConvertToImage()` and `FromString()` methods are used to convert the HTML pages whose height is less than 32767 pixels as image, and the options like `EnableHyperlinks`, `EnableJavascript`, and `AutoDetectPageBreak` have no effect.

![Figure 64: HTML to PDF Conversion Through FromString Method](https://user-images.githubusercontent.com/11642654/226714462-3462a61a-789f-4c6d-8191-a85b5102174d.png)

## HtmlConverter Options

HtmlConverter provides the following options to control HtmlToPDF conversions.

- EnableJavaScript
- AutoDetectPageBreak
- Enable Hyperlinks
```html

<!-- tags: [HtmlConverter, HtmlToPDF, PDF, FromString, ConvertToImage, AutoDetectPageBreak, EnableHyperlinks, EnableJavascript, Essential PDF] keywords: [HtmlConverter, HtmlToPDF, PDF, FromString, EnableHyperlinks, EnableJavaScript, AutoDetectPageBreak, ASP.NET, Windows Forms, Back Office, Microsoft Office, Adobe PDF] -->
```