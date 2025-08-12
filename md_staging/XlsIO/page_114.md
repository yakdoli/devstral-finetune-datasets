```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_114.jpeg
document_name: XlsIO
page_number: 114
page_id: XlsIO#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:07Z
fidelity: lossless
-->

## Formatting Last 4 Characters

- **Overview:**
  - Demonstrates how to apply font formatting to specific characters in a cell.
  - Creates a bold, italic, blue font and applies it to the last 4 characters of a string.

### Code Example

```csharp
' Formatting last 4 characters.
Dim blueFont As IFont = workbook.CreateFont()
blueFont.Bold = True
blueFont.Italic = True
blueFont.RGBColor = Color.Blue
rtf.SetFont(4, 7, blueFont)
```

### Visual Example

Figure 35: XlsIO with Font Settings

![Figure 35: XlsIO with Font Settings](https://i.imgur.com/example.png) <!-- Placeholder -->

### Explanation

The code snippet creates a custom font style with bold, italic, and blue color attributes. This font is then applied to the last 4 characters of the text in the specified cell range.

---

## 4.1.1.2 Alignment Settings

The following are some of the alignment settings available in Excel.

---

## API Reference (if applicable)
- None specified in this context.

## Code Examples (multi-language supported)
- Only the above code example is provided.

## Page-level Navigation/TOC (if applicable)
- None specified in this context.

## Cross References
- Refer to the previous sections for related font and formatting examples.

---

<!-- tags: [XlsIO, font settings, alignment settings, Excel formatting, bold italic font, color formatting] keywords: [XlsIO, IFont, workbook.CreateFont(), bold, italic, RGBColor, blue, rtf.SetFont()] -->
```