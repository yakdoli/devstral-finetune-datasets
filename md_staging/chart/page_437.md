<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_437.jpeg
document_name: chart
page_number: 437
page_id: chart#page_437
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:52Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Overview

- Demonstrates the use of individual Y-axis label placement in charts.
- Highlights chart division area support in **Essential Chart** for displaying multiple charts within a single ChartArea.

### Content

#### Figure 280: Customized Individual Y-Axis Label Placement

```markdown
**Net Export of Selected Nation**
- Displays net export values for countries such as the United States, Britain, Japan, France, and Canada.
- Uses a bar chart with customized Y-axis label placement.
```

#### 4.7 Chart Area

**Essential Chart** provides chart divide area support, enabling a single ChartArea to be divided into equal squares to display multiple charts (pie, funnel, or pyramid). To enable this feature, the `ChartArea.DivideArea` property should be set to `true`.

By enabling this property, the following are possible:

- Retrieving the bounds of each section of pie, funnel, or pyramid charts.
- Displaying the series name as the title for individual sections of pie, funnel, and pyramid chart types.
- Drawing series with the same radius.

The `GetSeriesBounds()` method can be used to get the bounds of the `DividedArea` when `ChartArea.DivideArea` is set to `true`.

```csharp
// Code snippet in C# for reference
[Your C# code here]
```

### API Reference

#### Properties

- `DivideArea`: Boolean property to enable chart division support in ChartArea.

#### Methods

- `GetSeriesBounds()`: Retrieves the bounds of the DividedArea.

### Code Examples

```csharp
// Example usage in C#
chart.ChartAreas[0].DivideArea = true;
```

### See also

- [ChartArea Documentation](#)
- [Pie Chart Example](#)
- [Funnel Chart Example](#)
- [Pyramid Chart Example](#)

---

<!-- tags: [chart, chartarea, dividarea, netexpor, selected, nation, piechart, funnelchart, pyramidchart] keywords: [chartarea, customized y-axis, net export, chart division, pie, funnel, pyramid, getseriesbounds, bounds, radius] -->