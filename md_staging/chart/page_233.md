```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_233.jpeg
document_name: chart
page_number: 233
page_id: chart#page_233
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:51Z
fidelity: lossless
-->

## Chart Configuration

### Overview
- Configure Funnel Chart elements based on Y value as height or width.
- Examples provided for C# and VB.NET coding.

---

### Configuration Details

| **Default Value**                      | **YIsHeight**           |
|-----------------------------------------|--------------------------|
| **2D / 3D Limitations**                | No                       |
| **Applies to Chart Element**           | All series               |
| **Applies to Chart Types**             | Funnel Chart             |

---

### Code Examples

#### C#
```csharp
this.chartControl1.Series[0].ConfigItems.FunnelItem.FunnelMode = 
ChartFunnelMode.YIsHeight;

this.chartControl1.Series[0].ConfigItems.FunnelItem.FunnelMode = 
ChartFunnelMode.YIsWidth;
```

#### VB.NET
```vb
Me.chartControl1.Series(0).ConfigItems.FunnelItem.FunnelMode = 
ChartFunnelMode.YIsHeight

Me.chartControl1.Series(0).ConfigItems.FunnelItem.FunnelMode = 
ChartFunnelMode.YIsWidth
```

---

### API Reference

- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: ChartFunnelMode
- **Enum Members**:
  - YIsHeight
  - YIsWidth

---

### Cross References
- See also: [Funnel Chart Documentation] (Link to detailed Funnel Chart guide)

<!-- tags: [product, module, control, api, version?] keywords: [chart, funnel chart, yisheight, yiswidth, syncfusion winforms, 11.4.0.26] -->
```