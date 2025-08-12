```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_566.jpeg
document_name: grid
page_number: 566
page_id: grid#page_566
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
' Don't allow clicking it.
Me.gridDataBoundGrid2.Enabled = False

' Form1_Load
End Sub

Private Function PrimaryTable() As DataTable
    Dim dt As New DataTable("PrimaryTable")
    dt.Columns.Add(New DataColumn("ID", GetType(Integer)))
    dt.Columns.Add(New DataColumn("CustID", GetType(Integer)))
    dt.Columns.Add(New DataColumn("Address"))
    dt.Columns.Add(New DataColumn("City"))

    Dim i As Integer
    While i < 10
        Dim dr As DataRow = dt.NewRow()
        dr(0) = i
        dr(1) = i Mod 4
        dr(2) = String.Format("address{0}", i)
        dr(3) = String.Format("city{0}", i)
        dt.Rows.Add(dr)
        i += 1
    End While
    Return dt
End Function

Private Function ForeignKeyTable() As DataTable

    ' Two columns CustID (Value Member) and Name (Display Member).
    Dim dt As New DataTable("ForeignKeyTable")
    dt.Columns.Add(New DataColumn("CustID", GetType(Integer)))
    dt.Columns.Add(New DataColumn("Name"))

    Dim i As Integer
    While i < 4
        Dim dr As DataRow = dt.NewRow()
        dr(0) = i
        dr(1) = String.Format("Name{0}", i)
        dt.Rows.Add(dr)
        i = i + 1
    End While
    Return dt
End Function
```

## Overview
- Demonstrates the creation and manipulation of `DataTable` objects in VB.NET.
- Illustrates the use of `DataColumn` and `DataRow` to populate a table.
- Highlights the creation of a foreign key relationship table.

### WinForms-specific conventions
- Utilizes the `gridDataBoundGrid2` control to display data, ensuring interaction is disabled by setting `.Enabled = False`.

## Code Examples (multi-language supported)

### VB.NET Example
The provided code snippet showcases:
1. Creation of a `DataTable` named `PrimaryTable`.
2. Addition of columns with specified types and names.
3. Populating the table with data using a loop.
4. Creation of a `DataTable` named `ForeignKeyTable` with two columns.
5. Populating it in a similar fashion.

This example is particularly relevant for scenarios requiring runtime data table generation and manipulation within a Windows Forms application using Syncfusion controls.

```vb
' Example usage of PrimaryTable and ForeignKeyTable in a Form's Load event.
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    Dim primaryTable As DataTable = PrimaryTable()
    Dim foreignKeyTable As DataTable = ForeignKeyTable()

    ' Assign tables to controls or use as datasets elsewhere.
    gridDataBoundGrid2.DataSource = primaryTable
End Sub
```

### Notes
- The `String.Format` method is used to format cell data dynamically.
- The loop ensures automatic generation of sample data for demonstration purposes.
- The `.Mod` operator is utilized to create a repeating pattern for certain columns, demonstrating modulo arithmetic in data generation.

## API Reference (if applicable)
- **Namespace**: `System.Data`
  - **Class**: `DataTable`
    - **Methods**: `.New()`, `.Columns.Add()`, `.Rows.Add()`
  - **Properties**: `.Enabled`

## Cross References
See also:
- [Syncfusion Grid Documentation](https://www.syncfusion.com/documentation/winforms/grid)
- [DataTable Class](https://docs.microsoft.com/dotnet/api/system.data.datatable)

---

<!-- tags: [syncfusion, grid, windows forms, datatable, databinding, vb.net] keywords: [primarytable, foreignkeytable, databoundgrid, datacolumn, datarow, stringformat, enabled] -->
```