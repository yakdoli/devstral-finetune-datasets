```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_384.jpeg
document_name: chart
page_number: 384
page_id: chart#page_384
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:31Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates placing x and y-axes in an opposed position to their default implied position.
- Explains how to configure custom axes and their properties.
- Describes the use of multiple axes in a chart for plotting.
- Provides guidance on implementing right-to-left cultures using axes settings.
- Includes steps to add a new axis to a chart.

## Content

### Axes Positioning

```csharp
// default left position
Me.chartControl1.PrimaryYAxis.OpposedPosition = True
```

The above code snippet will place both the x and y-axes in the position opposite to their default implied position.

![Figure 249: Chart displaying Opposed X and Y Axes](chart.png){width=6.29in}

You can similarly set this property on any custom `ChartAxis` that you might add to the chart. Using multiple axes in a chart is described in this topic: [Multiple Axes](#multiple-axes).

The OpposedPosition along with Inversed setting could be useful for implementing charts for right-to-left cultures.

#### 4.6.4 Multiple Axes

Often you will have to plot multiple series on a single chart, each in its own x or y axis. You will then need to add an x or y axis to the chart in addition to the already existing PrimaryXAxis and PrimaryYAxis. You can do this by instantiating a `ChartAxis` and adding it to the `Axes` collection. Then specify the newly created axis as the x or y axis of a particular series.

The following are the steps to include a new axis to the chart.

Footer: © 2013 Syncfusion. All rights reserved. | 384 Page

## API Reference

- `OpposedPosition`: Property to set the axis position opposite to the default.
- `ChartAxis`: Class for custom axes configuration.
- `Axes`: Collection to add custom axes to the chart.

## Code Examples

```csharp
// Example of setting OpposedPosition for the PrimaryYAxis
Me.chartControl1.PrimaryYAxis.OpposedPosition = True;
```

## Page-level Navigation/TOC

- [Multiple Axes](#multiple-axes)
- [4.6.4 Multiple Axes]

## Cross References

See also:
- [Axes Overview](#axes-overview)
- [Multiple Axes](#multiple-axes)

<!-- tags: [Syncfusion Winforms, Chart, Axes, Multiple Axes, OpposedPosition, Inversed, Right-to-left cultures] keywords: [axes, left position, multiple axes, chart, custom axes, right-to-left, configuration, axes collection, multiple series] -->
```