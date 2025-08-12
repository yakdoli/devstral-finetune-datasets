```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_883.jpeg
document_name: tools
page_number: 883
page_id: tools#page_883
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

### BorderStyle

This property indicates whether the edit control should have a border. The options are:

- FixedSingle
- Fixed3D
- None

## Code Examples

### C#

```csharp
this.numericUpDownExt1.Border3DStyle = System.Windows.Forms.Border3DStyle.Etched;
this.numericUpDownExt1.BorderColor = System.Drawing.Color.Crimson;
this.numericUpDownExt1.BorderSides = System.Windows.Forms.Border3DSide.All;
this.numericUpDownExt1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
```

### VB.NET

```vb
Me.numericUpDownExt1.Border3DStyle = System.Windows.Forms.Border3DStyle.Etched
Me.numericUpDownExt1.BorderColor = System.Drawing.Color.Crimson
Me.numericUpDownExt1.BorderSides = System.Windows.Forms.Border3DSide.All
Me.numericUpDownExt1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
```

### PercentTextBox with Border Set

![PercentTextBox with Border Set](attachment:image)

Figure 559: PercentTextBox with Border Set

### Displaying a Themed Border

We can display a themed border around the `NumericUpDownExt` control. This can be done using the `ThemedBorder` property.

## NumericUpDownExt Property

| Property        | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| ThemedBorder    | Specifies whether or not you want a themed border around the control when themes are enabled. |

## References

See also:
- `Syncfusion.Windows.Forms.Tools.NumericUpDownExt`
- `Border3DStyle`
- `BorderColor`
- `BorderSides`
- `BorderStyle`

### Legal Notice

© 2013 Syncfusion. All rights reserved.
Page 883 |
```