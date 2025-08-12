```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_862.jpeg
document_name: tools
page_number: 862
page_id: tools#page_862
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to handle events for customizing border styles and colors in masked edit boxes within Syncfusion WinForms.
- Demonstrates code samples in both C# and VB.NET for handling border-related events.
- Provides examples for `BorderStyleChanged`, `BorderColorChanged`, and `BorderSidesChanged` events.

## Content

### 3.5.8.8.4.2 BorderColorChanged
This event occurs when the `BorderColor` property is changed. The `BorderColor` property indicates the color of the 2D border.

#### Event Handler Details
The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Code Example
**[C#]**
```csharp
private void maskedEditBox1_BorderColorChanged(object sender, EventArgs e)
{
    Console.WriteLine("BorderColorChanged event is raised ");
}
```

**[VB.NET]**
```vb
Private Sub maskedEditBox1_BorderColorChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("BorderColorChanged event is raised ")
End Sub
```

### 3.5.8.8.4.3 BorderSidesChanged
This event occurs when the `BorderSides` property is changed. The `BorderSides` property indicates the border sides of the panel.

#### Event Handler Details
The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Code Example
**[C#]**
```csharp
private void maskedEditBox1_BorderSidesChanged(object sender, EventArgs e)
{
}
```

## Page-level Navigation/TOC (if applicable)
- No additional local TOC present on this page.

## Cross References
See also:
- Documentation for `Syncfusion.Windows.Forms.Tools.MaskedEditBox` control.
- Event handling and customization in Syncfusion WinForms.

## RAG Annotations
<!-- tags: [syncfusion, winforms, maskededitbox, events, border, color, sides, event handling] keywords: [BorderColorChanged, BorderSidesChanged, Border3DStyleChanged, Events, MaskedEditBox, BorderColor, BorderSides] -->
```