```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: calculate
page_number: 080
page_id: calculate#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:31Z
fidelity: lossless
-->

## Essential Calculate

### C#

```csharp
private void SingleDataGridForm_Load(object sender, System.EventArgs e)
{
    // Set up your DataTable.
    this.dt = GetTheDataTable();

    // Set the datasource to a DataTable.
    this.dataGrid1.DataSource = this.dt;

    // Set any formulas you want
    // or they might already be in the DataTable.
    this.dataGrid1[2, 2] = "= A1 + A3";

    // 1) Reset static members of CalcEngine.
    Syncfusion.Calculate.CalcEngine.ResetSheetFamilyID();

    // 2) Create a CalcEngine object and tie it to the DataGrid that implements ICalcData.
    engine = new Syncfusion.Calculate.CalcEngine(this.dataGrid1);

    // 3) Set the CalcEngine to track dependencies required for auto updating.
    engine.UseDependencies = true;

    // 4) Call RecalculateRange so any formulas in the data can be initially computed.
    engine.RecalculateRange(RangeInfo.Cells(1, 1, dt.Rows.Count, dt.Columns.Count), this.dataGrid1);
}
```

### VB

```vb
Private engine As Syncfusion.Calculate.CalcEngine
Private dt As DataTable

Private Sub SingleDataGridForm_Load(sender As Object, e As System.EventArgs)

    ' Set up your DataTable.
    Me.dt = GetTheDataTable()

    ' Set the datasource to a DataTable.
    Me.dataGrid1.DataSource = Me.dt

    ' Set any formulas you want
    ' or they might already be in the DataTable.
End Sub
```

## API Reference

<!-- tags: [Syncfusion, Winforms, CalcEngine, SingleDataGridForm_Load] keywords: [DataTable, DataSource, RangeInfo, RecalculateRange, UseDependencies, Essential Calculate] -->
```