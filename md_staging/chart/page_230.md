```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_230.jpeg
document_name: chart
page_number: 230
page_id: chart#page_230
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:56Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Overview

- Displays a figure of a Funnel Chart with a square base.
- Explains the concept of `FillMode` in detail.

### Funnel Chart with Figure Base = "Square"

#### Figure 132: Funnel Chart with Figure Base = "Square"

**See Also:**
- Pyramid Chart, Funnel Chart

---

### 4.5.1.27 FillMode

Specifies how the slice interior should be filled with gradient colors.

| **Details**                                      |
|--------------------------------------------------|
| **Possible Values**                             | - `AllPie`: Controls the interior shape style of All Pieltem. <br> - `EveryPie`: Controls the interior shape style of Every Pieltem. |
| **Default Value**                               | `AllPie`                                              |
| **2D / 3D Limitations**                        | No                                                   |
| **Applies to Chart Element**                   | All series                                           |
| **Applies to Chart Types**                     | Pie Chart                                             |

---

### Sample Code

#### C#

```csharp
// Setting Pie type
this.chartControl.Series[0].ConfigItems.PieItem.PieType = ChartPieType.Round;
// Setting the interiors of shapes in this GraphicsPath object are filled.
this.chartControl.Series[0].ConfigItems.PieItem.FillMode = ChartPieFillMode.EveryPie;
```

#### VB.NET

```vb
' Setting Pie type
Me.chartControl.Series(0).ConfigItems.PieItem.PieType = ChartPieType.Round
' Setting the interiors of shapes in this GraphicsPath object are
```

---

## Page-level Navigation/TOC (if applicable)

- **4.5.1.27 FillMode**: Specifies how the slice interior should be filled with gradient colors.
- **Sample Code**: Includes examples in both C# and VB.NET for setting the pie type and fill mode.

---

### Cross References

- **See Also:** Pyramid Chart, Funnel Chart

<!-- tags: essential chart, windows forms, funnel chart, fillmode, gradient colors, pie chart, sample code, c#, vb.net, syncfusion winforms, version: 11.4.0.26 -->
```