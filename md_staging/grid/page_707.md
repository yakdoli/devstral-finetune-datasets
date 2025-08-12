```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_707.jpeg
document_name: grid
page_number: 707
page_id: grid#page_707
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

To disallow a column being grouped by, the `AllowGroupByColumn` property should be set to False for that column. This property determines whether the grid can be grouped by a column when the user drags the column to the GroupDropArea.

## Disallowing Grouping by a Column

### C#

```csharp
this.gridGroupingControl1.TableDescriptor.Columns[0].AllowGroupByColumn = false;
```

### VB.NET

```vb
Me.gridGroupingControl1.TableDescriptor.Columns(0).AllowGroupByColumn = False
```

## Clearing Groups

The `GroupedColumns.Clear()` method will remove all the elements from the `GroupedColumns` Collection and hence the data will get ungrouped.

### C#

```csharp
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear();
```

### VB.NET

```vb
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear()
```

## Removing a given Group

The `GroupedColumns` property provide two methods to remove a specific group from the collection. `Remove()` method deletes the column with a given name from the `GroupedColumns` collection. As a result, the table data is ungrouped by that column. The `RemoveAt()` method deletes the element at the specified index from the collection.

### C#

```csharp
// Removes the first element.
this.gridGroupingControl1.TableDescriptor.GroupedColumns.RemoveAt(0);

// Removes the Title element from the columns collection.
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Remove("Title");
```

### VB.NET

```vb
' Removes the first element.
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.RemoveAt(0)

' Removes the Title element from the columns collection.
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Remove("Title")
```

## Footer
© 2013 Syncfusion. All rights reserved.
```