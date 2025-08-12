```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: chart
page_number: 032
page_id: chart#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:17:32Z
fidelity: lossless
-->

# Chart Control and Data Wizard

## Overview
- Guide on generating custom points for series using the Chart Wizard.
- Explains how to select and bind data sources for the chart.
- Describes techniques for changing chart types and selecting XValue and YValue columns using Series Data.

## Content

### Chart Wizard Interface
The Chart Wizard interface provides options to customize and configure a chart. Key elements of the interface include:

1. **Auto Run Wizard**: Generates custom points for the series.
2. **Chart Type**: Sets the type of chart (e.g., Line).
3. **Series**: Allows adding and removing points for the series.
4. **Appearance**: Modifies the visual properties of the chart.
5. **Axes**: Configures the axes of the chart.
6. **Points**: Manages individual data points.
7. **ToolBar**: Offers additional tools for chart customization.
8. **Legend**: Manages the legend for the chart.

### Data Source Selection
- The **Data Source** tab allows selection of the data source to connect with.
- Once a data source is selected, the wizard guides you through connectivity steps.
- For detailed information on data binding, refer to the "Data Binding in Chart Through Chart Wizard" topic.

#### Data Binding in Chart Through Chart Wizard
This topic describes data binding techniques at design time using Chart Wizard tools. It explains how to properly connect the chart to external data sources and configure the chart based on the data.

### Series Data Tab
The **Series Data** tab enables changing the type of the chart and connecting to external data sources. When an external data source is selected, the XValue and YValue ComboBoxes are automatically populated with the column names from the external data source.

#### Selecting XValue and YValue
- Choose one column for XValue and another for YValue to determine the axes of the chart.
- For detailed guidance on data binding, refer to the "Data Binding in Chart Through Chart Wizard" topic.

## Figure: Adding Points to Series
**Figure 13: Adding Points to Series**

This figure illustrates the process of adding custom points to a series using the Chart Wizard. The interface shows options to edit, add, or remove points, as well as to apply changes.

## API Reference
- **Series Data**: Methods to modify the type of the chart and bind external data sources.
- **Data Binding**: Techniques for connecting the chart to external data sources using the Chart Wizard.

## Code Examples
```csharp
// Example: Adding Points to Series
chart.Series.Add(new Series("Series1", ChartType.Line));
chart.Series["Series1"].Points.AddXY(0, 0);
chart.Series["Series1"].Points.AddXY(2, 4);
chart.Series["Series1"].Points.AddXY(6, 8);
chart.Series["Series1"].Points.AddXY(4, 3.5);
```

## Cross References
- See also:
  - "Data Binding in Chart Through Chart Wizard" for detailed information on binding techniques.
  - "Series Data" for information on modifying chart types using external data sources.

## Page-level Navigation/TOC (if applicable)
- **Data Source**: Explanation of data source selection and data binding.
- **Series Data**: Description of changing the chart type and configuring XValue and YValue columns.

### RAG Annotations
<!-- tags: [syncfusion, winforms, chart control, data wizard, data binding, series data, external data sources] keywords: [chart wizard, series, data source, xvalue, yvalue, line chart, design time, chart configuration] -->
```