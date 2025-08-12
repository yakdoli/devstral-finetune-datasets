```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_270.jpeg
document_name: DocIo
page_number: 270
page_id: DocIo#page_270
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:13Z
fidelity: lossless
-->

## Content

```csharp
doc.Save("NestedMailMerge.doc");
System.Diagnostics.Process.Start("NestedMailMerge.doc");
}

/// <summary>
/// Get the table
/// </summary>
/// <param name="sqlQuery"></param>
/// <returns></returns>
private DataTable GetNestedDataTable(string sqlQuery)
{
    OleDbConnection conn = null;
    try
    {
        string connectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" +
            System.IO.Path.Combine(dataPath, @"NestedMailMergel.mdb");

        // Get data from the database.
        conn = new OleDbConnection(connectionString);
        conn.Open();
        OleDbCommand cmd = new OleDbCommand(sqlQuery, conn);
        OleDbDataAdapter da = new OleDbDataAdapter(cmd);
        DataTable table = new DataTable();
        da.Fill(table);
        return table;
    }
    finally
    {
        if (conn != null)
            conn.Close();
    }
}
```


## WinForms-specific Example in VB.NET

```vb
[VB.NET]

Public Sub CreateDocument()
    Dim doc As WordDocument = New WordDocument()
    doc.Open(dataPath + "NestedMailMergel.doc")

    ' Get Data from the Database.
    Dim table1 As DataTable = GetNestedDataTable("select * from Table1")
    table1.TableName = "Table1"

    Dim table2 As DataTable = GetNestedDataTable("select * from Table2")
    table2.TableName = "Table2"
End Sub
```

## API Reference

### GetNestedDataTable Method

- **Description**: Retrieves a DataTable using the provided SQL query.
- **Parameters**:
    - `sqlQuery` (string): The SQL query to execute.
- **Returns**: `DataTable` - A DataTable containing the result of the query.
- **Exceptions**:
    - All exceptions related to database operations.

## Code Examples

### C# Example

```csharp
// Example usage of GetNestedDataTable
private DataTable GetTableData(string query)
{
    return GetNestedDataTable(query);
}
```

### VB.NET Example

```vb
' Example usage of GetNestedDataTable
Public Function GetTableData(query As String) As DataTable
    Return GetNestedDataTable(query)
End Function
```

## Cross References

See also:  
- [Data Manipulation Basics in WinForms](#)
- [Advanced SQL Queries with OleDb in .NET](#)

<!-- tags: [Syncfusion Windows Forms, Data Manipulation, OleDb, Database Connectivity, .NET] keywords: [GetNestedDataTable, DataTable, OleDbConnection, OleDbCommand, OleDbDataAdapter, WordDocument, NestedMailMerge, Data Source, SQL Query, VB.NET, C#] -->
```