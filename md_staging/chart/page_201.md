```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_201.jpeg
document_name: chart
page_number: 201
page_id: chart#page_201
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:08Z
fidelity: lossless
--> 

## Essential Chart for Windows Forms

### Overview
- This section discusses properties and their possible values related to chart elements in Windows Forms.
- Highlights the default value, support for 2D/3D limitations, applicability to chart elements and types.

### Content

#### Table: Chart Property Details
| **Possible Values**          | True, False |
|-------------------------------|-------------|
| **Default Value**            | False       |
| **2D / 3D Limitations**     | No          |
| **Applies to Chart Element** | All series and points |
| **Applies to Chart Types**   | All Chart types |

Here is some sample code.

#### Series wide setting

##### [C#]
```csharp
// Enabling DisplayText
this.chartControl1.Series[0].Style.DisplayText = true;
this.chartControl1.Series[0].Style.TextColor = Color.LightSlateGray;
```

##### [VB.NET]
```vb
' Enabling DisplayText
Me.chartControl1.Series(0).Style.DisplayText = True
Me.chartControl1.Series(0).Style.TextColor = Color.LightSlateGray
```

---

## API Reference

### Namespaces and Classes
- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: ChartControl

### Properties
- **DisplayText**:
  - **Type**: Boolean
  - **Description**: Controls whether the data points display text labels.
  - **Default Value**: False
  - **Applies To**: All series and points, across all chart types.
  
- **TextColor**:
  - **Type**: Color
  - **Description**: Specifies the color of the text displayed for data points.
  - **Default Value**: Default system color
  - **Applies To**: All series and points, across all chart types.

### Methods and Events
- **UpdateUI**: Updates the display of the chart control.
- **SeriesCollection**: Collection of series in the chart.

---

## Code Examples

### Enabling DisplayText in C#
```csharp
this.chartControl1.Series[0].Style.DisplayText = true;
this.chartControl1.Series[0].Style.TextColor = Color.LightSlateGray;
```

### Enabling DisplayText in VB.NET
```vb
Me.chartControl1.Series(0).Style.DisplayText = True
Me.chartControl1.Series(0).Style.TextColor = Color.LightSlateGray
```

---

## RAG Annotations
<!-- tags: [chart, series, displaytext, textcolor, winforms, syncfusion-sdk] keywords: [chartControl, DisplayText, TextColor, Series, Windows Forms, Syncfusion, 2D, 3D] -->
```