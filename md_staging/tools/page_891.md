```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_891.jpeg
document_name: tools
page_number: 891
page_id: tools#page_891
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:55Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes events related to `BorderStyle` and `ReadOnly` properties in Windows Forms controls.
- Focuses on `BorderStyleChanged` and `ReadOnlyChanged` events.

## Content

### 3.5.8.9.4.4 `BorderStyleChanged`
This event occurs when the `BorderStyle` property is changed. The `BorderStyle` property indicates whether the edit control should have a border.

#### Event Handler Description
The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Code Examples
##### [C#]
```csharp
private void numericUpDownExt1_BorderStyleChanged(object sender, EventArgs e)
{
    Console.WriteLine(" BorderStyleChanged event is raised ");
}
```

##### [VB.NET]
```vb
Private Sub numericUpDownExt1_BorderStyleChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" BorderStyleChanged event is raised ")
End Sub
```

### 3.5.8.9.4.5 `ReadOnlyChanged`
This event occurs when the `ReadOnly` property is changed. The `ReadOnly` property gets / sets a value indicating whether the text can be changed by the use of the up or down buttons only.

#### Event Handler Description
The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Code Examples
##### [C#]
```csharp
private void numericUpDownExt1_ReadOnlyChanged(object sender, EventArgs e)
{
    Console.WriteLine(" ReadOnlyChanged event is raised ");
}
```

##### [VB.NET]
```vb
Private Sub numericUpDownExt1_ReadOnlyChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" ReadOnlyChanged event is raised ")
End Sub
```

## Footer
© 2013 Syncfusion. All rights reserved. 891

<!-- tags: [product, module, control, api, version?] keywords: [winforms, BorderStyleChanged, ReadOnlyChanged, EventArgs, numericUpDownExt1] -->
```