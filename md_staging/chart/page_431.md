```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_431.jpeg
document_name: chart
page_number: 431
page_id: chart#page_431
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:14Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This section explains how to use the Axis Crossing Support feature in Essential Chart for Windows Forms.
- It describes how to customize the intersection point of X and Y axes based on specified data point values.
- Provides use case scenarios and properties related to axis crossing.
- Includes a code example for enabling axis crossing.

## Content

### 4.6.15 Axis Crossing Support

Essential Chart for Windows allows the X and Y axis to intersect at a desired point. The X and Y axis will intersect at a point based on the value specified in the `X axis Crossing` property and the `Y axis Crossing` property respectively.

#### Use Case Scenarios
This feature will be useful to customize the location of primary axes from default location, when you want to add huge number of negative and positive points in the chart.

#### Properties

| Property    | Description                                                                 | Type       | Data Type | Reference links |
|-------------|-----------------------------------------------------------------------------|------------|-----------|------------------|
| Crossing    | Specifies the point of intersect for X and Y axis based on the given data point value. | Server side | Double    | NA               |

#### Sample Link
To view a sample:
1. Open the Syncfusion Dashboard.
2. Click the Windows Forms drop-down list and select Run Locally Installed Samples.
3. Navigate to `Chart samples → Chart Axes → Axis Crossing`.

#### Enable crossing X and Y axis
To enable crossing X and Y axis, specify the Y axis data point value, where you want the X axis to cross, in the `X axis Crossing` property. Similarly specify the X axis data point value, where you want the Y axis to cross, in the `Y axis Crossing` property. The following code illustrates this:

```csharp
this.chartControl1.PrimaryXAxis.Crossing = 150;
```

## API Reference

### Properties
- **Crossing**
  - **Description:** Specifies the point of intersect for X and Y axis based on the given data point value.
  - **Type:** Server side
  - **Data Type:** Double

## Code Examples

### C#
```csharp
this.chartControl1.PrimaryXAxis.Crossing = 150;
```

## Page-level Navigation/TOC
- [4.6.15 Axis Crossing Support](#4.6.15-axis-crossing-support)
  - Use Case Scenarios
  - Properties
  - Sample Link
  - Enable crossing X and Y axis

## Cross References
See also:
- [Syncfusion Dashboard](#syncfusion-dashboard)
- [Chart samples → Chart Axes → Axis Crossing](#chart-samples-chart-axes-axis-crossing)

<!-- tags: [syncfusion, winforms, axis crossing, chart control, chart axes, properties, sample link, use case scenarios] keywords: [chart, axis crossing, data point, primaryXAxis, crossing] -->
```