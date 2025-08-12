```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_405.jpeg
document_name: grid
page_number: 405
page_id: grid#page_405
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates exporting data from a Windows Forms Grid to an Excel spreadsheet.
- Highlights the synchronization of Grid cell properties like TextColor, BackColor, Font, and Alignment to Excel cells.
- Provides a sample installation path for further exploration.

## Content

### Export to Excel

```vb
Dim gecc As Syncfusion.GridExcelConverter.GridExcelConverterControl =
    New Syncfusion.GridExcelConverter.GridExcelConverterControl()
gecc.GridToExcel(Me.gridDataBoundGrid1.Model, "C:\MyGC.xls")
```

#### Figure 148: Exported Excel Sheet
The figure shows an exported Excel sheet with the following features:

- **TextColors:** Black, Red, Blue, Green, Yellow, DimGray.
- **BackColors:** ActiveCaptionText (black text on active caption background), Red, Blue, Green, Yellow, DimGray.
- **Fonts:** 
  - Sizes: 6, 7, 8, 10, 12, 14.
  - Font Styles: Bold, Italic, Regular, Strikeout, Underline.
  - Font Families: Comic Sans MS, Arial, Century, Courier New, Times New Roman, Verdana.
- **Alignment:** Top Left, Center, Bottom Right.
- **Orientation:** Not shown in figure but implied in context.

The exported data includes a comprehensive display of grid properties in a visually formatted spreadsheet.

The sample demonstrating this feature is available under the following installation path:
```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Export\GC XLS Export Demo
```

### 4.1.4.10.3 PDF Export

## Page-level Navigation/TOC
- 4.1.4.10.3 PDF Export

## Cross References
- See also: Export functionality for Grid data in Syncfusion Essential Grid.

<!-- tags: [syncfusion, winforms, grid, export, excel, pdf, sample, essential grid, windows forms] keywords: [export, spreadsheet, textcolor, backcolor, font, alignment, orientation, grid to excel, pdf export, GC XLS Export Demo] -->
```