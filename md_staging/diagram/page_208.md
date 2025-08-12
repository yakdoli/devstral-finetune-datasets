```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_208.jpeg
document_name: diagram
page_number: 208
page_id: diagram#page_208
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:12Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Describes the usage of `OriginChangedEventArgs` to track changes in the origin point in Windows Forms.
- Demonstrates handling the `OriginChanged` event and extracting details such as new origin, offset, and original origin.
- Includes a sample code to illustrate adding event handling for origin changes and adding graphical elements like circles and polygons.

## Content

### WinForms-specific Conventions

The following code example demonstrates adding event handling for the `OriginChanged` event in a Windows Forms application using the Syncfusion library. The event handler updates a text box to display the new and original origin coordinates, as well as the offset between these points.

#### Event Arguments Member Table

| Origin EventArgs Member      | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| **NewOrigin**                | Returns the new X and Y origin values after moving the origin.            |
| **Offset**                   | Returns the difference between the old and new origin.                      |
| **OriginalOrigin**           | Returns the X and Y values before moving the origin.                       |

#### Sample Code

In the following code sample, when the `OriginChanged` event is handled, the various member values are listed in a text box as the control is scrolled accordingly.

```csharp
[C#]

public void Form1_Load(object sender, EventArgs e)
{
    ((DiagramViewerEventSink)diagram1.EventSink).OriginChanged += new ViewOriginEventHandler(Form1_OriginChanged);
    NodeCollection nodeStack = new NodeCollection();

    // Circle

    Syncfusion.Windows.Forms.Diagram.Ellipse circle = new Syncfusion.Windows.Forms.Diagram.Ellipse(0, 0, 96, 72);
    circle.Name = "Circle";
    circle.FillStyle.Type = FillStyleType.LinearGradient;
    circle.FillStyle.ForeColor = Color.AliceBlue;
    circle.ShadowStyle.Visible = true;
    nodeStack.Add(circle);

    // Polygon

    Point[] pts = { new Point(6, 36), new Point(48, 6), new Point(90, 36), new Point(48, 66) };
    Polygon polygon = new Polygon(pts);
    polygon.Name = "Polygon";
    polygon.FillStyle.ForeColor = Color.DarkSeaGreen;
    polygon.FillStyle.Color = Color.DarkSeaGreen;
    nodeStack.Add(polygon);

    int i = 0;
    this.model4.AppendChildren(nodeStack, out i);
    MessageBox.Show("Node count = " + "\n" +
}
```

## API Reference

### Events
- **OriginChanged**: Triggered when the origin of the diagram changes.

### Member Variables
- **NewOrigin**: Represents the new X and Y coordinates after the origin is moved.
- **Offset**: Represents the difference between the old and new origin.
- **OriginalOrigin**: Represents the X and Y coordinates before the origin is moved.

## Cross References
- Refer to the Syncfusion documentation for further details on diagram controls and their properties.

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, Diagram, OriginChangedEventArgs, EventHandling, OriginChanged, NewOrigin, Offset, OriginalOrigin] keywords: [diagram event args, event handling in WinForms, OriginChangedEventArgs, OriginChanged event, NewOrigin, Offset, OriginalOrigin, sample code, Syncfusion Windows Forms, graphical elements, ellipse, polygon] -->
```