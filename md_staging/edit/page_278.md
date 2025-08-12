```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_278.jpeg
document_name: edit
page_number: 278
page_id: edit#page_278
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:36Z
fidelity: lossless
-->

## Content

### Event Overview

- **ClipRectangle**: Gets the rectangle area to paint.
- **Graphics**: Gets the graphics that will be used to paint.

#### Event Code Example

**C\#**
```csharp
private void editControl_PaintUserMargin(object sender, PaintEventArgs e)
{
    Console.WriteLine(" PaintUserMargin event is raised ");
}
```

**VB.NET**
```vb
Private Sub editControl_PaintUserMargin(ByVal sender As Object, ByVal e As PaintEventArgs)
    Console.WriteLine(" PaintUserMargin event is raised ")
End Sub
```

### 4.14.29 WordWrapChanged Event

This event is fired when the value of the **WordWrapMode** property is changed. The **WordWrapMode** property specifies the mode of word wrapping.

The event handler receives an argument of type **EventArgs**.

#### WordWrapChanged Event Handling Example

**C\#**
```csharp
// Handle the WordWrapChanged event.
this.editControl.WordWrapChanged += new EventHandler(editControl_WordWrapChanged);

// Specify the mode of word wrapping.
this.editControl.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin;

private void editControl_WordWrapChanged(object sender, EventArgs e)
{
    // The below line will be displayed in the output window at runtime.
    Console.WriteLine(" WordWrapChanged event is raised ");
}
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Edit.Enums
- **Class**: WordWrapMode
  - **Properties**:
    - **WordWrapMargin**

## Code Examples

### C\#

```csharp
// Adding event handler for WordWrapChanged
this.editControl.WordWrapChanged += new EventHandler(editControl_WordWrapChanged);

// Setting WordWrapMode property
this.editControl.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin;

private void editControl_WordWrapChanged(object sender, EventArgs e)
{
    Console.WriteLine(" WordWrapChanged event is raised ");
}
```

### VB.NET

```vb
' Adding event handler for WordWrapChanged
AddHandler editControl.WordWrapChanged, AddressOf editControl_WordWrapChanged

' Setting WordWrapMode property
editControl.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin

Private Sub editControl_WordWrapChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" WordWrapChanged event is raised ")
End Sub
```

## Tags and Keywords

<!-- tags: [Syncfusion Winforms, editControl, WordWrapChanged, WordWrapMode, event handling, eventargs] keywords: [editControl, WordWrapChanged event, WordWrapMode property, event handler, EventArgs] -->
```