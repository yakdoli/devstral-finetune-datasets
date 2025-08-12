```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_238.jpeg
document_name: diagram
page_number: 238
page_id: diagram#page_238
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:22Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Describes the Label/Layers EventArgs member functions and their purpose.
- Explains the Label Events and their triggers.
- Provides examples for handling LabelChanged events programmatically in both C# and VB.

## Content

### Label / Layers EventArgs Member

The following table describes the members of the Label/Layers EventArgs and their functionalities:

| Label / Layers EventArgs Member | Description |
| --- | --- |
| **Cancel** | Cancels the LabelChanging event. |
| **ChangeType** | It returns the following possible values: <br> - Insert: Whether the label is inserted <br> - Remove: Whether the label is removed |
| **Element** | Returns whether the head or tail end is moved. |
| **Elements** | Returns the elements collection on which the event occurs. |
| **Index** | Returns the zero-based index into the collection on which the event occurred. |
| **Owner** | Returns the owner object. |

### Label Events

**Whenever labels are added to the label collection, this event will be triggered.**

#### Handling Label Events Programmatically

##### C#

```csharp
public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model1.EventSink).LabelsChanged += new CollectionExEventHandler(Form1_LabelsChanged);
}

void Form1_LabelsChanged(CollectionExEventArgs evtArgs)
{
    MessageBox.Show("LabelsChanged event is fired" + evtArgs.ChangeType.ToString() + evtArgs.Owner.ToString());
}
```

##### VB

```vb
Public Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(model1.EventSink, DocumentEventSink).LabelsChanged, AddressOf Form1_LabelsChanged
End Sub
```

### Conclusion

This section outlines the procedures to handle label events in a Windows Forms application using Syncfusion WinForms controls, providing both C# and VB examples for clarity.

---

## Page-level Navigation/TOC (if applicable)
- [Label / Layers EventArgs Members](#label-layers-eventargs-members)
- [Label Events](#label-events)
- [Programming Label Events in C#](#programming-label-events-in-csharp)
- [Programming Label Events in VB](#programming-label-events-in-vb)

## Cross References
- See also: Event Handling, Diagram Controls, Windows Forms Integration.

## RAG Annotations
<!-- tags: [WinForms, Diagram, Events, Controls] keywords: [LabelChanging, Insert, Remove, Element, EventSink, LabelEvent] -->
```