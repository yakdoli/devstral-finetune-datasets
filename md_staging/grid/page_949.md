```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_949.jpeg
document_name: grid
page_number: 949
page_id: grid#page_949
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates setting up a hierarchical datasource in Windows Forms.
- Examples show how to create DataTables representing parent, child, and grandchildren rows.
- Utilizes C# code to generate structured data for hierarchical data binding.

## Content

### Setting up an Hierarchical Datasource

#### Code Example: Creating Parent Table

```csharp
private int numberParentRows = 50;
private int numberChildRows = 200;
private int numberGrandChildRows = 500;

private DataTable GetParentTable()
{
    DataTable dt = new DataTable("ParentTable");
    dt.Columns.Add(new DataColumn("parentID"));
    dt.Columns.Add(new DataColumn("ParentName"));
    dt.Columns.Add(new DataColumn("GroupID"));

    Random r = new Random();
    for (int i = 0; i < numberParentRows; i++)
    {
        DataRow dr = dt.NewRow();
        dr[0] = i;
        dr[1] = string.Format("parentName{0}", i);
        dr[2] = r.Next(99, 111);
        dt.Rows.Add(dr);
    }
    return dt;
}
```

#### Code Example: Creating Child Table

```csharp
private DataTable GetChildTable()
{
    DataTable dt = new DataTable("ChildTable");

    dt.Columns.Add(new DataColumn("childID"));
    dt.Columns.Add(new DataColumn("Name"));
    dt.Columns.Add(new DataColumn("ParentID"));
    dt.Columns.Add(new DataColumn("ChildGroupID"));

    Random r = new Random();
    for (int i = 0; i < numberChildRows; i++)
    {
        DataRow dr = dt.NewRow();
        dr[0] = i.ToString();
        dr[1] = string.Format("ChildName{0}", i);
        dr[2] = (i % numberParentRows).ToString();
        dr[3] = r.Next(994, 1006).ToString();
        dt.Rows.Add(dr);
    }
}
```

## API Reference

### Methods
- `GetParentTable()`: Returns a DataTable with hierarchical parent information.
    - **Returns**: `DataTable` - A DataTable with columns: "parentID", "ParentName", and "GroupID".
- `GetChildTable()`: Returns a DataTable with hierarchical child information.
    - **Returns**: `DataTable` - A DataTable with columns: "childID", "Name", "ParentID", and "ChildGroupID".

## Code Examples
The provided examples demonstrate the creation of DataTables with structured hierarchical relationships, suitable for use with the Essential Grid control in Windows Forms. These DataTables can be used to bind data to Grid controls, allowing for hierarchical data display.

## Cross References
- Refer to the Essential Grid documentation for further details on data binding and hierarchical data display.
- Consult Syncfusion's documentation on DataTables and hierarchical data for additional insights.

<!-- tags: [syncfusion, windowsforms, essentialgrid, datatables, hierarchicaldatasource, version:11.4.0.26] keywords: [parent table, child table, grid control, data binding, hierarchical data, random generation, dataset creation] -->
```