```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_315.jpeg
document_name: chart
page_number: 315
page_id: chart#page_315
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:13Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### ShadowOffset Property

- In the provided C# example:
  ```csharp
  Private series.Styles(1).ShadowOffset = New Size(8, 8)
  Private series.Styles(2).ShadowOffset = New Size(6, 6)
  ```

- The corresponding VB.NET example mirrors the C# implementation.

### ShadowOffset in Action

![Figure 196: ColumnChart with ShadowOffset (7,7)](Illustrates ShadowOffset.png)

**Figure 196:** ColumnChart with ShadowOffset (7,7)

### Specific Data Point Setting

- **[C#]**
  ```csharp
  // For specific points
  series.Styles[0].ShadowOffset = new Size(7, 7);
  series.Styles[1].ShadowOffset = new Size(8, 8);
  series.Styles[2].ShadowOffset = new Size(6, 6);
  ```

- **[VB.NET]**
  ```vb
  ' For specific points
  Private series.Styles(0).ShadowOffset = New Size(7, 7)
  Private series.Styles(1).ShadowOffset = New Size(8, 8)
  Private series.Styles(2).ShadowOffset = New Size(6, 6)
  ```

## See Also

- Column Charts
- Bar Charts
- Line Charts
- Candle Chart
- Kagi Chart
- BoxandWhisker chart
- Histogram chart
- Polar and Radar Chart
- Point and Figure Chart
- Renko Chart
- Three Line Break Chart
- Gantt Chart
- Tornado Chart
- Pie Chart
- Area Chart
- Step Area Chart

## Page Footer

© 2013 Syncfusion. All rights reserved. | Page 315

<!-- tags: [syncfusion, windowsforms, chart, shadowoffset, columnchart, bardata, linedata, cakechart, kagichart, histogramchart, polar, radarchart, pointandfigurechart, renkochart, ganttchart, tornadochart, piechart, areachart, stepareachart] keywords: [shadowoffset, columnchart, bar chart, line chart, candle chart, kagi chart, boxandwhisker, histogram chart, polar chart, radar chart, point and figure chart, renko chart, three line break, gantt chart, tornado chart, pie chart, area chart, step area chart] -->
```