```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: Gauge
page_number: 026
page_id: Gauge#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:15:09Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

The Gauge control for Windows Forms includes support for customizing the number of major tick lines and number of minor tick lines using the **Major Difference** and **Minor Difference**. It also provides support to customize the number of tick lines using **MaximumValue** and **MinimumValue**.

## Properties

| Property          | Type       | Description                                                                 |
|-------------------|------------|-----------------------------------------------------------------------------|
| Minimum           | Float      | Gets or sets the minimum value for the radial scale. Default value is set to 0. |
| Maximum           | Float      | Gets or sets the maximum value for the radial scale. Default value is set to 120. |
| MajorDifference   | Float      | Gets or sets the major difference value. |
| MinorDifference   | Integer    | Gets or sets the minor difference value. |

### Example Code

- **C#**

    ```csharp
    this.radialGauge1.MajorDifference = 20F;
    this.radialGauge1.MaximumValue = 120F;
    this.radialGauge1.MinimumValue = 0F;
    this.radialGauge1.MinorDifference = 1;
    ```

- **VB**

    ```vb
    Me.radialGauge1.MajorDifference = 20F
    Me.radialGauge1.MaximumValue = 120F
    Me.radialGauge1.MinimumValue = 0F
    Me.radialGauge1.MinorDifference = 1
    ```

## 3.3 Visual Styles for all the Gauges

The Gauge control for Windows Forms includes four stunning skins for professional representation of gauges. You can easily modify the look and feel of the gauge component using the built-in visual styles and color schemes.

<!-- tags: [gauge, windows forms, visual styles, major difference, minor difference, maximum value, minimum value] keywords: [gauge control, windows forms, visual styles, customization, major ticks, minor ticks] -->
``` 
