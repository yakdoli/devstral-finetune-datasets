```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_012.jpeg
document_name: Gauge
page_number: 012
page_id: Gauge#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:45Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- The Gauge control is an extension of Windows Forms programming.
- Supports a broad range of dashboard development features.
- Includes resources, controls, graphics, layout, and data binding.

## Content

### 3.2.1.1 Creating a Radial Gauge

Radial gauges can be enhanced with a circle frame or semi-circle frame. This section covers how to include a radial gauge in an application.

#### Through Designer:

1. Drag the RadialGauge control from the toolbox onto the form.

![Figure: RadialGauge control selection](image.png)

#### Steps to Create a Radial Gauge:

- **Step 1:** Open the Windows Forms application in Visual Studio.
- **Step 2:** Navigate to the **Toolbox** panel.
- **Step 3:** Locate and drag the **RadialGauge** control to the form.
- **Step 4:** Customize the properties of the RadialGauge as needed.

## API Reference

### RadialGauge

#### Properties
- **Position:** The position of the gauge on the form.
- **Size:** The dimensions of the gauge.
- **Value:** The current value displayed on the gauge.
- **Range:** The minimum and maximum values the gauge can display.

### Example Usage

```csharp
using Syncfusion.Windows.Forms.Gauge;

// Create a RadialGauge instance
RadialGauge radialGauge = new RadialGauge();

// Set the position and size
radialGauge.Location = new System.Drawing.Point(50, 50);
radialGauge.Size = new System.Drawing.Size(200, 200);

// Set the value
radialGauge.Value = 75;

// Add the gauge to the form
this.Controls.Add(radialGauge);
```

## Code Examples

### Adding a RadialGauge to a Form

```csharp
private void InitializeRadialGauge()
{
    RadialGauge radialGauge = new RadialGauge();
    radialGauge.Location = new System.Drawing.Point(50, 50);
    radialGauge.Size = new System.Drawing.Size(200, 200);
    radialGauge.Value = 75;
    this.Controls.Add(radialGauge);
}
```

## References
- [Syncfusion WinForms Documentation](https://help.syncfusion.com/windowsforms/gauge)
- Additional resources and examples available from the Syncfusion website.

<!-- tags: [radial gauge, windows forms, dashboard development, radial frame, semi-circle frame, designer, control, windows forms programming] keywords: [RadialGauge, Visual Studio, toolbox, position, size, value, range, customization, windows forms, controls, graphics, layout, data binding, example, usage] -->
```