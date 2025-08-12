```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_223.jpeg
document_name: diagram
page_number: 223
page_id: diagram#page_223
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:04Z
fidelity: lossless
 -->

# Essential Diagram for Windows Forms

| NodeAffected                | Returns the node's name by which the node was affected. |
|-----------------------------|------------------------------------------------------------|
| RotationOffset              | Returns the angle by which the node was rotated.         |

## FlipEventArgs Members

| FlipEventArgs Member | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Cancel              | Cancels the FlipChanging event.                                             |
| FlipAxis            | Returns the axis around which the node was rotated.                      |
| FlipValue           | Returns the boolean value of the **Flip** property.                       |
| NodeAffected        | Returns the node's name by which the node was affected.                  |

### Overview

**Scope:** This page explains the handling of flip and rotation events in the Syncfusion diagram control. It introduces events like `FlipChanging`, `FlipChanged`, `RotationChanging`, and `RotationChanged`, and shows how to programmatically attach event handlers to respond to these events.

## Content

The `FlipEventArgs` structure and rotation events are used to manage changes in the orientation of nodes in the diagram. Below is an overview of how these events are typically handled in code.

### Event Handling for Flip and Rotation

#### Event Details

- **FlipChanging**: Triggered before the node is flipped, allowing you to cancel or modify the flip.
- **FlipChanged**: Triggered after the node is flipped.
- **RotationChanging**: Triggered before a node's rotation is changed.
- **RotationChanged**: Triggered after a node's rotation has been changed.

#### Sample Code: Handling Rotation Events

The following example demonstrates how to attach event handlers for `RotationChanged` and `FlipChanged` events in C#:

```csharp
[C#]

public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model1.EventSink).FlipChanged += new FlipChangedEventHandler(Form1_FlipChanged);
    ((DocumentEventSink)model1.EventSink).FlipChanging += new FlipChangingEventHandler(Form1_FlipChanging);
    ((DocumentEventSink)model1.EventSink).RotationChanged += new RotationChangedEventHandler(Form1_RotationChanged);
    ((DocumentEventSink)model1.EventSink).RotationChanging += new RotationChangingEventHandler(Form1_RotationChanging);

    // Circle
    Syncfusion.Windows.Forms.Diagram.Ellipse circle = new Syncfusion.Windows.Forms.Diagram.Ellipse(0, 0, 96, 72);
    circle.Name = "Circle";
    circle.FillStyle.Type = FillStyleType.LinearGradient;
    circle.FillStyle.ForeColor = Color.AliceBlue;
    circle.ShadowStyle.Visible = true;
    model4.AppendChild(circle);
}

void Form1_RotationChanged(RotationChangedEventArgs evtArgs)
{
    MessageBox.Show("RotationChanged event is fired" + "\n" + evtArgs.RotationOffset.ToString());
}
```

### Explanation

- **Adding Event Handlers**: Event handlers are added to the `FlipChanged`, `FlipChanging`, `RotationChanged`, and `RotationChanging` events using a delegate.
- **Creating a Circle Node**: A circle node is created with specified dimensions, filled with a linear gradient, and a shadow style is applied. This node is then appended to the diagram model.
- **Handling Rotation Changes**: The `Form1_RotationChanged` method is triggered when the rotation of the node changes. It displays a message indicating the event firing along with the rotation offset.

## API Reference

### Events

#### RotationChangedEventArgs

- **Properties**
  - **RotationOffset**: Returns the angle by which the node was rotated.
  - **NodeAffected**: Returns the node's name by which the node was affected.

#### FlipEventArgs

- **Properties**
  - **Cancel**: Indicates whether the flip action should be canceled.
  - **FlipAxis**: Indicates the axis around which the node was flipped.
  - **FlipValue**: Indicates the new boolean value of the `Flip` property.
  - **NodeAffected**: Indicates the node's name by which the node was affected.

## Code Examples

### Handling Rotation Events Example

The following example demonstrates programmatic handling of rotation events in a Syncfusion diagram:

```csharp
public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model1.EventSink).RotationChanged += new RotationChangedEventHandler(Form1_RotationChanged);
}

void Form1_RotationChanged(RotationChangedEventArgs evtArgs)
{
    MessageBox.Show("RotationChanged event is fired" + "\n" + evtArgs.RotationOffset.ToString());
}
```

### Handling Flip Events Example

```csharp
public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model1.EventSink).FlipChanging += new FlipChangingEventHandler(Form1_FlipChanging);
}

void Form1_FlipChanging(FlipChangingEventArgs evtArgs)
{
    MessageBox.Show("FlipChanging event is fired");
}
```

## References

- [Syncfusion Diagram API Documentation](https://help.syncfusion.com/windowsforms/diagram/)
- [Syncfusion FlipEventArgs Documentation](https://help.syncfusion.com/windowsforms/diagram/flipargs)

<!-- tags: [syncfusion, winforms, diagram, events, flipargs, rotation, sdk, windowsforms] keywords: [nodeaffected, rotationoffset, flipping, rotationevents, rotationoffsetevents, flipargs, cancel] -->
```
