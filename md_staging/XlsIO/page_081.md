```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_081.jpeg
document_name: XlsIO
page_number: 081
page_id: XlsIO#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:53:52Z
fidelity: lossless
-->

## Overview
- Describes various properties and their functionalities related to worksheet operations in Excel.
- Focuses on properties such as tab color, cell usage, active cell management, and visibility controls.
- Highlights Read-Only properties like `UsedCells` and `UsedRange`, along with properties for customization like `TabColor` and `Zoom`.
- Warns about potential memory usage for certain properties like `UsedCells`.

## Content

### Properties and Their Descriptions

| Property        | Description                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
|                 | the columns in the worksheet.                                                                                                     |
| TabColor        | Gets/sets tab color.                                                                                                             |
| TabColorRGB     | Gets/sets tab color.                                                                                                             |
| TabIndex        | Returns index in the parent ITabSheets collection. This is a Read-Only property.                                                 |
| Type            | Returns or sets the worksheet type.                                                                                              |
| UsedCells       | <p>Returns all accessed cells. This is a Read-Only property.</p>                                                              |
|                 | <p>WARNING: This property creates a Range object for each cell in the worksheet, and creates new arrays every time user calls to it. It can cause huge memory usage especially if called frequently.</p> |
| UsedRange       | Returns a Range object that represents the used range on the specified worksheet. This is a Read-Only property.               |
| UseRangesCache  | Indicates whether all created range objects should be cached. Default value is false.                                           |
| VerticalSplit   | Position of the vertical split (px, 0 = No vertical split): Unfrozen pane: Width of the left pane(s) (in twips = 1/20 of a point) Frozen pane: Number of visible columns in left pane(s). |
| Visibility      | Controls visibility of the worksheet to the end-user.                                                                           |
| VPageBreaks     | Returns a VPageBreaks collection that represents the vertical page breaks on the sheet. This is a Read-Only property.           |
| Workbook        | Returns parent workbook. This is a Read-Only property.                                                                         |
| Zoom            | Zoom factor of the document. Value must be in the range from 10 to 400.                                                         |

## API Reference

### Methods and Properties
- **TabColor**: Gets or sets the tab color for the worksheet.
- **TabColorRGB**: Gets or sets the tab color using RGB values.
- **TabIndex**: Retrieves the index of the worksheet in its parent ITabSheets collection.
- **Type**: Retrieves or sets the type of the worksheet.
- **UsedCells**: Retrieves all accessed cells in the worksheet. This property is Read-Only and creates Range objects for each cell.
- **UsedRange**: Returns a Range object representing the used range of the worksheet.
- **UseRangesCache**: Indicates whether created range objects should be cached.
- **VerticalSplit**: Control the vertical split position of the worksheet pane(s).
- **Visibility**: Control the visibility of the worksheet for the end-user.
- **VPageBreaks**: Retrieves the vertical page breaks collection.
- **Workbook**: Retrieves the parent workbook.
- **Zoom**: Controls the zoom factor of the document.

## Code Examples

Here's a sample snippet illustrating how to use some of the properties:

```csharp
// Example of setting tab color
// ws is an instance of the worksheet
ws.TabColor = KnownColor.LightBlue;

// Example of getting UsedCells
Range col0 = ws.UsedCells[0];

// Example of setting zoom level
ws.Zoom = 150;
```

## Cross References
- See also: Documentation on `Range`, `ITabSheets`, and `Workbook` for further details on their functionalities and usage.

<!-- tags: [XlsIO, worksheet, properties, Syncfusion Winforms, Read-Only properties, tab color, zoom, vertical split, visibility, used cells] keywords: [sheet, Range, WorksheetType, UsedRange, VPageBreaks, workbook, end-user] -->
```