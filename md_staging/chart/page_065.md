```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: chart
page_number: 065
page_id: chart#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:39Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the process of assigning the retrieved database column to the `X` value of the Series in the Chart and Data Wizard.
- Highlights the use of the `Syncfusion` Chart Wizard interface for configuring chart data binding.
- Explains the functionality of assigning data source members to chart series for databinding at runtime.

## Content

### Configuring Data Binding in the Chart Wizard
The Figure below illustrates the steps for assigning retrieved database columns to the `X` value of the Series within the `Chart & Data Wizard`.

#### Key Components in the Wizard Interface:
The wizard screen allows you to:
- **Auto Run Wizard**: Ensures that the chart is automatically configured based on the data source.
- **Series Data**: Allows selection and modification of the series data properties.
- **Add Points to Series**: Adds points dynamically to the series.
- **Data Source**: Enables the selection of the data source for the chart.
- **Series Data Properties**:
  - **Series Name**: Specifies the name of the series (e.g., `Series1`).
  - **Type**: Defines the type of chart (e.g., `Column`).
  - **X Value**: Assigns the database column to the `X` axis value.

#### Chart Control Visualization:
The `chartControl1` displayed on the right-hand side shows a Column Chart with six data points, each labeled with a value ranging from 60 to 80.

#### Series Data Assignment:
The process of assigning the `ID` column from the database to the `X` value of the Series is highlighted in the interface.

### Figure: Assigning the Retrieved Database Column to X Value of the Series
**Figure 39: Assigning the retrieved database column to X value of the Series**

The `Chart & Data Wizard` interface displays the configuration steps for associating database columns with chart datasets. The figure shows the `Auto Run Wizard` option checked, along with the ability to manipulate series data, configure axes, and set appearance properties. The visual output (chart on the right) is updated dynamically as the settings are configured.

## Page-level Navigation/TOC (if applicable)
- Configuring Data Binding in the Chart Wizard
- Key Components in the Wizard Interface
- Chart Control Visualization
- Series Data Assignment

## Cross References
See also:
- **Data Binding in Windows Forms Charts**
- **Configuring Chart Series Using Syncfusion**

## RAG Annotations
<!-- tags: [Syncfusion, Windows Forms, Chart, Data Binding, Series, Auto Run Wizard] keywords: [database column, X value, Chart Wizard, Series Name, Type, Auto Run Wizard, column chart] -->
```