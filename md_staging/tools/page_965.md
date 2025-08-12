<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_965.jpeg
document_name: tools
page_number: 965
page_id: tools#page_965
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:03Z
fidelity: lossless
-->

## Overview

- Provides a detailed explanation of the `CheckBoxAdv` control properties, focusing on background styles and gradient settings.
- Includes C# and VB.NET code examples for applying gradient backgrounds.
- Notes limitations and conditions under which gradient backgrounds are applicable.
- Describes border settings, including 3D border styles.

## Content

### Background Settings

The following code snippet demonstrates how to set a horizontal gradient background for a `CheckBoxAdv` control using both C# and VB.NET.

#### C#

```csharp
Syncfusion.Windows.Forms.Tools.CheckBoxAdvBackStyle.HorizanGradient;
this.checkBoxAdv1.GradientStart = System.Drawing.Color.Aqua;
this.checkBoxAdv1.GradientEnd = System.Drawing.Color.Magenta;
```

#### VB.NET

```vb
Me.checkBoxAdv1.BackgroundStyle = 
Syncfusion.Windows.Forms.Tools.CheckBoxAdvBackStyle.HorizanGradient
Me.checkBoxAdv1.GradientStart = System.Drawing.Color.Aqua
Me.checkBoxAdv1.GradientEnd = System.Drawing.Color.Magenta
```

The resulting gradient background is displayed as shown in Figure 621:

![Gradient Background Displayed](image621.png)
**Figure 621: Gradient Background Displayed**

#### Note: 
Gradient background cannot be applied to the `CheckBoxAdv` when its `BackgroundStyle` property is set to 'Default'. Additionally, the background image cannot be displayed with gradient settings.

A sample demonstrating the background settings of `CheckBoxAdv` is available at the following path:

```
..My Documents\Syncfusion\EssentialStudio\Version
Number\Windows\Tools.Windows\Samples\2.0\Editors Package\OptionControls
```

### Border Settings

Color and Styles can be applied to the border of the `CheckBoxAdv` as discussed below.

#### CheckBoxAdv Properties and Description

| CheckBoxAdv Properties   | Description                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------|
| Border3DStyle            | Indicates the style of the 3D border. The options included are as follows:                      |
|                          | RaisedOuter,                                                                                       |
|                          | SunkenOuter,                                                                                       |
|                          | RaisedInner,                                                                                       |
|                          | SunkenInner,                                                                                       |
|                          | Raised,                                                                                            |

## API Reference

### Properties

- **Border3DStyle**: Indicates the style of the 3D border. The available options include:

  - **RaisedOuter**
  - **SunkenOuter**
  - **RaisedInner**
  - **SunkenInner**
  - **Raised**

## Code Examples

The provided code examples show how to set gradient backgrounds for a `CheckBoxAdv` control in both C# and VB.NET.

### See also

- [CheckBoxAdv Control Overview](#checkboxadv-control-overview)
- [Advanced Styling Options](#advanced-styling-options)

## Page-level Navigation

- Background Settings
- Border Settings
- Sample Path for Background Settings

### Related Topics

- **Control Properties**: Detailed documentation on all properties available for the `CheckBoxAdv` control.
- **Customization**: Instructions on customizing the appearance and behavior of the `CheckBoxAdv` control.

<!-- tags: [syncfusion, winforms, checkboxadv, gradient, border, background, control properties, customization] keywords: [syncfusion, winforms, checkboxadv, gradient background, border3dstyle, raisedouter, sunkenouter, raisedinner, sunkeninner, raised, backgroundstyle, default style, gradient settings, sample path] -->