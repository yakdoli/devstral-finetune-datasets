<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_214.jpeg
document_name: XlsIO
page_number: 214
page_id: XlsIO#page_214
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:27Z
fidelity: lossless
-->

# Essential XlsIO

```vbasic
chart.PrimaryValueAxis.Title = "Months"

' Show Data Table.
chart.HasDataTable = True

' Format Chart Area.
Dim chartArea As IChartFrameFormat = chart.ChartArea

' Border

' Style
chartArea.Border.LinePattern = ExcelChartLinePattern.Solid

' Color
chartArea.Border.LineColor = Color.Blue

' Weight
chartArea.Border.LineWeight = ExcelChartLineWeight.Hairline

' Area

' Fill Effects
chartArea.Fill.FillType = ExcelFillType.Gradient

' Two Color
chartArea.Fill.GradientColorType = ExcelGradientColor.TwoColor

' Set two colors.
chartArea.Fill.BackColor = Color.FromArgb(205, 217, 234)
chartArea.Fill.ForeColor = Color.White

' Plot Area
Dim chartPlotArea As IChartFrameFormat = chart.PlotArea

' Border

' Style
chartPlotArea.Border.LinePattern = ExcelChartLinePattern.Solid

' Color
chartPlotArea.Border.LineColor = Color.Blue

' Weight
chartPlotArea.Border.LineWeight = ExcelChartLineWeight.Hairline

' Fill Effects
```

## Content

The provided code snippet demonstrates how to format a chart in an Excel document using the XlsIO library. Below is a detailed explanation of the code:

### 1. Naming the Primary Value Axis
- `chart.PrimaryValueAxis.Title = "Months"`
  - This line sets the title of the primary value axis to "Months". This axis typically represents the vertical axis in a chart.

### 2. Displaying the Data Table
- `chart.HasDataTable = True`
  - This enables the visibility of the data table associated with the chart, allowing users to view the data represented in the chart.

### 3. Formatting the Chart Area
#### a. Border Formatting
- **Line Pattern**: `chartArea.Border.LinePattern = ExcelChartLinePattern.Solid`
  - Sets the border line pattern to a solid line.
- **Line Color**: `chartArea.Border.LineColor = Color.Blue`
  - Sets the color of the border to blue.
- **Line Weight**: `chartArea.Border.LineWeight = ExcelChartLineWeight.Hairline`
  - Specifies the thickness of the border as "Hairline," which is a very thin line.

#### b. Area Fill Effects
- **Fill Type**: `chartArea.Fill.FillType = ExcelFillType.Gradient`
  - Indicates that the chart area fill will use a gradient effect.
- **Gradient Color Type**: `chartArea.Fill.GradientColorType = ExcelGradientColor.TwoColor`
  - Specifies that the gradient will use two distinct colors.
- **Back and Fore Colors**: 
  - `chartArea.Fill.BackColor = Color.FromArgb(205, 217, 234)`
  - `chartArea.Fill.ForeColor = Color.White`
    - Sets the starting and ending colors of the gradient to a light grayish-blue and white, respectively.

### 4. Plot Area Formatting
#### a. Border Formatting
- **Line Pattern**: `chartPlotArea.Border.LinePattern = ExcelChartLinePattern.Solid`
  - Sets the border line pattern to a solid line.
- **Line Color**: `chartPlotArea.Border.LineColor = Color.Blue`
  - Sets the color of the border to blue.
- **Line Weight**: `chartPlotArea.Border.LineWeight = ExcelChartLineWeight.Hairline`
  - Specifies the thickness of the border as "Hairline."

#### b. Area Fill Effects
- The code snippet mentions "Fill Effects," but the specific implementation is not provided in the given code snippet.

## API Reference
### Namespaces and Types Used
- `IChartFrameFormat`
- `ExcelChartLinePattern`
- `Color`
- `ExcelChartLineWeight`
- `ExcelFillType`
- `ExcelGradientColor`

### Methods Used
- `PrimaryValueAxis.Title`
- `HasDataTable`
- `ChartArea.Border.LinePattern`
- `ChartArea.Border.LineColor`
- `ChartArea.Border.LineWeight`
- `ChartArea.Fill.FillType`
- `ChartArea.Fill.GradientColorType`
- `ChartArea.Fill.BackColor`
- `ChartArea.Fill.ForeColor`
- `PlotArea.Border.LinePattern`
- `PlotArea.Border.LineColor`
- `PlotArea.Border.LineWeight`
- `Color.FromArgb`

## Code Examples

### VB.NET Example
The code snippet provided is already in VB.NET, demonstrating how to format the chart area and plot area.

### Note
- The code snippet focuses on setting styles, colors, and gradients for both the chart area and plot area, enhancing the visual appeal of the chart in the Excel document.

## Cross References
- See the XlsIO documentation for more details on chart customization and formatting options.

<!-- tags: [Syncfusion Winforms, XlsIO, Chart Formatting, Chart Area, Plot Area, Gradient Fill, Border Styling] keywords: [chart, axis, data table, gradient, color, line pattern, line weight] -->