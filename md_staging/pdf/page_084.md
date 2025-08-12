```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: pdf
page_number: 084
page_id: pdf#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:30Z
fidelity: lossless
-->

# Essential PDF

## Overview
- The `PdfMetafileLayoutFormat` class enables breaking HTML text into multiple pages.
- Supports a subset of XHTML-compliant tags for rendering HTML content in PDF documents.

## Content

### Supported Tags (Should be XHTML-compliant)

- **Font**
- **B**
- **I**
- **U**
- **St**
- **sub**
- **sup**
- **BR**

The following code example illustrates how to render the HTML string in a PDF document.

#### Code Example in C#
```csharp
[C#]

// HtmlString
string longText = "<font color='#0000F8'>Essential PDF</font> is a <u><i>.NET</i></u> " + 
                  "library with the capability to produce Adobe PDF files ";

// Rendering HtmlText
PdfHTMLTextElement richTextElement = new PdfHTMLTextElement(longText, font, 
                                                           brush);
richTextElement.TextAlign = TextAlign.Justify;

// Formatting Layout
PdfMetafileLayoutFormat format = new PdfMetafileLayoutFormat();
format.Layout = PdfLayoutType.OnePage;
format.Break = PdfLayoutBreakType.FitPage;

// Drawing htmlString
richTextElement.Draw(page, new RectangleF(30, 30, 600, 
                                         page.GetClientSize().Height), format);
```

#### Code Example in VB.NET
```vb
[VB.NET]

' HtmlString
Dim longText As String = "<font color='#0000F8'>Essential PDF</font> is a <u><i>.NET</i></u> " + 
                         "library with the capability to produce Adobe PDF files "

' Rendering HtmlText
PdfHTMLTextElement richTextElement = new PdfHTMLTextElement(longText, font, 
                                                           brush)
richTextElement.TextAlign = TextAlign.Justify

// Formatting Layout
PdfMetafileLayoutFormat format = new PdfMetafileLayoutFormat()
format.Layout = PdfLayoutType.OnePage
format.Break = PdfLayoutBreakType.FitPage

// Drawing htmlString
richTextElement.Draw(page, new RectangleF(30, 30, 600, 
                                         page.GetClientSize().Height), format)
```

### Note: The VB.NET example above seems to have been partially cut off. It should follow a similar structure to the C# example, ensuring complete code for clarity and functionality.

## API Reference

### Classes and Methods Used
- **PdfHTMLTextElement**: Represents an HTML text element for rendering.
- **PdfMetafileLayoutFormat**: Specifies the layout settings for rendering HTML content.
- **TextAlign**: Enum for text alignment options.
- **PdfLayoutType**: Enum for layout types (e.g., OnePage).
- **PdfLayoutBreakType**: Enum for break types (e.g., FitPage).

### Parameters and Values
- **longText**: The HTML string to be rendered.
- **font**: The font used for rendering the HTML text.
- **brush**: The brush used for rendering the HTML text.
- **page**: The PDF page where the HTML content is drawn.
- **RectangleF**: The bounding rectangle for the HTML content.

## Cross References
- Refer to the documentation for more information on [PdfMetafileLayoutFormat](#pdfmetafilelayoutformat) and [PdfHTMLTextElement](#pdfhtmltextelement) for advanced usage.

<!-- tags: [Essential PDF, HTML rendering, PDF, layout, text formatting] keywords: [PdfMetafileLayoutFormat, PdfHTMLTextElement, HtmlString, TextAlignment, OnePage, FitPage] -->
```