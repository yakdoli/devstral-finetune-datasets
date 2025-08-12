```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: Gauge
page_number: 021
page_id: Gauge#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:29Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- Demonstrates how to configure tick marks and inner lines for a radial gauge in Windows Forms.
- Includes code examples in both C# and VB for setting properties such as tick placement, color, and height.

## Content

### Configuring Tick Marks and Inner Lines
To customize the appearance of tick marks and inner lines in a radial gauge, the following properties can be set:

#### C#
```csharp
this.radialGaugel.MinorTickMarkHeight = 6;
this.radialGaugel.MajorTickMarkHeight = 12;
this.radialGaugel.MinorInnerLinesHeight = 6;
```

#### VB
```vb
Me.radialGaugel.TickPlacement = Syncfusion.Windows.Forms.Gauge.TickPlacement.Outside
Me.radialGaugel.MajorTickMarkColor = System.Drawing.Color.White
Me.radialGaugel.MinorTickMarkColor = System.Drawing.Color.White
Me.radialGaugel.InterLinesColor = System.Drawing.Color.White
Me.radialGaugel.MinorTickMarkHeight = 6
Me.radialGaugel.MajorTickMarkHeight = 12
Me.radialGaugel.MinorInnerLinesHeight = 6
```

#### Explanation
- **TickPlacement**: Sets the placement of the tick marks relative to the gauge.
- **MajorTickMarkColor** and **MinorTickMarkColor**: Define the color of major and minor tick marks.
- **InterLinesColor**: Sets the color of the inner lines.
- **MinorTickMarkHeight** and **MajorTickMarkHeight**: Control the height of minor and major tick marks.
- **MinorInnerLinesHeight**: Controls the height of the minor inner lines.

### Visual Representation
The following image illustrates a radial gauge with customized tick marks and inner lines:

![Radial Gauge](image.png)

### Description of the Image
- The gauge shows a range from 0 to 120.
- Major tick marks are placed at intervals of 10 (e.g., 0, 10, 20, ...).
- Minor tick marks are placed at intervals of 2 between major ticks.
- The gauge features a needle pointing to the center, indicating no specific value.
- The color scheme includes white for tick marks and inner lines.

## API Reference

### Properties
- **TickPlacement**
  - **Type**: `Syncfusion.Windows.Forms.Gauge.TickPlacement`
  - **Default**: `Inside`
  - **Description**: Determines the placement of tick marks (Inside or Outside the gauge).
  
- **MajorTickMarkColor**
  - **Type**: `System.Drawing.Color`
  - **Default**: `Black`
  - **Description**: Sets the color of major tick marks.
  
- **MinorTickMarkColor**
  - **Type**: `System.Drawing.Color`
  - **Default**: `Black`
  - **Description**: Sets the color of minor tick marks.
  
- **InterLinesColor**
  - **Type**: `System.Drawing.Color`
  - **Default**: `Black`
  - **Description**: Sets the color of the inner lines.
  
- **MinorTickMarkHeight**
  - **Type**: `int`
  - **Default**: `4`
  - **Description**: Sets the height of minor tick marks.
  
- **MajorTickMarkHeight**
  - **Type**: `int`
  - **Default**: `8`
  - **Description**: Sets the height of major tick marks.
  
- **MinorInnerLinesHeight**
  - **Type**: `int`
  - **Default**: `4`
  - **Description**: Sets the height of minor inner lines.

## Code Examples

### Full Example in C#

```csharp
using System;
using System.Drawing;
using Syncfusion.Windows.Forms.Gauge;

public class RadialGaugeExample
{
    public void ConfigureGauge()
    {
        RadialGauge radialGaugel = new RadialGauge();

        // Configure tick marks and inner lines
        radialGaugel.TickPlacement = TickPlacement.Outside;
        radialGaugel.MajorTickMarkColor = Color.White;
        radialGaugel.MinorTickMarkColor = Color.White;
        radialGaugel.InterLinesColor = Color.White;
        radialGaugel.MinorTickMarkHeight = 6;
        radialGaugel.MajorTickMarkHeight = 12;
        radialGaugel.MinorInnerLinesHeight = 6;

        // Additional configurations...
    }
}
```

### Full Example in VB

```vb
Imports System
Imports System.Drawing
Imports Syncfusion.Windows.Forms.Gauge

Public Class RadialGaugeExample
    Public Sub ConfigureGauge()
        Dim radialGaugel As New RadialGauge()

        ' Configure tick marks and inner lines
        radialGaugel.TickPlacement = TickPlacement.Outside
        radialGaugel.MajorTickMarkColor = Color.White
        radialGaugel.MinorTickMarkColor = Color.White
        radialGaugel.InterLinesColor = Color.White
        radialGaugel.MinorTickMarkHeight = 6
        radialGaugel.MajorTickMarkHeight = 12
        radialGaugel.MinorInnerLinesHeight = 6

        ' Additional configurations...
    End Sub
End Class
```

## Cross References
- Refer to the [Gauge Overview](#gauge-overview) for an introduction to the Gauge control.
- Refer to the [Customizations](#customizations) section for more examples of configuring the Gauge control.

<!-- tags: [Gauge, Windows Forms, Tick Marks, Inner Lines, Radial Gauge, Syncfusion, Version 11.4.0.26] keywords: [RadialGauge, TickPlacement, MajorTickMarkColor, MinorTickMarkColor, InterLinesColor, MinorTickMarkHeight, MajorTickMarkHeight, MinorInnerLinesHeight] -->
```
