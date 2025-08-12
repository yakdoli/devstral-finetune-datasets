```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_134.jpeg
document_name: diagram
page_number: 134
page_id: diagram#page_134
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:53Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Table Layout Manager Properties

The following table describes properties of a table layout manager:

| Property          | Description |
|-------------------|-------------|
|                   | The following options: |
|                   | - EqualToMaxNode |
|                   | - MinimalTable |
|                   | - Minimal |
| MaxSize           | Gets / sets the size of each table cell. It is an integer type value. |
| MaxColumnCount    | Represents the maximum horizontal cell count in the table. It is an integer type value. |
| MaxRowsCount      | Represents the maximum vertical cell count in the table. It is an integer type value. |
| HorizontalSpacing | Defines the horizontal offset between adjacent nodes. |
| VerticalSpacing   | Defines the vertical offset between adjacent nodes. |

## Programmatic Configuration

Programmatically, the table layout manager instance should be created with the respective arguments, assigned to the Layout Manager, and updated as follows.

### [C#]

```csharp
TableLayoutManagermt lLayout = new TableLayoutManager(this.diagram1.Model, 7, 7);
lLayout.VerticalSpacing = 20;
lLayout.HorizontalSpacing = 20;
lLayout.CellSizeMode = CellSizeMode.EqualToMaxNode;
lLayout.Orientation = Orientation.Horizontal;
lLayout.MaxSize = new SizeF(500, 600);

this.diagram1.LayoutManager = lLayout;
this.diagram1.LayoutManager.UpdateLayout(null);.AttachModel(modell);
documentExplorer1.Dock = DockStyle.Right;
documentExplorer1.BackColor = System.Drawing.SystemColors.Window;
documentExplorer1.Location = new System.Drawing.Point(0, 377);
documentExplorer1.Size = new System.Drawing.Size(200, 100);
documentExplorer1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
documentExplorer1.ShowNodeToolTips = true;
```

### [VB]
```vb
' [VB] section content is missing in the image.
```

## Contact Information

- **Copyright:** © 2013 Syncfusion. All rights reserved.
- **Page Number:** 134

```html
<!-- tags: [WinForms, table layout manager, Syncfusion, Essential Diagram, programming configuration] keywords: [table layout manager, diagram, layout manager, C#, VB, programmatically, cell size, spacing, orientation] -->
```