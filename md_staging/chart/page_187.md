```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_187.jpeg
document_name: chart
page_number: 187
page_id: chart#page_187
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:21Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
This page discusses the `ColumnDrawMode` set to "ClusteredMode" and elaborates on the `ColumnWidthMode` for column charts in the Syncfusion Winforms library. It includes details on possible values and their implications.

## Content

### ColumnDrawMode and Figure

#### Figure 102: ColumnDrawMode set to "ClusteredMode"
![](https://cdn.example.com/figure102.png)
**Figure 102:** ColumnDrawMode set to "ClusteredMode"

**See Also:**
- Column Chart
- ColumnRange Chart
- Bar Chart
- BoxAndWhisker Chart
- Gantt Chart

### 4.5.1.5 ColumnWidthMode

#### Description
Specifies the width drawing mode for the columns in a column chart.

#### Details
**Possible Values:**

- **DefaultWidthMode:** The width of the columns will always be calculated to fill the space between columns.
- **FixedWidthMode:** The width should be given in Series.Points[i].YValues[1], in pixels. If the width of the columns are not given in point YValues[1], then they are calculated to fill the space between columns.
- **RelativeWidthMode:** Similar to the 

## API Reference
- Namespace: Syncfusion.Windows.Forms.Chart
- Class: ColumnWidthMode

| Enum Member | Description |
|-------------|-------------|
| DefaultWidthMode | Calculates the width to fill the space between columns. |
| FixedWidthMode | Uses a fixed width provided in Series.Points[i].YValues[1]. |
| RelativeWidthMode | Adjusts the width relative to other columns. |

## Cross References
- This section references other chart types like Column Chart, ColumnRange Chart, Bar Chart, BoxAndWhisker Chart, and Gantt Chart.

<!-- tags: [Syncfusion, Winforms, Chart, ColumnWidthMode, ColumnDrawMode, ClusteredMode] keywords: [ColumnWidthMode, ColumnDrawMode, DefaultWidthMode, FixedWidthMode, RelativeWidthMode, Syncfusion Windows Forms] -->
```