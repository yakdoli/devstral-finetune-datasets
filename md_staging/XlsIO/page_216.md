```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_216.jpeg
document_name: XlsIO
page_number: 216
page_id: XlsIO#page_216
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:23Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
sheet.Range["A3"].Text = "Feb";
sheet.Range["A4"].Text = "Mar";
sheet.Range["A5"].Text = "Apr";
sheet.Range["A6"].Text = "May";

// Random Data.
Random r = new Random();
for (int i = 2; i <= 6; i++)
{
    for (int j = 2; j <= 3; j++)
    {
        sheet.Range[i, j].Number = r.Next(0, 500);
    }
}

// Embedded Chart.
IChartShape chart = sheet.Charts.Add();

// Setting chart type.
chart.ChartType = ExcelChartType.Line;

// Setting the Chart Title.
chart.ChartTitle = "Product Sales comparison";

// Product A.
IChartSerie productA = chart.Series.Add("ProductA");
productA.Values = sheet.Range["B2:B6"];
productA.CategoryLabels = sheet.Range["A2:A6"];

// Product B.
IChartSerie productB = chart.Series.Add("ProductB");
productB.Values = sheet.Range["C2:C6"];
productB.CategoryLabels = sheet.Range["A2:A6"];
```

### [VB.NET]

```vb
' Inserting sample data for the chart.
sheet.Range("A1").Text = "Month"
sheet.Range("B1").Text = "Product A"
sheet.Range("C1").Text = "Product B"

' Months
sheet.Range("A2").Text = "Jan"
sheet.Range("A3").Text = "Feb"
sheet.Range("A4").Text = "Mar"
```

## API Reference (if applicable)
- `sheet.Range[string].Text`: Set or get the text of the specified range.
- `Random.Next(int, int)`**: Generates a random number within the specified range.
- `IChartShape`: Represents an embedded chart in the worksheet.
- `IChartShape.ChartType`: Sets the type of the chart.
- `IChartShape.ChartTitle`: Sets the title of the chart.
- `IChartSerie`: Represents a series in the chart.
- `IChartSerie.Values`: Set the values for the series.
- `IChartSerie.CategoryLabels`: Set the category labels for the series.

## Code Examples (multi-language supported)

### C#
```csharp
// Example of creating a line chart with random data
// Refer to the code above for implementation details.
```

### VB.NET
```vb
' Example of creating a line chart with static data
' Refer to the code above for implementation details.
```

<!-- tags: [xlsio, embedded chart, line chart, product sales comparison, chart, random data, month labels, c# and vb.net examples] keywords: [EmbeddedChart, LineChart, ProductSalesComparison, MonthLabels, ChartTitle, ChartSeries, RandomNumbers] -->
```