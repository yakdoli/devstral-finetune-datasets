```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_595.jpeg
document_name: grid
page_number: 595
page_id: grid#page_595
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:26:51Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
this.gridGroupingControl1 = new Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl();
this.gridGroupingControl1.Size = new System.Drawing.Size(160, 200);
```

## [VB.NET]

```vb.net
Private gridGroupingControl1 As Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl

Me.gridGroupingControl1 = New Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl()
Me.gridGroupingControl1.Size = New System.Drawing.Size(160, 200)
```

### Set up the Data Source.

#### [C#]

```csharp
// Create a Connection Object.
OleDbConnection connection = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\\Data\\NWIND.MDB");

// Create a Data Adapter.
OleDbDataAdapter adapter = new OleDbDataAdapter("SELECT * FROM Customers", connection);

// Create and fill a Data Set.
DataSet dtSet = new DataSet();
adapter.Fill(dtSet);
```

#### [VB.NET]

```vb.net
' Create a Connection Object.
Dim Connection As OleDbConnection = New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\Data\NWIND.MDB")

' Create a Data Adapter.
Dim Adapter As OleDbDataAdapter = New OleDbDataAdapter("SELECT * FROM Customers", Connection)

' Create and fill a Data Set.
Dim dtSet As DataSet = New DataSet()
Adapter.Fill(dtSet)
```

### Bind the grid grouping control to this data table by setting its DataSource property.

---

## API Reference

### Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl
- **Properties:**
  - **Size:** `System.Drawing.Size` - Specifies the size of the control.

### System.Data.OleDb.OleDbConnection
- **Constructor:** `OleDbConnection(string connectionString)` - Creates a new OleDbConnection using the specified connection string.

### System.Data.OleDb.OleDbDataAdapter
- **Constructor:** `OleDbDataAdapter(string selectCommandText, OleDbConnection connection)` - Creates a new OleDbDataAdapter with the specified SQL SELECT statement and OleDbConnection.
- **Method:**
  - `Fill(DataSet dataSet)` - Fills the DataSet with data from the data source using the SELECT statement.

### System.Data.DataSet
- **Constructor:** `DataSet()`
- **Method:**
  - `Fill()` - Fills the DataSet with data from the data source using the SELECT statement.

---

## Code Examples

### C#
```csharp
// Example of setting up the DataSource for GridGroupingControl.
OleDbConnection connection = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\\Data\\NWIND.MDB");
OleDbDataAdapter adapter = new OleDbDataAdapter("SELECT * FROM Customers", connection);
DataSet dtSet = new DataSet();
adapter.Fill(dtSet);
gridGroupingControl1.DataSource = dtSet;
```

### VB.NET
```vb.net
' Example of setting up the DataSource for GridGroupingControl.
Dim Connection As OleDbConnection = New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\Data\NWIND.MDB")
Dim Adapter As OleDbDataAdapter = New OleDbDataAdapter("SELECT * FROM Customers", Connection)
Dim dtSet As DataSet = New DataSet()
Adapter.Fill(dtSet)
gridGroupingControl1.DataSource = dtSet
```

---

## RAG Annotations
<!-- tags: [Grid, Grouping, DataBinding, Windows Forms, DataSource, OleDbConnection, OleDbDataAdapter, DataSet] keywords: [Syncfusion, GridGroupingControl, Data Source, Data Binding, Connection Object, Data Adapter, Fill, DataSet] -->
```