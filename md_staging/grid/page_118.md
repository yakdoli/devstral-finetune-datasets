```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: grid
page_number: 118
page_id: grid#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:36:45Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## 3.1.6.3 Excel Converter Options

The `GridExcelConverter` class enables you to export specific grid elements like column headers, row headers, and so on. By default, the `GridExcelConverterControl` exports all the elements in the grid.

The following code example illustrates how to include both row and column headers during the export.

### C# Code Example

```csharp
gecc.GridToExcel(this.grid.Model, @"C:\MyGGC.xls",
    Syncfusion.GridExcelConverter.ConverterOptions.RowHeaders |
    Syncfusion.GridExcelConverter.ConverterOptions.ColumnHeaders);
```

### VB.NET Code Example

```vbnet
gecc.GridToExcel(Me.grid.Model, "C:\MyGGC.xls",
    Syncfusion.GridExcelConverter.ConverterOptions.RowHeaders |
    Syncfusion.GridExcelConverter.ConverterOptions.ColumnHeaders)
```

## 3.1.6.4 Exporting Grid Grouping Data To Excel

The `GroupingGridExcelConverter` class provides support for exporting data from a Grouping Grid control into an Excel spreadsheet for verification and/or computation. This control automatically copies the Grid's styles, formats, groups, summary rows, and expression fields to Excel. The `GroupingGridExcelConverter` control is derived from the `GridExcelConverterBase`. The XlsIO libraries support the conversion of Grid content to Excel.

To make use of the `GroupingGridExcelConverter` class, the following assemblies must be added along with the default assemblies present in the `References` folder of your application: `Syncfusion.XlsIO.Base` and `Syncfusion.GridConverter.Windows`.

The content of the Grid Grouping control can be transferred to Excel by using the `GroupingGridToExcel` method in the `GroupingGridExcelConverterControl` class. There are two export options provided by the Grid Grouping control: first option converts the entire content in the grid to Excel, and the second option converts only the visible content in the grid to Excel.

The following code example illustrates how to convert the entire Grid content to Excel.

## Page-level Navigation/TOC (if applicable)
- 3.1.6.3 Excel Converter Options
- 3.1.6.4 Exporting Grid Grouping Data To Excel

## Cross References
- Related topics or sections should be noted if present in the document.

## RAG Annotations
<!-- tags: [syncfusion, windowsforms, grid, excel, export, gridgrouping, xlsx] keywords: [GridExcelConverter, GridExcelConverterControl, GroupingGridExcelConverter, GroupingGridToExcel, XlsIO] -->
```