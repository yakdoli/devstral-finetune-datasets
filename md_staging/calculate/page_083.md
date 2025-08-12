```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: calculate
page_number: 083
page_id: calculate#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:27Z
fidelity: lossless
-->

## Essential Calculate

```csharp
{
    // 1) Set the datasource for the DataGrid.
    this.dataGrid1.DataSource = GetARandomTable();
    this.dataGrid2.DataSource = GetARandomTable();
    this.dataGrid3.DataSource = GetARandomTable();
    this.dataGrid4.DataSource = GetARandomTable();
    this.dataGrid5.DataSource = GetARandomTable();

    // 2) Call this to reset static members.
    Syncfusion.Calculate.CalcEngine.ResetSheetFamilyID();

    // 3) Create the engine.
    engine = new Syncfusion.Calculate.CalcEngine(this.dataGrid1);

    // 4) Track dependencies required for auto calculations.
    engine.UseDependencies = true;

    // 5) Register multiple ICalcData objects for cross sheet references.
    int sheetfamilyID = CalcEngine.CreateSheetFamilyID();
    engine.RegisterGridAsSheet("DG1", this.dataGrid1, sheetfamilyID);
    engine.RegisterGridAsSheet("DG2", this.dataGrid2, sheetfamilyID);
    engine.RegisterGridAsSheet("DG3", this.dataGrid3, sheetfamilyID);
    engine.RegisterGridAsSheet("DG4", this.dataGrid4, sheetfamilyID);
    engine.RegisterGridAsSheet("DG5", this.dataGrid5, sheetfamilyID);
}
```

### [VB]

```vb
Dim engine As Syncfusion.Calculate.CalcEngine

Private Sub DataGridWorkBookForm_Load(sender As Object, e As System.EventArgs)

    ' 1) Set the datasource for the DataGrid.
    Me.dataGrid1.DataSource = GetARandomTable()
    Me.dataGrid2.DataSource = GetARandomTable()
    Me.dataGrid3.DataSource = GetARandomTable()
    Me.dataGrid4.DataSource = GetARandomTable()
    Me.dataGrid5.DataSource = GetARandomTable()

    ' 2) Call this to reset static members in case the other form loaded first.
    Syncfusion.Calculate.CalcEngine.ResetSheetFamilyID()

    ' 3) Create the engine.
End Sub
```

### Page-level Navigation/TOC (if applicable)
- [Essential Calculate](#essential-calculate)

### Cross References
See also: 
- [CalcEngine](#calcengine)
- [RegisterGridAsSheet](#registergridassheet)
- [UseDependencies](#usedependencies)

### RAG Annotations
<!-- tags: [syncfusion-sdk, winforms, calculate, engine, data grid, sheet family, table of contents, essential calculate, registergridassheet, usedependencies] keywords: [datasource, reset, static members, dependencies, auto calculations, cross sheet references, ICalcData objects, grid, data grid, form, event, load, engine, register grid as sheet, useDependencies] -->
```