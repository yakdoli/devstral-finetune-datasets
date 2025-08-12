```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_798.jpeg
document_name: tools
page_number: 798
page_id: tools#page_798
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:31Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Overview of event handling related to text properties in Windows Forms.
- Focus on handling `MultilineChanged`, `ReadOnlyChanged`, and `RightToLeftChanged` events for edit controls.

## Content

### MultilineChanged Event

The `MultilineChanged` event occurs when the `Multiline` property of a control is changed. The `Multiline` property determines whether the text control can display multiple lines of text or not.

#### Event Handler Example

**[C#]**
```csharp
private void percentTextBox1_MultilineChanged(object sender, EventArgs e)
{
    Console.WriteLine("MultilineChanged event is raised ");
}
```

**[VB.NET]**
```vb
Private Sub percentTextBox1_MultilineChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("MultilineChanged event is raised ")
End Sub
```

### ReadOnlyChanged Event
This event occurs when the `ReadOnly` property is changed. The `ReadOnly` property controls whether the text in the edit control can be changed or not.

#### Event Handler Example

**[C#]**
```csharp
private void percentTextBox1_ReadOnlyChanged(object sender, EventArgs e)
{
    Console.WriteLine("ReadOnlyChanged event is raised ");
}
```

**[VB.NET]**
```vb
Private Sub percentTextBox1_ReadOnlyChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("ReadOnlyChanged event is raised ")
End Sub
```

### RightToLeftChanged Event
This event occurs when the `RightToLeft` property is changed. The `RightToLeft` property indicates whether the components should be drawn right-to-left for RTL languages.

#### Event Handler Example

**[C#]**
```csharp
private void percentTextBox1_RightToLeftChanged(object sender, EventArgs e)
{
}
```

---

### Footer

© 2013 Syncfusion. All rights reserved. 
798 | Page

<!-- tags: [windowsforms, event handling, syncfusion] keywords: [MultilineChanged, ReadOnlyChanged, RightToLeftChanged, property changes, edit controls, text properties] -->
```