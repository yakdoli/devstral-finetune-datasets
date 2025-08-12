```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_106.jpeg
document_name: diagram
page_number: 106
page_id: diagram#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:56Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

It is a property of `Diagram.View` class and its return type is `Syncfusion.Windows.Forms.Diagram.LayoutGrid`.

## Properties

| Properties         | Description                                                                 |
|-------------------- | --------------------------------------------------------------------------- |
| Color              | Color used for drawing the grid. It accepts `System.Color` value.           |
| ContainerView      | Gets or sets the view that this grid is attached to.                        |
| DashOffset         | Distance from the start of the line to the dash pattern. It accepts `Float` value. |
| DashStyle          | Style used for dashed lines. It accepts `System.Drawing.Drawing2D.DashStyle` value. |
| GridStyle          | Gets or sets the appearance of the grid. It is `GridStyle` enumerator type value. |
| HorizontalSpacing  | Determines the horizontal distance between grid points. It accepts `float` value. |
| MinPixelSpacing    | Indicates minimum spacing between grid points in device units. It accepts `Float` value. |
| SnapToGrid         | Adjust the node with nearest grid point. Specifies whether the snap to grid feature is enabled. It accepts `Boolean` value (true or false). |
| VerticalSpacing    | Determines the vertical distance between grid points. It accepts `Float` value. |
| Visible            | Specifies whether the grid is visible. It accepts `Boolean` value (true or false). |

## Code Examples

```csharp
[CS#]

diagram1.View.Grid.GridStyle = GridStyle.Line;
diagram1.View.Grid.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
diagram1.View.Grid.Color = Color.LightGray;
diagram1.View.Grid.VerticalSpacing = 15;
diagram1.View.Grid.HorizontalSpacing = 15;
```

<!-- tags: [Syncfusion Winforms, Diagram, LayoutGrid, Grid Properties, Grid Style, Dash Style, Horizontal Spacing, Vertical Spacing, Visible, C#] keywords: [Diagram.View, Syncfusion.Windows.Forms.Diagram.LayoutGrid, GridStyle, DashOffset, MinPixelSpacing, SnapToGrid, Visible, Color, ContainerView, HorizontalSpacing, VerticalSpacing] -->
``` 
