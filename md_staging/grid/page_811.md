```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_811.jpeg
document_name: grid
page_number: 811
page_id: grid#page_811
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:57Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes how to create a `datatable` with a column linked to a foreign key.
- Demonstrates the establishment of a `ForeignKeyReference` relationship using `GridRelationDescriptor`.

## Content

### Step 3: Creates a datatable with the Key from USState as one of the columns.

#### [C#]
```csharp
DataTable table = new DataTable();
table.Columns.Add("Id", typeof(string));
table.Columns.Add("State", typeof(string));

// Adding rows.
for (int i = 0; i < 25; i++)
{
    table.Rows.Add(table.NewRow());
    table.Rows[i][0] = i;
    table.Rows[i][1] = usStates[i % 8].Key;
}
```

#### [VB.NET]
```vb
Dim table As New DataTable()
table.Columns.Add("Id", GetType(String))
table.Columns.Add("State", GetType(String))

' Adding rows.
Dim i As Integer
For i = 0 To 24
    table.Rows.Add(table.NewRow())
    table.Rows(i)(0) = i
    table.Rows(i)(1) = usStates((i Mod 8)).Key
Next i
```

### Step 4: Establish the ForeignKeyReference relationship.

#### [C#]
```csharp
GridTableDescriptor mainTd = this.gridGroupingControl1.TableDescriptor;

GridRelationDescriptor usStatesRd = new GridRelationDescriptor();
usStatesRd.Name = "State";
```

## API Reference

### GridTableDescriptor

- **Properties:**
  - `TableDescriptor`: Represents the main table descriptor.

### GridRelationDescriptor

- **Properties:**
  - `Name`: Specifies the name of the relationship.

### Methods

- **AddForeignKeyReference:**
  - Establishes a foreign key reference between tables.

## Code Examples

### [C#]
```csharp
GridTableDescriptor mainTd = this.gridGroupingControl1.TableDescriptor;

GridRelationDescriptor usStatesRd = new GridRelationDescriptor();
usStatesRd.Name = "State";

mainTd.ForeignRelationDescriptors.Add(usStatesRd);
```

### [VB.NET]
```vb
Dim mainTd As GridTableDescriptor = Me.gridGroupingControl1.TableDescriptor

Dim usStatesRd As New GridRelationDescriptor()
usStatesRd.Name = "State"

mainTd.ForeignRelationDescriptors.Add(usStatesRd)
```

## Cross References
- Refer to `GridTableDescriptor` and `GridRelationDescriptor` for detailed API documentation.

<!-- tags: [grid, windowsforms, datatables, foreign key, relationship, c#, vb.net] keywords: [GridTableDescriptor, GridRelationDescriptor, datatable, foreign key, relationship, data, columns, table, usstate, syncfusion] -->
```