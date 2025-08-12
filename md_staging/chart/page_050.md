```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: chart
page_number: 050
page_id: chart#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:19Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates implementing a custom databinding interface for Series.
- Highlights the use of CustomModel for integrating data with Chart Series.
- Explains the use of indexed data and its implications on binding to the Chart.
- Describes Chart Data Binding with IEnumerable to adapt to both indexed and non-indexed model data.

## Content

### Figure 26: CustomModel bound to the Chart Series

![Illustrates Implementing Custom Databinding Interface](https://example.com/image.png)
*Figure 26: CustomModel bound to the Chart Series*

####Indexed data

Note that if you have indexed data, which implies that the X values are simply categories and don’t carry any cardinal value, then you can instead implement the **IChartSeriesIndexedModel** interface and bind it to the **ChartSeries.SeriesIndexedModelImpl**. The main difference in this interface is that you don’t have to implement the `GetX` method.

### 4.2.3 Chart Data Binding with IEnumerables

Syncfusion chart provides an option of binding the Chart with IEnumerables, like ArrayList for Indexed or Non Indexed model data through ChartDataBindModel implementation.

#### Code Example

```csharp
class PopulationData
{
    // Implementation details
}
```

## Comments and Notes
- The figure illustrates the custom model data binding interface for the Chart Series, providing clarity on how to implement custom databinding.
- The use of `IChartSeriesIndexedModel` simplifies the process when dealing with indexed data, where X values are treated as categories.
- The ability to bind with IEnumerable enhances flexibility in integrating both indexed and non-indexed data models efficiently.

### References and Considerations
- Ensure that the `GetX` method is skipped when using indexed data through the `IChartSeriesIndexedModel` interface.
- When implementing the `ChartDataBindModel`, consider the specific requirements of indexed versus non-indexed data models.

<!-- tags: [custom databinding, indexed data, IChartSeriesIndexedModel, IEnumerable, ChartDataBindModel, Syncfusion Winforms, chart series] -->
```