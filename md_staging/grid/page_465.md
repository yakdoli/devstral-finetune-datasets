```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_465.jpeg
document_name: grid
page_number: 465
page_id: grid#page_465
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:17Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

To have a Grid List control in a Grid cell, set its `CellType` property as `GridListControl`. An array is used as the data source in the following example. You can set its `DataSource` and `DisplayMember` properties as follows:

### C#

```csharp
ArrayList array = new ArrayList();
array.Add(new MyClass(001, "John David"));
array.Add(new MyClass(002, "Tom"));
array.Add(new MyClass(003, "Bretney"));
array.Add(new MyClass(004, "Jessy"));
array.Add(new MyClass(005, "Bruch"));
array.Add(new MyClass(006, "Johny"));

// Set up a Grid List control cell.
this.gridControl1[rowIndex, 2].CellType = "GridListControl";

// Specify the data source and display member for the Grid List control.
this.gridControl1[rowIndex, 2].DataSource = array;
this.gridControl1[rowIndex, 2].DisplayMember = "Name";
```

### VB.NET

```vb
Dim array As ArrayList = New ArrayList()
array.Add(New [MyClass](1, "John David"))
array.Add(New [MyClass](2, "Tom"))
array.Add(New [MyClass](3, "Bretney"))
array.Add(New [MyClass](4, "Jessy"))
array.Add(New [MyClass](5, "Bruch"))
array.Add(New [MyClass](6, "Johny"))

' Set up a Grid List control cell.
Me.gridControl1(rowIndex, 2).CellType = "GridListControl"

' Specify the data source and display member for the Grid List control.
Me.gridControl1(rowIndex, 2).DataSource = array
Me.gridControl1(rowIndex, 2).DisplayMember = "Name"
```

We have now added a Grid List control in a Grid cell and bound the data to it.

This Grid List control can be customized by accessing the `GridDropDownGridListControlCellRenderer` class, inside the `CurrentCellShowedDropDown` event handler.

<!-- tags: [syncfusion, grid, windows forms, GridListControl, DataSource, DisplayMember, customization, event handler, GridDropDownGridListControlCellRenderer] -->
```