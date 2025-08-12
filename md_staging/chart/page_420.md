```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_420.jpeg
document_name: chart
page_number: 420
page_id: chart#page_420
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:32Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- 3D Chart settings and rotation features explained.
- How to enable mouse rotation for 3D charts in Windows Forms.
- Code examples for configuring the `RealMode3D` and `EnableMouseRotation` properties in both C# and VB.NET.

## Content

### 3D Chart Settings

Figure 270 depicts a 3D chart in a 3-D plane with the following configurations:
- **Tilt:** "0"
- **Depth:** "150"
- **Rotation:** "10"

![Illustrates 3D Settings](https://example.com/image_url/Illustrates_3D_Settings.png)

*Figure 270: 3D Chart in a 3-D plane with Tilt = "0"; Depth = "150"; Rotation = "10"*

### Rotating Chart

#### Enabling Chart Rotation

The end-users can be allowed to rotate the chart at run-time using the mouse (middle or right mouse button) by setting the `EnableMouseRotation` property to `true`.

#### Note

Rotation will not be possible with the LEFT-MOUSE button by enabling this property.

#### Code Examples

- **C#**
  ```csharp
  this.chartControl1RealMode3D = true;
  this.chartControl1.EnableMouseRotation = true;
  ```

- **VB.NET**
  ```vb
  Me.chartControl1.RealMode3D = True
  Me.chartControl1.EnableMouseRotation = True
  ```

## API Reference

### Properties
- `RealMode3D`: A property to enable 3D mode for the chart.
- `EnableMouseRotation`: A property to allow users to rotate the chart using the mouse.

## Code Examples

#### C#
```csharp
this.chartControl1.RealMode3D = true;
this.chartControl1.EnableMouseRotation = true;
```

#### VB.NET
```vb
Me.chartControl1.RealMode3D = True
Me.chartControl1.EnableMouseRotation = True
```

## Page-level Navigation/TOC (if applicable)
- [Rotating Chart](#rotating-chart)
- [Enabling Chart Rotation](#enabling-chart-rotation)

<!-- tags: [chart, 3D, Windows Forms, mouse rotation, rotation, depth, tilt, C#, VB.NET] keywords: [rotating chart, 3D settings, enable mouse rotation, RealMode3D, EnableMouseRotation, mouse interaction, Windows Forms/chart, 3D, properties, methods] -->
```