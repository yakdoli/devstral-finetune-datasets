```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_946.jpeg
document_name: grid
page_number: 946
page_id: grid#page_946
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:54:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This page discusses Excel export functionality for the Essential Grid Control in .NET, focusing on exporting data to Excel for offline verification or computation.
- Highlights the use of the `GroupingGridExcelConverter` class to convert grid contents into Excel files with various export options.
- Provides a detailed explanation of converter options and properties for customization.

## Content

### 4.3.4.8.2 Excel Export

**Export to Excel** is one of the most common functionalities required in the .NET world. The Essential Grid Control has in-built support for Excel Export. Users can download the data from the Grouping Grid control into an Excel spreadsheet for offline verification and/or computation. This can be achieved by making use of the `GroupingGridExcelConverter` class. This section will walk you through the conversion of the contents of the grid to an Excel file as well as discuss the various converter options.

#### GroupingGridExcelConverter
The `GroupingGridExcelConverter` class derives from `GridExcelConverterBase`. It contains a number of methods that helps in exporting different components of the grouping grid. Its properties will let you control the export of the grid schema like styles and grid elements. You can be able to export Styles, RecordPlusMinus, GroupCaptionPlusMinus, Borders and PreviewRows as well.

#### ConverterOptions

Exporting of a Grouping Grid to Excel has two options: **Visible** and **Default**. The **Visible** option will allow you to export only the visible contents of the grid, whereas the **Default** option exports the entire elements of the grouping grid. Converter options are defined in `GridExcelConverter.ConverterOptions` enumeration.

The following table lists the properties offered by Grouping Grid Excel Converter. By setting these properties, you could be able to choose the elements you need to export.

| Property                | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| ExportBorders           | Specifies if borders should be exported.                                  |
| ExportStyle             | Indicates if style should be exported.                                    |
| ExportGroupPlusMinus    | Specifies if GridGroup should be exported as Excel Group.                 |
| ExportRecordPlusMinus   | When true, the record with related tables will be exported as Excel Group. |
| ExportPreviewRows       | When enabled, PreviewRows will be exported.                               |
| CaptionBackColor        | Specifies the color to be used for Caption in the worksheet.               |

## API Reference (if applicable)
- **Namespace**: `Syncfusion.Windows.Forms.Grid`
- **Class**: `GroupingGridExcelConverter`
- **Properties**:
  - `ExportBorders`: Determines if borders are exported.
  - `ExportStyle`: Indicates if styles are exported.
  - `ExportGroupPlusMinus`: Specifies if GridGroup is exported as an Excel Group.
  - `ExportRecordPlusMinus`: Exports records with related tables as Excel Groups.
  - `ExportPreviewRows`: Enables the export of PreviewRows.
  - `CaptionBackColor`: Sets the caption background color.

## Code Examples (multi-language supported)
- **C# Example**:
  ```csharp
  using Syncfusion.Windows.Forms.Grid;
  
  var grid = new GridControl();
  var converter = new GroupingGridExcelConverter(grid);
  converter.ExportStyle = true;
  converter.ExportBorders = true;
  converter.ExportGroupPlusMinus = true;
  converter.ExportRecordPlusMinus = true;
  converter.ExportPreviewRows = true;
  converter.CaptionBackColor = System.Drawing.ColorTranslator.FromHtml("#FF0000");
  converter.ExportGrid();
  ```

## Page-level Navigation/TOC (if applicable)
- **4.3.4.8.2 Excel Export**
- **Overview of Excel Export**
- **Converter Options**
- **API Reference**
- **Code Examples**

## Cross References
- See also: Section on "Grid Control Overview" and "Grouping Grid Control" for basic setup and usage.

<!-- tags: [EssentialGrid, WindowsForms, ExcelExport, GridControl, GroupingGrid, Converters] keywords: [ExcelExport, GroupingGridExcelConverter, ConverterOptions, ExportStyles, ExportBorders, ExportGroupPlusMinus, ExportRecordPlusMinus, ExportPreviewRows] -->
```