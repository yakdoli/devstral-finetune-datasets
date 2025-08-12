```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: XlsIO
page_number: 052
page_id: XlsIO#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:47Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Border settings and fill settings are supported.
- Autofit is not supported.
- Cell styles and conditional formatting are available.
- RGB colors are supported with indexed options.

## Content

### Features Matrix

| Feature                | Feature 1 | Feature 2 |
|------------------------|-----------|-----------|
| Border settings       | Yes       | Yes       |
| Fill settings         | Yes       | Yes       |
| Autofit               | No        | No        |
| Cell styles           | Yes       | Yes       |
| RGB Colors            | Yes (Indexed) | Yes (Indexed) |
| Conditional formatting | Yes       | Yes       |
| Hide/unhide rows/cols | Yes       | Yes       |
| Hide/Unhide worksheet | Yes       | Yes       |
| Copy/Move worksheet   | Yes       | Yes       |
| Sheet protection       | Yes       | Yes       |
| Workbook protection    | Yes       | Yes       |
| Sheet format ([sheet name, tab color] | Yes       | Yes       |
| Bitmap Images         | Yes       | Yes       |
| Vector Images         | Yes       | Yes       |
| Charts                | Yes       | Yes       |
| Hyperlinks            | Yes       | Yes       |
| Header/Footer         | Yes       | Yes       |
| Pivot tables           | No        | No        |
| Auto Shapes            | No        | No        |
| Text Box              | Yes       | Yes       |
| Check Box             | Yes       | Yes       |
| Combo Box             | Yes       | Yes       |

## API Reference (if applicable)

This section is not provided in the image content. APIs related to XlsIO could include:
- **Namespace**: Syncfusion.XlsIO
- **Classes**: Workbook, Worksheet
- **Properties**: Border, Fill, ConditionalFormatting, CellStyle
- **Methods**: HideRow(), UnhideRow(), HideSheet(), UnhideSheet()

## Code Examples (multi-language supported)

```csharp
// Example: Setting border and fill for a cell
using Syncfusion.XlsIO;

Workbook wb = new Workbook();
IWorksheet sheet = wb.Worksheets[0];

// Set border and fill
sheet.Range["A1"].Border.Color = ExcelKnownColor.Blue;
sheet.Range["A1"].Fill.ForeColor.Color = ExcelKnownColor.LightBlue;
sheet.Range["A1"].Fill.Pattern = ExcelFillPattern.Solid;

// Save and close
wb.Save(fileName);
wb.Close();
```

## Page-level Navigation/TOC (if applicable)

No table of contents or additional navigation elements are present in the given image.

## Cross References

- See also: For more information on Excel formatting options, refer to the official XlsIO documentation: [Link to Documentation](https://help.syncfusion.com/xlsio/overview).

<!-- tags: [XlsIO, Excel, formatting, features, Border settings, Fill settings, Autofit, Cell styles, RGB Colors, Conditional formatting, Hide/Unhide, Sheet protection, Workbook protection, Bitmap Images, Vector Images, Charts, Hyperlinks, Header/Footer, Pivot tables, Auto Shapes, Text Box, Check Box, Combo Box] keywords: [Syncfusion XlsIO, Excel features, formatting, styling, data protection, images, charts, hyperlinks, sheet management] -->
```