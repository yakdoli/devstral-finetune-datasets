```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_665.jpeg
document_name: tools
page_number: 665
page_id: tools#page_665
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:15Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Learn how to include Any .NET Windows Forms control as a primitive in the GradientPanelExt.
- Discover the process of collapsing and expanding options using the HostControl property.
- Explore examples in both C# and VB.NET for implementing HostPrimitives.

## Content

### 3.5.6.3.3.1.3 Host Primitives

#### Explanation
Any .NET Windows Forms control or custom control can be included as a primitive in the `GradientPanelExt`. The host control should be referred to in the `HostControl` property of the GradientPanelExt Collection Editor.

#### Code Examples

##### C# Example

```csharp
[C#]

//button1
Button button1 = new Button();
button1.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
button1.Text = "Button";

//hostPrimitive1
HostPrimitive hostPrimitive1 = new HostPrimitive();
hostPrimitive1.BackColor = System.Drawing.Color.Transparent;
hostPrimitive1.HostControl = button1;
hostPrimitive1.Size = new System.Drawing.Size(60, 20);

//progressBarAdv1
ProgressBarAdv progressBarAdv1 = new ProgressBarAdv();
progressBarAdv1.BackColor = System.Drawing.Color.Transparent;
progressBarAdv1.ProgressStyle = Syncfusion.Windows.Forms.Tools.ProgressBarStyles.Tube;
progressBarAdv1.TubeStartColor = System.Drawing.Color.FromArgb(((int)((byte)(255))), 
                                                             ((int)((byte)(192))), 
                                                             ((int)   (((byte)(192)))));

//hostPrimitive2
HostPrimitive hostPrimitive2 = new HostPrimitive();
hostPrimitive2.Alignment = Syncfusion.Windows.Forms.Tools.Alignment.Bottom;
hostPrimitive2.BackColor = System.Drawing.Color.Transparent;
hostPrimitive2.HostControl = progressBarAdv1;
hostPrimitive2.Position = 200;
hostPrimitive2.Size = new System.Drawing.Size(100, 20);

//Adding Primitives
gpe.Primitives.AddRange(new Syncfusion.Windows.Forms.Tools.Primitive []
{
    hostPrimitive1,
    hostPrimitive2});
```

##### VB.NET Example

```vb
[VB.NET]
```

## API Reference

### HostPrimitive Class
- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **HostControl Property**: Specifies the control to be hosted.
- **Alignment Property**: Defines the alignment of the hosted control within the primitive.

### ProgressBarAdv Class
- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **ProgressStyle Property**: Defines the style of the progress bar.

## Code Examples (continued)

##### C# Example (continued)
The example demonstrates how to include a `System.Windows.Forms.Button` and a `Syncfusion.Windows.Forms.Tools.ProgressBarAdv` as primitives in a `GradientPanelExt`. The `HostPrimitive` objects are configured with transparent background colors and appropriate sizes and positions.

##### VB.NET Example (to be filled in based on equivalent C# code)

## Related Topics
- **3.5.6.3.3.1.2 Expand Options**
- **3.5.6.3.3.1.4 Collapse Options**

<!-- tags: [winforms, syncfusion, gradienteclipsext, primitives, hostcontrol, button, progressbar, alignment] keywords: [hostprimitive, progressbaradv, style, transparent, expand, collapse, gradientpanelext] -->
```
