```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_467.jpeg
document_name: grid
page_number: 467
page_id: grid#page_467
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
listRenderer.ListControlPart.Grid.TableStyle.TextColor = Color.MidnightBlue
listRenderer.ListControlPart.Grid.Properties.GridLineColor = Color.FromArgb(208, 215, 229)
listRenderer.ListControlPart.FillLastColumn = False
End Sub
```

You can apply various styles such as table style, border style, text color, grid line color, etc., to the Grid List control inside a grid cell as in Figure 1.

## 4.1.4.14 Working with Rows and Columns

Grid control has properties that allow users to manipulate rows and columns programmatically. The following properties will be discussed in this section.

- GridControl.Cols, GridControl.Rows - Allows you to hide rows and columns, to freeze them to prevent scrolling and to control the number of headers.
- GridControl.ColWidths, GridControl.RowHeights - Allows you to set the row heights and column widths programmatically.
- GridListControl.ColStyles, GridListControl.RowStyles - Allows you to set the row or column styles.

For a Grid Data Bound Grid, you can access the first two items through the GridDataBoundGrid.Model property. The Grid Data Bound Grid does not use **RowStyles** or **ColStyles**. It uses the GridBoundColumn.StyleInfo object to set column styles with row styles not being directly supported. See the section on Grid Data Bound Grid for more information on how to set its styles.

This section comprises the following topics:

### 4.1.4.14.1 Hiding Rows and Columns

The GridControl.Cols.Hidden collection will allow you to specify whether a column is hidden or not. You can index these properties directly as shown in the code below or you can use the Hidden.SetRange method to provide settings for a range of rows or columns.

```csharp
// Hide column 2.
```

## API Reference

### GridControl.Cols.Hidden
- **Type**: Collection
- **Description**: Specifies whether a column is hidden or not.
- **Usage**: Can be indexed directly or used with the Hidden.SetRange method.

### GridControl.RowStyles
- **Type**: Collection
- **Description**: Allows you to set the row styles.
- **Usage**: Available only for GridListControl but not GridDataBoundGrid.

### GridDataBoundGrid.Model
- **Type**: Property
- **Description**: Provides access to the GridDataBoundGrid Model.
- **Usage**: Used to set column and row properties for data-bound grids.

## Code Examples

### C#
```csharp
// Example: Hiding column 2
listRenderer.ListControlPart.Grid.Cols.Hidden[1] = true;
```

### VB.NET
```vb
' Example: Hiding column 2
listRenderer.ListControlPart.Grid.Cols.Hidden(1) = True
```

## Cross References

See also:
- Grid Data Bound Grid
- GridListControl properties
- GridControl properties

<!-- tags: [Grid, GridListControl, GridDataBoundGrid, Syncfusion Winforms, version 11.4.0.26] keywords: [GridControl.Cols.Hidden, GridControl.RowStyles, GridBoundColumn.StyleInfo, Grid, WinForms, Syncfusion] -->
```