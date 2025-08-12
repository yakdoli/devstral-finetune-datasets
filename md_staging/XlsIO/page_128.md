```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_128.jpeg
document_name: XlsIO
page_number: 128
page_id: XlsIO#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:28Z
fidelity: lossless
-->

## Overview

- Demonstrates how XlsIO handles number formatting in Excel cells.
- Explains the application of various number formats and their effects on data presentation.
- Introduces border settings in Excel cells and how they can be controlled.

## Content

### Border Settings

#### Introduction

Microsoft Excel provides a default appearance for a cell background. For example, it surrounds the cell with a gray border and a white background. You can control this default appearance through the Formatting toolbar or the Border tab in the Format Cells dialog box.

#### Figure: XlsIO with Number Formatting

The figure below illustrates different number formats applied to various data values and their resulting display formats in an Excel sheet. The table below lists the data, the applied number format, and the final result:

| Data                     | Number Format Applied | Result                          |
|--------------------------|-----------------------|----------------------------------|
| 1000000.00075           | 0.00                  | 1000000.00                      |
| 1000000.500             | ###,###               | 1,000,001                       |
| 1.20                    | $#,##0.00            | $1.20                           |
| 10000                   | 0.00                  | 10000.00                        |
| -500                    | [Blue]#,###0         | -500                            |
| 0.000000000000000001234567890 | [Blue]#,###0 | 0.000000000000000001234567890 |
| 1.20                    | 0.00%                | 120.00%                         |
| 1.20                    | 0.00E+00             | 1.20E+00                        |

The sample Excel sheet is shown in the image below:

![XlsIO with Number Formatting](attachment://Figure_39.png)

#### Explanation of Border Settings

Microsoft Excel allows you to customize the appearance of cell borders to enhance data visibility and organization. You can adjust border styles, line weights, and colors to suit your needs. This can be particularly useful for highlighting specific rows or columns, or for creating visual groupings within a worksheet. The options for border customization are accessible through the Formatting toolbar or the Border tab in the Format Cells dialog box, providing a flexible way to manage the visual presentation of your data.

### Figure: XlsIO with Number Formatting Explained

The figure shows how various number formats affect the presentation of data in an Excel sheet. Each row demonstrates a different number format applied to a specific value, resulting in a transformed display format. This allows users to present numerical data in a way that is not only precise but also visually intuitive and easy to understand.

#### Summary

This section covers the concepts of number formatting and border settings in Excel using XlsIO. It demonstrates how to apply various number formats to data cells and explains how to adjust the default border appearance for enhanced visual clarity. These features are essential for creating professional-looking spreadsheets that effectively communicate data.

### API Reference

- **Namespace**: Syncfusion.XlsIO
- **Class**: Workbook
- **Members**:
  - **Methods**: ApplyNumberFormat(String cellRange, String format)
  - **Properties**: Cells.Style.Border
  - **Events**: None

#### Parameters

| Name           | Type         | Description                                                                                                                                                 | Default | Required |
|----------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|----------|
| cellRange      | String       | The range or cell reference where the number format is applied.                                                                                           | N/A     | Yes      |
| format         | String       | The number format to be applied (e.g., "0.00", "###,###", "[$#,##0.00]", etc.).                                                                         | N/A     | Yes      |

#### Returns

- No return value. The method is used for side effects on the specified cell range.

#### Exceptions

- ArgumentException: If the `cellRange` or `format` is invalid.

### Code Examples

```csharp
// Example: Applying a number format to a range of cells
using(SpreadsheetDocument document = SpreadsheetDocument.Create("NumberFormat.xlsx", SpreadsheetDocumentType.Excel))
{
    WorkbookPart workbookPart = document.AddWorkbookPart();
    workbookPart.Workbook = new Workbook();

    WorksheetPart worksheetPart = workbookPart.AddNewPart<WorksheetPart>();
    Sheet sheet = new Sheet() { Id = workbookPart.GetIdOfPart(worksheetPart), SheetId = 1, Name = "Sample" };

    workbookPart.Workbook.Append(sheet);

    Worksheet worksheet = new Worksheet();
    worksheetPart.Worksheet = worksheet;

    // Add a CellStyleFormat for the workbook
    WorkbookPart workbookPart = document.AddWorkbookPart();
    Workbook workbook = new Workbook();
    workbookPart.AddPart(workbookPart);

    // Add a cell reference and style information
    Cell cell = new Cell() { CellReference = "A1", StyleIndex = 1 };
    CellValue cellValue = new CellValue("12345");
    cell.Append(cellValue);

    // Add row and column information
    Row row = new Row() { RowIndex = 1 };
    row.Append(cell);

    // Create a TableStyleElement to define the number format
    TableStyleElement tableStyleElement = new TableStyleElement() { NumberFormatId = 2, CellFillId = 1 };
    CellFormat cellFormat = new CellFormat() { NumberFormatId = 2 };

    // Apply formatting
    workbookPart.AddPart(tableStyleElement);
    workbookPart.AddPart(cellFormat);
}
```

## Page-level Navigation/TOC

- Figure: XlsIO with Number Formatting
- 4.1.1.4 Border Settings
- Summary

## Cross References

- See also: Chapter 4: XlsIO Formatting and Styling
- Chapter 5: Advanced Excel Features

## RAG Annotations

<!-- tags: XlsIO, number formatting, border settings, formatting toolbar, format cells dialog, Excel, Winforms keywords: XlsIO, Microsoft Excel, number format, border style, formatting toolbar, format cells dialog, visual presentation, data, number formatting, Excel cells, border settings -->
```