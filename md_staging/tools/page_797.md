```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_797.jpeg
document_name: tools
page_number: 797
page_id: tools#page_797
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:36Z
fidelity: lossless
-->

## Overview
- This section discusses the handling of several events related to minimum and maximum size changes, as well as multiline changes for controls in Windows Forms. These events occur when specific properties of the control are modified, such as MinimumSize, MaximumSize, or Multiline.

## Content

### MinimumSizeChanged

**Description:**
This event occurs when the MinimumSize property is changed. The MinimumSize property defines the smallest possible dimensions of the control.

**Code Example (VB.NET):**
```vb.net
Private Sub percentTextBox1_MinimumSizeChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" MinimumSizeChanged event is raised ")
End Sub
```

**Code Example (C#):**
```csharp
private void percentTextBox1_MinimumSizeChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MinimumSizeChanged event is raised ");
}
```

### MaximumSizeChanged

**Description:**
This event occurs when the MaximumSize property is changed. The MaximumSize property defines the largest possible dimensions of the control.

**The event handler receives an argument of type EventArgs containing data related to this event.**

**Code Example (C#):**
```csharp
private void percentTextBox1_MaximumSizeChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MaximumSizeChanged event is raised ");
}
```

**Code Example (VB.NET):**
```vb.net
Private Sub percentTextBox1_MaximumSizeChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" MaximumSizeChanged event is raised ")
End Sub
```

### MultilineChanged

**Description:**
This event occurs when the Multiline property is changed. The Multiline property controls whether the text of the edit control can span more than one line.

**The event handler receives an argument of type EventArgs containing data related to this event.**

**Code Example (C#):**
```csharp
private void percentTextBox1_MultilineChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MultilineChanged event is raised ");
}
```

### Conclusion
- The MinimumSizeChanged, MaximumSizeChanged, and MultilineChanged events provide a way to monitor and respond to changes in control properties related to size and text formatting.

---

## Page-level Navigation/TOC (if applicable)
- 3.5.8.5.4.12  `MaximumSizeChanged`
- 3.5.8.5.4.13  `MultilineChanged`

## Cross References
- Refer to related sections or controls for additional details on managing events and properties in Syncfusion WinForms.

## RAG Annotations
<!-- tags: [Windows Forms, MinimumSize, MaximumSize, Multiline, Event Handling] keywords: [MinimumSizeChanged, MaximumSizeChanged, MultilineChanged, Syncfusion WinForms] -->
```