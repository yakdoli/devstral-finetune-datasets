```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_354.jpeg
document_name: chart
page_number: 354
page_id: chart#page_354
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:00Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Getting Started with ToolTips

### Overview
This section covers the configuration and usage of ToolTips for chart series in Windows Forms. The focus is on applying ToolTips to both the entire series and individual data points within a series.

#### Key Features Highlighted:
- Configuring ToolTips for Series
- Applying ToolTips to individual data points
- Usage scenarios and implementation details

---

### Specific Data Point Setting

#### Tooltip for Series

**ToolTip can be applied to individual points of a Series.**

```csharp
[C#]

for (int i = 0; i < series1.Points.Count; i++)
{
    series1.Stylies[i].ToolTip = string.Format("X = {0}, Y = {1}",
        series1.Points[0].X.ToString(),
        series1.Points[i].YValues[0]);
}
```

```vb
[VB]

Dim i As Integer = 0
Do While i < series1.Points.Count
    series1.Styles(i).ToolTip = String.Format("X = {0}, Y = {1}",
        series1.Points(i).X.ToString(),
        series1.Points(i).YValues(0))
    i += 1
Loop
```

---

### Example

The figure below illustrates the usage of ToolTips for a specific data point within a chart series.

![Figure 223: ToolTip set for Chart Series](https://via.placeholder.com/600x300?text=Figure+223:+ToolTip+set+for+Chart+Series)

---

## Conclusion

This section provides a detailed guide on how to configure and utilize ToolTips for chart series in Syncfusion Windows Forms. Understanding these concepts allows developers to enhance the interactivity and user experience of data visualizations.

---

### Code Examples

Below is the complete code example demonstrating the application of ToolTips to a chart series in both C# and VB.NET.

#### C#

```csharp
[C#]

// Example code for setting ToolTips on a Series
for (int i = 0; i < series1.Points.Count; i++)
{
    series1.Stylies[i].ToolTip = string.Format("X = {0}, Y = {1}",
        series1.Points[i].X.ToString(),
        series1.Points[i].YValues[0]);
}
```

#### VB.NET

```vb
[VB]

// Example code for setting ToolTips on a Series
Dim i As Integer = 0
Do While i < series1.Points.Count
    series1.Stylies(i).ToolTip = String.Format("X = {0}, Y = {1}",
        series1.Points(i).X.ToString(),
        series1.Points(i).YValues(0))
    i += 1
Loop
```

---

### References

- See also: [Tooltip in Chart Series](#)

---

### Notes

- Ensure that the series object `series1` is properly initialized and populated with data points before applying ToolTips.
- ToolTips can be customized further by modifying the `ToolTip` property with additional information or formatting.
- Always test tooltip functionality in different scenarios to ensure clarity and usability.

---

<!-- tags: [chart, tooltip, windows forms, syncfusion, Chart Series, data point, ToolTips] keywords: [ToolTip, Chart Series, data point, windows forms, tooltips, syncfusion] -->
```