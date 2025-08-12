```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_117.jpeg
document_name: grid
page_number: 117
page_id: grid#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:34:08Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## 3.1.6.1.1.7 Formula Cell Conversion

### If Format specified

The cell is checked whether it is a Formula cell type using the CellType property. If it is a Formula cell type then the GridCell's Text string is stored to Range's Formula property. The values in Excel cells can be formatted by specifying the format in Formula cell types.

### If Format not specified

If no formula is specified for the cell then the formula is set to Excel sheet's range Formula property with its default format.

## 3.1.6.2 Import an Excel Sheet into Essential Grid

An Excel sheet can also be imported to the Grid control or Grid Data Bound Grid. This can be done by using the `ExcelToGrid` method in the `GridExcelConverterControl` class.

The following code example illustrates how to transfer Excel content to the Grid control.

### C\#

```csharp
Syncfusion.GridExcelConverter.GridExcelConverterControl gecc = new Syncfusion.GridExcelConverter.GridExcelConverterControl();
gecc.ExcelToGrid(@"C:\MyGC.xls", this.gridControl1.Model);
```

### VB.NET

```vb
Dim gecc As Syncfusion.GridExcelConverter.GridExcelConverterControl = New Syncfusion.GridExcelConverter.GridExcelConverterControl()
gecc.ExcelToGrid("C:\MyGC.xls", Me.gridControl1.Model)
```

The following code example illustrates how to transfer Excel content to the Grid Data Bound Grid.

### C\#

```csharp
Syncfusion.GridExcelConverter.GridExcelConverterControl gecc = new Syncfusion.GridExcelConverter.GridExcelConverterControl();
gecc.ExcelToGrid(@"C:\MyGC.xls", this.gridDataBoundGrid1.Model);
```

### VB.NET

```vb
Dim gecc As Syncfusion.GridExcelConverter.GridExcelConverterControl = New Syncfusion.GridExcelConverter.GridExcelConverterControl()
gecc.ExcelToGrid("C:\MyGC.xls", Me.gridDataBoundGrid1.Model)
```

## API Reference (if applicable)

### Code Examples (multi-language supported)

- C\#
```csharp
Syncfusion.GridExcelConverter.GridExcelConverterControl gecc = new Syncfusion.GridExcelConverter.GridExcelConverterControl();
gecc.ExcelToGrid(@"C:\MyGC.xls", this.gridControl1.Model);
```

- VB.NET
```vb
Dim gecc As Syncfusion.GridExcelConverter.GridExcelConverterControl = New Syncfusion.GridExcelConverter.GridExcelConverterControl()
gecc.ExcelToGrid("C:\MyGC.xls", Me.gridControl1.Model)
```

## RAG Annotations

<!-- tags: [Essential Grid, Windows Forms, Excel Sheet, Control, Grid Data Bound Grid, Formula Cell, Version: 11.4.0.26] keywords: [GridExcelConverterControl, ExcelToGrid, CellType, Formula property, Grid control, Model, GridDataBoundGrid, Syncfusion] -->
```