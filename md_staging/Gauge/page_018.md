```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: Gauge
page_number: 018
page_id: Gauge#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:45Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- This page provides an overview of the Essential Gauge control for Windows Forms.
- It includes detailed property descriptions and a visual example of the gauge layout.
- The properties listed help in customizing the appearance and behavior of the gauge.

## Content

### Table 3: Property Table

| Property            | Type     | Description                                                                 |
|---------------------|----------|-----------------------------------------------------------------------------|
| ShowScaleLabel      | Boolean  | Gets or sets the scale label visibility.                                |
| ScaleLabelColor     | Color    | Gets or sets the scale label color of the gauge.                        |
| LabelPlacement      | Enum     | Gets or sets whether to place the ticks inside or outside the arc.     |
| TextOrientation     | Enum     | Gets or sets the text orientation layout.                                |

### Figure 10: Scale outside the arc

![Scale outside the arc](https://example.com/image.png)
*Figure 10: Scale outside the arc*

## API Reference

### Properties
- **ShowScaleLabel**: Boolean
  - Description: Gets or sets the visibility of the scale label.
- **ScaleLabelColor**: Color
  - Description: Gets or sets the color of the scale label.
- **LabelPlacement**: Enum
  - Description: Gets or sets the placement of ticks relative to the arc.
- **TextOrientation**: Enum
  - Description: Gets or sets the orientation layout of the text.

## Code Examples

### Example: Configuring Gauge Properties

```csharp
// Example of configuring gauge properties
Syncfusion.Windows.Forms.GaugeControl gauge = new Syncfusion.Windows.Forms.GaugeControl();
gauge.ShowScaleLabel = true;
gauge.ScaleLabelColor = Color.Red;
gauge.LabelPlacement = Syncfusion.Windows.Forms.Gauge.LabelPlacementType.Outside;
gauge.TextOrientation = Syncfusion.Windows.Forms.Gauge.TextOrientationType.Vertical;
```

## RAG Annotations
<!-- tags: [Gauge, Windows Forms, properties, customization, ScaleLabel, LabelPlacement, TextOrientation] keywords: [Essential Gauge, Windows Forms, control, properties, visibility, placement, orientation, color, scale label, text] -->
```