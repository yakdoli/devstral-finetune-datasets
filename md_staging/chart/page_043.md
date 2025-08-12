```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_043.jpeg
document_name: chart
page_number: 043
page_id: chart#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:17:51Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Wizard and Legend Customization

### Overview
- The Chart Wizard interface offers tools for customizing the appearance of data visualization elements, particularly focusing on the legend styling.
- The legend's border appearance can be tailored within the wizard, allowing for precise control over the chart's presentation.

### Content

#### 4.2 Chart Data
- **Built-in Support for data-binding**
  - **Essential Chart** provides robust built-in support for binding to DataTables, DataSets, DataViews, as well as any implementation of `IListSource`, `IBindingList`, or `ITypedList`.
  - Data points and axis labels within `ChartSeries` are the elements that can be databound.

---

### Figure: Customizing the Border Appearance of the Legend

![Figure 23: Customizing the Border Appearance of the Legend](#fig23)

**Description**: The figure demonstrates how to customize the border appearance of a chart legend using the Syncfusion Chart Wizard interface. The interface shows various properties that can be adjusted, such as border style, color, and width, to fine-tune the legend's visual characteristics.

### See Also
- **Chart Legend**

---

### API Reference
- **Namespaces**: Syncfusion.Windows.Forms.Chart
- **Methods**: `.SetSeriesDataBinding()`
- **Properties**: 
  - `ChartSeries.DataPoints`
  - `Axis.Labels`

---

### Code Examples
- **C# Example**: Binding a DataTable to a ChartSeries
  ```csharp
  DataTable dataTable = new DataTable();
  // Populate dataTable with data
  chart.Series[0].DataSource = dataTable;
  ```

---

<!-- tags: ChartWizard, Legend, DataBinding, ChartSeries, SyncfusionWinForms. keywords: Chart customization, data visualization, legend styling, data binding, series data points, axis labels, user guide, Windows Forms -->
```