```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_657.jpeg
document_name: tools
page_number: 657
page_id: tools#page_657
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:45Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```csharp
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.PathEllipse, 
    New System.Drawing.Color() { 
    System.Drawing.Color.Bisque, System.Drawing.Color.LightSalmon, 
    System.Drawing.Color.LightCoral})

'button1
Private button1 As Button = New Button()
Private button1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
Private button1.Text = "Button"

'hostPrimitive1
Private hostPrimitive1 As HostPrimitive = New HostPrimitive()
Private hostPrimitive1.HostControl = button1

'progressBarAdv1
Private progressBarAdv1 As ProgressBarAdv = New ProgressBarAdv()
Private progressBarAdv1.ProgressStyle = 
    Syncfusion.Windows.Forms.Tools.ProgressBarStyles.Tube

'textPrimitive1
Private textPrimitive1 As TextPrimitive = New TextPrimitive()
Private textPrimitive1.Alignment = 
    Syncfusion.Windows.Forms.Tools.Alignment.Bottom
Private textPrimitive1.Text = "ProgressbarAdv"

'textPrimitive2
Private textPrimitive2 As TextPrimitive = New TextPrimitive()
Private textPrimitive2.Text = "Windows Forms Button"

'Adding Primitives
gpe.Primitives.AddRange(New Syncfusion.Windows.Forms.Tools.Primitive() 
    {hostPrimitive, hostPrimitive2, textPrimitive1, 
    textPrimitive2})
```

5. Run and build the application to view the output.

### 3.5.6.3.3 Concepts and Features

A few important aspects of the GradientPanelExt have been discussed in this section.

#### 3.5.6.3.3.1 Primitives

One of the most sophisticated features provided by the GradientPanelExt is its ability to include primitives in the borders.

The primitives that can be included in the GradientPanelExt are,

---

© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [windows forms, gradient panel ext, primitives, tools, syncfusion winforms] keywords: [gradient style, path ellipse, button, flat style, progress bar, text primitive, run and build, output view, sophisticated features, primitives in borders] -->
```