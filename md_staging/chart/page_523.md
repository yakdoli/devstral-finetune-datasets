```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_523.jpeg
document_name: chart
page_number: 523
page_id: chart#page_523
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:32Z
fidelity: lossless
-->

## Chart with Skins

### Turquoise Skin

The following output is displayed when the Skins value is set to Turquoise.

![Figure 343: Turquoise](https://example.com/figure343.png)

### Vista Skin

The following output is displayed when the Skins value is set to Vista.

![Figure 344: Vista](https://example.com/figure344.png)

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Chart
- **Class:** ChartControl
- **Property:** Skins
  - **Description:** Sets the skin style for the chart.
  - **Type:** SkinStyle
  - **Possible Values:** 
    - `Turquoise`
    - `Vista`
  - **Default:** `Turquoise`

## Code Examples

### Example 1: Setting Skins to Turquoise
```csharp
using Syncfusion.Windows.Forms.Chart;

ChartControl chart = new ChartControl();
chart.Series.Add(new ChartSeries("Series"));
chart.Series[0].Points.Add(5, 30);
chart.Series[0].Points.Add(3, 20);
chart.Series[0].Points.Add(7, 40);
chart.Skins = SkinStyle.Turquoise;
```

### Example 2: Setting Skins to Vista
```csharp
using Syncfusion.Windows.Forms.Chart;

ChartControl chart = new ChartControl();
chart.Series.Add(new ChartSeries("Series"));
chart.Series[0].Points.Add(5, 30);
chart.Series[0].Points.Add(3, 20);
chart.Series[0].Points.Add(7, 40);
chart.Skins = SkinStyle.Vista;
```

## See also
- [Syncfusion WinForms Chart Control Documentation](link-to-doc)
- [Skins and Themes for Chart Control](link-to-skins-themes)

<!-- 
tags: [chart, skins, themes, winforms, syncfusion] keywords: [chart with skins, turquoise, vista, chartcontrol, series, points, skinstyle] 
-->
```