```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_066.jpeg
document_name: chart
page_number: 066
page_id: chart#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:13Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Chart binding to a data source in Windows Forms.
- Assigning database columns to series in a chart control.
- Configuring chart properties and data binding settings.

## Content

### Setting Up Series Data

The following steps demonstrate how to configure series data in a chart control using the Syncfusion Chart Wizard.

1. **Select Chart Type and Data Source**:
   - Choose the appropriate chart type (e.g., Column).
   - Assign the data source, such as a database table or dataset.

2. **Assign Retrieved Database Column**:
   - In the "Series Data" tab, assign the retrieved database column to the Y value of the Series.
   - Ensure the series is databound by selecting the correct data source member.

   **Figure 40: Assigning the retrieved database column to Y value of the Series**

   ![Syncfusion Chart Wizard Interface](image.jpg)

### Finalizing the Chart Configuration

1. **Click Finish**:
   - Click the "Finish" button to apply the data binding settings to the Chart.
   - This step ensures the chart is databound with the custom data.

   The following image illustrates the Chart bound with custom data:

   ![Chart with Custom Data](image.jpg)

### Key Steps Summary

1. Assign the chart series to the selected data source members.
2. Define the X and Y values for the series.
3. Click "Finish" to apply the data binding.

## Page-level Navigation/TOC (if applicable)

- Essential Chart for Windows Forms
  - Setting Up Series Data
  - Finalizing the Chart Configuration

## Cross References

- Refer to the documentation on configuring data sources in Windows Forms.
- Additional resources on advanced chart customization and data binding.

## RAG Annotations

<!-- tags: Syncfusion, Windows Forms, Chart Wizard, Data Binding, Series, Database Column, Chart Control keywords: Chart Wizard, Applying Data Binding, Series Data, X Value, Y Value, Finish, Custom Data -->
```