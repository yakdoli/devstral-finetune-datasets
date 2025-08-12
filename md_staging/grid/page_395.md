```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_395.jpeg
document_name: grid
page_number: 395
page_id: grid#page_395
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:26Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Me.gridControl1.ColCount = 10
Me.gridControl1.RowCount = 100

' Position it on the form.
Me.gridControl1.Location = New System.Drawing.Point(20, 15)
Me.gridControl1.Size = New System.Drawing.Size(344, 150)

' Add it to the forms' controls.
Me.Controls.Add(Me.gridControl1)
```

## 4.1.4.8 Using the ReadOnly Attribute

There are several ways by which, you can prevent the user from making a change to the contents of a grid cell. If you set a cell's `GridStyleInfo.CellType` to "Static", the user will not be able to type in the cell. Another way to accomplish this is to use the Read-only attribute. This can be done on a grid-wide or cell-by-cell basis.

A Static cell will not allow the edit cursor to become visible. With a Read-only text box cell, the edit cursor may be visible. But, a Static cell can be pasted over or cleared by hitting the Delete key. Read-only cells cannot be pasted over or cleared. If you want a cell that will not show an edit cursor and which, cannot be pasted over or cleared, you must set the `CellType` to "Static" and also set the Read-only property to `True`.

### 4.1.4.8.1 Setting ReadOnly Grid Wide

The property `GridControl.ReadOnly` or `GridDataBoundGrid.Model.ReadOnly` will allow you to set the ReadOnly behavior on a grid-wide basis.

#### C#

```csharp
// Changes cannot be made to the Grid control.
this.gridControl1.ReadOnly = true;

// Changes cannot be made to the Grid Data Bound Grid.
this.gridDataBoundGrid1.ReadOnly = true;
```

#### VB.NET

```vb
' Specify VB.NET code if needed. 
```

## Page-level Navigation/TOC (if applicable)
- 4.1.4.8 Using the ReadOnly Attribute
  - 4.1.4.8.1 Setting ReadOnly Grid Wide

## Cross References
- None

## RAG Annotations

<!-- tags: [grid, readonly attribute, static cell, winforms, syncfusion, control properties] keywords: [read-only, cell type, grid control, griddata bound grid, model, readonly behavior, static cell behavior, edit cursor, delete key, pasting, clearing, grid data bounds] -->
```