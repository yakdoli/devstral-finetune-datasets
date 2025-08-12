```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_801.jpeg
document_name: grid
page_number: 801
page_id: grid#page_801
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:37Z
fidelity: lossless
-->

## Windows Forms Grid Example

### Creating Hierarchical DataTables

The following code snippet demonstrates how to create hierarchical `DataTables` for a parent, child, and grandchild relationship, typically used in a `WinForms` application to populate hierarchical grids or tree structures.

#### C# Example

```csharp
dt.Columns.Add(new DataColumn("childID"));
dt.Columns.Add(new DataColumn("Name"));
dt.Columns.Add(new DataColumn("ParentID"));

for (int i = 0; i < numberChildRows; i++)
{
    DataRow dr = dt.NewRow();
    dr[0] = i.ToString();
    dr[1] = string.Format("ChildName{0}", i);
    dr[2] = (i % numberParentRows).ToString();
    dt.Rows.Add(dr);
}
return dt;
}

// Create Grand Child Table.
private DataTable GetGrandChildTable()
{
    DataTable dt = new DataTable("GrandChildTable");

    dt.Columns.Add(new DataColumn("GrandChildID"));
    dt.Columns.Add(new DataColumn("Name"));
    dt.Columns.Add(new DataColumn("ChildID"));

    for (int i = 0; i < numberGrandChildRows; i++)
    {
        DataRow dr = dt.NewRow();
        dr[0] = i.ToString();
        dr[1] = string.Format("GrandChildName{0}", i);
        dr[2] = (i % numberChildRows).ToString();
        dt.Rows.Add(dr);
    }
    return dt;
}
```

#### VB.NET Example

```vb
Private numberParentRows As Integer = 5
Private numberChildRows As Integer = 20
Private numberGrandChildRows As Integer = 50

' Create Parent Table.
Private Function GetParentTable() As DataTable
    Dim dt As New DataTable("ParentTable")
```

## Notes

- The code snippets show how to dynamically create `DataTables` with predefined column structures and populate them with sample data.
- The `Parent`, `Child`, and `GrandChild` tables demonstrate a parent-child relationship, which is useful for hierarchical data binding in `WinForms`.
- The VB.NET example provides the framework for creating a `ParentTable`, leaving the continuation of the process (such as adding columns and rows) as an exercise for the user.

### Tags and Keywords
<!-- tags: [WinForms, Grid, DataTable, hierarchical data] keywords: [DataColumn, DataRow, ParentTable, ChildTable, GrandChildTable, numberParentRows, numberChildRows, numberGrandChildRows] -->
```