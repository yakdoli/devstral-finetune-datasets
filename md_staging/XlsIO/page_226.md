```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_226.jpeg
document_name: XlsIO
page_number: 226
page_id: XlsIO#page_226
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:37Z
fidelity: lossless
-->

## Content

### Chart Area Styling and Layout

The following code examples demonstrate how to manually position and resize chart elements, such as the chart title area, plot area, and legend, within a chart:

```csharp
chart.ChartTitleArea.Layout.Left = 1
chart.ChartTitleArea.Layout.Top = 20
' Manually positioning and resizing chart plot area
' Inner: Specifies that the plot area size shall determine the size of the plot area without including the tick marks and axis labels
chart.PlotArea.Layout.LayoutTarget = LayoutTargets.inner
chart.PlotArea.Layout.LeftMode = LayoutModes.edge
chart.PlotArea.Layout.TopMode = LayoutModes.edge
' Floating point value between -1 and 1
chart.PlotArea.Layout.Left = 50
chart.PlotArea.Layout.Top = 75
chart.PlotArea.Layout.Width = 300
chart.PlotArea.Layout.Height = 200
' Manually positioning and resizing chart legend
chart.Legend.Layout.LeftMode = LayoutModes.edge
chart.Legend.Layout.TopMode = LayoutModes.edge
chart.Legend.Layout.Left = 400
chart.Legend.Layout.Top = 150
chart.Legend.Layout.Width = 50
chart.Legend.Layout.Height = 100
' Saving the workbook to disk
workbook.SaveAs(fileName)
' Close the workbook
workbook.Close()
' No exception will be thrown if there are unsaved workbooks
excelEngine.ThrowNotSavedOnDestroy = False
excelEngine.Dispose()
```

### 4.2.2.3.2 Rich-Text Formatting for Chart Elements

**Overview**

- **Chart Titles and Data Labels**: Chart titles and data labels not linked to worksheet data can be directly edited on the chart.
- **Enhancing Appearance**: Rich-text formatting can be applied to chart elements to improve their visual appeal.

**Content**

Chart titles and data labels that are not linked to the worksheet data can be edited directly on the chart. You can also use rich-text formatting for the chart elements to enhance their appearance.

The following code examples explain how to apply rich-text formatting to the chart elements.
```markdown
## API Reference

This page does not provide specific API references. For detailed information on `LayoutTargets`, `LayoutModes`, and other relevant members, refer to the Syncfusion XlsIO API documentation.

## Code Examples

### Sample Code for Rich-Text Formatting in Chart Elements

This section includes example code demonstrating how to apply rich-text formatting to chart elements. Additional examples can be found in the Syncfusion XlsIO documentation.

## RAG Annotations

<!-- tags: XlsIO, Chart, Layout, Rich-Text Formatting, Workspace, Data Labels, UI, Formatting, Elements, Chart Styles, Workbook, LayoutModes, LayoutTargets, Visual Appeal, Enhancing Appearance, Direct Editing -->
```
```