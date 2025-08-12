```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_468.jpeg
document_name: grid
page_number: 468
page_id: grid#page_468
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:37Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
this.gridControl1.Cols.Hidden[2] = true;
// Hide row 3.
this.gridControl1.Rows.Hidden[3] = true;
```

```vbnet
' Hide column 2.
Me.GridControl1.Cols.Hidden(2) = True
' Hide row 3.
Me.GridControl1.Rows.Hidden(3) = True
```

You can also use this property to hide the default row headers and column headers. These headers are just column zero and row zero respectively. To hide them you can use code like the one given below.

```csharp
// Hide default row headers.
this.gridControl1.Cols.Hidden[0] = true;
// Hide default column headers.
this.gridControl1.Rows.Hidden[0] = true;
```

```vbnet
' Hide default row headers.
Me.GridControl1.Cols.Hidden(0) = True
' Hide default column headers.
Me.GridControl1.Rows.Hidden(0) = True
```

## API Reference

### Parameters

- **Name**: `Hidden` (Property of `Cols` or `Rows`)
- **Type**: `Boolean`
- **Description**: Specifies whether the column or row is hidden.
- **Default**: `false`
- **Required**: No

### Returns
- Type: `Void`
- Description: Sets the visibility state of the specified column or row.

### Exceptions
- None explicitly mentioned in the provided text.

## Code Examples

### C#
```csharp
this.gridControl1.Cols.Hidden[2] = true; // Hide column 2.
this.gridControl1.Rows.Hidden[3] = true; // Hide row 3.
this.gridControl1.Cols.Hidden[0] = true; // Hide default row headers.
this.gridControl1.Rows.Hidden[0] = true; // Hide default column headers.
```

### VB.NET
```vbnet
Me.GridControl1.Cols.Hidden(2) = True ' Hide column 2.
Me.GridControl1.Rows.Hidden(3) = True ' Hide row 3.
Me.GridControl1.Cols.Hidden(0) = True ' Hide default row headers.
Me.GridControl1.Rows.Hidden(0) = True ' Hide default column headers.
```

<!-- tags: [Syncfusion, WinForms, Grid, Hide, Rows, Columns, Headers, Properties, C#, VB.NET] keywords: [grid, windows forms, hide, row, column, headers, hidden property, default headers, gridcontrol, synchronization, display, customization] -->
```