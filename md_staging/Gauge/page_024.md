```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: Gauge
page_number: 024
page_id: Gauge#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:25Z
fidelity: lossless
-->

## Overview

This page explains the configuration of ranges for a radial gauge using the `Syncfusion.Windows.Forms.Gauge.Range` class. It covers essential properties such as `Height` and `Color` and provides code samples in both C# and VB to demonstrate adding ranges to a radial gauge.

### Key Points

- **Height**: Specifies the height of the range. Default is set to 5.
- **Color**: Gets or sets the color of the range.

## Content

### Properties of Range

| Property   | Type     | Description                                                                                     |
|------------|----------|-------------------------------------------------------------------------------------------------|
| Height     | Integer  | Specify the height of the range. Default value is set to 5.                                  |
| Color      | Color    | Gets or sets the color of the range.                                                             |

### Adding Ranges to a Radial Gauge

The following code sample illustrates how to add ranges to the radial gauge:

#### C#

```csharp
Syncfusion.Windows.Forms.Gauge.Range range1 = new Syncfusion.Windows.Forms.Gauge.Range();

range1.Color = System.Drawing.Color.FromArgb(((int)((byte)(225))),
                                           ((int)((byte)(128))),
                                           ((int)((byte)(128))));
range1.EndValue = 0F;
range1.Height = 5;
range1.InRange = false;
range1.Name = "GaugeRange1";
range1.RangePlacement = Syncfusion.Windows.Forms.Gauge.TickPlacement.Inside;
range1.StartValue = 0F;
this.radialGauge1.Ranges.Add(range1);
```

#### VB

```vb
Dim range1 As New Syncfusion.Windows.Forms.Gauge.Range()
range1.Color = System.Drawing.Color.FromArgb(CInt(CByte(225)),
                                           CInt(CByte(128)),
                                           CInt(CByte(128)))
range1.EndValue = 0F
range1.Height = 5
range1.InRange = False
range1.Name = "GaugeRange1"
range1.RangePlacement = Syncfusion.Windows.Forms.Gauge.TickPlacement.Inside
range1.StartValue = 0F
Me.radialGauge1.Ranges.Add(range1)
```

## Page-level Navigation/TOC (if applicable)

- Overview
  - Key Points
- Content
  - Properties of Range
  - Adding Ranges to a Radial Gauge
  - Code Examples

## Cross References

See also:

- `Syncfusion.Windows.Forms.Gauge.Range`
- `Syncfusion.Windows.Forms.Gauge.TickPlacement`
- `System.Drawing.Color`

<!-- tags: [Syncfusion, Windows Forms, Gauge, Range, TickPlacement, color, height] keywords: [radial gauge, range configuration, C#, VB, Syncfusion.Windows.Forms.Gauge.Range, Syncfusion.Windows.Forms.Gauge.TickPlacement] -->
```