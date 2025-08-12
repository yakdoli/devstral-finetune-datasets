<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_501.jpeg
document_name: chart
page_number: 501
page_id: chart#page_501
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:39Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## ChartPlot Area Margins

### Overview

- ChartPlotArea margins are specified using the `ChartPlotAreaMargins` property.
- The margin values indicate the space around the axis labels for left, top, right, and bottom sides of the chart.
- Proper functionality is dependent on the `EdgeLabelsDrawingMode` being set to `Shift`.

### ChartControl Property Table

| ChartControl Property             | Description                                                                                                    |
|------------------------------------|----------------------------------------------------------------------------------------------------------------|
| ChartPlotAreaMargins              | Indicates the margin of the axis labels. This margin is supported for left, top, right, and bottom sides of the chart. This property works only if `EdgeLabelsDrawingMode` property is set to `Shift`. <br> Default is `{10, 10, 10, 10}`. |
| AdjustPlotAreaMargins             | Gets / sets the mode of drawing the edge labels. Default is `AutoSet`.                                           |
| EdgeLabelsDrawingMode             | Gets or sets the edge labels drawing mode.                                                                   |

### Code Examples

#### [C#]

```csharp
this.chartControl1.PrimaryYAxis.EdgeLabelsDrawingMode = Syncfusion.Windows.Forms.Chart.ChartAxisEdgeLabelsDrawingMode.Shift;
this.chartControl1.ChartArea.AdjustPlotAreaMargins = Syncfusion.Windows.Forms.Chart.ChartSetMode.UserSet;
this.chartControl1.ChartArea.ChartPlotAreaMargins.Left = 200;
```

#### [VB.NET]

```vb
Me.chartControl1.PrimaryYAxis.EdgeLabelsDrawingMode = Syncfusion.Windows.Forms.Chart.ChartAxisEdgeLabelsDrawingMode.Shift
Me.chartControl1.ChartArea.AdjustPlotAreaMargins = Syncfusion.Windows.Forms.Chart.ChartSetMode.UserSet
Me.chartControl1.ChartArea.ChartPlotAreaMargins.Left = 200
```

### Spacing between elements

#### Overview

- The spacing between elements in the chart is specified using the `ElementsSpacing` property.
- For example, the space between the chart right border and legend right border if `LegendPosition` is set to `Right`.

#### Chart Control Property Table

| Chart control Property | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| ElementsSpacing        | Specifies the spacing between the elements in the chart. Default is 20.|

## References

- See also: [Formatting Chart Elements](#Formatting-Chart-Elements)

<!-- tags: [Syncfusion, Winforms, Chart, ChartPlotAreaMargins, EdgeLabelsDrawingMode, ElementsSpacing] keywords: [ChartArea, Margin, Spacing, EdgeLabels, AutoSet, UserSet, LegendPosition] -->