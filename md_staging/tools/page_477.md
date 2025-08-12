```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_477.jpeg
document_name: tools
page_number: 477
page_id: tools#page_477
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:56Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

DateTimePickerAdv control can have custom back color and background images using the properties discussed in this section.

## Background Color

The control's back color can be set using the below properties.

| DateTimePickerAdv Properties | Description |
| --- | --- |
| BackColor | Sets the back color for the DateTimePickerAdv control. |
| BackgroundColor | Sets Solid, Gradient, or Pattern style of background for the control. This property setting will override the BackColor property setting. |

```csharp
[C#]

this.dateTimePickerAdv1.BackColor = System.Drawing.Color.Cornsilk;
this.dateTimePickerAdv1.BackColor = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.Linen, System.Drawing.Color.BurlyWood);
```

```vbnet
[VB.NET]

Me.dateTimePickerAdv1.BackColor = System.Drawing.Color.Cornsilk
Me.dateTimePickerAdv1.BackColor = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.Linen, System.Drawing.Color.BurlyWood)
```

![Gradient Background for DateTimePicker](attachment:figure_275.png)

**Figure 275: Gradient Background for DateTimePicker**

## Background Image

Background image for the DateTimePickerAdv is set using the below property.

| DateTimePickerAdv Properties | Description |
| --- | --- |
| BackgroundImage | Sets the background image for the control. |
| BackgroundImageLayout | Sets the background image layout for the |

<!-- tags: [product, module, control, api, version] keywords: [DateTimePickerAdv, back color, background color, solid, gradient, pattern, background image, background image layout, WinForms, Syncfusion] -->
```