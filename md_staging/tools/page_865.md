```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_865.jpeg
document_name: tools
page_number: 865
page_id: tools#page_865
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:50Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes key event properties and handling for Windows Forms controls.
- Focuses on the MaskCustomValidate and MaskSatisfied events for masked input processing.

## Content

### Event Properties

| Property               | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Accepted               | Indicates whether the event has been handled and no further processing should happen. |
| CurrentCharacter       | Returns the current character.                                              |
| CurrentIndex           | Returns the current position. It will be a valid mask position.            |
| CurrentMaskCharacter    | Returns the current mask character.                                        |
| Handled                | Indicates whether the event has been handled and no further processing should happen. |

### Code Examples

#### MaskCustomValidate

[C#]
```csharp
private void maskedEditBox1_MaskCustomValidate(object sender, Syncfusion.Windows.Forms.Tools.MaskCustomValidateArgs e)
{
    Console.WriteLine(" MaskCustomValidate event is raised ");
}
```

[VB.NET]
```vb
Private Sub maskedEditBox1_MaskCustomValidate(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Tools.MaskCustomValidateArgs)
    Console.WriteLine(" MaskCustomValidate event is raised ")
End Sub
```

### Event Handler for MaskSatisfied

#### 3.5.8.8.4.8 MaskSatisfied

This event is raised when the required fields in a mask have been satisfied after new text has been entered / the text changes.

The event handler receives an argument of type `EventArgs` containing data related to this event.

[C#]
```csharp
private void maskedEditBox1_MaskSatisfied(object sender, EventArgs e)
{
    Console.WriteLine(" MaskSatisfied event is raised ");
}
```

## RAG Annotations
<!-- tags: [Windows Forms, Syncfusion Winforms, Masked Input, Event Handling, Version 11.4.0.26] keywords: [MaskCustomValidate, MaskSatisfied, Event Arguments, Masked Input] -->
```