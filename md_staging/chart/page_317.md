```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_317.jpeg
document_name: chart
page_number: 317
page_id: chart#page_317
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:36Z
fidelity: lossless
--> 

## Essential Chart for Windows Forms

### Chart Data From Database

```markdown
Chart Data From Database

- **Houston**: 13
- **Tokyo**: 17
- **Los Angeles**: 15
- **London**: 6
- **New York**: 11
```

#### Figure 197: Doughnut Chart with Data-Bound Labels

The figure illustrates a doughnut chart visualizing data from different cities: Houston, Tokyo, Los Angeles, London, and New York. Each segment of the chart is labeled with its respective value.

### API Reference

- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: DoughnutChart
- **Properties**:
  - `DataBoundLabels`: Enables or disables the display of data-bound labels on the chart.
  - `Legend`: Configures the legend for the chart.
  - `Series`: Contains the collection of series data for the chart.

### Code Examples

#### C#

```csharp
// Creating a Doughnut Chart
DoughnutChart chart = new DoughnutChart();
chart.Series.Add("City", new object[] { 13, 17, 15, 6, 11 });

// Enabling Data-Bound Labels
chart.DataBoundLabels = true;

// Adding Labels
chart.Series[0].Points[0].Label = "Houston";
chart.Series[0].Points[1].Label = "Tokyo";
chart.Series[0].Points[2].Label = "Los Angeles";
chart.Series[0].Points[3].Label = "London";
chart.Series[0].Points[4].Label = "New York";
```

### Cross References

- **Related Pages**: Doughnut Chart Customization, Data Binding in Chart, Chart Series and Data Points

## Notes

The doughnut chart provides an aesthetically pleasing way to visualize data with clear distinctions between different segments. The use of data-bound labels enhances readability by directly associating each data point with its label.

<!-- tags: [syncfusion, winforms, chart, essentialchart, doughnutchart, databoundlabels] keywords: [chart data, essentialchart, windows forms, doughnut chart, data-bound labels, visualization, data binding] -->
``` 
