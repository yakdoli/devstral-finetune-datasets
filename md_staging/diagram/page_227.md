```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_227.jpeg
document_name: diagram
page_number: 227
page_id: diagram#page_227
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:33Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Describes how data can be retrieved and set using specific members.
- Details the functionality of ZOrder EventArgs members and their descriptions.
- Provides examples of how to handle ZOrderChanging and ZOrderChanged events programmatically in C# and VB.

## Content

Data can be retrieved / set by using the following members.

### ZOrder EventArgs Members

| ZOrder EventArgs Members | Description |
|---------------------------|-------------|
| **Cancel**               | Cancels the ZOrderChanging event. |
| **ChangeType**           | It returns the following possible values: <br> • Front—whether the controller brings the node to the front <br> • Back—whether the controller sends the node to the back |
| **NodeAffected**         | Returns the node's name by which the node was affected. |
| **ZOrder**               | Returns the current zorder value. |

### Handling Events Programmatically

Programmatically, the events are written as follows:

#### C#

```csharp
[C#]

public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model1.EventSink).ZOrderChanged
        += new ZOrderChangedEventHandler(Form1_ZOrderChanged);
    ((DocumentEventSink)model1.EventSink).ZOrderChanging
        += new ZOrderChangingEventHandler(Form1_ZOrderChanging);

    diagram1.Controller.BringToFront();
}

void Form1_ZOrderChanging(ZOrderChangingEventArgs evtArgs)
{
    MessageBox.Show("ZOrderChanging event is fired" +
        "\n" + "Node: " + evtArgs.NodeAffected.Name.ToString());
}

void Form1_ZOrderChanged(ZOrderChangedEventArgs evtArgs)
{
    MessageBox.Show("ZOrderChanged event is fired" +
        "\n" + "New ZOrder: " + evtArgs.ZOrder.ToString());
}
```

#### VB

```vb
[VB]

Public Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
```

## API Reference

### Members

- **Cancel**
  - **Description**: Cancels the ZOrderChanging event.
- **ChangeType**
  - **Description**: Determines whether the node is brought to the front or sent to the back.
- **NodeAffected**
  - **Description**: Identifies the affected node.
- **ZOrder**
  - **Description**: Retrieves the current zorder value.

## Code Examples

The provided examples demonstrate how to handle ZOrderChanging and ZOrderChanged events, allowing users to interact with and respond to changes in the z-order of nodes within the diagram.

## Cross References

See also:
- Documentation on handling event handlers in Windows Forms.
- Additional details on working with nodes and their properties in the Diagram control.

<!-- tags: [Syncfusion, WinForms, Diagram, ZOrder, EventArgs, Event Handling, C#, VB] -->
<!-- keywords: [ZOrderEventArgs, EventSink, ZOrderChanging, ZOrderChanged, BringToFront, NodeAffected, ChangeType, Cancel, MessageBox, documentation, event handler, Diagram control] -->
```