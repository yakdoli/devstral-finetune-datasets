```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_330.jpeg
document_name: chart
page_number: 330
page_id: chart#page_330
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:06Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.chartControl1.SpacingBetweenPoints = 70;
```

```vb
Me.chartControl1.SpacingBetweenSeries = 70
```

## See Also

- Column Chart
- Bar Chart
- HiLo Chart
- HiLo Open Close Chart
- Candle Chart
- Tornado Chart
- Box and Whisker Chart

---

### 4.5.1.77 Stacking Group

This section illustrates how to group the stacking series with another stacking series.

1. In order to group the stacking series with another stacking series in chart control, you need to set a StackingGroup property of the chart series with the desired group name.
   
The below example demonstrates the code on setting the StackingGroup for the series in the Chart control.

#### C#

```csharp
ChartSeries ser1 = new ChartSeries("Series 1");
ser1.Type = ChartSeriesType.StackingColumn;
// specifying group name .
ser1.StackingGroup = "FirstGroup";

ChartSeries ser2 = new ChartSeries("Series 2");
ser2.Type = ChartSeriesType.StackingColumn;
// specifying group name .
ser2.StackingGroup = "SecondGroup";

ChartSeries ser3 = new ChartSeries("Series 3");
ser3.Type = ChartSeriesType.StackingColumn;
// specifying group name .
ser3.StackingGroup = "FirstGroup";
```

#### VB

```vb
[VB]
```

---

© 2013 Syncfusion. All rights reserved. 330 | Page
```