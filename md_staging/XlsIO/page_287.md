```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_287.jpeg
document_name: XlsIO
page_number: 287
page_id: XlsIO#page_287
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:32Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This page describes the properties related to chart types and features in MS Excel, specifically focusing on fields and buttons in Pivot charts.
- It highlights the functionality of various public properties for controlling filtering and display options for different areas in Pivot charts.
- The properties listed are Boolean, enabling or disabling specific fields and buttons in Pivot charts.

## Content

| Property                | Description                                                                                          | Type          | Data Type    | Reference links |
|-------------------------|------------------------------------------------------------------------------------------------------|---------------|--------------|------------------|
|                         | all the chart types supported by MS Excel.                                                          |               |              |                  |
| ShowAllFieldButtons     | It displays all the field buttons of the Pivot chart.                                               | Public Property | True/false   | NA               |
| ShowAxisFieldButtons    | It displays all the axis area fields as buttons in the Pivot chart with filtering options for the axis field values. | Public Property | True/false   | NA               |
| ShowLegendFieldButtons  | It displays all the legend area fields as buttons in the Pivot chart with filtering options for the legend field values. | Public Property | True/False   | NA               |
| ShowReportFilterFieldButtons | It displays all the Report filter area fields as buttons in the Pivot chart with filtering options for the Report filter field values. | Public property | True/False   | NA               |
| ShowValueFieldButtons   | It displays all the Values area fields as buttons in the Pivot chart with filtering options for the Values area fields. | Public property | True/False   | NA               |

### Sample Link
To understand this process, consider the sample project:

## API Reference (if applicable)
- **Namespace**: Syncfusion.XlsIO
- **Class**: XlsIOChart
- **Properties**:
  - **ShowAllFieldButtons**: A public property to enable or disable the display of all field buttons in the Pivot chart.
  - **ShowAxisFieldButtons**: A public property to enable or disable the display of axis area fields as buttons in the Pivot chart.
  - **ShowLegendFieldButtons**: A public property to enable or disable the display of legend area fields as buttons in the Pivot chart.
  - **ShowReportFilterFieldButtons**: A public property to enable or disable the display of Report filter area fields as buttons in the Pivot chart.
  - **ShowValueFieldButtons**: A public property to enable or disable the display of Values area fields as buttons in the Pivot chart.

### Parameters
- Name | Type | Description | Default | Required
- ShowAllFieldButtons | Boolean | Enables or disables the display of all field buttons. | False | Yes
- ShowAxisFieldButtons | Boolean | Enables or disables the display of axis field buttons. | False | Yes
- ShowLegendFieldButtons | Boolean | Enables or disables the display of legend field buttons. | False | Yes
- ShowReportFilterFieldButtons | Boolean | Enables or disables the display of Report filter field buttons. | False | Yes
- ShowValueFieldButtons | Boolean | Enables or disables the display of Values field buttons. | False | Yes

### Returns
- Type: Void
- Description: Configures the visibility of different field buttons in the Pivot chart based on the boolean values provided.

### Exceptions
- ArgumentException: When an invalid parameter is passed.
- NullReferenceException: If the Pivot chart object is not initialized.

## Code Examples
```csharp
// Example to configure Pivot chart buttons
using(SpreadsheetInfo = new XlsIOChart()){
    // Configure chart options
    chart.ShowAllFieldButtons = true;
    chart.ShowAxisFieldButtons = true;
    chart.ShowLegendFieldButtons = true;
    chart.ShowReportFilterFieldButtons = true;
    chart.ShowValueFieldButtons = true;
}
```

## Cross References
- For more details on Pivot charts and chart configurations in XlsIO, refer to the XlsIO SDK documentation.

<!-- tags: [Pivot chart, Excel, chart options, filtering, field buttons, XlsIO, Syncfusion Winforms] keywords: [chart types, axis fields, legend fields, report filter fields, value fields, boolean properties, filtering options, Pivot chart buttons] -->
```