```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: chart
page_number: 062
page_id: chart#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:58Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Describes the Chart & Data Wizard interface for selecting and binding data sources in Windows Forms applications.
- Explains how to choose a database or create a new one for chart data.

## Content

### Data Source Configuration

Figure 36 illustrates selecting a database from the drop-down list in the Data Source Tab:

```plaintext
Figure 36: Selecting the Database from the drop-down List in the Data Source Tab
```

The interface provides options for selecting existing or creating new data sources. Key elements of the interface include:
- **Data Source**: Drop-down menu for selecting existing or configuring new data sources, such as **chartDataDataSet1**, **bindingSource1**, or creating a **new BindingSource...**.
- **Series Data**: Tab for series data configuration, which becomes visible once a data source is selected.

#### Wizard Steps
1. **Select Data Source**: 
   - Instructions above the interface indicate selecting an existing data source or creating a new one.
   - Navigate to the 'Series Data' Tab for further configuration.
2. **Series Data Visibility**:
   - Once the source is selected, the selected table will be visible.
   - Example: Selecting **chartDataDataSet1** or another binding source will show its corresponding data in the interface.

### User Interface Overview
The interface includes:
- **Auto Run Wizard**: Checkbox to enable automatic execution of the wizard steps.
- **Tabs**: Options for configuring chart properties such as:
  - Chart Type
  - Series
  - Appearance
  - Axes
  - Points
  - ToolBar
  - Legend

### Actions
- **Apply**: Applies the current settings.
- **Finish**: Completes the wizard and applies all configurations.
- **Cancel**: Cancels the wizard without applying changes.
- Navigation buttons (**Prev**, **Next**) allow stepping through the wizard.

### Demonstration of Data Source Selection
The figure displays the drop-down menu where the user selects the desired data source. This step is crucial for populating the chart with the required data.

## Page-level Navigation/TOC (if applicable)
- **Figure 36**: Selecting the Database from the drop-down List in the Data Source Tab.

## Cross References
- Refer to related sections on chart series configuration, appearance settings, and data binding documentation in the user guide.

<!-- tags: [syncfusion, windowsforms, chart, databinding, datasources] keywords: [chart wizard, data source drop-down, series data, database selection, syncfusion, windows forms, data binding] -->
```