```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_238.jpeg
document_name: XlsIO
page_number: 238
page_id: XlsIO#page_238
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:14Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
// Set floor fill option.
chart.Floor.Fill.FillType = ExcelFillType.Pattern;
chart.Floor.Fill.Pattern = ExcelGradientPattern.Pat_Divot;
chart.Floor.Fill.ForeColor = System.Drawing.Color.Blue;
chart.Floor.Fill.BackColor = System.Drawing.Color.White;
chart.Floor.Thickness = 3;

// First series and second category of the chart is filtered.
series[0].IsFiltered = true;
categories[1].IsFiltered = true;

// Series and category names of the chart are filtered.
chart.SeriesNameLevel = ExcelSeriesNameLevel.SeriesNameLevelNone;
chart.CategoryLabelLevel =
    ExcelCategoriesLabelLevel.CategoriesLabelLevelNone;

// Chart size setting.
chart.LeftColumn = 8;
chart.RightColumn = 16;
chart.TopRow = 9;
chart.BottomRow = 27;

// Setting legend.
chart.Legend.Position = ExcelLegendPosition.Right;
chart.Legend.IsVerticalLegend = false;

// Save the workbook.
workbook.SaveAs("Sample.xlsx");
```

### [VB]

```vb
' Set floor fill option.
chart.Floor.Fill.FillType = ExcelFillType.Pattern
chart.Floor.Fill.Pattern = ExcelGradientPattern.Pat_Divot
chart.Floor.Fill.ForeColor = System.Drawing.Color.Blue
chart.Floor.Fill.BackColor = System.Drawing.Color.White
chart.Floor.Thickness = 3

' First series and second category of the chart is filtered.
series(0).IsFiltered = true
categories(1).IsFiltered = true

' Series and category names of the chart are filtered.
chart.SeriesNameLevel = ExcelSeriesNameLevel.SeriesNameLevelNone
chart.CategoryLabelLevel = ExcelCategoriesLabelLevel.CategoriesLabelLevelNone

' Chart size setting.
chart.LeftColumn = 8
chart.RightColumn = 16
chart.TopRow = 9
chart.BottomRow = 27

' Setting legend.
chart.Legend.Position = ExcelLegendPosition.Right
chart.Legend.IsVerticalLegend = false

' Save the workbook.
workbook.SaveAs("Sample.xlsx")
```

## API Reference

- **Namespaces, Classes, Members:** (`ExcelFillType`, `ExcelGradientPattern`, `ExcelLegendPosition`, `ExcelSeriesNameLevel`, `ExcelCategoriesLabelLevel`, `IsFiltered`, `Position`, `IsVerticalLegend`)

## Code Examples

- C# Example: Demonstrates setting up a chart with fill options, filtering series and categories, size adjustments, legend settings, and saving the workbook.
- VB Example: Equivalent to the C# example, structured for Visual Basic.

## Page-level Navigation/TOC

- **Topics Covered:**
  - Floor fill options
  - Series and category filtering
  - Chart size setup
  - Legend customization
  - Saving the workbook

## Cross References

- **Related Topics:**
  - Chart formatting and styling
  - Workbook saving and file handling
  - Legend positioning and orientation

## RAG Annotations

<!-- tags: [XlsIO, chart, fill, filtering, legend, workbook, C#, VB] keywords: [ExcelFillType, ExcelGradientPattern, ExcelLegendPosition, ExcelSeriesNameLevel, ExcelCategoriesLabelLevel, IsFiltered, Position, IsVerticalLegend, SaveAs] -->
```