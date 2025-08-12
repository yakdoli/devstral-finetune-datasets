```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: Gauge
page_number: 015
page_id: Gauge#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:58Z
fidelity: lossless
-->

## Overview
- Discusses the properties related to setting colors and visibility for different parts of the gauge control in Windows Forms.
- Focuses on gradient colors for the background, inner frame, and outer frame.
- Includes properties for setting the color of the gauge arc, label, and value.
- Contains a boolean property for controlling the visibility of the gauge value.

## Content

The following table summarizes the properties related to configuring the visual appearance of the gauge control:

### Gauge Properties
| Property Name                | Type      | Description                                                                 |
|------------------------------|-----------|-----------------------------------------------------------------------------|
| BackgroundGradientStartColor | Color     | Gets or sets the gradient start color for the gauge background.           |
| BackgroundGradientEndColor   | Color     | Gets or sets the gradient end color for the gauge background.              |
| InnerFrameGradientStartColor | Color     | Gets or sets the gradient start color for the inner frame.                |
| InnerFrameGradientEndColor   | Color     | Gets or sets the gradient end color for the inner frame.                  |
| OuterFrameGradientStartColor | Color     | Gets or sets the gradient start color for the outer frame.                |
| OuterFrameGradientEndColor   | Color     | Gets or sets the gradient end color for the outer frame.                  |
| GaugeArcColor                | Color     | Gets or sets the arc color of the gauge.                                |
| GaugeLableColor              | Color     | Gets or sets the gauge label color.                                     |
| GaugeValueColor              | Color     | Gets or sets the gauge value color.                                     |
| ShowGaugeValue               | Boolean   | Gets or sets the gauge value visibility.                                |

## API Reference

### Properties
The following table lists the properties and their descriptions:

| Property Name                | Type      | Description                                                                 |
|------------------------------|-----------|-----------------------------------------------------------------------------|
| BackgroundGradientStartColor | Color     | Gets or sets the gradient start color for the gauge background.           |
| BackgroundGradientEndColor   | Color     | Gets or sets the gradient end color for the gauge background.              |
| InnerFrameGradientStartColor | Color     | Gets or sets the gradient start color for the inner frame.                |
| InnerFrameGradientEndColor   | Color     | Gets or sets the gradient end color for the inner frame.                  |
| OuterFrameGradientStartColor | Color     | Gets or sets the gradient start color for the outer frame.                |
| OuterFrameGradientEndColor   | Color     | Gets or sets the gradient end color for the outer frame.                  |
| GaugeArcColor                | Color     | Gets or sets the arc color of the gauge.                                |
| GaugeLableColor              | Color     | Gets or sets the gauge label color.                                     |
| GaugeValueColor              | Color     | Gets or sets the gauge value color.                                     |
| ShowGaugeValue               | Boolean   | Gets or sets the gauge value visibility.                                |

## Code Examples

### Setting Colors and Visibility
```csharp
// Example: Setting background gradient colors
gauge1.BackgroundGradientStartColor = Color.Red;
gauge1.BackgroundGradientEndColor = Color.Blue;

// Example: Setting frame gradient colors
gauge1.InnerFrameGradientStartColor = Color.Green;
gauge1.InnerFrameGradientEndColor = Color.Yellow;
gauge1.OuterFrameGradientStartColor = Color.Orange;
gauge1.OuterFrameGradientEndColor = Color.Purple;

// Example: Setting gauge arc, label, and value colors
gauge1.GaugeArcColor = Color.Black;
gauge1.GaugeLableColor = Color.White;
gauge1.GaugeValueColor = Color.Gray;

// Example: Showing or hiding the gauge value
gauge1.ShowGaugeValue = true;
```

## Cross References
- For more information on configuring other aspects of the gauge control, see the [Gauge Control Documentation](#gauge-control-documentation).
- Additional details on color management and gradients can be found in the [Color and Gradient Properties](#color-and-gradient-properties) section.

<!-- tags: [gauge, windows forms, color, gradient, visibility] keywords: [color, gradient, background, frame, arc, label, value, visibility] -->
```