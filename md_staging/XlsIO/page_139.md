```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_139.jpeg
document_name: XlsIO
page_number: 139
page_id: XlsIO#page_139
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:16Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- Provides support for adding and modifying common (or global) styles that can be applied to several ranges of cells in a workbook.
- Usage of global styles is recommended to improve performance when multiple cells require the same formatting.

## Content

### Global Styles

#### 4.1.1.6.1.2 Global Styles

XlsIO provides support for adding and modifying common (or global) styles that can be applied to one or more cells in a workbook. These styles can be created and applied to several ranges of cells in the workbook. Note that the usage of common styles to format spreadsheets is the recommended approach, since setting a separate style for each cell can reduce the performance considerably.

---

**Note:** If you want to apply more than one style for cells, enclose the style within the Begin and End calls. This will improve the performance.

```csharp
// Formatting

// Global styles should be used when the same style needs to be applied to
// more than
// one cell. This usage of a global style reduces memory usage.

// Header Style
IStyle headerStyle = workbook.Styles.Add("HeaderStyle");

// Add custom colors to the palette.
headerStyle.BeginUpdate();
workbook.SetPaletteColor(8, Color.FromArgb(255, 174, 33));
headerStyle.Color = Color.FromArgb(255, 174, 33);
headerStyle.Font.Bold = true;
headerStyle.Borders[ExcelBordersIndex.EdgeLeft].LineStyle = ExcelLineStyle.Thin;
headerStyle.Borders[ExcelBordersIndex.EdgeRight].LineStyle = ExcelLineStyle.Thin;
headerStyle.Borders[ExcelBordersIndex.EdgeTop].LineStyle = ExcelLineStyle.Thin;
headerStyle.Borders[ExcelBordersIndex.EdgeBottom].LineStyle = ExcelLineStyle.Thin;
headerStyle.EndUpdate();

// Body Style
IStyle bodyStyle = workbook.Styles.Add("BodyStyle");

// Add custom colors to the palette.
bodyStyle.BeginUpdate();
```

## RAG Annotations

<!-- tags: [XlsIO, global styles, performance improvement, styling, workbook formatting] keywords: [global styles, performance, cell formatting, workbook, Excel, custom colors, thin lines, bold font] -->
```