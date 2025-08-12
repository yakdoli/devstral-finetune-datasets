```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_285.jpeg
document_name: XlsIO
page_number: 285
page_id: XlsIO#page_285
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:48Z
fidelity: lossless
-->

## Essential XlsIO

### Inserting a Pivotchart Sheet and Configuring Options

```csharp
// Insert the Pivotchart sheet to the workbook.
IChart pivotChartSheet = workbook.Charts.Add();

// Set the PivotSource for the Chart.
pivotChartSheet.PivotSource = pivotTable;

// Select the PivotChart type.
pivotChartSheet.PivotChartType = ExcelChartType.Column_Clustered;
```

```vb
' Insert the Pivotchart sheet to the workbook
Dim pivotChartSheet As IChart = workbook.Charts.Add()

' Set the PivotSource for the Chart.
pivotChartSheet.PivotSource = pivotTable

' Select the PivotChart type.
pivotChartSheet.PivotChartType = ExcelChartType.Column_Clustered
```

### PivotChart Options

The field buttons of the PivotChart can be displayed or hidden by selecting **PivotChart Tools > Analyze > Field Buttons**. XlsIO provides an equivalent API to perform simple properties as follows:

#### Note: These properties are exclusive for Excel 2010.

<!-- tags: [XlsIO, pivotchart, workbook, chart, API, Excel 2010] keywords: [pivotchart, pivotsource, clusterchart, field buttons, Excel 2010, display, hide] -->
```