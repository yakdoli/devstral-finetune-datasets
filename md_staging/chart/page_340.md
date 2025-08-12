```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_340.jpeg
document_name: chart
page_number: 340
page_id: chart#page_340
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:19Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Detailed information about chart types such as Column Charts, Bar Charts, Bubble Chart, Financial Chart, Line Charts, BoxandWhisker Chart, Gantt chart, Tornado chart, Radar Chart, Polar Chart, Area Charts, and Scatter Chart.
- Focuses on the `Text (Series)` property, which specifies the chart series text displayed in the legend at runtime.

## Content

### 4.5.1.81 Text (Series)
It specifies the chart series text. This will be displayed at run-time in the legend.

#### Details
| Property             | Description                                      |
|----------------------|--------------------------------------------------|
| Possible Values      | Any string value                                 |
| Default Value        | Name of the series                               |
| 2D / 3D Limitations | No                                               |
| Applies to Chart Element | Any Series                                 |
| Applies to Chart Types | All Chart Types                                |

Text can be set directly by using the Series object.

#### Sample Code Snippet

The text can be set as shown in the following C# and VB.NET code examples.

```csharp
// C#

// Here the series text will be taken from the series name
ChartSeries series1 = 
    this.chartControl1.Model.NewSeries("August", ChartSeriesType.Column);

// Add points to series1.
// .....
// .....

// Here, the text is given explicitly.
ChartSeries series2 = 
    this.chartControl1.Model.NewSeries("June", ChartSeriesType.Column);
series2.Text = "JuneSales";
```

```vb
// VB.NET

// [Sample VB.NET code is not provided in the image; use the C# example as a reference.]
```

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Chart
- **Class:** ChartSeries
- **Property:** Text (Series)
  - **Description:** Specifies the chart series text.
  - **Possible Values:** Any string value
  - **Default Value:** Name of the series
  - **Applicable Chart Types:** All Chart Types

## Code Examples

### C#
The following C# code demonstrates setting the series text explicitly:

```csharp
ChartSeries series2 = 
    this.chartControl1.Model.NewSeries("June", ChartSeriesType.Column);
series2.Text = "JuneSales";
```

### VB.NET
A VB.NET example is not explicitly provided in the given image. However, it can be inferred as follows:

```vb
Dim series2 As ChartSeries = 
    Me.chartControl1.Model.NewSeries("June", ChartSeriesType.Column)
series2.Text = "JuneSales"
```

### Cross References
- Refer to the relevant sections on different chart types for more detailed information on their usage and customization.

## RAG Annotations
<!-- tags: [chart, windows forms, syncfusion, series text, legend, text properties] keywords: [chart series, legend text, 2D/3D charts, chart types, series object] -->
```