```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_220.jpeg
document_name: diagram
page_number: 220
page_id: diagram#page_220
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:57Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This page explains how to handle events related to pinpoints and offsets in a WinForms Diagram component using C# and VB.NET code samples.

## Code Examples

### C# Example

```csharp
name: " + evtArgs.NodeAffected.Name.ToString() + "\n" +
    " };

void Form1_PinPointChanged(PinPointChangedEventArgs evtArgs)
{
    MessageBox.Show("PinPointChanged event is fired" + "\n" + "Offset values: " + evtArgs.Offset.ToString());
}

void Form1_PinOffsetChanging(PinOffsetChangingEventArgs evtArgs)
{
    MessageBox.Show("PinOffsetChanging event is fired" + "\n" + "Node name: " + evtArgs.NodeAffected.Name);
}

void Form1_PinOffsetChanged(PinOffsetChangedEventArgs evtArgs)
{
    MessageBox.Show("PinOffsetChanged event is fired" + "\n" + "Offset values: " + evtArgs.Offset.ToString());
}
```

### VB.NET Example

```vb
[VB]

Public Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(model4.EventSink, DocumentEventSink).PinOffsetChanged, AddressOf Form1_PinOffsetChanged
    AddHandler DirectCast(model4.EventSink, DocumentEventSink).PinOffsetChanging, AddressOf Form1_PinOffsetChanging
    AddHandler DirectCast(model4.EventSink, DocumentEventSink).PinPointChanged, AddressOf Form1_PinPointChanged
    AddHandler DirectCast(model4.EventSink, DocumentEventSink).PinPointChanging, AddressOf Form1_PinPointChanging

    ' Circle
    Dim circle As New Syncfusion.Windows.Forms.Diagram.Ellipse(0, 0, 96, 72)
    circle.Name = "Circle"
    circle.FillStyle.Type = FillStyleType.LinearGradient
    circle.FillStyle.ForeColor = Color.AliceBlue
    circle.ShadowStyle.Visible = True
    model4.AppendChild(circle)
End Sub

Private Sub Form1_PinPointChanging(ByVal evtArgs As PinPointChangingEventArgs)
    MessageBox.Show("PinPointChanging event is fired" & vbCrLf & "Node
```

## Page-level Navigation/TOC (if applicable)
- This page includes sections for C# and VB.NET code examples related to handling events in WinForms Diagrams.

### Cross References
- This page provides examples and event handling for the Diagram control, showing how to use it in both C# and VB.NET environments.

<!-- tags: [Syncfusion, WinForms, Diagram, Events, C#, VB.NET] keywords: [WinForms, Diagram, PinPoint, Offset, EventHandling, C#, VB.NET] -->
```