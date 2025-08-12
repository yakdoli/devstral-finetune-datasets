```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_989.jpeg
document_name: tools
page_number: 989
page_id: tools#page_989
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:46:34Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses background settings for `RadioButtonAdv`.
- Explains how to apply gradient backgrounds using specific properties.
- Provides examples in C# and VB.NET.

## Content

### 3.5.11.2.3.5 Background Settings

The background settings of the `RadioButtonAdv` are discussed below.

The `RadioButtonAdv` can be provided with a gradient background using the properties given below.

| `RadioButtonAdv` Properties | Description |
| --- | --- |
| BackgroundStyle | Sets the background style of the <br> `RadioButtonAdv`. <br><br> The options included are as follows. <br> `HorizontalGradient`, <br> `VerticalGradient` and <br> `Default`. |
| GradientStart | Sets the start color of the gradient of the <br> background of the `RadioButtonAdv`. |
| GradientEnd | Sets the end color of the gradient of the <br> background of the `RadioButtonAdv`. |

#### Code Examples

```csharp
// C#
this.radioButtonAdv1.BackgroundStyle = 
    Syncfusion.Windows.Forms.Tools.CheckBoxAdvBackStyle.HorizontalGradient;
this.radioButtonAdv1.GradientStart = System.Drawing.Color.LightBlue;
this.radioButtonAdv1.GradientEnd = System.Drawing.Color.DarkSalmon;
```

```vb
' VB.NET
```

## API Reference

### Properties
- `BackgroundStyle`: Gets or sets the background style of the `RadioButtonAdv`.
- `GradientStart`: Gets or sets the start color of the gradient of the background of the `RadioButtonAdv`.
- `GradientEnd`: Gets or sets the end color of the gradient of the background of the `RadioButtonAdv`.

## See Also
- Text Settings, `RadioButtonAdv` Settings

## Cross References
- Essential Tools for Windows Forms

## Page-level Navigation/TOC
- 3.5.11.2.3.5 Background Settings
  - `RadioButtonAdv` Properties and Description
  - Code Examples

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, RadioButtonAdv, background settings, gradient background, C#, VB.NET] -->
```