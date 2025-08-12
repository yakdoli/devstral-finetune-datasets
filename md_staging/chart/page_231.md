```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_231.jpeg
document_name: chart
page_number: 231
page_id: chart#page_231
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:43Z
fidelity: lossless
-->

### WinForms Chart

#### Overview
This page discusses the use of the `ChartPieFillMode` property within the Syncfusion WinForms Chart control to configure the fill mode of pie chart elements. An example demonstrates how to apply the `EveryPie` fill mode, where each segment of the pie chart is individually filled.

---

#### Content

##### Configuring Pie Chart Fill Mode
The `ChartPieFillMode` property is used to define how each segment of the pie chart should be filled. By setting this property, you can control the visual representation of the chart to enhance readability and aesthetics.

Here is an example using the `EveryPie` fill mode:

```csharp
Me.chartControl1.Series(0).ConfigItems.PieItem.FillMode = 
ChartPieFillMode.EveryPie
```

This code snippet configures the pie chart to apply distinct fills to each segment, ensuring that each segment is individually differentiated.

---

##### Visual Representation
The following pie chart demonstrates the use of the `EveryPie` fill mode:

![Project Cost Breakdown](#)
*Figure 133: Pie Chart with "EveryPie" FillMode*

**Legend:**
- **Labour:** 28%
- **Production:** 20%
- **Facilities:** 23%
- **Insurance:** 12%
- **Taxes:** 10%
- **Legal:** 2%
- **Licenses:** 3%

---

#### API Reference

##### Namespace: Syncfusion.Windows.Forms.Chart

- **Class:** Series
  - **Property:** ConfigItems
    - **Type:** ChartConfigItems
    - **Description:** Configuration settings for the chart series.

  - **Property:** PieItem
    - **Type:** ChartPieItem
    - **Description:** Configuration settings specific to pie chart items.

  - **Property:** FillMode
    - **Type:** ChartPieFillMode
    - **Description:** Specifies the fill mode for the pie chart. Default value is `EveryPie`.

##### Enum: ChartPieFillMode
- **EveryPie**
  - Each segment of the pie chart is individually filled.

---

#### Code Examples

##### Example 1: Setting Fill Mode to `EveryPie`
```csharp
using Syncfusion.Windows.Forms.Chart;

ChartControl chartControl1 = new ChartControl();
chartControl1.Series.Add(new Series());

// Configure the pie chart fill mode
chartControl1.Series[0].ConfigItems.PieItem.FillMode = 
ChartPieFillMode.EveryPie;

// Add data to the series
chartControl1.Series[0].Points.Add(new Point3D(28, "Labour"));
chartControl1.Series[0].Points.Add(new Point3D(20, "Production"));
chartControl1.Series[0].Points.Add(new Point3D(23, "Facilities"));
chartControl1.Series[0].Points.Add(new Point3D(12, "Insurance"));
chartControl1.Series[0].Points.Add(new Point3D(10, "Taxes"));
chartControl1.Series[0].Points.Add(new Point3D(2, "Legal"));
chartControl1.Series[0].Points.Add(new Point3D(3, "Licenses"));
```

---

#### References
For more information on pie chart customization and fill modes, refer to the Syncfusion documentation on ChartControls. 

---

<!-- tags: [winforms, chart, pie chart, fill mode, ChartPieFillMode] keywords: [Syncfusion, every pie, pie chart, charts, visual representation] -->
```