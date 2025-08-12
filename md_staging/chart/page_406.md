```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_406.jpeg
document_name: chart
page_number: 406
page_id: chart#page_406
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:33Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Table of Chart Properties

| Property | Description |
| --- | --- |
| HidePartialLabels | When this property is set to true and when label overlap occurs, the chart will selectively hide certain labels (usually the min and max labels to begin with) to keep the rest of labels readable. Default value is false. |

## Clipping Protection

- **ClippingProtection**: Uses some intelligent logic to avoid clipping.

## Code Examples

### C#

```csharp
this.ChartWebControl1.PrimaryXAxis.HidePartialLabels = true;
this.ChartWebControl1.PrimaryXAxis.LabelIntersectAction = ChartLabelIntersectAction.Rotate;
```

### VB

```vb
Me.ChartWebControl1.PrimaryXAxis.HidePartialLabels = True
Me.ChartWebControl1.PrimaryXAxis.LabelIntersectAction = ChartLabelIntersectAction.Rotate
```

### Figure: Intersecting Labels

![Unique Visitors Count](https://i.imgur.com/Figure-261.png)

*Figure 261: Intersecting Labels*

## Grouping Labels

### 4.6.8.4 Grouping Labels

This section discusses the grouping labels feature in charts.

---

<!-- tags: [chart, WinForms, grouping labels, ClippingProtection, HidePartialLabels, labelIntersectAction, Syncfusion, version: 11.4.0.26] keywords: [chart, Windows Forms, labels, grouping, clipping protection, label intersection, interactivity, synchronization] -->
```