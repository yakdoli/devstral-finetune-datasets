```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_452.jpeg
document_name: chart
page_number: 452
page_id: chart#page_452
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:52Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

| ShowIcon |                                      |
| -------- | ------------------------------------ |
|          | • Spline                           |
|          | • SplineArea                       |
|          | • StraightLine                     |
|          | • Rectangle                        |

If set to `false`, no icons will be rendered. This overrides most of the other settings including **ShowSymbol**.

## Series Type Icon

An icon representing the series type can be rendered in the legend.

### Rendering Series Type Icons in Legend Items

To do this for all the legend items:

#### C#

```csharp
this.chartControl1.Legend.RepresentationType =
    ChartLegendRepresentationType.SeriesType;
```

#### VB.NET

```vb
Me.chartControl1.Legend.RepresentationType =
    ChartLegendRepresentationType.SeriesType
```

![Legend Item with the Series Type Icon](https://i.imgur.com/someimage.png)

*Figure 287: Legend Item with the Series Type Icon*

### Rendering Series Type Icons for Specific Legend Items

To do this for specific legend items,

#### C#

```csharp
// The general setting affecting all Legend items could be anything
this.chartControl1.Legend.RepresentationType =
    ChartLegendRepresentationType.SeriesImage;

// This will force a specific legend item to show a series icon
this.chartControl1.Legend.Items[0].DrawSeriesIcon = true;
```

---

### Page-level Navigation/TOC
- [Essential Chart for Windows Forms](#essential-chart-for-windows-forms)
  - [Series Type Icon](#series-type-icon)
    - Rendering Series Type Icons in Legend Items
    - Rendering Series Type Icons for Specific Legend Items

### Cross References
See also:
- Series Symbol
- ChartLegendRepresentationType
- Series Image

<!-- tags: [syncfusion, winforms, chart, legend, series type icon, series symbol, series image] keywords: [chartcontrol, legend, series, icons, representationtype, symbol, image, display, rendering, legendlayout, chartseries, visiobasic.NET] -->
```