```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_215.jpeg
document_name: XlsIO
page_number: 215
page_id: XlsIO#page_215
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:15Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to create and format charts in Excel using Series.
- Explains the process of adding data series and setting colors for the chart plot area and individual series.

## Content

### Chart Formatting and Series Example

#### Code Example: Setting Gradient Fill and Series Formatting
The following code snippet sets up a chart with a gradient fill and formats individual data series with different colors.

```csharp
chartPlotArea.Fill.FillType = ExcelFillType.Gradient

' Two Color
chartPlotArea.Fill.GradientColorType = ExcelGradientColor.TwoColor

' Set two colors.
chartPlotArea.Fill.BackColor = Color.FromArgb(205, 217, 234)
chartPlotArea.Fill.ForeColor = Color.White

' Format Data Series.
Dim chartAppleSerie As IChartSerie = chart.Series("Apples")

' Color of first serie.
chartAppleSerie.SerieFormat.AreaProperties.ForeColor = Color.Red
chartAppleSerie = chart.Series("Oranges")

' Color of second serie.
chartAppleSerie.SerieFormat.AreaProperties.ForeColor = Color.Orange
chartAppleSerie = chart.Series("Grapes")

' Color of third serie.
chartAppleSerie.SerieFormat.AreaProperties.ForeColor = Color.Purple
chartAppleSerie = chart.Series("Banana")

' Color of fourth serie.
chartAppleSerie.SerieFormat.AreaProperties.ForeColor = Color.Yellow

' Embedded chart position.
chart.TopRow = 10
chart.BottomRow = 40
chart.LeftColumn = 5
chart.RightColumn = 15
```

#### Explanation
- **Gradient Fill Setup**: The chart plot area is configured with a two-color gradient where the background color is set to a light gray `(205, 217, 234)` and the foreground color is white.
- **Series Color Formatting**: Individual data series ("Apples", "Oranges", "Grapes", "Banana") are accessed and their fill colors are set to red, orange, purple, and yellow, respectively.
- **Chart Position**: The chart is embedded in the worksheet, positioned between rows 10 and 40, and columns 5 to 15.

### Inserting Data for the Chart
The following code example shows how to insert sample data for the chart into an Excel sheet.

```csharp
[C#]

// Inserting sample data for the chart.
sheet.Range["A1"].Text = "Month";
sheet.Range["B1"].Text = "Product A";
sheet.Range["C1"].Text = "Product B";

// Months
sheet.Range["A2"].Text = "Jan";
```

#### Explanation
- **Data Header Setup**: Headers for the columns are added to cells A1, B1, and C1, representing "Month", "Product A", and "Product B", respectively.
- **Inserting Data**: The month "Jan" is entered into cell A2 as the first data point.

### Summary
This section demonstrates how to create and format Excel charts by adding and customizing data series. By setting different properties like gradient fill for the chart area and distinct fill colors for individual series, the visual representation of data can be tailored effectively.

## API Reference (if applicable)
- **`ExcelFillType.Gradient`**: Enumerates the fill type for the chart plot area.
- **`ExcelGradientColor.TwoColor`**: Specifies the gradient color type with two colors.
- **`IChartSerie`**: Represents a series in the chart.
- **`AreaProperties.ForeColor`**: Sets the foreground color of the series.
- **`Range.Text`**: Specifies the text content for a cell.

## Code Examples (multi-language supported)
The example showcases the use of C# for formatting Excel charts and inserting data.

<!-- tags: [xlsio, excel, chart, series, gradient, color, fill] keywords: [chart, series, gradient fill, color, data series, excel formatting, embedded chart] -->
```