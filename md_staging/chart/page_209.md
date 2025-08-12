```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_209.jpeg
document_name: chart
page_number: 209
page_id: chart#page_209
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:33Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

Here is an example of creating a line chart with horizontal error bars using Syncfusion WinForms. The code snippet below demonstrates how to configure and add error bars to a chart series.

## Content

### Setting Up a Line Chart with Error Bars

- **Code Example**
    ```csharp
    ' Type of Series
    s1.Type = ChartSeriesType.Line
    s1.ConfigItems.ErrorBars.Enabled = True
    
    ' Set the orientation to horizontal
    s1.ConfigItems.ErrorBars.Orientation = ChartOrientation.Horizontal
    s1.ConfigItems.ErrorBars.SymbolShape = ChartSymbolShape.None
    
    s1.Style.Interior = New Syncfusion.Drawing.BrushInfo(Color.Red)
    Me.chartControl1.PrimaryXAxis.DrawGrid = False
    Me.chartControl1.PrimaryYAxis.DrawGrid = False
    
    Me.chartControl1.Series.Add(s1)
    ```

    The above code snippet creates a line chart with horizontal error bars. It configures the error bars to have no symbol shape and sets the line style to red. The grid lines for both axes are disabled for a cleaner presentation.

### Visual Representation

- **Figure 118: Errorbar Orientation = "Horizontal"**
  ![LineChart with ErrorBars](https://i.imgur.com/1234567.png)

  The figure shows a line chart with horizontal error bars. The red lines indicate the error range at each data point.

### Additional Resources

- **See Also**
    - Line Chart
    - Column Chart
    - Hi Lo Chart
    - ErrorBarsSymbolShape

## API Reference

- **Classes**
    - `ChartSeriesType`
    - `ChartOrientation`
    - `ChartSymbolShape`
    - `BrushInfo`
    - `ChartControl`
    - `PrimaryXAxis`
    - `PrimaryYAxis`

## Code Examples

The code example provided above demonstrates how to configure a line chart with horizontal error bars. It can be directly used in a Syncfusion WinForms application to visualize data with error ranges.

## Page-level Navigation/TOC (if applicable)

- [Line Chart with Error Bars](#line-chart-with-error-bars)

## Cross References

- **See also**:
    - Line Chart
    - Column Chart
    - Hi Lo Chart
    - ErrorBarsSymbolShape

## RAG Annotations

<!-- tags: [charts, error bars, line chart, windows forms, syncfusion, orientation] keywords: [error bars, line chart, windows forms, horizontal orientation, error ranges, chart series, grid lines, error bars symbol shape] -->
```