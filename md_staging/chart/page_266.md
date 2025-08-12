```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_266.jpeg
document_name: chart
page_number: 266
page_id: chart#page_266
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:24Z
fidelity: lossless
-->

## Content

### LabelStyle in Pyramid Chart

#### Overview
- This section describes how to configure the LabelStyle for Pyramid charts in Windows Forms.
- The `LabelStyle` property determines the placement of labels on the chart elements.
- Example usage is provided in both C# and VB.NET.

#### Table of LabelStyle Properties

| Property                | Description                           |
|-------------------------|----------------------------------------|
| Disabled                | DataPoint labels are disabled.        |
| Default Value           | OutsideInColumn                       |
| 2D / 3D Limitations    | No                                    |
| Applies to Chart Element | All Series                           |
| Applies to Chart Types  | Funnel, Pyramid charts                |

#### Code Snippet Example

Here is the code snippet using `LabelStyle` in Pyramid Chart.

**[C#]**
```csharp
this.chartControl1.Series[0].ConfigItems.PyramidItem.LabelStyle = ChartAccumulationLabelStyle.OutsideInColumn;
```

**[VB.NET]**
```vbnet
Me.chartControl1.Series(0).ConfigItems.PyramidItem.LabelStyle = ChartAccumulationLabelStyle.OutsideInColumn
```

#### Chart Visualization

The following image illustrates how the `LabelStyle` as `OutsideInColumn` affects the display of labels in a Pyramid chart.

![Pyramid Chart with OutsideInColumn LabelStyle](https://example.com/pyramid-chart-outsideincolumn.png)

**Figure 157: ChartAccumulationLabelStyle as OutsideInColumn**

---

## API Reference

### Namespace: Syncfusion.Windows.Forms.Chart

#### Enum: ChartAccumulationLabelStyle

- **OutsideInColumn**: Labels are placed outside the column in the pyramid chart.

#### Property: LabelStyle

- **Type**: ChartAccumulationLabelStyle
- **Description**: Specifies the placement style for labels on the chart elements.
- **Default**: OutsideInColumn
- **Applies to**: PyramidItem in ConfigItems

---

## Code Examples

### C# Example

```csharp
using Syncfusion.Windows.Forms.Chart;

public void ConfigurePyramidChart()
{
    this.chartControl1.Series[0].ConfigItems.PyramidItem.LabelStyle = ChartAccumulationLabelStyle.OutsideInColumn;
}
```

### VB.NET Example

```vbnet
Imports Syncfusion.Windows.Forms.Chart

Public Sub ConfigurePyramidChart()
    Me.chartControl1.Series(0).ConfigItems.PyramidItem.LabelStyle = ChartAccumulationLabelStyle.OutsideInColumn
End Sub
```

---

### Notes
- The `LabelStyle` property can significantly impact the readability and design of the Pyramid chart by controlling the placement of labels.
- This feature is applicable only to Funnel and Pyramid chart types in the Windows Forms environment.

---

## Page-level Navigation/TOC (if applicable)
- Overview
- Table of LabelStyle Properties
- Code Snippet Example
- Chart Visualization
- API Reference
- Code Examples

## Cross References
- See also: Funnel Chart, DataPoint Labeling, Chart Styling

## RAG Annotations
<!-- tags: [WinForms, Chart, LabelStyle, PyramidChart] keywords: [LabelStyle, OutsideInColumn, PyramidItem, ChartAccumulationLabelStyle] -->
```