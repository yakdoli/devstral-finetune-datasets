```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_494.jpeg
document_name: chart
page_number: 494
page_id: chart#page_494
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:38Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the use of the `BackgroundImage` property to set a custom image as the background in Windows Forms charts.
- Explains how to specify the layout of the background image using different options such as `Tile`, `Center`, `Stretch`, and `Zoom`.

## 4.10.2 Background Image

### Chart Settings

In Windows Forms, use the `BackgroundImage` property to specify a custom image as the background of the chart. The image layout can also be specified using the property below.

**Chart control Property** | **Description**
--- | ---
`BackgroundImage` | Indicates the background image used for the control.
`BackgroundImageLayout` | Indicates the background image layout used for the component. Possible values are:<br> - Tile (default setting)<br> - Center<br> - Stretch<br> - Zoom

### C# Code Example

```csharp
this.chartControl1.BackgroundImage =
    ((System.Drawing.Image)(resources.GetObject("chartControl1.BackgroundImage")));
```

## Figure: ChartInterior = "LightBlue"

The figure below illustrates the interior of the `ChartControl` with the `ChartInterior` property set to `"LightBlue"`.

![Figure 318: ChartInterior = "LightBlue"](https://example.com/figure_318.png)  
*Figure 318: ChartInterior = "LightBlue"*

## API Reference

### Properties
- `BackgroundImage`: Indicates the background image used for the control.
- `BackgroundImageLayout`: Indicates the background image layout used for the component. Possible values are:
  - `Tile` (default setting)
  - `Center`
  - `Stretch`
  - `Zoom`

### Methods
- `SetBackgroundImage`: Sets the background image for the chart control.
- `GetBackgroundImage`: Retrieves the current background image set for the chart control.

### Events
- `BackgroundImageChanged`: Triggered when the `BackgroundImage` property is changed.
- `BackgroundImageLayoutChanged`: Triggered when the `BackgroundImageLayout` property is changed.

## Code Examples

### Setting the Background Image

```csharp
// Load the image from resources
System.Drawing.Image backgroundImage = 
    (System.Drawing.Image)(resources.GetObject("chartControl1.BackgroundImage"));

// Set the background image for the chart control
this.chartControl1.BackgroundImage = backgroundImage;
this.chartControl1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
```

## Page-level Navigation/TOC (if applicable)

- **4.10.2 Background Image**
  - Chart Settings
  - Code Example

## Cross References

- See also: Properties list, Events list, Methods list.

## RAG Annotations

<!-- tags: [chart, windowsforms, backgroundimage, syncfusion-sdk, essentialchart] keywords: [chartcontrol, backgroundimage, backgroundimagelayout, tile, center, stretch, zoom, windows forms, syncfusion winforms] -->
```