```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_561.jpeg
document_name: grid
page_number: 561
page_id: grid#page_561
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:00Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Code Example: Customizing Column Styles

The following VB.NET code demonstrates how to customize the appearance and style of columns in a `GridDataBoundGrid`. The example modifies the header text, background color, text color, and font boldness for specific columns.

```vb
Dim binder As GridModelDataBinder = Me.gridDataBoundGrid1.Binder
Dim gbc As GridBoundColumn = binder.InternalColumns("FirstName")
gbc.HeaderText = "Name"
gbc.StyleInfo.BackColor = Color.FromArgb(&HCO, &HC9, &HDB)
gbc.StyleInfo.TextColor = Color.Blue

' Set the second column.
gbc = binder.InternalColumns("LastName")
gbc.HeaderText = "FamilyName"
gbc.StyleInfo.Font.Bold = True

' Just use the default third column... no changes.
' Resize the column headers.
Me.gridDataBoundGrid1.Model.ColWidths.ResizeToFit(GridRangeInfo.Row(0), GridResizeToFitOptions.NoShrinkSize)

' Form1_Load
End Sub
```

#### 4.2.2.7 Changing Column Order in a Grid Data Bound Grid

The simplest way to change the column order in a `GridDataBoundGrid` is to use the `GridDataBoundGrid.Model.Cols.MoveRange` method. This method rearranges the columns based on the parameters passed into it.

##### [C#]
```csharp
// Move columns 4 and 5, to column 1.
this.gridDataBoundGrid1.Model.Cols.MoveRange(4, 2, 1);
```

##### [VB.NET]
```vb
' Move columns 4 and 5, to column 1.
Me.gridDataBoundGrid1.Model.Cols.MoveRange(4, 2, 1)
```

#### 4.2.2.8 Using a Master-Details Relation

### Footer

- **Copyright Notice:** © 2013 Syncfusion. All rights reserved.
- **Page Number:** 561

<!-- tags: [Essential Grid, Windows Forms, Column Order, Master-Detail Relation] keywords: [GridDataBoundGrid, GridBoundColumn, Model.Cols.MoveRange, HeaderText, Font.Bold, ColWidths.ResizeToFit, Syncfusion Winforms] -->
```