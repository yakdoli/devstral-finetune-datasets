```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_135.jpeg
document_name: diagram
page_number: 135
page_id: diagram#page_135
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:34Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Layout Configuration Example

```vb
Dim lLayout As TableLayoutManagert = New
TableLayoutManagert(Me.diagram1.Model, 7, 7)
lLayout.VerticalSpacing = 20
lLayout.HorizontalSpacing = 20
lLayout.CellSizeMode = CellSizeMode.EqualToMaxNode
lLayout.Orientation = Orientation.Horizontal
lLayout.MaxSize = New SizeF(500, 600)

Me.diagram1.LayoutManager = lLayout
Me.diagram1.LayoutManager.UpdateLayout(Nothing).AttachModel(model1)
documentExplorer1.Dock = DockStyle.Right
documentExplorer1.BackColor = System.Drawing.SystemColors.Window
documentExplorer1.Location = New System.Drawing.Point(0, 377)
documentExplorer1.Size = New System.Drawing.Size(200, 100)
documentExplorer1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
documentExplorer1.ShowNodeToolTips = True
```

### Diagram Layout Visualization

**Figure 75: Horizontal Orientation**

![Horizontal Orientation Diagram](#)

This figure demonstrates the horizontal orientation layout for the diagram, showcasing nodes arranged in a grid-like structure with interconnected paths.

## Summary

- Configures a `TableLayoutManager` for a diagram control, setting spacing, cell size mode, orientation, and maximum size.
- Integrates the layout manager with a model and updates the layout.
- Customizes the appearance and behavior of a `documentExplorer` control, including docking, background color, location, size, border style, and tooltip visibility.

### Related Sections
- [Layout Managers in Essential Diagram for WinForms](リンク先)
- [Working with Document Explorer in Diagrams](リンク先)

<!-- tags: [syncfusion-sdk, windows-forms, layout-manager, diagram, horizontal-orientation, document-explorer] keywords: [layout manager, table layout, horizontal orientation, diagram control, document explorer, winforms, synchronization] -->
```