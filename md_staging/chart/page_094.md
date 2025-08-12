```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: chart
page_number: 094
page_id: chart#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:51Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Daily Performance Chart

![Daily Performance Chart](https://<image_url>/chart_displaying_column_series.png)

**Figure 52: Chart displaying Column Series**

### Chart Details

| Details                     |                                                                 |
|-----------------------------|-----------------------------------------------------------------|
| Number of Y values per point | 1                                                               |
| Number of Series            | One or More                                                    |
| Cannot be Combined with      | Pie, Bar, Stacked Bar charts, Polar, Radar.                  |

### Column Series Addition

Column series can be added to the chart using the following code.

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Column);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 4);
```

## Page-level Navigation/TOC (if applicable)

The page primarily focuses on the use and implementation of column series in an Essential Chart for Windows Forms. It includes details on chart configuration, specific properties, and examples of code to add column series to a chart.

### Cross References

See also:
- Documentation on [Pie, Bar, Stacked Bar charts, Polar, Radar] for alternative chart types.
- "Creating and Customizing Chart Series" for comprehensive guidance on various chart types and configurations.

<!-- tags: [product: Syncfusion Winforms, module: Essential Chart, control: Column Series, api: ChartSeries, version: 11.4.0.26] keywords: [chart series, column series, windows forms, daily performance, task finished, chart control, syncfusion, c#, data points, chart configuration] -->
```