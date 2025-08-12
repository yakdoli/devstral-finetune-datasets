```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_231.jpeg
document_name: diagram
page_number: 231
page_id: diagram#page_231
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:50Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates the use of Events in Windows Forms with Syncfusion Diagram components.
- Includes connection event handling to monitor changes in connections.
- Explains Ports Events and their use cases.

## Content

### Event Handling in Diagrams

Below is the VB.NET code snippet defining event handling for connection changes in a Windows Forms application:

```vb
Public Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(model1.EventSink, DocumentEventSink).ConnectionsChanged, AddressOf Form1_ConnectionsChanged
        Dim line As New LineConnector(circle.PinPoint, polygon.PinPoint)
        polygon.CentralPort.TryConnect(line.HeadEndPoint)
        circle.CentralPort.TryConnect(line.TailEndPoint)
        model1.AppendChild(line)
End Sub

Private Sub Form1_ConnectionsChanged(ByVal evtArgs As CollectionExEventArgs)
    MessageBox.Show(evtArgs.ChangeType.ToString())
End Sub
```

### Sample Diagram

The sample diagram visualizes the connection event functionality:

![Connection Changed Event](attachment:Connection_Changed_Event.png)

**Figure 144: Connection Changed Event**

### Ports Events

This section introduces Ports Events, which will be detailed further in the upcoming content.

## API Reference

### Connected Properties
- `ConnectionsChanged`: Event triggered when the connection status changes.
- `EventSink`: Interface for handling various events within the model.

### Methods
- `TryConnect`: Attempts to connect the specified endpoints.
- `AppendChild`: Adds the specified child to the model.

### CollectionExEventArgs
- `ChangeType`: Indicates the type of change that occurred in the connection.

## Code Examples

The provided code shows how to:
- Listen for connection changes using `ConnectionsChanged` event.
- Connect elements via ports using `TryConnect`.
- Handle changes by displaying a message box with details about the change type.

## Page-level Navigation/TOC

- **Overview**: Provides a brief summary of the page's content.
- **Content**: Detailed explanation and sample code.
- **API Reference**: Lists relevant events, properties, and methods.
- **Ports Events**: Brief introduction to Ports Events.

## Cross References

See also:
- Related sections on handling events in Syncfusion Diagram components.
- Detailed documentation on `ConnectionsChanged` and `EventSink`.

<!-- tags: [syncfusion, windows forms, diagram, events, ports events, version 11.4.0.26] keywords: [connection changes, event handling, line connector, collectionexeventargs, connectionschanged event, ports events, tryconnect] -->
```