```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_396.jpeg
document_name: grid
page_number: 396
page_id: grid#page_396
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:37Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
' Changes cannot be made to the Grid control.
Me.GridControl1.ReadOnly = True

' Changes cannot be made to the Grid Data Bound Grid.
Me.GridDataBoundGrid1.ReadOnly = True
```

## 4.1.4.8.2 Setting ReadOnly Cell by Cell

To set the ReadOnly behavior on a cell-by-cell basis, you must use the cell's `GridStyleInfo` object, which has a `ReadOnly` property.

### Code in C#
```csharp
// Changes cannot be made to the cell (1, 1).
this.gridControl1[1, 1].ReadOnly = true;
```

### Code in VB.NET
```vbnet
' Changes cannot be made to the cell (1, 1).
Me.GridControl1(1, 1).ReadOnly = True
```

## 4.1.4.8.3 Making a Change to a ReadOnly Cell

If you set the ReadOnly behavior, the user will be able to type in the cell and he will also not be able to change the cell's value programmatically. So, to make changes to a ReadOnly cell, you must use the `GridControl.IgnoreReadOnly` property, which will allow you to change a Read-Only cell.

### Code in C#
```csharp
this.gridControl1[1, 1].ReadOnly = true;

// Cell (1, 1) has been set to Read-only.
// To change its value, you need to use the IgnoreReadOnly property.
this.gridControl1.IgnoreReadOnly = true;

// Turn off Read-only checking.
this.gridControl1[1, 1].CellValue = 256;
```
```