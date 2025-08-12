```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_210.jpeg
document_name: diagram
page_number: 210
page_id: diagram#page_210
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:27Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```vb
MessageBox.Show("Node count =" & vbLf) + 
nodeStack.Count.ToString()

textBox1.Text = model4.Nodes.Last.Name

Me.diagram1.HScroll = True
Me.diagram1.VScroll = True
End Sub

Private Sub Form1_OriginChanged(ByVal e As ViewOriginEventArgs)

    textBox1.Text = ((("X = " & e.OriginalOrigin.X & "," & "Y = ") + 
    e.OriginalOrigin.Y & " " & "New X = ") + e.NewOrigin.X & "," & "New " & 
vbTab & "Y = ") + e.NewOrigin.Y
End Sub
```

## Overview
- Demonstrates how to handle node count display and manage scroll settings in a Windows Forms diagram.
- Includes event handling for detecting changes in the diagram's origin.

## Content

### Diagram Handling in Windows Forms

This section provides code examples and explanations for managing diagrams in Windows Forms applications.

- **Node Count Display**: Displays the number of nodes in the diagram using a message box.
- **Text Box Update**: Updates a text box with the name of the last node in the diagram.
- **Scroll Configuration**: Enables horizontal and vertical scrolling for the diagram.
- **Origin Change Event Handling**: Captures and displays changes in the diagram's origin coordinates in a text box.

### Sample Diagram

Figure 130 demonstrates the initial stage of a simple flow diagram within the Windows Forms interface.

#### Figure 130: Origin Initial Stage

![Sample Diagram](https://i.imgur.com/diagram_image.png)

This figure illustrates a basic flow of a diagram starting from "START," proceeding through a "PROCESS," and evaluating a "CHECK." It also includes a text box displaying origin coordinates, showcasing the OriginChanged event in action.

### Detailed Explanation

- **MessageBox Invocation**: Displays the node count in the diagram.
- **TextBox Updates**: Dynamically updates the text box with the latest node name.
- **Scrolling Enablement**: Ensures the diagram can be scrolled both horizontally and vertically.
- **Event-driven Updates**: The `OriginChanged` event is used to reflect changes in the diagram's position.

## API Reference

### Properties
- **HScroll (Diagram)**: Enables horizontal scrolling for the diagram control.
- **VScroll (Diagram)**: Enables vertical scrolling for the diagram control.

### Methods
- **MessageBox.Show(String)**: Displays a message box with the specified content.
- **Name Property (Node)**: Retrieves the name of the node.

## Code Examples

### C# Example

```csharp
private void OnDiagramOriginChanged(object sender, ViewOriginEventArgs e)
{
    textBox1.Text = string.Format("X={0}, Y={1} | New X={2}, New Y={3}",
        e.OriginalOrigin.X, e.OriginalOrigin.Y, e.NewOrigin.X, e.NewOrigin.Y);
}

private void DisplayNodeCount()
{
    MessageBox.Show("Node count = " + nodeStack.Count);
}

private void EnableScrolling()
{
    diagram1.HScroll = true;
    diagram1.VScroll = true;
}
```

### VB.NET Example

```vb
Private Sub Form1_OriginChanged(ByVal e As ViewOriginEventArgs)
    textBox1.Text = ((("X = " & e.OriginalOrigin.X & "," & "Y = ") + 
        e.OriginalOrigin.Y & "  " & "New X= ") + e.NewOrigin.X & "," & "New " & 
        vbTab & "Y= ") + e.NewOrigin.Y
End Sub

Private Sub DisplayNodeCount()
    MessageBox.Show("Node count =" & vbLf) + nodeStack.Count.ToString()
End Sub

Private Sub EnableScrolling()
    diagram1.HScroll = True
    diagram1.VScroll = True
End Sub
```

## See also
- [Syncfusion Diagram Properties](#diagram-properties)
- [Event Handling in Windows Forms](#event-handling)

<!-- tags: [winforms, diagram, node count, scroll settings, origin changes, event handling] keywords: [node count, horizontal scroll, vertical scroll, origin, event handler, windows forms, diagram control] -->
```