```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_646.jpeg
document_name: tools
page_number: 646
page_id: tools#page_646
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![Figure 395: PatternStyle Gradient Panel Created Programmatically](https://example.com/path/to/image.png)
**Figure 395: PatternStyle Gradient Panel Created Programmatically**

## See Also

- [Concepts and Features](#concepts-and-features)

### Concepts and Features

This section will take you in detail about the concepts and features available for the gradient panel and guides you to customize the control using the features available.

#### GradientPanel Appearance

The background of the GradientPanel can be customized using the below properties.

| GradientPanel Properties    | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| BackColor                   | Background color used to display the text and graphics in the control.     |
| BackgroundColor             | Sets a gradient style background for the control.                          |

### Code Examples

#### [C#]

```csharp
this.gradientPanel1.BackColor = System.Drawing.Color.LightCoral;
this.gradientPanel1.BackColor = new
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.PathRectangle, System.Drawing.Color.AliceBlue, System.Drawing.Color.SteelBlue);
```

#### [VB.NET]

```vb
this.gradientPanel1.BackColor = System.Drawing.Color.LightCoral
this.gradientPanel1.BackColor = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.PathRectangle, System.Drawing.Color.AliceBlue, System.Drawing.Color.SteelBlue)
```

---

© 2013 Syncfusion. All rights reserved.
```