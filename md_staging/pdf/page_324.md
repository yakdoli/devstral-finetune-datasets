```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_324.jpeg
document_name: pdf
page_number: 324
page_id: pdf#page_324
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:36Z
fidelity: lossless
-->

## Overview
- Essential PDF conversion examples using the HTML to PDF conversion feature.
- Limitations of HTML to PDF conversion, particularly with dynamic scripts and specific features.
- Introduction to tagged PDF generation using the MSHTML rendering engine.

## Content

### Essential PDF

```csharp
// Initializing the html converter
HtmlConverter converter = new HtmlConverter(renderer);

// Converting html to pdf
HtmlToPdfResult result = converter.Convert(txtUrl.Text, ImageType.Metafile, width, height, AspectRatio.KeepWidth);

// Rendering the image in the PDF document
result.Render(document);
```

#### Limitations
1. **Formatting / styles created using dynamic scripts will not be rendered in the resultant PDF.**
2. **Other features in HTML to PDF conversion such as hyperlinks will not be available for conversion using Gecko rendering engine. However, the page breaks are supported but we can't explicitly control the page break.**

### 4.4.1.2 Tagged PDF

HTML to PDF conversion handled using MSHTML rendering library can now generate tagged PDF documents.

#### Overview
- Tagged PDF is a stylized use of PDF that builds on the logical structure framework. It defines a set of standard structure types and attributes that allow page content (text, graphics, and images) to be extracted and reused. The contents are accessible to users with visual impairments.
- HTML documents can be converted to tagged PDFs using the `ConvertToTaggedPDF` method. It returns `PdfLayoutResult` which provides the end rectangle bounds and PDF page after the conversion.

#### API Reference

##### C#
```csharp
public PdfLayoutResult ConvertToTaggedPDF(PdfDocument document, string url);

public PdfLayoutResult ConvertToTaggedPDF(PdfDocument document, string url, string userName, string password);

public PdfLayoutResult ConvertToTaggedPDF(PdfDocument document, string html, string baseURL);
```

##### VB.NET
```vb
public PdfLayoutResult ConvertToTaggedPDF(PdfDocument document, String url)

public PdfLayoutResult ConvertToTaggedPDF(PdfDocument document, String url, String userName, String password)

public PdfLayoutResult ConvertToTaggedPDF(PdfDocument document, String html, String baseURL)
```

<!-- tags: [syncfusion, winforms, essentialpdf, htmltopdfconverter, taggedpdf, mshtml, conversion, accessibility, dynamicscripts, hyperlinks, pagebreaks, rendering, imageformatting] keywords: [htmlto_pdf, pdf_conversion, accessibility_features, dynamic_styles, hyperlinks_support, support, page_breaks, tagged_pdf_generation, pdf_layout_result] -->
```