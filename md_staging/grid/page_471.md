```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_471.jpeg
document_name: grid
page_number: 471
page_id: grid#page_471
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
// Total of three column header rows.
this.gridControl1.Rows.HeaderCount = 2;
```

```vb.net
' Have 3 non-scrollable rows at the top.
Me.GridControl1.Rows.FrozenCount = 2

' Total of three column header rows.
Me.GridControl1.Rows.HeaderCount = 2
```

![Figure 181: Grid with Three Frozen Column Header Rows](https://example.com/image_url)

As we have said, frozen rows will always appear at the top of the grid and frozen columns will always appear to the left of the grid. It is possible to freeze an interior range of row or columns, using the `GridControl.Rows.FreezeRange` or `GridControl.Cols.FreezeRange` method. But, the `FreezeRange` method will move the requested rows / columns to the top or left and then it will set the `FrozenCount` to actually freeze the rows or columns.

## Code Examples

```csharp
// Moves rows 3 and 4 to the top of the grid and freezes them.
this.gridControl1.Rows.FreezeRange(3, 4);
```

```vb.net
' Moves rows 3 and 4 to the top of the grid and freezes them.
Me.GridControl1.Rows.FreezeRange(3, 4)
```
```html
<!-- tags: [product, module, control, api, version?] keywords: [Essential Grid, Windows Forms, frozen rows, frozen columns, header rows, FreezeRange, GridControl] -->
```