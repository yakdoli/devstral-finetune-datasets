```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_198.jpeg
document_name: tools
page_number: 198
page_id: tools#page_198
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:27:49Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to use `dockingManager1` to convert a control into an MDI child window and back to a docked window.

## Content

### Handling MDI Child Form Transitions

The following code shows how to transform a control (listBox1) into an MDI child form and revert it back to a docked window using buttons.

```vb
''' Overloaded
Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles button1.Click
    ' Sets the panel as a child form for the MDI form
    Me.dockingManager1.SetAsMDIChild(listBox1, True, New Rectangle(200, 400, 500, 300))
End Sub

Private Sub button2_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles button2.Click
    ' Sets the MDI child form to the normal Docking window.
    Me.dockingManager1.SetAsMDIChild(listBox1, True, New Rectangle(200, 400, 500, 300))
End Sub
```

#### Instructions to Run the Application
1. Run the application.
2. Click the buttons to see the respective transitions.

### Visual Representation

The following figure illustrates the transition of a docked window into an MDI child window.

![](https://example.com/image.png)  
*Figure 99: Docked Window transformed into MDI Child Window*  
  

## API Reference

### `SetAsMDIChild`
- **Namespace:** `Syncfusion.Windows.Forms.Tools`
- **Parameters:**
  - Control to convert
  - Boolean indicating if the control should be converted to an MDI child
  - Position and size of the MDI child window

### Code Examples

```vb
Me.dockingManager1.SetAsMDIChild(listBox1, True, New Rectangle(200, 400, 500, 300))
```

## RAG Annotations
<!-- tags: [syncfusion , windows forms, mdi child, docked window] keywords: [SetAsMDIChild, DockingManager, MDIChild, DockedWindow, Windows Forms, Windows Forms MDI, Syncfusion Tools] -->
```