```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_056.jpeg
document_name: HTMLUI
page_number: 056
page_id: HTMLUI#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:55Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates bubbling event architecture in HTMLUI.
- Provides an example of button click event handling.
- Includes a sample code snippet for handling mouse events on HTML elements.

## Content

### 4.4.1 HTMLUI Bubbling Events Sample

This sample demonstrates the implementation of Bubbling Event architecture in HTMLUI.

```vb
If Not elem Is Nothing AndAlso TypeOf elem Is IHTMLElementImpl Then
    If elem.ID = "button1" Then
        Me.label1.Text = "Mouse just left Button 1"
    ElseIf elem.ID = "button2" Then
        Me.label1.Text = "Mouse just left Button 2"
    End If
End If
End Sub
```

#### Figure: HTMLUIBubblingEvents Sample
The image below shows the interface for the HTMLUI Bubbling Events Sample:

![HTMLUIBubblingEvents Sample](image_path)

**Description:**
- The sample interface displays several buttons.
- The right section shows the event output when a button is clicked.
- A checkbox option includes the mouse leave event.

**Figure 25: HTMLUIBubblingEvents Sample**

By default, this sample can be found under the following location:

```
C:\Documents and Settings\username\My Documents.Syncfusion\EssentialStudio\Version 
Number\Windows\HTMLUI.Windows\Samples\2.0\HTMLUI Events\HTMLUIBubblelingEvents
```

## API Reference

- **Namespace:** Syncfusion.Winforms
- **Event Handling:** Supports bubbling event architecture for HTML elements.

## Code Examples

The provided VB code snippet illustrates how to handle mouse events on HTML elements:

```vb
If Not elem Is Nothing AndAlso TypeOf elem Is IHTMLElementImpl Then
    If elem.ID = "button1" Then
        Me.label1.Text = "Mouse just left Button 1"
    ElseIf elem.ID = "button2" Then
        Me.label1.Text = "Mouse just left Button 2"
    End If
End If
End Sub
```

## Page-level Navigation/TOC
- [Overview]
- [Content]
  - [4.4.1 HTMLUI Bubbling Events Sample]
    - [Figure: HTMLUIBubblingEvents Sample]
    - [Sample Location and Description]

## Cross References
- Refer to the Syncfusion Winforms documentation for more details on event handling in HTMLUI.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, HTMLUI, Events, Bubbling, Sample, Mouse Events] keywords: [HTMLUIEvent, BubblingEvents, EventHandling, Fig.25, SampleLocation, ButtonClick, MouseLeaveEvent] -->
```