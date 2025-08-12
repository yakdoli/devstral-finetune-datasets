```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: chart
page_number: 064
page_id: chart#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:44Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates assigning series to data sources in the Chart Wizard.
- Explains how to bind data to series using the Chart Wizard interface.
- Guides on configuring the X and Y values for series in the chart.

## Content

### Chart Wizard Interface

The Chart Wizard interface allows users to create and customize charts by assigning data to series. This section focuses on the process of selecting series and assigning data to them.

#### Figure 38: Selecting the Series to which the data is to be Bound

The following interface screenshot shows the user interface where series are selected and bound to data:

- **Auto Run Wizard**: A checkbox to enable automatic running of the wizard.
- **Series Data**: Options to assign chart series to data source members.
- **Chart Type**: A menu to choose the type of chart (e.g., Column).
- **Series**: Displays the selected series and its properties (e.g., Series1).
- **Appearance**, **Axes**, **Points**, **ToolBar**, **Legend**: Tabs to configure various chart attributes.
- **Apply**, **Finish**, **Cancel**, **Previous**, **Next**: Buttons to navigate the wizard and apply changes.

#### Data Assignment

To assign the retrieved database column to X and Y values of the series, use the **X Value** and **Y Value** boxes as shown in the interface:

- **X Value**: Assigns the database column associated with the x-axis values.
- **Y Value**: Assigns the database column associated with the y-axis values.

## API Reference

For more detailed information on configuring series data and binding to databases, consult the Syncfusion WinForms API documentation.

## Code Examples

Here is an example of how to programmatically assign data to a series in a chart using Syncfusion WinForms:

```csharp
// Example: Assigning data to a series
chartControl1.DataSource = yourDataSource;
chartControl1.Series[0].XName = "YourXColumn";
chartControl1.Series[0].YName = "YourYColumn";
```

### Conclusion

The Chart Wizard provides a user-friendly interface for designing and implementing charts in Windows Forms applications, ensuring that data is accurately represented and visualized.

<!-- tags: [Syncfusion, WinForms, Chart Wizard, Data Binding, Series, Column Chart] keywords: [series selection, data assignment, X Value, Y Value, chart control, interface, wizard] -->
```