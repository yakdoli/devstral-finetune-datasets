```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_215.jpeg
document_name: pdf
page_number: 215
page_id: pdf#page_215
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:30Z
fidelity: lossless
-->

# Essential PDF

```vb
'Define the text formats
Dim format As PdfStringFormat = New PdfStringFormat()
format.Alignment = PdfTextAlignment.Justify
format.LineAlignment = PdfVerticalAlignment.Top
format.ParagraphIndent = 15f

'Create a text element
Dim element As PdfTextElement = New PdfTextElement(text, font)
element.Brush = New PdfSolidBrush(Color.Black)
element.StringFormat = format
element.Font = New PdfStandardFont(PdfFontFamily.Helvetica, 12)

'Set pagination properties for the text
Dim layoutFormat As PdfLayoutFormat = New PdfLayoutFormat()
layoutFormat.Break = PdfLayoutBreakType.FitPage
layoutFormat.Layout = PdfLayoutType.Paginate
Dim bounds As RectangleF = New RectangleF(PointF.Empty, page.Graphics.ClientSize)

'Draw the text element with the specified layout and formats
Dim result As PdfTextLayoutResult = element.Draw(page, bounds, layoutFormat)

'Save the document
doc.Save("Sample.pdf")
```

## Overview
- Describes how to format and draw text in a PDF document using Syncfusion's PDF library.
- Covers text alignment, indentation, font selection, and pagination.
- Demonstrates saving the formatted document as a PDF file.

## Code Example

The provided code snippet demonstrates the following:
- **Setting Text Formats**: Defines alignment, line alignment, and paragraph indent.
- **Creating a Text Element**: Creates a `PdfTextElement` with specified font settings.
- **Pagination Settings**: Configures layout to paginate text within the page bounds.
- **Rendering Text**: Draws the text element on a PDF page with the specified layout.
- **Saving the Document**: Saves the final PDF document with the formatted text.

This example is particularly useful for developers working with Syncfusion's PDF library to ensure text is properly formatted and paginated in WinForms applications.

<!-- tags: [Syncfusion, WinForms, PDF Library, Text Formatting, Pagination, PDF] keywords: [Syncfusion, WinForms, PDF, TextElement, Pagination, Layout, Formatting] -->
```