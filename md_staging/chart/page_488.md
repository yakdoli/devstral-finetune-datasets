```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_488.jpeg
document_name: chart
page_number: 488
page_id: chart#page_488
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:23Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates setting up tooltips for chart series using C# and VB.NET.
- Illustrates the use of callbacks for each series' preparation style event.
- Explains how to apply formatting to tooltips to display percentages of a quota.

## Content

### Tooltip Formatting Example

#### C#

```csharp
// Setting the Tooltip Format
series1.PointsToolTipFormat = "{2}";

protected void series1_PrepareStyle(object sender, ChartPrepareStyleInfoEventArgs args)
{
    // Style formatting using a callback. You can apply the same settings directly on the series style on the
    // point styles.
    ChartSeries series = sender as ChartSeries;
    if (series != null)
    {
        args.Style.ToolTip = "Made " + (series.Points[args.Index].YValues[0] / 150) * 100) + "% of quota";
        args.Handled = true;
    }
}
```

#### VB.NET

```vb
' Setting the Tooltip Format
series1.PointsToolTipFormat = "{2}"

Protected Sub series1_PrepareStyle(ByVal sender As Object, ByVal args As ChartPrepareStyleInfoEventArgs)
    ' Style formatting using a callback. You can apply the same settings directly on the series style on the
    ' point styles.
    Dim series As ChartSeries = CType(IIf(TypeOf sender Is ChartSeries, sender, Nothing), ChartSeries)
    If Not series Is Nothing Then
        args.Style.ToolTip = "Made " + (series.Points[args.Index].YValues[0] / 150) * 100) + "% of quota"
        args.Handled = True
    End If
End Sub
```

### Explanation

The code snippets above show how to programmatically set up tooltips for chart series in a Windows Forms application using Syncfusion's chart control. The tooltips are formatted to display a percentage of a quota, calculated based on the Y-axis values of the chart data points. 

- **PointsToolTipFormat**: This property is used to define the basic tooltip format, where `{2}` likely refers to a placeholder for the Y-axis value.
- **PrepareStyle Event**: The `PrepareStyle` event is triggered for each data point in the series, allowing for customized formatting of tooltips and other styles.
- **Tooltip Calculation**: The tooltip value is calculated as a percentage of 150 by multiplying the Y-axis value by 100 and dividing by 150. The result is then formatted as a percentage.

### Tips for Customization

- You can apply similar formatting directly on the series style by modifying the point styles using the same logic.
- Ensure that the `PrepareStyle` event handler properly handles null or invalid series references to avoid runtime errors.

---

## Page-level Navigation/TOC (if applicable)
- The above content focuses on setting up tooltips for chart series in a Windows Forms application using Syncfusion's chart control.

## Cross References
- For more information on chart controls and their customization, refer to the Syncfusion Windows Forms documentation.

<!-- tags: [syncfusion, winforms, chart, tooltip, formatting, preparestyle] keywords: [C#, VB.NET, tooltip format, percentage, quota, preparation style, callback, programming, Windows Forms] -->
```