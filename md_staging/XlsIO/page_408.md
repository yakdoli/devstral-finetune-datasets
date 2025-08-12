```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_408.jpeg
document_name: XlsIO
page_number: 408
page_id: XlsIO#page_408
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:40Z
fidelity: lossless
-->

# Essential XlsIO

- Sheet Tabs

## Grid Lines

Some users may find it easier to work with your worksheet applications, if they cannot see the grid lines. Excel provides options to show/hide grid lines in the worksheet. This is done by accessing the GridLines option by opening the Tools menu, pointing to Option, and then selecting GridLines.

XlsIO provides support for this feature through the IsGridLine property of IWorksheet. Color for the grid line can also be set through the GridLineColor property of IWorksheet.

### Example: Hiding Grid Lines

```csharp
// Hides grid line.
sheet.IsGridLinesVisible = false;
```

```vb
' Hides grid line.
sheet.IsGridLinesVisible = False
```

## Headings

Headings are the display labels in worksheets that enable users to find out the cell number with ease. You can show/hide these headings by using the IsRowColumnHeadersVisible property of IWorksheet.

### Example: Hiding Row and Column Headers

```csharp
sheet.IsRowColumnHeadersVisible = false;
```

```vb
sheet.IsRowColumnHeadersVisible = False
```

## API Reference

- **IsGridLine** (Property): Indicates whether the grid lines are visible in the worksheet.
- **GridLineColor** (Property): Specifies the color of the grid lines in the worksheet.
- **IsRowColumnHeadersVisible** (Property): Controls the visibility of row and column headings in the worksheet.

<!-- tags: [XlsIO, worksheet, grid lines, head, property, visible, hide, show] keywords: [XlsIO, worksheet, grid lines, headings, hide, show] -->
```