```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_569.jpeg
document_name: chart
page_number: 569
page_id: chart#page_569
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:41Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Overview
- Explains how to import data into a chart from various data stores.
- Focuses on converting CSV files into a DataSet and binding it to the chart.
- Demonstrates a sample for importing data from a CSV file.

## 4.13 Importing

The Chart provides a simple API to let you populate it with any kind of data, provided, you bring that data from the data store at the runtime. You can then either populate the chart with that data, or bind the chart to the DataTable or DataSet, in which the data is contained. See ChartData for more information on Data Binding.

In this section, we will illustrate how the data from certain data stores can be brought to the runtime and bound to the chart. In a way this deals more with extracting data from the mentioned data stores than any support in Chart for binding to such data stores.

### 4.13.1 Importing a CSV file

There is no built-in support in Chart for importing data from CSV (Comma Separated Values) files. But this can be easily accomplished by using the "Microsoft.Jet.OLEDB.4.0" to first convert it into a DataSet and then bind it to the chart. This is illustrated in this sample that is distributed with the installation:

```csharp
Imports Syncfusion.Windows.Forms.Chart.Statistics
double x = Statistics.UtilityFunctions.TCumulativeDistribution(tvalue, degreeOfFreedom, OneTail)
```

![Figure 350: Importing a CSV File](CSV File → DataSet → Chart)

### Sample Location:

```
..My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Chart.Windows\Samples\2.0\Import\Data from CSV
```

## Code Examples

### VB.NET
```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
double x = Statistics.UtilityFunctions.TCumulativeDistribution(tvalue, degreeOfFreedom, OneTail)
```

## API Reference

### Essential Statistical Functions
- `TCumulativeDistribution(tvalue, degreeOfFreedom, OneTail)`

## Related Information
- See_chartdata Section for more information on Data Binding.
- Sample demonstrating importing data from a CSV file: `..My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Chart.Windows\Samples\2.0\Import\Data from CSV`

### Tags: [Syncfusion Winforms, Chart, Data Import, CSV, DataSet, Data Binding]
```