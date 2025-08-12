```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: pdf
page_number: 083
page_id: pdf#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:19Z
fidelity: lossless
-->

# Essential PDF

- Subscript and superscript modes
- ParagraphIndent customization
- WordWrapType style
- MeasureTrailingSpaces

## 4. RTF Support

The Rich Text Format (RTF) specification is a method of encoding formatted text and graphics such as bold characters and typefaces, document formatting and structures, for easy transfer between applications. Essential PDF supports drawing RTF text into a PDF document by using the `FromRtf` method in the `PdfImage` class.

You can draw RTF text by converting it into a bitmap or metafile image. Converting RTF text into a bitmap file provides improved performance, while converting RTF text into a metafile image provides high resolution and searchable text.

The following code example illustrates this.

### [C#]

```csharp
public PdfImage FromRtf(string rtf, float width, PdfImageType type)
public PdfImage FromRtf(string rtf, float width, float height, PdfImageType type)
```

### [VB.NET]

```vbnet
Public PdfImage FromRtf(String rtf, single width, PdfImageType type)
Public PdfImage FromRtf(String rtf, single width, single height, PdfImageType type)
```

## For More Information Refer:

- [Draw Rich Text](Draw%20Rich%20Text)

### 4.1.2.1.2 Html Styled Text

Essential PDF provides support to render the HTML string in a PDF document, which can flow to multiple pages by using the `PdfHTMLTextElement` class. The `PdfHTMLTextElement` class contains methods, which are used to render the specified HTML string in the PDF document. It draws the specified text string at the specified location with the specified size, brush and font. You can also align the text by using the `TextAlign` property.

<!-- tags: [pdf, rtf, html, styled text, text rendering, winforms, syncfusion] keywords: [essential pdf, rtf support, html text rendering, text element, pdfimage, fromrtf, pdfhtmltextelement, textalign, render html in pdf] -->
```