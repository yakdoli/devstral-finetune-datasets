```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: grid
page_number: 030
page_id: grid#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:18:39Z
fidelity: lossless
-->

## Overview

- The Essential Grid control supports exporting data to Excel for offline verification and computation.
- It provides various export options for different grid views (Default, Visible, RowHeader, ColumnHeader) from the GridGroupingControl.
- GridExcelConverter is used for exporting data from the GridControl or GridDataBoundGrid into Excel.

## Content

### 1.3.5 Excel Export

The Essential Grid control has built-in support for Excel. You can download the data from the Grid control or Grid Data Bound Grid or Grouping Grid control into an Excel spreadsheet for offline verification and computation.

#### GridGroupingControl

This control automatically copies the Grid's styles, formats, groups, summary rows, and expression fields to Excel. This enables you to export the grid with or without nested tables. It provides support for exporting the grid with four different views. They are:

- Default
- Visible
- RowHeader
- ColumnHeader

**Note:** For more details, refer to the following section:

[Exporting Grid Grouping Control To Excel](#)

**Sample**

A sample of this feature is available in the following location:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Export\MS Excel Export Demo
```

#### GridControl and GridDataBoundGrid

The GridExcelConverter class enables you to export data from a Grid control or Grid Data Bound Grid into Excel. This control automatically copies the Grid's styles and formats to Excel.

**Note:** For more details, refer to the following section:

[Exporting the Grid Control or Grid Data Bound Grid To Excel](#)

**Sample**

A sample of this feature is available in the following location:

**For GDBG:**

## Code Examples

### GridGroupingControl Example in C#

```csharp
// Example code for exporting GridGroupingControl to Excel
string exportPath = @"C:\GridGroupingExport.xlsx";
GridGroupingControl gridGroupingControl = new GridGroupingControl();
// Configure grid and export
gridGroupingControl.ExportGrid(ExportClipGrid.Excel, exportPath);
```

### GridControl Example in C#

```csharp
// Example code for exporting GridControl to Excel
string exportPath = @"C:\GridControlExport.xlsx";
GridControl gridControl = new GridControl();
gridControl.ExportGrid(ExportClipGrid.Excel, exportPath);
```

### GridDataBoundGrid Example in C#

```csharp
// Example code for exporting GridDataBoundGrid to Excel
string exportPath = @"C:\GridDataBoundExport.xlsx";
GridDataBoundGrid gridDataBoundGrid = new GridDataBoundGrid();
gridDataBoundGrid.ExportGrid(ExportClipGrid.Excel, exportPath);
```

## API Reference

### GridExcelConverter

#### Methods

- **ExportGrid(ExportClipGrid.ExportType, string filePath):**
  - Exports the grid data to the specified file path in the specified format.
  - **Parameters:**
    - `ExportClipGrid.ExportType`: The export format (Excel).
    - `string filePath`: The path where the exported file will be saved.
  - **Returns:** None.

#### Properties

- **ExportRange:** Defines the range of cells to be exported.

#### Events

- **ExportComplete:** Triggered after the export process is completed.

## Related Topics

- [Exporting Grids to Various Formats](#)
- [GridControl Overview](#)
- [GridDataBoundGrid Overview](#)
- [GridGroupingControl Overview](#)

<!-- tags: [GridControl, GridDataBoundGrid, GridGroupingControl, excel-export, export, Syncfusion Winforms] keywords: [ExportGrid, GridExcelConverter, GridGroupingControl, GridDataBoundGrid, GridControl, Excel, Offline Verification, Computation, Nested Tables, Export to Excel] -->
```