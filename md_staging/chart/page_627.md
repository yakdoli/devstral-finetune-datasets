```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_627.jpeg
document_name: chart
page_number: 627
page_id: chart#page_627
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:10Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- This page explains how to hide the Chart Zoom Button, showing its usage in different scenarios.
- Demonstrates how to show or hide tabs in the series style dialog in a Chart.

## Content

### Hiding the Chart Zoom Button

![With Zoom Button](https://user-images.githubusercontent.com/123456789/123456789_123456.png)
**Figure 375: Hiding the Chart Zoom Button**

This setting will be useful if you need to display the scrollbar without the ZoomingCancel operation or if you need to change the backcolor and other properties, as `ZoomButton` is derived from the `Button` control.

#### See Also
- [Zooming and Scrolling](https://docs.syncfusion.com/windowsforms/chart/zooming-and-scrolling)

### How to show or hide the tabs in the series style dialog in a Chart

#### Overview
The tabs in the series style dialog can be shown or hidden using the below properties settings.

```csharp
[C#]
this.chartControl1.StyleDialogOptions.ShowBorderTab = true;
this.chartControl1.StyleDialogOptions.ShowTextTab = false;
this.chartControl1.StyleDialogOptions.ShowFancyToolTipsTab = false;
this.chartControl1.StyleDialogOptions.ShowInteriorTab = false;
this.chartControl1.StyleDialogOptions.ShowShadowTab = false;
this.chartControl1.StyleDialogOptions.ShowSymbolTab = false;
```

## Page-level Navigation/TOC (if applicable)
- Hiding the Chart Zoom Button
- How to show or hide the tabs in the series style dialog in a Chart

## Cross References
- See Also: [Zooming and Scrolling](https://docs.syncfusion.com/windowsforms/chart/zooming-and-scrolling)

<!-- tags: [chart, windowsforms, series, style dialog, tabs, zoombutton, scrollbar, syncfusion, version: 11.4.0.26] keywords: [hide, show, tabs, series style dialog, chartControl, StyleDialogOptions, zoombutton, scrollbar, windowsforms, syncfusion, chart] -->
```