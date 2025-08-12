```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_054.jpeg
document_name: chart
page_number: 054
page_id: chart#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:32Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```vb
Dim dataLabelsModel As New ChartDataBindAxisLabelModel(populations)
dataLabelsModel.LabelName = "City"
chartControl1.Series.Add(series)
chartControl1.PrimaryXAxis.LabelsImpl = dataLabelsModel
```

![](attachment:fig_27.png)
**Figure 27: Binding Chart with IEnumerables**

## 4.2.4 Data Binding in Chart Through Chart Wizard

You can easily implement data binding technique at design-time, using Chart Wizard.

The below steps lets you bind a database table with the ChartControl.

1. Open the Chart Wizard tool, Click Series button and go to the **Data Source** tab as shown in the image below.

```markdown
## API Reference (if applicable)

Image-related APIs and methods are not directly included in this section. However, the following are related to data binding in charts:

- **ChartDataBindAxisLabelModel**
  - Represents a model to bind data to axis labels in a chart.

- **Series**
  - Collection of series that can be added to a chart to represent data.

- **PrimaryXAxis**
  - Represents the primary X-axis of the chart.

**Parameters**
- **populations**: The data source to bind to the chart.

**Returns**
- None.

**Exceptions**
- None specified in the provided content.
```

## Code Examples

Visual Basic (VB) example:
```vb
Dim dataLabelsModel As New ChartDataBindAxisLabelModel(populations)
dataLabelsModel.LabelName = "City"
chartControl1.Series.Add(series)
chartControl1.PrimaryXAxis.LabelsImpl = dataLabelsModel
```

## Page-level Navigation/TOC (if applicable)

- [4.2.4 Data Binding in Chart Through Chart Wizard](#4.2.4-data-binding-in-chart-through-chart-wizard)

## Cross References

See also:
- Chart Wizard Tool
- Design-Time Data Binding

<!-- tags: [Syncfusion, Windows Forms, Chart, Data Binding, Design Time, Chart Wizard] keywords: [ChartWizard, ChartControl, DataBinding, series, LabelName, PrimaryXAxis, populations] -->
```