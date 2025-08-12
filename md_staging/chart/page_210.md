```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_210.jpeg
document_name: chart
page_number: 210
page_id: chart#page_210
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:52Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## 4.5.1.15 DrawHistogramNormalDistribution

The normal distribution curve is drawn by setting this property of the ChartSeries class to `true`.

### Details

| Possible Values | True or False |
|------------------|---------------|
| Default Value    | False         |
| 2D / 3D Limitations | No          |
| Applies to Chart Element | All series |
| Applies to Chart Types | Histogram Chart |

### Sample Code

#### [C#]

```csharp
// This draws the normal distribution curve for the histogram chart.
series2.DrawHistogramNormalDistribution = true;

// Set the desired number of intervals required for the histogram chart.
series2.NumberOfHistogramIntervals = 10;
```

#### [VB.NET]

```vb
' This draws the normal distribution curve for the histogram chart.
series2.DrawHistogramNormalDistribution = True

' Set the desired number of intervals required for the histogram chart.
series2.NumberOfHistogramIntervals = 10
```

<!-- tags: [syncfusion, winforms, chart, histogram, normal distribution] keywords: [chartseries, drawhistogramnormaldistribution, histogram chart, intervals, c#, vb.net] -->
```