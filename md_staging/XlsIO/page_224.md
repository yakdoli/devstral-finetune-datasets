```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_224.jpeg
document_name: XlsIO
page_number: 224
page_id: XlsIO#page_224
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:02Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explore how to resize and position chart elements such as titles, legends, and plot areas in Excel charts.
- Address spacing issues caused by lengthy chart elements.
- Specify exact positions for chart elements in the chart area.

## Resizing and Positioning of Chart Elements

Chart elements such as chart title, legend, and plot area, can be positioned and resized easily as needed. To avoid spacing problems caused by the lengthy chart titles, plot area, or legends, the user can change the way that how these elements have to be positioned in the chart. You can also specify the exact position of the chart elements in the chart area.

The following code examples illustrate how to resize and position the chart elements.

```csharp
[C#]
' Step 1: Instantiate the spreadsheet creation engine
ExcelEngine excelEngine = new ExcelEngine();
' Step 2: Instantiate the excel application object
IApplication application = excelEngine.Excel;
IWorkbook workbook = 
application.Workbooks.Open(@"../../Data/Sample.xlsx",
ExcelOpenType.Automatic);
IWorksheet sheet = workbook.Worksheets[0];
IChart chart = sheet.Charts[0];

//Manually positioning chart title
//Edge: Specifies that the width or Height will be interpreted as right
// or bottom of the chart element
//Factor: Specifies that the width or Height will be interpreted as the
// width or height of the chart element
chart.ChartTitleArea.Layout.LeftMode = LayoutModes.edge;
chart.ChartTitleArea.Layout.TopMode = LayoutModes.edge;
//Value in points should not be a negative value if LayoutMode is Edge
//It can be a negative value if the LayoutMode is Factor.
chart.ChartTitleArea.Layout.Left = 1;
chart.ChartTitleArea.Layout.Top = 20;

//Manually positioning and resizing chart plot area
//Inner: Specifies that the plot area size will determine the size of
// the plot area, without including the tick marks and axis labels
chart.PlotArea.Layout.LayoutTarget = LayoutTargets.inner;
chart.PlotArea.Layout.LeftMode = LayoutModes.edge;
chart.PlotArea.Layout.TopMode = LayoutModes.edge;
chart.PlotArea.Layout.Left = 50;
chart.PlotArea.Layout.Top = 75;
```

## API Reference
### LayoutModes
Specifies how the position or size of a chart element is interpreted.  
- **Edge**: Specifies positional measurement relative to the edge.  
- **Factor**: Specifies positional measurement relative to the width or height of the chart element.

### LayoutTargets
Specifies the target area for chart layout adjustments.  
- **Inner**: Adjusts plot area size excluding tick marks and axis labels.

## Code Examples
The code above demonstrates:
1. Instantiating the Excel engine and application object.
2. Opening a workbook and accessing the chart elements.
3. Adjusting the chart title and plot area using the `LayoutMode` property.
4. Specifying target areas and positioning values using `LayoutTarget`.

## Cross References
- Refer to the documentation on chart formatting and customization for more information on additional chart properties.
- See related sections on chart elements and their attributes for comprehensive guidance.

<!-- tags: XlsIO, Chart Elements, Chart Title, Plot Area, LayoutModes, LayoutTargets, C#, .NET, Syncfusion Winforms keywords: Excel chart elements, resizing charts, positioning charts, chart title, plot area, layout modes, layout targets -->
```