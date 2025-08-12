```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_235.jpeg
document_name: diagram
page_number: 235
page_id: diagram#page_235
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:22:07Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- **Purpose**: Demonstrates handling property changed and property changing events in a Windows Forms application.
- **Key Components**:
  - `PropertyChanging` event handling in VB.NET.
  - Event triggering and value updates in a diagram.

## Content

### Sample Code

**PropertyChanging Event Handling (VB.NET)**

```vb
Public Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(model1.EventSink, DocumentEventSink).PropertyChanged, AddressOf Form1_PropertyChanged
    AddHandler DirectCast(model1.EventSink, DocumentEventSink).PropertyChanging, AddressOf Form1_PropertyChanging
End Sub

Private Sub Form1_PropertyChanged(ByVal evtArgs As Syncfusion.Windows.Forms.Diagram.PropertyChangedEventArgs)
    MessageBox.Show(("PropertyChanged event is fired" & vbLf & "Property Name: ") + evtArgs.PropertyName)
End Sub

Private Sub Form1_PropertyChanging(ByVal eprop As Syncfusion.Windows.Forms.Diagram.PropertyChangingEventArgs)
    MessageBox.Show((("PropertyChanging event is fired" & vbLf & "Property Name: ") + eprop.PropertyName & vbLf & "new " & vbTab & vbTab & vbTab & vbTab & "Value: ") + eprop.NewValue)
End Sub
```

### Sample Diagrams

**Sample diagrams are as follows.**

## Page-level Navigation/TOC (if applicable)
- Essential Diagram for Windows Forms
  - Overview
  - Content
    - Sample Code
    - Sample Diagrams

## Cross References
- **Related Topics**:
  - Diagram Events and Handling
  - Event Sinks in Diagrams

## RAG Annotations
<!-- tags: [windows forms, events, property changed, property changing, vb.net, diagram, syncfusion] keywords: [propertychangingeventargs, eventchanging, eventhandlers] -->
```