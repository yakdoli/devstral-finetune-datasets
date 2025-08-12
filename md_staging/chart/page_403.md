```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_403.jpeg
document_name: chart
page_number: 403
page_id: chart#page_403
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:25Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
// Setting drawing mode
this.chartControl1.PrimaryXAxis.TickLabelsDrawingMode = ChartAxisTickLabelDrawingMode.UserMode;

// Adding new labels
this.chartControl1.PrimaryXAxis.Labels.Add(new ChartAxisLabel("Q1 Mid Point", Color.OrangeRed, new Font("Arial", 8F, System.Drawing.FontStyle.Bold), new DateTime(2007, 2, 15), "", "", ChartValueType.Custom));
this.chartControl1.PrimaryXAxis.Labels.Add(new ChartAxisLabel("Q2 Mid Point", Color.OrangeRed, new Font("Arial", 8F, System.Drawing.FontStyle.Bold), new DateTime(2007, 5, 15), "", "", ChartValueType.Custom));
```

```vb
' Setting drawing mode
Me.chartControl1.PrimaryXAxis.TickLabelsDrawingMode = ChartAxisTickLabelDrawingMode.UserMode

' Adding new labels
Me.chartControl1.PrimaryXAxis.Labels.Add(New ChartAxisLabel("Q1 Mid Point", Color.OrangeRed, New Font("Arial", 8F, System.Drawing.FontStyle.Bold), New DateTime(2007, 2, 15), "", "", ChartValueType.Custom))
Me.chartControl1.PrimaryXAxis.Labels.Add(New ChartAxisLabel("Q2 Mid Point", Color.OrangeRed, New Font("Arial", 8F, System.Drawing.FontStyle.Bold), New DateTime(2007, 5, 15), "", "", ChartValueType.Custom))
```

<!-- tags: [chart, axis, labels, drawing mode, custom labels, winforms, syncfusion chart] keywords: [chartControl, PrimaryXAxis, TickLabelsDrawingMode, ChartAxisTickLabelDrawingMode.UserMode, ChartAxisLabel, Font, FontStyle.Bold, DateTime, ChartValueType.Custom] -->
```