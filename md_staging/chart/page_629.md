<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_629.jpeg
document_name: chart
page_number: 629
page_id: chart#page_629
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:54:11Z
fidelity: lossless
-->

## Chart Appearance Customization

### Overview
- Explains how to customize the appearance of a chart by enabling gradient effects.
- Demonstrates the difference between a flat and gradient chart look.

### Content

#### Setting a Flat Look

**Figure 376: Chart with Flat Look and Feel**

To achieve a flat look, no specific settings are needed, as this is the default appearance.

#### Enabling Gradient Appearance

To enable the gradient appearance, set the `ChartControl.Model.ColorModel.AllowGradient` property to `true`.

##### C#

```csharp
// Sets the Gradient look and feel.
this.chartControl1.Model.ColorModel.AllowGradient = true;
```

##### VB.NET

```vb
' Sets the Gradient look and feel.
Me.chartControl1.Model.ColorModel.AllowGradient = True
```

### Explanation

By default, the `AllowGradient` property is set to `false`, resulting in a flat appearance. Setting it to `true` adds gradient effects to the chart elements, enhancing their visual appeal.

### API Reference

#### Properties
- `AllowGradient`: A boolean property that controls whether the chart elements should have a gradient appearance.
  - **Type**: Boolean
  - **Default**: `false`
  - **Description**: When set to `true`, the chart elements will display with a gradient effect.

### Code Examples

The examples above demonstrate how to enable gradient effects in both C# and VB.NET. This property can be set programmatically to achieve the desired visual style.

### See also
- Other chart customization options in the documentation.

<!-- tags: [Syncfusion, WinForms, Chart, Appearance, Gradient, Flat] keywords: [chart appearance, gradient effect, flat look, AllowGradient, customization, C#, VB.NET] -->