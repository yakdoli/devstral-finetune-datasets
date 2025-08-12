```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_947.jpeg
document_name: grid
page_number: 947
page_id: grid#page_947
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:42Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the `HeaderBackColor` property and its function in the worksheet.
- Describes the `GroupingGridExcelConverterControl` and its method for converting grid contents to an Excel file.
- Outlines the `QueryExportPreviewRowInfo` event for customizing export rows.

## Content

### Header BackColor Property
The `HeaderBackColor` property indicates the color to be used for the Header in the worksheet.

| HeaderBackColor | Indicates the color to be used for Header in the worksheet. |
|------------------|------------------------------------------------------------|

### Method

#### Grouping Grid Excel Converter
The `Grouping Grid Excel Converter` control provides a method called `GroupingGridToExcel`. This method converts grouping grid contents to an Excel file. It accepts three parameters:
- The grouping grid to be converted.
- The filename of the destination worksheet.
- Conversion options.

#### Syntax

##### C#
```csharp
GroupingGridExcelConverterControl converter = new GroupingGridExcelConverterControl();
converter.GroupingGridToExcel(this.gridGroupingControl1, "Grid.xls", ConverterOptions.Visible);
```

##### VB.NET
```vbnet
Dim converter As GroupingGridExcelConverter = New GroupingGridExcelConverter()
converter.GroupingGridToExcel(Me.gridGroupingControl1, "Grid.xls", ConverterOptions.Visible)
```

### Events

#### `QueryExportPreviewRowInfo`
The `QueryExportPreviewRowInfo` event is offered by the `Grouping Grid Excel Converter` control to customize the export process. It occurs for each `PreviewRow` element before exporting the grid, allowing you to modify the preview row. The event accepts two parameters:
- The element to export.
- The `GridStyleInfo` object representing the style information.

#### Syntax

##### C#
```csharp
GroupingGridExcelConverter converter = new GroupingGridExcelConverter();

converter.QueryExportPreviewRowInfo += new GroupingGridExcelConverterControl.GroupingGridExportPreviewRowQueryInfoEventHandler(converter_QueryExportPreviewRowInfo);
```

## API Reference

### Name | Description
- `HeaderBackColor` | Indicates the color to be used for Header in the worksheet.
- `GroupingGridToExcel` | Converts grouping grid contents to an Excel file.
- `QueryExportPreviewRowInfo` | Customizes export rows before exporting.

## Code Examples

### C#
```csharp
GroupingGridExcelConverterControl converter = new GroupingGridExcelConverterControl();
converter.GroupingGridToExcel(this.gridGroupingControl1, "Grid.xls", ConverterOptions.Visible);
```

### VB.NET
```vbnet
Dim converter As GroupingGridExcelConverter = New GroupingGridExcelConverter()
converter.GroupingGridToExcel(Me.gridGroupingControl1, "Grid.xls", ConverterOptions.Visible)
```

## Page-level Navigation/TOC

- [Header BackColor Property](#header-backcolor-property)
- [Method](#method)
- [Grouping Grid Excel Converter](#grouping-grid-excel-converter)
- [Events](#events)
- [QueryExportPreviewRowInfo](#queryexportpreviewrowinfo)

## Cross References

- See also: [Grid Excel Converter](#grid-excel-converter)

<!-- tags: [Essential Grid, Windows Forms, HeaderBackColor, Grouping Grid Excel Converter, QueryExportPreviewRowInfo] keywords: [HeaderBackColor, GroupingGridToExcel, QueryExportPreviewRowInfo] -->
```
