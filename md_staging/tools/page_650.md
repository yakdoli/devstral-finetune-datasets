```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_650.jpeg
document_name: tools
page_number: 650
page_id: tools#page_650
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:20Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Properties

| Property       | Description                                                                 |
|-----------------|------------------------------------------------------------------------------|
| BorderStyle     | `BorderStyle` property is set to `FixedSingle`.                           |
| BorderSides    | Specifies the sides of the control which should have a border.           |

### Using Border Styles in C#

```csharp
// Sets the 3D border style
this.gradientPanel1.BorderStyle =
    System.Windows.Forms.BorderStyle.FixedSingle;
this.gradientPanel1.Border3DStyle =
    System.Windows.Forms.Border3DStyle.Etched;

// Sets the 2D Border style
this.gradientPanel1.BorderColor = System.Drawing.Color.Blue;
this.gradientPanel1.BorderSingle =
    System.Windows.Forms.ButtonBorderStyle.Dashed;
this.gradientPanel1.BorderSides =
    System.Windows.Forms.Border3DSide.All;
```

### Using Border Styles in VB.NET

```vb
' Sets the 3D border style
Me.gradientPanel1.BorderStyle =
    System.Windows.Forms.BorderStyle.FixedSingle
Me.gradientPanel1.Border3DStyle =
    System.Windows.Forms.Border3DStyle.Etched
Me.gradientPanel1.BorderColor = System.Drawing.Color.Blue

' Sets the 2D Border style
Me.gradientPanel1.BorderSingle =
    System.Windows.Forms.ButtonBorderStyle.Dashed
Me.gradientPanel1.BorderSides = System.Windows.Forms.Border3DSide.All
```

### Visual Representation

![Border3DStyle = "Etched"](https://<image_url_here>)
*Figure 399: Border3DStyle = "Etched"*

## References

- **API Reference**: `System.Windows.Forms.BorderStyle`, `System.Windows.Forms.Border3DStyle`, `System.Windows.Forms.BorderSingle`, `System.Windows.Forms.BorderSides`
- **Related Concepts**: 2D and 3D border styles, gradient panels

## Code Examples

### C# Example

```csharp
// Setting Border Styles in C#
this.gradientPanel1.BorderStyle = BorderStyle.FixedSingle;
this.gradientPanel1.Border3DStyle = Border3DStyle.Etched;
this.gradientPanel1.BorderColor = Color.Blue;
this.gradientPanel1.BorderSingle = ButtonBorderStyle.Dashed;
this.gradientPanel1.BorderSides = Border3DSide.All;
```

### VB.NET Example

```vb
' Setting Border Styles in VB.NET
Me.gradientPanel1.BorderStyle = BorderStyle.FixedSingle
Me.gradientPanel1.Border3DStyle = Border3DStyle.Etched
Me.gradientPanel1.BorderColor = Color.Blue
Me.gradientPanel1.BorderSingle = ButtonBorderStyle.Dashed
Me.gradientPanel1.BorderSides = Border3DSide.All
```

### HTML Output

```html
<!-- Embedding the Border Styles directly into an HTML document -->
<code>
    this.gradientPanel1.BorderStyle = BorderStyle.FixedSingle;
    this.gradientPanel1.Border3DStyle = Border3DStyle.Etched;
    this.gradientPanel1.BorderColor = Color.Blue;
    this.gradientPanel1.BorderSingle = ButtonBorderStyle.Dashed;
    this.gradientPanel1.BorderSides = Border3DSide.All;
</code>
```

### Notes on Usage

- The `Border3DStyle` property defines the 3D effect of the border.
- The `BorderSingle` property specifies the style of the border if it is drawn as a 2D line.
- The `BorderSides` property determines which sides of the control will display a border when the `BorderStyle` is set to `FixedSingle`.

## Additional Information

- **Syncfusion Documentation**: For more detailed information on implementing border styles in Windows Forms, refer to the [Syncfusion Documentation](https://www.syncfusion.com/documentation/windows-forms/).

<!-- tags: [Syncfusion, Windows Forms, Border Styles, Gradient Panel, Border3DStyle, BorderSingle] keywords: [Border Styles, BorderSides, FixedSingle, Etched, Dashed] -->
```