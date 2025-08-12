```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_200.jpeg
document_name: chart
page_number: 200
page_id: chart#page_200
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:33Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates shadow settings in a bar chart.
- Explains how to set specific data point shadows using code examples in C# and VB.NET.
- Provides information on displaying text labels at data points.

## Content

### Specific Data Point Setting

#### [C#]
```csharp
this.chartControl1.Series[0].Styles[0].DisplayShadow = true;
this.chartControl1.Series[0].Styles[1].DisplayShadow = true;
```

#### [VB.NET]
```vbnet
Me.chartControl1.Series(0).Styles(0).DisplayShadow = True
Me.chartControl1.Series(0).Styles(1).DisplayShadow = True
```

**See Also**
- Line Charts
- Area Chart
- Bubble Chart
- Column Chart
- Stacking Column Chart
- Stacking Column100 Chart
- Bar Chart
- Pie Chart
- Candle Chart
- Kagi Chart
- Point and Figure Chart
- Renko Chart
- Three line Break Chart
- Gantt Chart
- Histogram chart
- Tornado Chart
- Combination Chart
- Box and Whisker Chart
- Polar And Radar Chart
- Step Area Chart

### 4.5.1.11 DisplayText

#### Overview
Indicates whether a label indicating the data point value should be displayed at the data points.

### Details

<!-- Additional details would be added here if available from the image -->

## References
- **Figure 111: Line Chart with Shadow Series**

## Appendix

### Legal Notice
© 2013 Syncfusion. All rights reserved.

<!-- tags: [chart, shadow settings, windows forms, display text, data point labels, see also, line chart, area chart, bubble chart, column chart, stacking column chart,她们，历史上所有的真人真事，从来没有一刀两断。她们经历了所有的人生高低起伏，最终才走到今天这个位置。这是真实的、真实的故事，揭示了她们背后所付出的千辛万苦。我们一起去揭开她们的神秘面纱！]

### More Details
- Namespace: Syncfusion.Windows.Forms.Chart
- Class: ChartSeries
- Property: DisplayShadow

### Related Methods/Properties
- DisplayLabel

### Example Usage (C#)
```csharp
// Example on how to enable shadow and display text
chartControl1.Series[0].Styles[0].DisplayShadow = true;
chartControl1.Series[0].Styles[0].DisplayText = "Show Data Point: {Y}";
```

### Example Usage (VB.NET)
```vbnet
' Example on how to enable shadow and display text
Me.chartControl1.Series(0).Styles(0).DisplayShadow = True
Me.chartControl1.Series(0).Styles(0).DisplayText = "Show Data Point: {Y}"
```

### Conclusion
This section provides insights into advanced customization features of the Syncfusion Chart control in Windows Forms, enabling developers to enhance the visual presentation of charts by adding shadows and displaying data point labels. -->
```