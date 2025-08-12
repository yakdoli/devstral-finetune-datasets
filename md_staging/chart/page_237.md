```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_237.jpeg
document_name: chart
page_number: 237
page_id: chart#page_237
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:03Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Types

### 4.5.1.30 GanttDrawMode

Specifies the drawing mode of Gantt chart.

| **Details**                    |                                                                                               |
|---------------------------------|------------------------------------------------------------------------------------------------|
| **Possible Values**            | - **AutoSizeMode** - Plots the Gantt Chart side by side.                                   |
|                                 | - **CustomPointWidthMode** - Plots the Gantt Chart as Overlapped.                          |
| **Default Value**              | **CustomPointWidthMode**                                                                    |
| **2D / 3D Limitations**       | None                                                                                         |
| **Applies to Chart Element**   | All series                                                                                  |
| **Applies to Chart Types**     | Gantt Chart                                                                                 |

#### Sample Code

[C#]

```csharp
// Specifies GanttDrawMode as CustomPointWidthMode
this.chartControl1.Series[0].GanttDrawMode = ChartGanttDrawMode.CustomPointWidthMode;
this.chartControl1.Series[0].Style.PointWidth = 0.7f;
this.chartControl1.Series[1].GanttDrawMode = ChartGanttDrawMode.CustomPointWidthMode;
this.chartControl1.Series[1].Style.PointWidth = 1f;
```

[VB.NET]

```vb
' Specifies GanttDrawMode as CustomPointWidthMode
Me.chartControl1.Series(0).GanttDrawMode = ChartGanttDrawMode.CustomPointWidthMode
Me.chartControl1.Series(0).Style.PointWidth = 0.7f
Me.chartControl1.Series(1).GanttDrawMode = ChartGanttDrawMode.CustomPointWidthMode
```

<!-- tags: [Syncfusion Winforms, GanttDrawMode, Chart, Gantt Chart, DrawMode, AutoSizeMode, CustomPointWidthMode] keywords: [Gantt chart, drawing mode, AutoSizeMode, CustomPointWidthMode, C#, VB.NET, sample code] -->
```