```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_119.jpeg
document_name: grid
page_number: 119
page_id: grid#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:37:03Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to export data from a GroupingGrid to an Excel file.
- Explains exporting visible or expanded records and groups.
- Illustrates exporting multiple grids as worksheets in a single XLS file.

## Content

### Grouping Grid to Excel Export

#### C#

```csharp
Syncfusion.GroupingGridExcelConverter.GroupingGridExcelConverterControl converter = new Syncfusion.GroupingGridExcelConverter.GroupingGridExcelConverterControl();
converter.GroupingGridToExcel(this.gridGroupingControl, @"C:\MyGGC.xls", Syncfusion.GridExcelConverter.ConverterOptions.Default);
```

#### VB.NET

```vb.net
Dim converter As Syncfusion.GroupingGridExcelConverter.GroupingGridExcelConverterControl = New Syncfusion.GroupingGridExcelConverter.GroupingGridExcelConverterControl()
converter.GroupingGridToExcel(Me.gridGroupingControl, "C:\MyGGC.xls", Syncfusion.GridExcelConverter.ConverterOptions.Default)
```

You can export the visible, or expanded records or groups alone by using the following code.

#### C#

```csharp
converter.GroupingGridToExcel(this.gridGroupingControl, @"C:\MyGGC.xls", Syncfusion.GridExcelConverter.ConverterOptions.Visible);
```

#### VB.NET

```vb.net
converter.GroupingGridToExcel(this.gridGroupingControl, "C:\MyGGC.xls", Syncfusion.GridExcelConverter.ConverterOptions.Visible)
```

### 3.1.6.5 Exporting Multiple Grids

It is possible to save multiple grids to a single XLS file as worksheets. The following code example illustrates how to do this.

#### C#

```csharp
using Syncfusion.XlsIO;
using Syncfusion.GridExcelConverter;
```

## Page-level Navigation/TOC
- Grouping Grid to Excel Export
  - Exporting Visible or Expanded Records
  - Exporting Multiple Grids

## Cross References
- See also: [Syncfusion.XlsIO Documentation](#)
- See also: [Syncfusion.GridExcelConverter Documentation](#)

<!-- tags: [Syncfusion, WinForms, GroupingGrid, Excel, Export] keywords: [GroupingGrid, Excel, export, multiple grids, Syncfusion.Windows.Forms.Grid, Visible, Expanded Records, XLSIO, GridExcelConverter] -->
```