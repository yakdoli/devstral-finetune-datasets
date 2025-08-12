```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_129.jpeg
document_name: XlsIO
page_number: 129
page_id: XlsIO#page_129
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:06Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Provides support to insert and format borders in MS Excel through the `IBorder` interface.
- Demonstrates how borders can be applied using the `IBorder` interface in C#.

## Content

### Border Settings in XlsIO

XlsIO provides support to insert and format borders through the `IBorder` interface. The following code example illustrates how this can be done.

#### Code Example

```csharp
// The first worksheet object in the Worksheets collection is accessed.
IWorksheet sheet = workbook.Worksheets[0];

// Setting Border Line Styles.
sheet.Range["A2"].CellStyle.Borders.LineStyle = ExcelLineStyle.Medium;
sheet.Range["A4"].CellStyle.Borders.LineStyle = ExcelLineStyle.Double;
sheet.Range["A6"].CellStyle.Borders.LineStyle = ExcelLineStyle.Dash_dot;
sheet.Range["A8"].CellStyle.Borders.LineStyle = ExcelLineStyle.Thick;
sheet.Range["A10"].CellStyle.Borders.LineStyle = ExcelLineStyle.Thin;
sheet.Range["A12"].CellStyle.Borders.LineStyle = ExcelLineStyle.Medium_dashed;
sheet.Range["B2"].CellStyle.Borders.LineStyle = ExcelLineStyle.Slanted_dash_dot;
```

### Figure: Format Cells Dialog of MS Excel - Border tab
![Figure 40: Format cells Dialog of MS Excel - Border tab](https://i.imgur.com/ExampleFigure.png)

## API Reference

### Namespace: Excel.IO

#### Class: IBorder
- Methods and Properties related to setting border styles in Excel cells.

### Member Details
- **LineStyle**: Sets the line style of the border.
  - **Type**: `ExcelLineStyle`
  - **Possible Values**:
    - `Medium`
    - `Double`
    - `Dash_dot`
    - `Thick`
    - `Thin`
    - `Medium_dashed`
    - `Slanted_dash_dot`
  - **Usage**: `sheet.Range["A2"].CellStyle.Borders.LineStyle = ExcelLineStyle.Medium;`

## Code Examples

#### Example: Setting Border Line Styles
```csharp
// Access the first worksheet
IWorksheet sheet = workbook.Worksheets[0];

// Set different line styles for borders
sheet.Range["A2"].CellStyle.Borders.LineStyle = ExcelLineStyle.Medium;
sheet.Range["A4"].CellStyle.Borders.LineStyle = ExcelLineStyle.Double;
sheet.Range["A6"].CellStyle.Borders.LineStyle = ExcelLineStyle.Dash_dot;
sheet.Range["A8"].CellStyle.Borders.LineStyle = ExcelLineStyle.Thick;
sheet.Range["A10"].CellStyle.Borders.LineStyle = ExcelLineStyle.Thin;
sheet.Range["A12"].CellStyle.Borders.LineStyle = ExcelLineStyle.Medium_dashed;
sheet.Range["B2"].CellStyle.Borders.LineStyle = ExcelLineStyle.Slanted_dash_dot;
```

## Cross References
- See also: [XlsIO Documentation](#XlsIO-Doc)
- Related features: Border styling, Excel cell formatting.

<!-- 
tags: [XlsIO, Border settings, MS Excel, IBorder interface, Excel formatting, Syncfusion Winforms]
keywords: [XlsIO, Border settings, ExcelLineStyle, IBorder, worksheet formatting, line styles]
-->
```