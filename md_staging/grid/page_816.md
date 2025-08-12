```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_816.jpeg
document_name: grid
page_number: 816
page_id: grid#page_816
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:17Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Example Code in C#

```csharp
dt.Columns.Add(new DataColumn("CustomerID"));
dt.Columns.Add(new DataColumn("Price"));
Random rand = new Random();
for (int i = 0; i < numberChildRows; ++i)
{
    DataRow dr = dt.NewRow();
    dr[0] = i.ToString();
    dr[1] = string.Format("ItemName{0}", i);
    dr[2] = (i % numberParentRows).ToString();
    dr[3] = rand.Next(500).ToString();
    dt.Rows.Add(dr);
}

return dt;
}
```

### Example Code in VB.NET

```vbnet
Private numberParentRows As Integer = 6
Private numberChildRows As Integer = 20

Private Function GetParentTable() As DataTable
    Dim dt As DataTable = New DataTable("Customers")

    dt.Columns.Add(New DataColumn("customerID"))
    dt.Columns.Add(New DataColumn("CustomerName"))
    dt.Columns.Add(New DataColumn("Address"))

    Dim i As Integer = 0

    Do While i < numberParentRows
        Dim dr As DataRow = dt.NewRow()
        dr(0) = i
        dr(1) = String.Format("CustomerName{0}", i)
        dr(2) = String.Format("Address{0}", i)
        dt.Rows.Add(dr)
        i += 1
    Loop
    Return dt
End Function

Private Function GetChildTable() As DataTable
    Dim dt As DataTable = New DataTable("Items")

    dt.Columns.Add(New DataColumn("ItemID"))
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: DataTable
- **Methods**:
  - `AddColumn(columnName As String)`
  - `NewRow()`
  - `Add(row As DataRow)`
  - `ToString()`
  - `Format(format As String, arg As Object)`
  - `Random.Next(maxValue As Integer)`
  - `GetParentTable()`
  - `GetChildTable()`

### Properties

- **CustomerID**: Type `String`
- **Price**: Type `String`
- **CustomerName**: Format `CustomerName{index}`
- **Address**: Format `Address{index}`
- **ItemID**: Type `String`
- **ItemName**: Format `ItemName{index}`

## Code Examples

### C# Example

```csharp
// Sample code for creating and populating a DataTable with customer and item information.
DataTable customerTable = GetParentTable();
DataTable itemTable = GetChildTable();
```

### VB.NET Example

```vbnet
' Sample code for creating and populating a DataTable with customer and item information.
Dim customerTable As DataTable = GetParentTable()
Dim itemTable As DataTable = GetChildTable()
```

<!-- tags: [grid, table, datarow, datable] keywords: [customerid, price, customername, address, itemname, itemid, datacolumns, datamethods] -->
```