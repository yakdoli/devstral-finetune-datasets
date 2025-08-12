```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_582.jpeg
document_name: chart
page_number: 582
page_id: chart#page_582
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:00Z
fidelity: lossless
--> 

## Essential Chart for Windows Forms

### Overview
- Demonstrates how to export chart data to an Excel file.
- Creates a cluster column chart with specified data.

### Content

#### C#
```csharp
string exportFileName = Application.StartupPath + @"\chartexport" + 
".xls";

// A new workbook with a worksheet should be created.
IWorkbook chartBook = ExcelUtils.CreateWorkbook(1);
IWorksheet sheet = chartBook.Worksheets[0];

// Fill the worksheet with chart data.
for (int i = 1; i <= 5; i++)
{
    sheet.Range[i, 1].Number = this.chartControl1.Series[0].Points[i - 
1].X;
    sheet.Range[i, 2].Number = this.chartControl1.Series[0].Points[i - 
1].YValues[0];
}

// Create a chart worksheet.
IChart chart = chartBook.Charts.Add("Essential Chart");
// Specify the title of the Chart.
chart.ChartTitle = "Essential Chart";

// Initialize a new series instance and add it to the series collection 
of the chart.
IChartSerie series = chart.Series.Add();

// Specify the chart type of the series.
series.SerieType = ExcelChartType.Column_Clustered;

// Specify the name of the series. This will be displayed as the text 
of the legend.
series.Name = "Sample Series";

// Specify the value ranges for the series.
series.Values = sheet.Range["B1:B5"];

// Specify the Category labels for the series.
series.CategoryLabels = sheet.Range["A1:A5"];
```

#### VB.NET
```vb
Imports Syncfusion.XlsIO
```

### API Reference
- **Namespace**: `Syncfusion.XlsIO`
- **Class**: `IWorkbook`
  - **Method**: `CreateWorkbook()`
- **Class**: `IWorksheet`
  - **Member**: `Range`
    - **Property**: `Number`
- **Class**: `IChart`
  - **Property**: `ChartTitle`
- **Class**: `IChartSerie`
  - **Property**: `SerieType`
  - **Property**: `Name`
  - **Property**: `Values`
  - **Property**: `CategoryLabels`

### Code Examples
The above examples demonstrate how to:
1. Create a new workbook and worksheet.
2. Populate the worksheet with chart data.
3. Add a chart to the worksheet.
4. Configure the chart type, title, and series.

### Conclusion
This example illustrates the process of exporting chart data and creating a proper chart in an Excel file using Syncfusion's XlsIO library for WinForms.

<!-- tags: [Syncfusion, WinForms, XlsIO, EssentialChart, Export] keywords: [chart export, Excel, cluster column chart, data export, chart data, Series, ChartTitle, CategoryLabels] -->
```