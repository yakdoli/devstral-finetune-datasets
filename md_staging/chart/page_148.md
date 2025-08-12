```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_148.jpeg
document_name: chart
page_number: 148
page_id: chart#page_148
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:09Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Code Example for Configuring HeightCoefficient

```csharp
false;
this.chartControl1.Series[0].ConfigItems.PieItem.HeightCoefficient = 0.1f;
```

```vb
[VB.NET]

Me.chartControl1.Series(0).ConfigItems.PieItem.HeightByAreaDepth = False
Me.chartControl1.Series(0).ConfigItems.PieItem.HeightCoefficient = 0.1f
```

#### Figure: Pie Chart with HeightCoefficient Property Set

![Illustrates HeightCoefficient](https://raw.githubusercontent.com/syncfusion/samples/master/windowsforms/xpchart/Samples/Charts/Pie/Doughnut/PieExamples/HeightCoefficient.png)

**Figure 83: Pie Chart with HeightCoefficient Property Set**

### Customization Options

The following customization options are available for configuring the chart:

- AngleOffset
- Border
- DisplayShadow
- DisplayText
- DoughnutCoefficient
- DrawSeriesNameInDepth
- ElementBorders
- ExplodedAll
- ExplodedIndex
- ExplosionOffset
- FillMode
- Gradient
- HeightByAreaDepth
- HeightCoefficient
- HighlightInterior
- InSideRadius
- OptimizePiePointPositions
- PieType
- ShadowInterior
- ShadowOffset
- ShowTicks
- VisibleAllPies
- FancyToolTip
- Font
- Interior
- LegendItem
- Name
- PointsToolTipFormat
- SmartLabels
- Summary
- Text
- TextColor
- TextFormat
- TextOffset
- TextOrientation
- Visible
- ShowDataBindLabels

### 4.4.9 Polar And Radar Chart

#### Overview
- Explains how to configure and customize Polar and Radar charts in Windows Forms.
- Includes setting properties such as:
  - AngleOffset
  - Border
  - DisplayShadow
  - DisplayText
  - DoughnutCoefficient
  - and more.

This section details the various customization options available for configuring Polar and Radar charts, enhancing their visual representation and functionality in Windows Forms applications.

---

<!-- tags: [syncfusion, windowsforms, chart, piechart, polarchart, radarchart, customization, properties, api] keywords: [angleoffset, border, displayshadow, displaytext, doughnutcoefficient, explodedindex, explosionoffset, fillmode, piechart, polar, radar, properties, shadowinterior, showdata bindlabels, summary, textformat, visible] -->
```