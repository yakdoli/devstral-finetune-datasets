```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: XlsIO
page_number: 079
page_id: XlsIO#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:53:16Z
fidelity: lossless
-->

## Overview

- Provides details about various properties available in the XlsIO module, focusing on spreadsheet view configuration and security settings.
- Includes properties to manage visibility of panes, gridlines, headers, and merged cells.
- Highlights attributes related to freezing panes, page breaks, hyperlinks, and password protection.

## Content

### Spreadsheet View Properties

The following table lists the properties that control the appearance and behavior of a worksheet in XlsIO:

| Property | Description |
|----------|-------------|
| `FirstVisibleColumn` | Index to first visible column in right pane(s). |
| `FirstVisibleRow` | Index to first visible row in bottom pane(s). |
| `HorizontalSplit` | Position of the horizontal split (by, 0 = No horizontal split): Unfrozen pane: Height of the top pane(s) (in twips = 1/20 of a point) Frozen pane: Number of visible rows in top pane(s). |
| `HPageBreaks` | Returns an HPageBreaks collection that represents the horizontal page breaks on the sheet. This is a Read-Only property. |
| `HyperLinks` | Collection of all worksheet's hyperlinks. |
| `Index` | Returns the index number of the object within the collection of similar objects. This is a Read-Only property. |
| `IsFreezePanes` | Defines whether frozen panes are applied. |
| `IsGridLinesVisible` | This property is set to true if gridlines are visible; false otherwise. |
| `IsPasswordProtected` | Indicates if the worksheet is password protected. |
| `IsRightToLeft` | Indicates whether worksheet is displayed right to left. |
| `IsRowColumnHeadersVisible` | This property is set to true if row and column headers are visible; false otherwise. |
| `IsSelected` | Indicates whether tab of this sheet is selected. This is a Read-Only property. |
| `IsStringsPreserved` | Indicates if all values in the workbook are preserved as strings. |
| `MergedCells` | Returns all merged ranges. This is a Read-Only property. |
| `MigrantRange` | Returns instance of migrant range - row and column of this range object can be changed by user. This is a Read-Only property. |

## API Reference

### Properties

The properties listed above are part of the `ExcelWorksheet` class in the XlsIO module. They are used to configure and retrieve the settings related to the visibility, layout, and security of a worksheet.

#### Example Usage

```csharp
// Example: Set the first visible row in the bottom pane to row 5
worksheet.FirstVisibleRow = 5;

// Example: Freeze panes at row 1 and column 1
worksheet.IsFreezePanes = true;
worksheet.FreezePanes(1, 1);

// Example: Check if the worksheet is password protected
bool isProtected = worksheet.IsPasswordProtected;
```

## Page-level Navigation/TOC

- [Properties Overview]
- [Horizontal Split Configuration]
- [Gridlines and Headers Visibility]
- [Security and Selection Properties]
- [Merged Cells and Migrant Range]

## Cross References

- Refer to the `ExcelWorksheet` class documentation for details on other properties and methods.
- For more information on handling page breaks, see the `HPageBreaks` collection documentation.

<!-- tags: [product, module, control, api, version?] keywords: [XlsIO, spreadsheet, worksheet, properties, frozen panes, gridlines, hyperlinks, security] -->
```