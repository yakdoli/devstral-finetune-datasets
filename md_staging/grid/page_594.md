```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_594.jpeg
document_name: grid
page_number: 594
page_id: grid#page_594
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:27:13Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### 4.3.1.1 Through Designer

For details, see Tutorials Lesson 1: Grid Grouping Control Designer.

### 4.3.1.2 Through Code

This section will give you a step by step tutorial on creating a Grid Grouping control through code. You can bind the Grid Grouping control either to an MDB file or to a data source that has been created manually.

In this lesson, you will learn about the following topics.

#### 4.3.1.2.1 Binding a Grid Grouping Control to an MDB File

This example illustrates how to bind a Grid Grouping control to an MDB file at run time. It uses OleDbConnection and OleDbAdapter objects to get connected to a data source that exposes OLE DB interface. Try a similar approach to connect to a database from MS SQL Server.

1. Include the required namespace.

   ```csharp
   using Syncfusion.Windows.Forms.Grid.Grouping;
   using System.Data.OleDb;
   ```

   ```vb
   Imports Syncfusion.Windows.Forms.Grid.Grouping
   Imports System.Data.OleDb
   ```

2. Create an instance of Grid Grouping control and specify its size.

   ```csharp
   private Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl gridGroupingControl;
   ```

## API Reference

### Namespaces and Classes

#### Namespace: Syncfusion.Windows.Forms.Grid.Grouping
- **Class**: GridGroupingControl

### Properties
- **Size**: Specifies the size of the Grid Grouping control.

### Events
- **GridInitializeCell**: Occurs when a cell is initialized.
- **RecordLoaded**: Occurs when a record is loaded into the Grid Grouping control.

### Methods
- **BindToData**: Binds the Grid Grouping control to a data source.

### Parameters
| Name       | Type                  | Description                                                                 | Default     | Required |
|------------|-----------------------|-----------------------------------------------------------------------------|-------------|----------|
| DataSource | `object`             | Specifies the data source to bind.                                             | `null`      | Yes      |
| ClearCache | `bool`               | Specifies whether to clear the cache when binding.                              | `true`      | Yes      |

### Returns
- **Type**: `void`
- **Description**: This method does not return a value. It is used to bind the data source to the Grid Grouping control.

## Code Examples

#### C#

```csharp
using Syncfusion.Windows.Forms.Grid.Grouping;
using System.Data.OleDb;

private void BindToMdbFile()
{
    // Step 1: Declare the required objects
    GridGroupingControl gridGroupingControl = new GridGroupingControl();

    // Step 2: Set the size of the Grid Grouping control
    gridGroupingControl.Size = new System.Drawing.Size(800, 600);

    // Step 3: Define the connection string
    string connectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=your_database.mdb";

    // Step 4: Create the OleDbConnection
    using (OleDbConnection connection = new OleDbConnection(connectionString))
    {
        connection.Open();

        // Step 5: Define the SQL query
        string query = "SELECT * FROM your_table";

        // Step 6: Create the OleDbCommand
        OleDbCommand command = new OleDbCommand(query, connection);

        // Step 7: Create the OleDbDataAdapter
        OleDbDataAdapter adapter = new OleDbDataAdapter(command);

        // Step 8: Create the DataSet
        DataSet dataSet = new DataSet();

        // Step 9: Fill the DataSet
        adapter.Fill(dataSet);

        // Step 10: Bind the Grid Grouping control to the dataset
        gridGroupingControl.DataSource = dataSet.Tables[0];
    }
}
```

#### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Grid.Grouping
Imports System.Data.OleDb

Private Sub BindToMdbFile()
    ' Step 1: Declare the required objects
    Dim gridGroupingControl As New GridGroupingControl()

    ' Step 2: Set the size of the Grid Grouping control
    gridGroupingControl.Size = New System.Drawing.Size(800, 600)

    ' Step 3: Define the connection string
    Dim connectionString As String = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=your_database.mdb"

    ' Step 4: Create the OleDbConnection
    Using connection As New OleDbConnection(connectionString)
        connection.Open()

        ' Step 5: Define the SQL query
        Dim query As String = "SELECT * FROM your_table"

        ' Step 6: Create the OleDbCommand
        Dim command As OleDbCommand = New OleDbCommand(query, connection)

        ' Step 7: Create the OleDbDataAdapter
        Dim adapter As OleDbDataAdapter = New OleDbDataAdapter(command)

        ' Step 8: Create the DataSet
        Dim dataSet As DataSet = New DataSet()

        ' Step 9: Fill the DataSet
        adapter.Fill(dataSet)

        ' Step 10: Bind the Grid Grouping control to the dataset
        gridGroupingControl.DataSource = dataSet.Tables(0)
    End Using
End Sub
```

<!-- tags: [Grid Grouping Control, Designer, Windows Forms, Controls, Data Binding, OLE DB, MS SQL Server] keywords: [GridGroupingControl, OleDbConnection, OleDbDataAdapter, DataSet, ClearCache, Binding] -->
```