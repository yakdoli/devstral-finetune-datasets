```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_242.jpeg
document_name: chart
page_number: 242
page_id: chart#page_242
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:47Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Properties Summary

Here is a summary of some essential properties concerning chart configurations:

### Properties Table

| Property                      | Description                     |
|-------------------------------|---------------------------------|
| **2D / 3D Limitations**      | No                              |
| **Applies to Chart Element** | All series                      |
| **Applies to Chart Types**   | Pie Chart                       |

### Sample Code

The following sample code demonstrates how to apply custom gradient styles to pie charts.

#### C#

```csharp
series.ConfigItems.PieItem.PieType = ChartPieType.Custom;
ColorBlend clrblnd = new ColorBlend();
clrblnd.Positions = new float[] { 0f, 0.05f, 1f };
clrblnd.Colors = new Color[] { Color.SteelBlue, Color.LightSteelBlue, Color.AliceBlue };
// Specifying Gradient Style
series.ConfigItems.PieItem.Gradient = clrblnd;
```

#### VB.NET

```vb
series.ConfigItems.PieItem.PieType = ChartPieType.Custom
Private clrblnd As ColorBlend = New ColorBlend()
clrblnd.Positions = New Single() { 0f, 0.05f, 1f }
clrblnd.Colors = New Color() { Color.SteelBlue, Color.LightSteelBlue, Color.AliceBlue }
' Specifying Gradient Style
series.ConfigItems.PieItem.Gradient = clrblnd
```

## API Reference

### Pie Chart Gradient Customization

The `ChartPieType` property allows specifying the type of pie chart, with `Custom` as one of the available options. The `Gradient` property of the `PieItem` object accepts a `ColorBlend` object, which defines the gradient styles to be applied.

#### Parameters

- **clrblnd**: A `ColorBlend` object that contains:
  - **Positions**: An array of `float` values specifying the relative positions in the gradient.
  - **Colors**: An array of `Color` objects specifying the colors for the gradient.

## Code Examples

### C# Example

This example shows how to apply a custom gradient to a pie chart using the Syncfusion library.

```csharp
// Configuring the pie chart type to custom
series.ConfigItems.PieItem.PieType = ChartPieType.Custom;

// Creating a ColorBlend object
ColorBlend clrblnd = new ColorBlend();

// Setting gradient positions
clrblnd.Positions = new float[] { 0f, 0.05f, 1f };

// Setting gradient colors
clrblnd.Colors = new Color[] { Color.SteelBlue, Color.LightSteelBlue, Color.AliceBlue };

// Applying the gradient to the pie chart
series.ConfigItems.PieItem.Gradient = clrblnd;
```

### VB.NET Example

This example demonstrates the equivalent setup in VB.NET.

```vb
' Configuring the pie chart type to custom
series.ConfigItems.PieItem.PieType = ChartPieType.Custom

' Creating a ColorBlend object
Private clrblnd As ColorBlend = New ColorBlend()

' Setting gradient positions
clrblnd.Positions = New Single() { 0f, 0.05f, 1f }

' Setting gradient colors
clrblnd.Colors = New Color() { Color.SteelBlue, Color.LightSteelBlue, Color.AliceBlue }

' Applying the gradient to the pie chart
series.ConfigItems.PieItem.Gradient = clrblnd
```

<!-- tags: [windows forms, pie chart, gradient, chart properties, Syncfusion, C#, VB.NET] keywords: [chartpieType, ColorBlend, gradients, pie charts, vb.net, csharp] -->
```