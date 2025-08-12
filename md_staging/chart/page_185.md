```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_185.jpeg
document_name: chart
page_number: 185
page_id: chart#page_185
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:05Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Details on possible values, default values, limitations, and applicability of the `ColumnDrawMode` in various chart types.
- Example code snippets in C# and VB.NET to set the `ColumnDrawMode` in a Column Chart.

## Content

### ColumnDrawMode Details

| Possible Values                           | Possible Values                                                                 |
|-------------------------------------------|---------------------------------------------------------------------------------|
| - InDepthMode<br> - PlaneMode<br> - ClusteredMode                                                                                 | - Columns from different series are drawn at different depths.<br> - Columns from all series are drawn side-by-side.<br> - Columns from all series are drawn in depth with the same size. |
| Default Value                             | InDepthMode                                                                    |
| 2D / 3D Limitations                      | 3D only                                                                        |
| Applies to Chart Element                   | All Series                                                                     |
| Applies to Chart Types                    | Column Chart, ColumnRange Chart, Bar Chart, BoxAndWhisker Chart, Gantt Chart |

### Sample Code Snippet

Here is the sample code snippet using `ColumnDrawMode` in Column Chart.

#### C#
```csharp
this.chartControl1.ColumnDrawMode = ChartColumnDrawMode.PlaneMode;
```

#### VB.NET
```vb
Me.chartControl1.ColumnDrawMode = ChartColumnDrawMode.PlaneMode
```

## Page-level Navigation/TOC (if applicable)

- This page covers the configuration and usage of `ColumnDrawMode` in Syncfusion Windows Forms Chart control, with a focus on different rendering modes for column-based charts.

## Cross References

- See also: the documentation on other chart customization features and properties in the Syncfusion Windows Forms Chart control.

## RAG Annotations
<!-- tags: Essential Chart, Windows Forms, ColumnDrawMode, 3D Charts, Chart Customization, VB.NET, C# keywords: Essential Chart, Windows Forms, ColumnDrawMode, 3D, Chart Customization, Bar Chart, BoxAndWhisker Chart, Gantt Chart, Column Range Chart -->
```