```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_994.jpeg
document_name: tools
page_number: 994
page_id: tools#page_994
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:47:21Z
fidelity: lossless
-->

### Essential Tools for Windows Forms

```csharp
Me.radioButtonAdv1.DisabledImage = 
(CType(Resources.GetObject("checkBoxAdv1.DisabledImage"), 
System.Drawing.Image))
Me.radioButtonAdv1.StretchImage = False
```

![Figure: Image displayed for Checked State of RadioButtonAdv](https://i.imgur.com/4444.png)
*Figure 642: Image displayed for Checked State of RadioButtonAdv*

### Images displayed during Mouse Hover

Images can also be set when the mouse is hovered over the RadioButtonAdv control.

| **RadioButtonAdv Properties**          | **Description**                                                |
|----------------------------------------|----------------------------------------------------------------|
| MouseOverCheckedImage                  | Gets / sets the image used to draw the RadioButton when checked and mouse over. |
| MouseOverUncheckedImage                | Gets / sets the image used to draw the RadioButton when unchecked and mouse over. |

### [C#]

```csharp
this.radioButtonAdv1.MouseOverCheckedImage =
((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.MouseOverCheckedImage")));
this.radioButtonAdv1.MouseOverUncheckedImage =
((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.MouseOverUncheckedImage")));
```

### [VB.NET]

```vb
Me.checkBoxAdv1.MouseOverCheckedImage =
(CType(Resources.GetObject("checkBoxAdv1.MouseOverCheckedImage"), 
System.Drawing.Image))
Me.checkBoxAdv1.MouseOverUncheckedImage =
(CType(Resources.GetObject("checkBoxAdv1.MouseOverUncheckedImage"), 
System.Drawing.Image))
```

![Figure: RadioButtonAdv Hover Image](https://i.imgur.com/5555.png)

*© 2013 Syncfusion. All rights reserved.*
*994 | Page*
```