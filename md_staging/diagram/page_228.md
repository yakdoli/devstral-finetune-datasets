```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_228.jpeg
document_name: diagram
page_number: 228
page_id: diagram#page_228
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:40Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates handling events related to ZOrderchanging and ZOrderchanged in Visual Basic.NET.
- Provides sample code for setting event handlers and showing notifications when ZOrder events are triggered.
- Includes a sample diagram illustrating the flow of handling ZOrder changing and checking.

## Content

### Event Handling Example

The following code snippet shows how to handle `ZOrderChanging` and `ZOrderChanged` events in a Windows Forms application using Visual Basic.NET:

```vb
AddHandler DirectCast(model1.EventSink, DocumentEventSink).ZOrderChanged, AddressOf Form1_ZOrderChanged
AddHandler DirectCast(model1.EventSink, DocumentEventSink).ZOrderChanging, AddressOf Form1_ZOrderChanging

diagram1.Controller.BringToFront()
End Sub

Private Sub Form1_ZOrderChanging(ByVal evtArgs As 
ZOrderChangingEventArgs)
    MessageBox.Show(("ZOrderChanging event is fired" & vbCrLf & "Node: ") + 
evtArgs.NodeAffected.Name.ToString())
End Sub

Private Sub Form1_ZOrderChanged(ByVal evtArgs As 
ZOrderChangedEventArgs)
    MessageBox.Show(("ZOrderChanged event is fired" & vbCrLf & "New 
ZOrder: ") + evtArgs.ZOrder.ToString())
End Sub
```

### Sample Diagram

The diagram below illustrates the process flow for handling the `ZOrderChanging` event:

- **START**: The process begins.
- **PROCESS**: The `ZOrderChanging` event is triggered.
- **CHECK**: A notification box shows the event details.
- **END**: The process terminates.

![Sample Diagram](https://via.placeholder.com/600x400?text=Sample+Diagram)

This diagram depicts the sequence of actions from the start to the end of the process, highlighting the point where the `ZOrderChanging` event is fired and the associated notification.

---

## RAG Annotations
<!-- tags: [Windows Forms, Diagram, Events, ZOrderChanging, ZOrderChanged, Visual Basic.NET] keywords: [event handling, event notification, ZOrderChangingEventArgs, ZOrderChangedEventArgs, Windows Forms, Diagram, UI, Syncfusion, VB.NET] -->
```