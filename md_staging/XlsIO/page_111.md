```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_111.jpeg
document_name: XlsIO
page_number: 111
page_id: XlsIO#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:43Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- MS Excel provides support to customize font settings through the **Format Cells** dialog box.
- The Font tab in the format dialog box offers options to set font name, size, color, and additional settings.
- XlsIO provides API support for specifying font styles in cell text using the **CellStyle** property.
- The **CellStyle.Font** property exposes various font settings.

## Content

### MS Excel Font Settings

MS Excel provides support to customize the font settings through the **Format Cells** dialog box. The Font tab in the format dialog box provides options to set the font name, size, color, and so on.

![Font settings in MS Excel](Figure 34: Font settings in MS Excel)
*Figure 34: Font settings in MS Excel*

### Font Settings in XlsIO

XlsIO also has API support for specifying the font style for the text in the cells. The **CellStyle** property exposes various font settings, which is illustrated in the following code.

#### Code Example

```csharp
// Setting Font Type.
sheet.Range["A2"].CellStyle.Font.FontName = "Arial Black";
sheet.Range["A4"].CellStyle.Font.FontName = "Castellar";

// Setting Font Styles.
sheet.Range["A6"].CellStyle.Font.Bold = true;
sheet.Range["A8"].CellStyle.Font.Italic = true;

// Setting Font Size.
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

## Cross References
- Add See also: bullet list of explicit links/texts present on this page. Do not fabricate.

## RAG Annotations
<!-- tags: [XlsIO, font settings, MS Excel, CellStyle, API support, font types, font styles, FontSize, FontName, Bold, Italic] keywords: [font configuration, font customization, Format Cells dialog box, TrueType font, Arial, properties, cell styles, C# code example] -->
```