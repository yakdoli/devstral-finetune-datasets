```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_212.jpeg
document_name: XlsIO
page_number: 212
page_id: XlsIO#page_212
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:50Z
fidelity: lossless
-->

## ChartCustomization in XlsIO

- **Overview**:  
  - This section demonstrates how to customize chart borders and fill effects using the XlsIO library.
  - It includes detailed steps to set the style, color, weight, and fill effects for both the chart area and plot area.

## Content

```csharp
// Chart Area Customization

// Style
chartArea.Border.LinePattern = ExcelChartLinePattern.Solid;

// Color
chartArea.Border.LineColor = Color.Blue;

// Weight
chartArea.Border.LineWeight = ExcelChartLineWeight.Hairline;

// Area

// Fill Effects
chartArea.Fill.FillType = ExcelFillType.Gradient;

// Two Color
chartArea.Fill.GradientColorType = ExcelGradientColor.TwoColor;

// Set two colors.
chartArea.Fill.BackColor = Color.FromArgb(205, 217, 234);
chartArea.Fill.ForeColor = Color.White;

// Plot Area Customization

// Border

// Style
chartPlotArea.Border.LinePattern = ExcelChartLinePattern.Solid;

// Color
chartPlotArea.Border.LineColor = Color.Blue;

// Weight
chartPlotArea.Border.LineWeight = ExcelChartLineWeight.Hairline;

// Fill Effects
chartPlotArea.Fill.FillType = ExcelFillType.Gradient;

// Two Color
chartPlotArea.Fill.GradientColorType = ExcelGradientColor.TwoColor;

// Set two colors.
chartPlotArea.Fill.BackColor = Color.FromArgb(205, 217, 234);
chartPlotArea.Fill.ForeColor = Color.White;

```

## API Reference

### Namespace: Syncfusion.XlsIO

#### Classes
- **ExcelChartLinePattern**: Enumeration defining the line pattern styles.
- **ExcelChartLineWeight**: Enumeration defining the line weight styles.
- **ExcelFillType**: Enumeration defining the fill type styles.
- **ExcelGradientColor**: Enumeration defining the gradient color styles.

#### Methods
- **chartArea.Border.LinePattern**: Sets the line pattern of the chart area border.
- **chartArea.Border.LineColor**: Sets the line color of the chart area border.
- **chartArea.Border.LineWeight**: Sets the line weight of the chart area border.
- **chartArea.Fill.FillType**: Sets the fill type for the chart area.
- **chartArea.Fill.GradientColorType**: Sets the gradient color type for the chart area fill.
- **chartArea.Fill.BackColor**: Sets the background color for the chart area fill.
- **chartArea.Fill.ForeColor**: Sets the foreground color for the chart area fill.
- **chartPlotArea.Border.LinePattern**: Sets the line pattern of the plot area border.
- **chartPlotArea.Border.LineColor**: Sets the line color of the plot area border.
- **chartPlotArea.Border.LineWeight**: Sets the line weight of the plot area border.
- **chartPlotArea.Fill.FillType**: Sets the fill type for the plot area.
- **chartPlotArea.Fill.GradientColorType**: Sets the gradient color type for the plot area fill.
- **chartPlotArea.Fill.BackColor**: Sets the background color for the plot area fill.
- **chartPlotArea.Fill.ForeColor**: Sets the foreground color for the plot area fill.

## Code Examples

The provided code snippet demonstrates how to customize the chart area and plot area in an Excel chart using the XlsIO library. This includes setting the border style, color, weight, and fill gradient for both areas.

### Example: Customizing Chart and Plot Area

```csharp
using Syncfusion.XlsIO;

// Create a new Excel engine
ExcelEngine engine = new ExcelEngine();
IApplication application = engine.Excel;

// Create a new workbook
IWorkbook workbook = application.Workbooks.Create();

// Access the first worksheet
IWorksheet worksheet = workbook.Worksheets[0];

// Add data to the worksheet
worksheet.Range["A1"].Text = "Month";
worksheet.Range["B1"].Text = "Sales";
worksheet.Range["A2"].Text = "Jan";
worksheet.Range["B2"].Text = "1000";
worksheet.Range["A3"].Text = "Feb";
worksheet.Range["B3"].Text = "1500";

// Add a chart
IChart chart = worksheet.Charts.Add(ChartType.Bar2DClustered, 2, "A1:B3");

// Get the chart area
IChartArea chartArea = chart.ChartAreas[0];

// Set the chart area border
chartArea.Border.LinePattern = ExcelChartLinePattern.Solid;
chartArea.Border.LineColor = Color.Blue;
chartArea.Border.LineWeight = ExcelChartLineWeight.Hairline;

// Set the chart area fill
chartArea.Fill.FillType = ExcelFillType.Gradient;
chartArea.Fill.GradientColorType = ExcelGradientColor.TwoColor;
chartArea.Fill.BackColor = Color.FromArgb(205, 217, 234);
chartArea.Fill.ForeColor = Color.White;

// Get the plot area
IChartFrameFormat chartPlotArea = chart.PlotArea;

// Set the plot area border
chartPlotArea.Border.LinePattern = ExcelChartLinePattern.Solid;
chartPlotArea.Border.LineColor = Color.Blue;
chartPlotArea.Border.LineWeight = ExcelChartLineWeight.Hairline;

// Set the plot area fill
chartPlotArea.Fill.FillType = ExcelFillType.Gradient;
chartPlotArea.Fill.GradientColorType = ExcelGradientColor.TwoColor;
chartPlotArea.Fill.BackColor = Color.FromArgb(205, 217, 234);
chartPlotArea.Fill.ForeColor = Color.White;

// Save the workbook
workbook.Save("ChartCustomization.xlsx");

// Dispose of the engine
engine.Dispose();
```

## See also
- [Syncfusion XlsIO Documentation](https://help.syncfusion.com/xlsio/overview)
- [Customizing Chart Appearance in XlsIO](https://help.syncfusion.com/xlsio/chart#customizing-chart-appearance)

<!-- tags: [xlsio, chart, customization, border, fill, gradient, syncfusion, winforms] keywords: [chart area, plot area, line pattern, line color, line weight, gradient fill, two color, background color, foreground color, customization, appearance] -->
```