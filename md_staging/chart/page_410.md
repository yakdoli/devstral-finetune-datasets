```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_410.jpeg
document_name: chart
page_number: 410
page_id: chart#page_410
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:44Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
}
}
e.Handled = true;
}
```

### Visual Basic Code Example

```vb
[VB]

AddHandler chartControl1.ChartFormatAxisLabel, AddressOf chartControl1_ChartFormatAxisLabel

Dim series As ChartSeries = New ChartSeries("Series")
    series.Points.Add(0, 120)
    series.Points.Add(1, 220)
    series.Points.Add(2, 150)
    series.Points.Add(3, 240)

Me.chartControl1.Series.Add(series)

' Set labeltext
arrLabel.Add("India")
arrLabel.Add("Pakistan")
arrLabel.Add("Srilanka")
arrLabel.Add("Japan")

' Set tooltip content
arrTooltip.Add("IND")
arrTooltip.Add("PAK")
arrTooltip.Add("SRL")
arrTooltip.Add("JPN")
Me.chartControl1.ShowToolTips = True
Me.chartControl1.Series3D = True
Me.chartControl1.PrimaryYAxis.Title = "Product sold (Millions)"
Me.chartControl1.PrimaryXAxis.Title = "Country"
Me.chartControl1.Title.Text = "Product Sales"
```

This section demonstrates how to configure and customize chart properties, including adding data points, setting axis labels and tooltips, and enabling 3D visual effects for chart series in a Windows Forms application.

### Key Features Highlighted:
1. **Adding Chart Data Points**: Demonstrates adding multiple data points to a `ChartSeries`.
2. **Customizing Axis Labels**: Sets custom labels for the X-axis (countries) and Y-axis (product sold in millions).
3. **Enabling Tooltips**: Configures tooltips to display additional information when hovering over chart elements.
4. **3D Chart Series**: Turns on 3D rendering for enhanced visual impact.

<!-- tags: [chart, windows forms, axis labels, tooltips, 3d charts, visual basic, csharp] keywords: [syncfusion, Windows Forms, ChartSeries, ChartControl, data points, axis customization, 3D charts, tooltips, 2013] -->
```