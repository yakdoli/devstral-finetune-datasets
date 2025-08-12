<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_553.jpeg
document_name: grid
page_number: 553
page_id: grid#page_553
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:29Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Your first inclination might be to grab the row number from the grid and try to use it as an index in the datatable. But, the relationship between the grid's row number and the data table row numbers will break if your grid has been sorted. So, instead of using the row number as an index in the data table, you should use it as an index in the **CurrencyManager** List.

## Accessing Grid Rows via CurrencyManager

Given below are some code samples.

### C#

```csharp
// Assuming the grid is bound to a Data Table.
CurrencyManager cm =
    (CurrencyManager)this.grid.BindingContext[this.grid.DataSource,
    this.grid.DataMember];
DataRowView drv = cm.List[1] as DataRowView;

// Access row 2 of the grid.
if (drv != null)
{
    DataRow dr = drv.Row;
    Console.WriteLine(dr["FirstName"].ToString());
}
```

### VB.NET

```vb
' Assuming grid is bound to a Data Table.
Dim cm As CurrencyManager =
    CType(Me.grid.BindingContext(Me.grid.DataSource, Me.grid.DataMember), CurrencyManager)
Dim drv As DataRowView = cm.List(1)

' Access row 2 of the grid.
If Not (drv Is Nothing) Then
    Dim dr As DataRow = drv.Row
    Console.WriteLine(dr("FirstName").ToString())
End If
```

## Filtering a Grid Data Bound Grid

### Overview
- Filtering is essential for narrowing down the data shown in a grid bound to a data source.
- This section illustrates the filtering procedure using an example.

### Content

#### 4.2.2.5 Filtering a Grid Data Bound Grid

We will use an example to illustrate the filtering procedure for the grid.

## API Reference

This section assumes familiarity with the `CurrencyManager` and `Grid` classes in Syncfusion WinForms Grid. For detailed API information, refer to the Syncfusion documentation.

## Code Examples

The code examples provided demonstrate accessing grid rows using the `CurrencyManager` in both C# and VB.NET.

## See also

- [Data Binding in Syncfusion Grid](#)
- [Filtering in Syncfusion Grid](#)

<!-- tags: [syncfusion, winforms, grid, datagrid, dataset, currencymanager, sorting, filtering, gridview, currencymanager] keywords: [currencymanager, datagrid, winforms, filtering, sorting, dataset, gridview, syncfusion] -->