```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_023.jpeg
document_name: Gauge
page_number: 023
page_id: Gauge#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:36Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- Explains how to customize needle styles and visibility in a radial gauge.
- Demonstrates setting needle properties such as color and style in C# and VB.
- Introduces the concept of ranges in a gauge to highlight value ranges.
- Lists attributes for customizing ranges including start/end values and placement.

## Content

### Customizing Needle Styles and Visibility

The following properties can be used to set the needle style and visibility in a radial gauge:

| Property      | Type   | Description                |
|---------------|--------|-----------------------------|
| NeedleStyle  | Enum   | Gets or sets the needle style. |
| ShowNeedle   | Boolean| Gets or sets the needle visibility. |

#### Code Examples

##### C#
```csharp
this.radialGauge1.ShowNeedle = true;
this.radialGauge1.NeedleColor = System.Drawing.Color.Black;
this.radialGauge1.NeedleStyle = Syncfusion.Windows.Forms.Gauge.NeedleStyle.Advanced;
```

##### VB
```vb
Me.radialGauge1.ShowNeedle = True
Me.radialGauge1.NeedleColor = System.Drawing.Color.Black
Me.radialGauge1.NeedleStyle = Syncfusion.Windows.Forms.Gauge.NeedleStyle.Advanced
```

### 3.2.2.5 Ranges

Ranges are objects that highlight a range of values and can display different ranges in different colors. Ranges can be customized using various attributes such as range placement, height, color of the range, and so on. All the available attributes are listed in the following table:

| Property         | Type   | Description                                                                                       |
|------------------|--------|---------------------------------------------------------------------------------------------------|
| Startvalue      | Integer| Specify the start value of the range. Default value is set to 0.                               |
| Endvalue        | Integer| Specify the end value of the range. Default value is set to 0.                                 |
| RangePlacement  | Enum   | Using this attribute, the range can be positioned in two areas along the radial scale. It includes the following options: |
|                  |        |- Inside<br>- Outside<br>The default value is Inside.                                           |

## API Reference (if applicable)

- **Namespace**: `Syncfusion.Windows.Forms.Gauge`
- **Types**:
  - `NeedleStyle`: Enum for setting the needle style.
  - `RangePlacement`: Enum for setting the placement of ranges.

## Code Examples (multi-language supported)

The above examples demonstrate how to customize both the needle properties and the range attributes in a radial gauge using both C# and VB.

## Page-level Navigation/TOC (if applicable)
- 3.2.2.5 Ranges

<!-- tags: [Syncfusion, Winforms, Gauge, NeedleStyle, RangePlacement, RadialGauge] keywords: [Customizing, Needle, Visibility, Ranges, Startvalue, Endvalue, Placement] -->
```