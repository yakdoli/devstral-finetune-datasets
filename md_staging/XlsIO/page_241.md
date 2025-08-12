```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_241.jpeg
document_name: XlsIO
page_number: 241
page_id: XlsIO#page_241
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:37Z
fidelity: lossless
-->

## Chart Customization Example in XlsIO

### Chart Styling and Filtering

#### Styling the Chart
The following code snippet demonstrates how to style and configure a chart's wall, floor, and series, including filtering specific categories and series.

```csharp
chart.Floor.Fill.FillType = ExcelFillType.Pattern
chart.Floor.Fill.Pattern = ExcelGradientPattern.Pat_Divot
chart.Floor.Fill.ForeColor = System.Drawing.Color.Blue
chart.Floor.Fill.BackColor = System.Drawing.Color.White
chart.Floor.Thickness = 3
```

#### Filtering Series and Categories
This section filters specific series and categories of the chart.

```csharp
series(0).IsFiltered = True
categories(1).IsFiltered = True
```

#### Hiding Series and Category Names
The chart's series and category names can be hidden as shown below.

```csharp
chart.SeriesNameLevel = ExcelSeriesNameLevel.SeriesNameLevelNone
chart.CategoryLabelLevel = ExcelCategoriesLabelLevel.CategoriesLabelLevelNone
```

### Positioning and Legend Configuration

#### Setting Chart Position
The chart's position on the worksheet can be defined as follows:

```csharp
chart.LeftColumn = 8
chart.RightColumn = 16
chart.TopRow = 9
chart.BottomRow = 27
```

#### Configuring the Legend
The legend can be customized for visibility and orientation.

```csharp
chart.Legend.Position = ExcelLegendPosition.Right
chart.Legend.IsVerticalLegend = False
```

### Saving the Workbook

Finally, the workbook is saved with the specified filename.

```csharp
workbook.SaveAs("Sample.xlsx")
```

## API Reference

- `ExcelFillType.Pattern`: Specifies the fill type of the chart floor.
- `ExcelGradientPattern.Pat_Divot`: Defines the pattern style for the chart floor.
- `System.Drawing.Color.Blue`: Sets the foreground color of the chart floor.
- `System.Drawing.Color.White`: Sets the background color of the chart floor.
- `ExcelSeriesNameLevel.SeriesNameLevelNone`: Indicates no series names are displayed.
- `ExcelCategoriesLabelLevel.CategoriesLabelLevelNone`: Indicates no category labels are displayed.

## Code Examples

The example demonstrates creating and configuring a chart with specific styles, filters, and positioning within a worksheet, ultimately saving it to a file.

### References

For more information on the Syncfusion XlsIO API, refer to the [official documentation](https://help.syncfusion.com/xlsio/overview).

<!-- tags: [XlsIO, chart customization, filtering, legend, positioning, ExcelFillType, ExcelGradientPattern, Syncfusion Winforms] keywords: [chart, fillType, pattern, color, filtering, legend position, workbook, saveAs] -->
```