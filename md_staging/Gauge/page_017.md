```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_017.jpeg
document_name: Gauge
page_number: 017
page_id: Gauge#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:14Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- Demonstrates customizing the frame type and background frame of a Radial Gauge.
- Explains the importance of scales in controlling element placement and value ranges.
- Provides code examples in both C# and VB for configuring the Radial Gauge.

## Content

### Setting Frame Type

The following code snippet sets the frame type of the radial gauge to a half-circle.

```csharp
Me.radialGauge1.FrameType = 
Syncfusion.Windows.Forms.Gauge.FrameType.HalfCircle
```

### Configuring ShowBackgroundFrame

The following figure shows the Radial Gauge with `ShowBackgroundFrame` set to `false`, resulting in transparency.

![Figure: ShowBackgroundFrame as False(Transparency)](https://user-images.githubusercontent.com/88415645/233167458-66242e37-537a-4708-9a63-0f8934baf986.png)
*Figure 9: ShowBackgroundFrame as False(Transparency)*

#### Code Example in C#

```csharp
this.radialGauge1.ShowBackgroundFrame = false;
```

#### Code Example in VB

```vb
Me.radialGauge1.ShowBackgroundFrame = false;
```

### Scales

**3.2.2.2 Scales**

Scales are used to control element placement and value ranges.

#### Customizing Scales

You can customize scales added to the Radial Gauge using the properties listed in the following table:

## API Reference

This section will list the specific APIs related to configuring the Radial Gauge, such as properties for `FrameType` and `ShowBackgroundFrame`.

### Code Examples

These examples demonstrate configuring a Radial Gauge in both C# and VB, focusing on frame type and background frame settings.

## Cross References

- Refer to the documentation on different scale configuration options for more details.

### More Information

- For detailed information on scales and their configuration, see the documentation on customizing Radial Gauge properties.

<!-- tags: [radial gauge, frames, scales, transparency, configuration, syncfusion winforms version 11.4.0.26] keywords: [frame type, background frame, showbackgroundframe, customizing scales, label interval, half circle, speedometer, c#, vb, winforms] -->
```