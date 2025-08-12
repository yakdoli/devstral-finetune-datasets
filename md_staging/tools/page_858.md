```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_858.jpeg
document_name: tools
page_number: 858
page_id: tools#page_858
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:25Z
fidelity: lossless
-->

## Border Properties in Windows Forms

### Overview
- Describes the properties related to the border of a control in Windows Forms, including color, sides, style, and appearance.
- Implements examples in both C# and VB.NET for configuring these properties.

### Content

| Property           | Description                                                                 |
|--------------------|------------------------------------------------------------------------------|
| **BorderColor**    | Specifies the color of the 2D border.                                      |
| **BorderSides**    | Indicates the border sides of the panel. The options included are as follows:<br>- Left,<br>- Top,<br>- Right,<br>- Bottom,<br>- Middle and<br>- All. |
| **BorderStyle**    | Indicates whether the edit control should have a border. The options included are given below:<br>- FixedSingle,<br>- Fixed3D and<br>- None. |

#### Example Code: C#

```csharp
this.maskedTextBox1.Border3DStyle = System.Windows.Forms.Border3DStyle.Bump;
this.maskedTextBox1.BorderColor = System.Drawing.Color.Lime;
this.maskedTextBox1.BorderSides = System.Windows.Forms.Border3DSide.All;
this.maskedTextBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
```

#### Example Code: VB.NET

```vb
Me.maskedTextBox1.Border3DStyle = System.Windows.Forms.Border3DStyle.Bump
Me.maskedTextBox1.BorderColor = System.Drawing.Color.Magenta
Me.maskedTextBox1.BorderSides = System.Windows.Forms.Border3DSide.All
Me.maskedTextBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
```

## API Reference

### Properties

- **BorderColor**: Indicates the color of the 2D border.  
- **BorderSides**: Indicates which sides of the border are displayed. Options include Left, Top, Right, Bottom, Middle, and All.  
- **BorderStyle**: Indicates the style of the border. Options include FixedSingle, Fixed3D, and None.

### Parameters

| Name              | Type                                         | Description                                     |
|-------------------|----------------------------------------------|-------------------------------------------------|
| **Color**         | `System.Drawing.Color`                      | The color of the border.                        |
| **BorderSides**   | `System.Windows.Forms.Border3DSide`         | Enumerates the sides of the panel to display.   |
| **BorderStyle**   | `System.Windows.Forms.BorderStyle`          | Enumerates the style of the border.             |

### Returns

None.

## Code Examples

The above sections provide examples in both C# and VB.NET for configuring the border properties of a control.

## RAG Annotations

<!-- tags: [Windows Forms, Border Properties, BorderStyle] keywords: [BorderColor, BorderSides, FixedSingle, Fixed3D, None, C#, VB.NET] -->
```