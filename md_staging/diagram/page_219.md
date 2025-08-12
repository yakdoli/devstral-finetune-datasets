```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_219.jpeg
document_name: diagram
page_number: 219
page_id: diagram#page_219
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:48Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Explanation of PinPointChanged and PinPointChanging events triggered during movements and repositioning of a pinpoint.
- Description of how to retrieve or set data using specific members such as Cancel, NodeAffected, and Offset.

## Content

### Events Triggered during PinPoint Operations
| PinPointChanged | Triggered after the pinpoint is repositioned. |
| PinPointChanging | Triggered when the pinpoint is moved. |

### Data Retrieval and Modification Members
| PinPoint / PinPointOffset EventArgs Member | Description |
|---|---|
| Cancel | Cancels the PinPoint Changing events. |
| NodeAffected | Returns the node's name by which the node was affected. |
| Offset | Returns the X and Y values. |

## Programmatic Implementation of Events

### Code Example in C#
```csharp
[C#]

public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model4.EventSink).PinOffsetChanged += new PinOffsetChangedEventHandler(Form1_PinOffsetChanged);
    ((DocumentEventSink)model4.EventSink).PinOffsetChanging += new PinOffsetChangingEventHandler(Form1_PinOffsetChanging);
    ((DocumentEventSink)model4.EventSink).PinPointChanged += new PinPointChangedEventHandler(Form1_PinPointChanged);
    ((DocumentEventSink)model4.EventSink).PinPointChanging += new PinPointChangingEventHandler(Form1_PinPointChanging);

    // Circle
    Syncfusion.Windows.Forms.Diagram.Elipse circle = new Syncfusion.Windows.Forms.Diagram.Elipse(0, 0, 96, 72);
    circle.Name = "Circle";
    circle.FillStyle.Type = FillStyleType.LinearGradient;
    circle.FillStyle.ForeColor = Color.AliceBlue;
    circle.ShadowStyle.Visible = true;
    model4.AppendChild(circle);
}

void Form1_PinPointChanging(PinPointChangingEventArgs evtArgs)
{
    MessageBox.Show("PinpointChanging event is fired" + "\n" + "Node")
}
```

## API Reference
- **PinOffsetChangedEventHandler**: Triggered after the pinpoint is repositioned.
- **PinOffsetChangingEventHandler**: Triggered when the pinpoint is moved.
- **PinPointChangedEventHandler**: Triggered after the pinpoint is repositioned.
- **PinPointChangingEventHandler**: Triggered when the pinpoint is moved.
- **Cancel**: Cancel the PinPoint Changing events.
- **NodeAffected**: Returns the node's name by which the node was affected.
- **Offset**: Returns the X and Y values for the offset.

### Getting Started Example
In this example, a PinPointChanging event is generated when a node named "Circle" is moved, and a message box is displayed indicating that the event has been fired.

<!-- tags: [diagram, pinpoint changing event, windows forms, c# code example] keywords: [pinpoint, offset, event handler, Syncfusion Winforms, API reference] -->
```