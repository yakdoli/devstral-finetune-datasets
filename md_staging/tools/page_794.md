```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_794.jpeg
document_name: tools
page_number: 794
page_id: tools#page_794
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Event Handling in Windows Forms

#### BorderStyle Changed Event

**Description:**
- **Event Name:** BorderStyleChanged
- **Trigger:** This event occurs when the `BorderStyle` property is changed.
- **Purpose:** The `BorderStyle` property indicates whether the edit control should have a border.

**Event Handler:**
- The event handler receives an argument of type `EventArgs` containing data related to this event.

##### C# Implementation

```csharp
private void percentTextBox1_BorderStyleChanged(object sender, EventArgs e)
{
    Console.WriteLine("BorderStyleChanged event is raised ");
}
```

##### VB.NET Implementation

```vb
Private Sub percentTextBox1_BorderStyleChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("BorderStyleChanged event is raised ")
End Sub
```

#### ClipTextChanged Event

**Description:**
- **Event Name:** ClipTextChanged
- **Trigger:** This event occurs when the `ClipText` property is changed.
- **Purpose:** The `ClipText` property returns the clipped text without the formatting.

**Event Handler:**
- The event handler receives an argument of type `EventArgs` containing data related to this event.

##### C# Implementation

```csharp
private void percentTextBox1_ClipTextChanged(object sender, EventArgs e)
{
    Console.WriteLine("ClipTextChanged event is raised ");
}
```

##### VB.NET Implementation

```vb
Private Sub percentTextBox1_ClipTextChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("ClipTextChanged event is raised ")
End Sub
```

## Page-level Navigation/TOC (if applicable)

- **3.5.8.5.4.6 BorderStyleChanged**
- **3.5.8.5.4.7 ClipTextChanged**

## Footer

**Copyright Notice:**
© 2013 Syncfusion. All rights reserved.

**Page Information:**
Page 794 | tools#page_794

<!-- tags: [Syncfusion Winforms, Event Handling, BorderStyleChanged, ClipTextChanged, EventHandler, C#, VB.NET] -->
```