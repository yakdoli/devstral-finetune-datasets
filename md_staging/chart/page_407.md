```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_407.jpeg
document_name: chart
page_number: 407
page_id: chart#page_407
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:38Z
fidelity: lossless
-->

## Charting with Grouping Labels

### Overview
- Introduces the ability to group sets of adjoining labels and assign them a new label, such as marking the first three months as Q1.
- Utilizes properties like `GroupingLabels` and `DrawTickLabelGrid` for enhanced charting functionality.
- Demonstrates implementation in both C# and VB.NET.

### Content

#### Chart Axis Properties and Their Descriptions

| **ChartAxis Property**             | **Description**                                                                                           |
|------------------------------------|----------------------------------------------------------------------------------------------------------|
| GroupingLabels                     | Lets you group a range of default labels and provide them a custom name/label.                        |
| DrawTickLabelGrid                  | Puts the labels within a grid. Though commonly used when in grouping mode, this feature can be used even otherwise. |

#### Implementation Examples

##### C#

```csharp
ChartAxisGroupingLabel Q1 = new ChartAxisGroupingLabel(new DoubleRange(1, 3), "Q1");
Q1.BorderStyle = ChartAxisGroupingLabelBorderStyle.Rectangle;
Q1.Font = new Font("Arial", 10F, FontStyle.Bold);
this.chartControl1.PrimaryXAxis.GroupingLabels.Add(Q1);

ChartAxisGroupingLabel Q2 = new ChartAxisGroupingLabel(new DoubleRange(4, 6), "Q2");
Q2.BorderStyle = ChartAxisGroupingLabelBorderStyle.Rectangle;
Q2.Font = new Font("Arial", 10F, FontStyle.Bold);
this.chartControl1.PrimaryXAxis.GroupingLabels.Add(Q2);

this.chartControl1.PrimaryXAxis.DrawTickLabelGrid = true;
```

##### VB.NET

```vb
Dim Q1 As New ChartAxisGroupingLabel(New DoubleRange(1, 3), "Q1")
Q1.BorderStyle = ChartAxisGroupingLabelBorderStyle.Rectangle
Q1.Font = New Font("Arial", 10.0F, FontStyle.Bold)
Me.chartControl1.PrimaryXAxis.GroupingLabels.Add(Q1)

Dim Q2 As New ChartAxisGroupingLabel(New DoubleRange(4, 6), "Q2")
Q2.BorderStyle = ChartAxisGroupingLabelBorderStyle.Rectangle
Q2.Font = New Font("Arial", 10.0F, FontStyle.Bold)
Me.chartControl1.PrimaryXAxis.GroupingLabels.Add(Q2)

Me.chartControl1.PrimaryXAxis.DrawTickLabelGrid = True
```

### Notes
- The `GroupingLabels` feature allows for custom labeling of grouped ranges on the chart axis.
- The `DrawTickLabelGrid` feature adds a grid around the grouped labels, enhancing readability and visual clarity.

## Page-level Navigation/TOC (if applicable)
- This section explains how to group and label data points on a ChartAxis in Syncfusion WinForms.

## Cross References
- Refer to related documentation on ChartAxis customization and styling options in the Syncfusion WinForms library.

<!-- tags: [chart, axis, grouping labels, chartaxis, drawticklabelgrid, windows forms, syncfusion] keywords: [grouping labels, chartaxis, drawticklabelgrid, custom labels, grid, windows forms, c#, vb.net] -->
```