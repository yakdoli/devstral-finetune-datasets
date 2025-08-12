```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_990.jpeg
document_name: tools
page_number: 990
page_id: tools#page_990
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:47:04Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Me.radioButtonAdv1.BackgroundStyle =
Syncfusion.Windows.Forms.Tools.CheckBoxAdvBackStyle.HorizontalGradient
Me.radioButtonAdv1.GradientStart = System.Drawing.Color.LightBlue
Me.radioButtonAdv1.GradientEnd = System.Drawing.Color.DarkSalmon
```

![Gradient Background Displayed](image.png)

Figure 639: Gradient Background Displayed

**Note:** Gradient background cannot be applied to the `RadioButtonAdv` when its `BackgroundStyle` property is set to `'Default'`. Also, the background image cannot be displayed with gradient settings.

A sample which demonstrates the Background Settings of `RadioButtonAdv` is available in the below sample installation path:

```
..My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Tools.Windows\Samples\2.0\Editors Package\OptionControls
```

### 3.5.11.2.3.6 Border Settings

Color and Styles can be applied to the border of the `RadioButtonAdv` as discussed below.

| RadioButtonAdv Properties | Description |
|---------------------------|-------------|
| Border3DStyle            | Indicates the style of the 3D border. The options included are as follows:<br><br>- RaisedOuter<br>- SunkenOuter<br>- RaisedInner<br>- SunkenInner<br>- Raised<br>- Etched<br>- Bump<br>- Sunken<br>- Adjust and<br>- Flat. |

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **Class**: `RadioButtonAdv`
- **Properties**:
  - `BackgroundStyle`: Specifies the background style for the `RadioButtonAdv`.
  - `GradientStart`: Specifies the starting color of the background gradient.
  - `GradientEnd`: Specifies the ending color of the background gradient.
  - `Border3DStyle`: Specifies the 3D border style for the `RadioButtonAdv`.

## Code Examples

```csharp
// Configuring the gradient background
Me.radioButtonAdv1.BackgroundStyle = Syncfusion.Windows.Forms.Tools.CheckBoxAdvBackStyle.HorizontalGradient;
Me.radioButtonAdv1.GradientStart = System.Drawing.Color.LightBlue;
Me.radioButtonAdv1.GradientEnd = System.Drawing.Color.DarkSalmon;

// Configuring the border style
Me.radioButtonAdv1.Border3DStyle = Border3DStyle.RaisedOuter;
```

## Cross References

See also: [Sample Installation Path for RadioButtonAdv](../My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Tools.Windows\Samples\2.0\Editors Package\OptionControls)

<!-- tags: [Syncfusion Winforms, RadioButtonAdv, BackgroundStyle, Gradient, Border3DStyle, DesignTime, RuntimeFeatures, Version11.4.0.26] keywords: [radioButtonAdv, backgroundstyle, gradientstart, gradientend, border3dstyle, horizontalgradient, raisedouter, sunkenouter, raisedinner, sunkeninner, raised, etched, bump, sunken, adjust, flat] -->
```