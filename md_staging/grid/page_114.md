```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_114.jpeg
document_name: grid
page_number: 114
page_id: grid#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:33:29Z
fidelity: lossless
-->

## `3.1.6.1 Exporting the Grid Control or Grid Data Bound Grid To Excel`

The `GridExcelConverter` class provides support for exporting data from a Grid control or Grid Data Bound Grid into an Excel spreadsheet for verification and/or computation. This control automatically copies the Grid's styles and formats to Excel. The `GridExcelConverter` control is derived from the `GridExcelConverterBase`. The XlsIO libraries support the conversion of Grid content to Excel.

To make use of the `GridExcelConverter` class, the following assemblies should be added along with the default assemblies present in the `References` folder of your application: `Syncfusion.GridConverter.Base` and `Syncfusion.XlsIO.Base`.

### Converting Grid Content to Excel

The `GridToExcel` method is used to export the grid to an Excel sheet. The following code example illustrates how to convert the Grid content to Excel.

#### C#

```csharp
Syncfusion.GridExcelConverter.GridExcelConverterControl gecc = new 
Syncfusion.GridExcelConverter.GridExcelConverterControl();
gecc.GridToExcel(this.gridControl.Model, @"C:\MyGC.xls");
```

#### VB.NET

```vb
Dim gecc As Syncfusion.GridExcelConverter.GridExcelConverterControl = 
New Syncfusion.GridExcelConverter.GridExcelConverterControl()
gecc.GridToExcel(Me.gridControl1.Model, "C:\MyGC.xls")
```

### Converting Grid Data Bound Grid Content to Excel

The following code example illustrates how to convert the Grid Data Bound Grid content to Excel.

#### C#

```csharp
Syncfusion.GridExcelConverter.GridExcelConverterControl gecc = new
Syncfusion.GridExcelConverter.GridExcelConverterControl();
gecc.GridToExcel(this.gridDataBoundGrid1.Model, @"C:\MyGC.xls");
```

#### VB.NET

```vb
Dim gecc As Syncfusion.GridExcelConverter.GridExcelConverterControl =
New Syncfusion.GridExcelConverter.GridExcelConverterControl()
gecc.GridToExcel(Me.gridDataBoundGrid1.Model, "C:\MyGC.xls")
```
```