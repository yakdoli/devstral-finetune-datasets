```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_082.jpeg
document_name: pdf
page_number: 082
page_id: pdf#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:05Z
fidelity: lossless
-->

# Essential PDF

## Overview
- This page explains how to format and layout text elements in a PDF document using Syncfusion's PDF library. It provides examples in both C# and VB.NET for setting layout properties and using PdfStringFormat for string formatting.

## Content

### C# Example
// Set the layout format properties to make the text flow through multiple pages.
```csharp
PdfLayoutFormat layoutFormat = new PdfLayoutFormat();
layoutFormat.Break = PdfLayoutBreakType.FitPage;
layoutFormat.Layout = PdfLayoutType.Paginate;

// Set the bounds.
RectangleF bounds = new RectangleF(PointF.Empty, page.Graphics.ClientSize);

// Draw the text element.
element.Draw(page, bounds, layoutFormat);
```

### [VB]
```vb
' Create a text element with large amount of text.
Dim element As Syncfusion.Pdf.Graphics.PdfTextElement = New Syncfusion.Pdf.Graphics.PdfTextElement(Text, Font)

' Set the properties for the text element.
element.Brush = New PdfSolidBrush(Color.Black)

' Set the string format. This can be used for setting unicode text.
element.StringFormat = format

' Set the layout format properties to make the text flow through multiple pages.
Dim layoutFormat As Syncfusion.Pdf.Graphics.PdfLayoutFormat = New Syncfusion.Pdf.Graphics.PdfLayoutFormat()
layoutFormat.Break = PdfLayoutBreakType.FitPage
layoutFormat.Layout = PdfLayoutType.Paginate

' Set the bounds.
Dim bounds As RectangleF = New RectangleF(PointF.Empty, page.Graphics.ClientSize)

' Draw the text element.
element.Draw(page, bounds, layoutFormat)
```

### 3. String Formatting

For dedicated presentation of text in a PDF document, use a PdfStringFormat object. The PdfStringFormat class provides support for the following features:

- CharacterSpacing, WordSpacing and LineSpacing
- Right-To-Left languages such as Arabic, Hebrew, Urdu, and so on
- Center, Left, Right and Justify text alignments

<!-- tags: [pdf, layoutformat, stringformat, textformat, pdfstringformat, textelement, pagelayout, textspacing] keywords: [pdf, layout, string format, text format, pdf text element, text alignment, text spacing, text formatting, pdfstringformat, pdflayoutformat, pdfgraphics, text pagination, text layout] -->
```