```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_230.jpeg
document_name: diagram
page_number: 230
page_id: diagram#page_230
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:22:39Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Data can be retrieved or set using specific members outlined in this documentation.
- Focuses on handling EventArgs for Connection and Port events in Diagram controls.
- Includes programmatic examples for managing connection events in C# and VB.

## Content

### Connection and Port Event Args Members

The following table describes the members used for retrieving or setting data:

| Connection and Port Event Args Member | Description |
|--------------------------------------|-------------|
| **Cancel**                           | Cancels the `ConnectionChanging` event.                            |
| **ChangeType**                       | Returns the following possible values:<br>- **Insert**: Whether the node is inserted<br>- **Remove**: Whether the node is removed |
| **Element**                          | Returns whether the head or tail end is moved.                     |
| **Elements**                         | Returns the elements collection on which the event occurs.         |
| **Index**                            | Returns the zero-based index into the collection on which the event occurred. |
| **Owner**                            | Returns the owner object. This is a read-only boolean value.        |

### Connection Events

#### Programmatic Handling of Connection Events

**Description**  
Programmatically, the Connection Event is handled as follows:

```csharp
[C#]
public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)modell.EventSink).ConnectionsChanged += new CollectionExEventHandler(Form1_ConnectionsChanged);
    LineConnector line = new LineConnector(circle.PinPoint, polygon.PinPoint);
    polygon.CentralPort.TryConnect(line.HeadEndPoint);
    circle.CentralPort.TryConnect(line.TailEndPoint);
    modell.AppendChild(line);
}
void Form1_ConnectionsChanged(CollectionExEventArgs evtArgs)
{
    MessageBox.Show(evtArgs.ChangeType.ToString());
}
```

```vb
[VB]
```

## API Reference

### Members
The `ConnectionChanging` event and `CollectionExEventArgs` are key components in handling events for Diagram controls. The `ChangeType` member provides information about the type of change (insert or remove) to the node in the collection.

### Parameters
- **evtArgs**: The event arguments object of type `CollectionExEventArgs`, which contains information about the event, such as the `ChangeType`.

## Code Examples

### Example in C#
The following example demonstrates how to handle the `ConnectionsChanged` event and display the type of change in a message box:

```csharp
[C#]
public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)modell.EventSink).ConnectionsChanged += new CollectionExEventHandler(Form1_ConnectionsChanged);
    LineConnector line = new LineConnector(circle.PinPoint, polygon.PinPoint);
    polygon.CentralPort.TryConnect(line.HeadEndPoint);
    circle.CentralPort.TryConnect(line.TailEndPoint);
    modell.AppendChild(line);
}
void Form1_ConnectionsChanged(CollectionExEventArgs evtArgs)
{
    MessageBox.Show(evtArgs.ChangeType.ToString());
}
```

## Tags and Keywords
<!-- tags: [Syncfusion, WinForms, Diagram control, ConnectionEvents, CollectionExEventArgs, ChangeType, EventArgs, ConnectionChanging, LineConnector] keywords: [diagram, connection, event, eventargs, change, insert, remove, node, collection, onboarded, boolean] -->
```