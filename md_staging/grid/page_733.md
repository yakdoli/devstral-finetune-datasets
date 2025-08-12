```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_733.jpeg
document_name: grid
page_number: 733
page_id: grid#page_733
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:53Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates handling events for grouped columns in Syncfusion Grid.
- Includes handling the `Changing` and `Changed` events for grouped columns.
- Provides examples in both C# and VB.NET.

## Content

### Event Handling for Grouped Columns

The following demonstrates how to subscribe to and handle the `GroupedColumns_Changing` and `GroupedColumns_Changed` events for grouped columns in the Syncfusion Grid.

#### C# Example

```csharp
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Changing += new ListPropertyChangedEventHandler(GroupedColumns_Changing);
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Changed += new ListPropertyChangedEventHandler(GroupedColumns_Changed);

// Event Handlers.
// GroupedColumns_Changing event.
void GroupedColumns_Changing(object sender, ListPropertyChangedEventArgs e)
{
    SortColumnDescriptor scd = e.Item as SortColumnDescriptor;
    if (e.Action == Syncfusion.Collections.ListPropertyChangedType.Insert)
        Console.WriteLine("Column Added - {0}", scd.Name);
}

// GroupedColumns_Changed event.
void GroupedColumns_Changed(object sender, ListPropertyChangedEventArgs e)
{
    SortColumnDescriptor scd = e.Item as SortColumnDescriptor;
    if (e.Action == Syncfusion.Collections.ListPropertyChangedType.Remove)
        Console.WriteLine("Column Removed - {0}", scd.Name);
}
```

#### VB.NET Example

```vb
' Subscribe to the events.
AddHandler gridGroupingControl1.TableDescriptor.GroupedColumns.Changing, AddressOf GroupedColumns_Changing

' Event Handlers.
' GroupedColumns_Changing event.
Private Sub GroupedColumns_Changed(ByVal sender As Object, ByVal e As ListPropertyChangedEventArgs)
    Dim scd As SortColumnDescriptor = CType(e.Item, SortColumnDescriptor)
    If e.Action = ListPropertyChangedType.Insert Then
        Console.WriteLine("Column Added - {0}" + scd.Name)
    End If
End Sub

' GroupedColumns_Changed event.
Private Sub GroupedColumns_Changing(ByVal sender As Object, ByVal e As ListPropertyChangedEventArgs)
    Dim scd As SortColumnDescriptor = CType(e.Item, SortColumnDescriptor)
End Sub
```

### Explanation

#### `GroupedColumns_Changing Event`

- This event is raised **before** a column is added to the grouped columns list.
- The handler checks if the action is an **insert** operation and logs the addition of the column.

#### `GroupedColumns_Changed Event`

- This event is raised **after** a column has been removed from the grouped columns list.
- The handler checks if the action is a **remove** operation and logs the removal of the column.

### API Reference

- **`GridGroupingControl.TableDescriptor.GroupedColumns.Changing`**
  - Type: `ListPropertyChangedEventHandler`
  - **Parameters:**
    - `sender`: The source of the event.
    - `e`: `ListPropertyChangedEventArgs` containing event data, including the column being added or removed.
  - **Action Types:**
    - `Syncfusion.Collections.ListPropertyChangedType.Insert`: Indicates a column is being added.
    - `Syncfusion.Collections.ListPropertyChangedType.Remove`: Indicates a column is being removed.

- **`GridGroupingControl.TableDescriptor.GroupedColumns.Changed`**
  - Type: `ListPropertyChangedEventHandler`
  - **Parameters:**
    - `sender`: The source of the event.
    - `e`: `ListPropertyChangedEventArgs` containing event data, including the column being added or removed.
  - **Action Types:**
    - `Syncfusion.Collections.ListPropertyChangedType.Insert`: Indicates a column was added.
    - `Syncfusion.Collections.ListPropertyChangedType.Remove`: Indicates a column was removed.

### Code Examples

The above examples demonstrate how to subscribe to and handle these events, logging the addition and removal of grouped columns in the Grid.

## Cross References

- Refer to the official Syncfusion documentation for additional details on GridGroupingControl events and properties.
- Also see related topics on handling column manipulation in WinForms Grid.

<!-- tags: [WinForms, Grid, GridGroupingControl, Events, GroupedColumns, SortColumnDescriptor] keywords: [GroupedColumns_Changing, GroupedColumns_Changed, ListPropertyChangedEventHandler, Syncfusion.Collections.ListPropertyChangedType] -->
```