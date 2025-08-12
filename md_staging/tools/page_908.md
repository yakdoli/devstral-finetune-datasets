```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_908.jpeg
document_name: tools
page_number: 908
page_id: tools#page_908
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:58Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the event handling for changes in Border3DStyle, BorderColor, and BorderSides properties.
- Demonstrates handling changes in the appearance of a control's border.

## Content

### Border3DStyleChanged

#### C#
```csharp
private void textBoxExt1_Border3DStyleChanged(object sender, EventArgs e)
{
    Console.WriteLine(" Border3DStyleChanged event is raised ");
}
```

#### VB.NET
```vb
Private Sub textBoxExt1_Border3DStyleChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" Border3DStyleChanged event is raised ")
End Sub
```

#### Description
This event occurs when the `Border3DStyle` property is changed. The `Border3DStyle` property indicates the style of the 3D border.

---

### BorderColorChanged

#### C#
```csharp
private void textBoxExt1_BorderColorChanged(object sender, EventArgs e)
{
    Console.WriteLine(" BorderColorChanged event is raised ");
}
```

#### VB.NET
```vb
Private Sub textBoxExt1_BorderColorChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" BorderColorChanged event is raised ")
End Sub
```

#### Description
This event occurs when the `BorderColor` property is changed. The `BorderColor` property indicates the color of the 2D border. The event handler receives an argument of type `EventArgs` containing data related to this event.

---

### BorderSidesChanged

#### Description
This event occurs when the `BorderSides` property is changed. The `BorderSides` property indicates the border sides of the panel.

## Footer
© 2013 Syncfusion. All rights reserved.
```