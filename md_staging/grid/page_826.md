```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_826.jpeg
document_name: grid
page_number: 826
page_id: grid#page_826
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:01Z
fidelity: lossless
-->

## Content

### Setting up Grid Relations in Windows Forms

In this section, we demonstrate how to configure grid relations in a `GridGroupingControl` using both C# and VB.NET, focusing on creating a `ListItemReference` type relation.

#### C#

```csharp
countriesRd.ChildTableDescriptor.AllowNew = true;
mainTd.Relations.Add(countriesRd);
// Assign data source.
this.gridGroupingControl1.DataSource = table;
mainTd.Name = "ListItemReference";
```

#### VB.NET

```vb
Dim mainTd As GridTableDescriptor = Me.gridGroupingControl1.TableDescriptor
Dim countriesRd As New GridRelationDescriptor()
countriesRd.Name = "Country"
countriesRd.MappingName = "Country"
countriesRd.RelationKind = RelationKind.ListItemReference

' SourceListSet name for look up.
countriesRd.ChildTableName = "Countries"

' Format ChildList.
countriesRd.ChildTableDescriptor.Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 245, 227)

' To hide the Key Column.
countriesRd.ChildTableDescriptor.VisibleColumns.Add("Name")
countriesRd.ChildTableDescriptor.SortedColumns.Add("Name")
countriesRd.ChildTableDescriptor.AllowEdit = True

' Disallow users to modify states.
countriesRd.ChildTableDescriptor.AllowNew = True

mainTd.Relations.Add(countriesRd)

' Assign data source.
Me.gridGroupingControl1.DataSource = Table
mainTd.Name = "ListItemReference"
```

### Sample Output

Here is a sample output that displays a look up child list for the data column **Country** with value **Brazil**.

#### Note

This configuration enables users to interact with the grid by adding new child records directly from the `GridGroupingControl`, using `ListItemReference` to manage the relationship between parent and child tables.

## API Reference

- **GridRelationDescriptor**: Represents the relationship between tables in a `GridTableDescriptor`.

  - **Methods**
    - `Add`: Adds a new relation to the `GridGroupingControl`.

  - **Properties**
    - **Name**: The name of the relation.
    - **MappingName**: The name used for lookup in the source list set.
    - **RelationKind**: The type of relationship (e.g., `ListItemReference`).
    - **ChildTableName**: The name of the child table.
    - **ChildTableDescriptor**: Provides access to the properties of the child table.

- **GridTableDescriptor**: Represents a table in the `GridGroupingControl` with properties to configure table behavior.

  - **Properties**
    - **Name**: The name of the table descriptor.
    - **Relations**: Collection of `GridRelationDescriptor` objects.

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.Grid.Grouping;

public void ConfigureGrid()
{
    GridTableDescriptor mainTd = gridGroupingControl1.TableDescriptor;
    GridRelationDescriptor countriesRd = new GridRelationDescriptor
    {
        Name = "Country",
        MappingName = "Country",
        RelationKind = RelationKind.ListItemReference,
        ChildTableName = "Countries"
    };

    // Configure appearance and behaviors.
    countriesRd.ChildTableDescriptor.Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 245, 227);
    countriesRd.ChildTableDescriptor.VisibleColumns.Add("Name");
    countriesRd.ChildTableDescriptor.SortedColumns.Add("Name");
    countriesRd.ChildTableDescriptor.AllowEdit = true;
    countriesRd.ChildTableDescriptor.AllowNew = true;

    mainTd.Relations.Add(countriesRd);
    gridGroupingControl1.DataSource = table;
    mainTd.Name = "ListItemReference";
}
```

### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Grid.Grouping

Public Sub ConfigureGrid()
    Dim mainTd As GridTableDescriptor = Me.gridGroupingControl1.TableDescriptor
    Dim countriesRd As New GridRelationDescriptor()
    With countriesRd
        .Name = "Country"
        .MappingName = "Country"
        .RelationKind = RelationKind.ListItemReference
        .ChildTableName = "Countries"
    End With

    ' Configure appearance and behaviors.
    With countriesRd.ChildTableDescriptor
        .Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 245, 227)
        .VisibleColumns.Add("Name")
        .SortedColumns.Add("Name")
        .AllowEdit = True
        .AllowNew = True
    End With

    mainTd.Relations.Add(countriesRd)
    Me.gridGroupingControl1.DataSource = Table
    mainTd.Name = "ListItemReference"
End Sub
```

<!-- tags: [Syncfusion, GridGroupingControl, RelationDescriptor, ListItemReference, C#, VB.NET, Windows Forms] keywords: [GridRelationDescriptor, GridTableDescriptor, AllowNew, AllowEdit, VisibleColumns, SortedColumns, DataSource] -->
```