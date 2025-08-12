```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_419.jpeg
document_name: chart
page_number: 419
page_id: chart#page_419
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:20Z
fidelity: lossless
-->

## Overview
- Provides examples of configuring 3D chart settings in Syncfusion Winforms.
- Demonstrates setting title and rotation attributes for a 3D chart control.
- Offers code snippets in C# and VB.NET for enabling Real3D mode in charts.

## Content

### Title and Rotation
The chart is configured to display in 3D with a specified depth, tilt, and rotation.

```csharp
Me.chartControl1.Tilt = 55F
Me.chartControl1.Rotation = 60
```

![Illustrates 3D Settings](charts_settings_image)

*Figure 269: 3-D Chart control with Depth = "55f", Tilt = "55f", Rotation = "60"*

### Real 3D Mode sample

#### C#
```csharp
this.chartControl1.ChartArea.Series3D = true;
this.chartControl1.Tilt = 0;
this.chartControl1.Depth = 150;
this.chartControl1.Rotation = 10;
this.chartControl1.RealMode3D = true;
```

#### VB.NET
```vb
Me.chartControl1.ChartArea.Series3D = True
Me.chartControl1.Tilt = 0
Me.chartControl1.Depth = 150
Me.chartControl1.Rotation = 10
Me.chartControl1.RealMode3D = True
```

## API Reference

### Chart Control Properties
- **Series3D**: Enables or disables the 3D series rendering.
- **Tilt**: Sets the tilt angle of the 3D chart.
- **Depth**: Specifies the depth of the chart slices.
- **Rotation**: Sets the rotation of the chart around the Y-axis.
- **RealMode3D**: Activates real 3D mode for rendering.

## Code Examples

### Example: Setting Up a 3D Chart in C#
```csharp
// Enable 3D series
this.chartControl1.ChartArea.Series3D = true;

// Configure tilt and depth
this.chartControl1.Tilt = 60;
this.chartControl1.Depth = 150;

// Set rotation and enable real 3D mode
this.chartControl1.Rotation = 10;
this.chartControl1.RealMode3D = true;
```

### Example: Setting Up a 3D Chart in VB.NET
```vb
' Enable 3D series
Me.chartControl1.ChartArea.Series3D = True

' Configure tilt and depth
Me.chartControl1.Tilt = 60
Me.chartControl1.Depth = 150

' Set rotation and enable real 3D mode
Me.chartControl1.Rotation = 10
Me.chartControl1.RealMode3D = True
```

## Cross References

- **Related Documentation**: Chart Control in Syncfusion Winforms.
- **API Reference**: Detailed API documentation for Syncfusion.Windows.Forms.Tools.ChartControl.

<!-- tags: [syncfusion, winforms, chart, 3D, real mode, rotation, tilt, depth] keywords: [chartControl1, Series3D, Tilt, Depth, Rotation, RealMode3D, C#, VB.NET] -->
```