```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_215.jpeg
document_name: diagram
page_number: 215
page_id: diagram#page_215
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:26Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- VertexChanged and VertexChanging events are detailed for handling node vertex changes.
- VertexEventArgs members provide essential properties for handling vertex events programmatically.

## Content

### DocumentEventSink Events
The following table describes the events related to vertex changes:

| DocumentEventSink    | Description                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------|
| VertexChanged        | Gets fired after the vertex of the node has been changed.                                    |
| VertexChanging       | Gets fired when the vertex of the node is changed.                                           |

Data can be retrieved or set using the following members:

| Vertex EventArgs Member | Description                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------|
| Cancel                  | Cancels the Vertex Changed event from being fired.                                           |
| ChangeType              | Returns the following possible value:<br>- **Set** - whether the vertex is set for the node. |
| NodeAffected            | Returns the node's name by which the node was affected.                                       |
| VertexIndex            | Returns the index of the current vertex.                                                       |
| VertexLocation          | Returns the position of the vertex.                                                           |

### Programmatic Event Handling
Programmatically, the events are written as follows:

```csharp
[![C#](https://i.imgur.com/a/CsharpIcon.png)](https://i.imgur.com/a/CsharpIcon.png)

public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model1.EventSink).VertexChanged += new VertexChangedEventHandler(Form1_VertexChanged);
    ((DocumentEventSink)model1.EventSink).VertexChanging += new VertexChangingEventHandler(Form1_VertexChanging);
    LineConnector line = new LineConnector(circle.PinPoint, polygon.PinPoint);
    polygon.CentralPort.TryConnect(line.HeadEndPoint);
    circle.CentralPort.TryConnect(line.TailEndPoint);
    model1.AppendChild(line);
}
```

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Diagram
- **Class**: DocumentEventSink
- **Events**:
  - **VertexChanged**: Triggered after the vertex of a node has been changed.
  - **VertexChanging**: Triggered when the vertex of a node is changed.
- **VertexEventArgs Members**:
  - **Cancel**: Boolean property to cancel the Vertex Changed event.
  - **ChangeType**: Property indicating whether the vertex is set for the node.
  - **NodeAffected**: Property returning the node affected by the vertex change.
  - **VertexIndex**: Property returning the index of the vertex.
  - **VertexLocation**: Property returning the position of the vertex.

## Code Examples

### Example: Handling Vertex Changed and Vertex Changing Events

#### C#
```csharp
[![C#](https://i.imgur.com/a/CsharpIcon.png)](https://i.imgur.com/a/CsharpIcon.png)

public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model1.EventSink).VertexChanged += new VertexChangedEventHandler(Form1_VertexChanged);
    ((DocumentEventSink)model1.EventSink).VertexChanging += new VertexChangingEventHandler(Form1_VertexChanging);
    LineConnector line = new LineConnector(circle.PinPoint, polygon.PinPoint);
    polygon.CentralPort.TryConnect(line.HeadEndPoint);
    circle.CentralPort.TryConnect(line.TailEndPoint);
    model1.AppendChild(line);
}
```

<!-- tags: [Syncfusion, Diagram, Vertex, VertexChangedEventArgs, VertexChanged, VertexChanging, Windows Forms, Events, Programming, C#] keywords: [vertex, diagram, vertexchanged, vertexchanging, documenteventsink, eventsink, eventArgs, csharp] -->
```