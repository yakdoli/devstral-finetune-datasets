```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_280.jpeg
document_name: diagram
page_number: 280
page_id: diagram#page_280
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:16Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- This section demonstrates how to dynamically update node colors using the `MouseMove` event in a Windows Forms application.
- It highlights the use of a timer to trigger continuous random color changes for selected polygons.
- Utilizes `Node` and `Polygon` types from the Diagram control.

## Content

### Handling Mouse Movement

The `diagram1_MouseMove` event handler retrieves the node under the mouse and updates the tooltip and timer based on the node's properties.

```csharp
[C#]

Node globalNode;
Polygon PolygonNode;
public Timer timer1;

private void diagram1_MouseMove(object sender, MouseEventArgs e)
{
    try
    {
        // Retrieves node under the mouse action
        Node node1 = (Node)this.diagram1.Controller.GetNodeUnderMouse(new Point(e.X, e.Y));

        if (node1 != null && (node1.Name.ToString() != "TextNode"))
        {
            this.toolTip1.SetToolTip(this.diagram1, node1.Name);
            this.toolTip1.Active = true;

            globalNode = node1;
            PolygonNode = node1 as Polygon;
            defaultColor = PolygonNode.FillStyle.Color;

            this.timer1.Start();
        }
        else
        {
            this.toolTip1.Active = false;
            this.timer1.Stop();
        }
    }
    catch
    {
    }
}
```

### Timer Tick Event

The `timer1_Tick` event handler changes the fill color of the selected polygon using a random color generator.

```csharp
private void timer1_Tick(object sender, EventArgs e)
{
    // Convert node as polygon
    Polygon poly = globalNode as Polygon;
    Random r = new Random();

    if (poly != null)
    {
        // Setting fillstyle for the polygon
        poly.FillStyle.Color = Color.FromArgb(r.Next(255), r.Next(255), r.Next(255));
        globalNode.LineStyle.DashStyle = 
    }
}
```

## Notes

- The `globalNode` variable is used to store the selected node during mouse movement.
- The `PolygonNode` variable is cast to access polygon-specific properties like `FillStyle`.
- The `timer1` timer is used to trigger continuous updates to the polygon's fill color.
- The `Random` class is employed to generate random colors for the polygon's fill style.

<!-- tags: [product, diagram, windows forms, mouse movement, timer, random color, node, polygon] keywords: [diagram1_MouseMove, Node, Polygon, Timer, MouseMove, toolTip1, timer1_Tick, getnodeundermouse, color.FromArgb, fillstyle, random] -->
```