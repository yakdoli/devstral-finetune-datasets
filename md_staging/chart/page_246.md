```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_246.jpeg
document_name: chart
page_number: 246
page_id: chart#page_246
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:09Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Focuses on configuring the height of pie chart items based on area depth.
- Includes code examples in C# and VB.NET to demonstrate the configuration.

## Content

### Applies to Chart Types

| Applies to Chart Types | Pie Chart |
|------------------------|-----------|
|                        |           |

Here is some sample code.

#### C# Code Example
```csharp
this.chartControl1.Series[0].ConfigItems.PieItem.HeightByAreaDepth = true;
this.chartControl1.ChartArea.Depth = 25f;
```

#### VB.NET Code Example
```vb.net
Me.chartControl1.Series(0).ConfigItems.PieItem.HeightByAreaDepth = True
Me.chartControl1.ChartArea.Depth = 25f
```

### Pie Chart with Default Dimension
![Figure 145: Pie Chart with Default Dimension](./Illustates_HeightAreaByDepth.png)

**Figure 145: Pie Chart with Default Dimension**

---

## API Reference

### Namespace: 

#### Properties
- `HeightByAreaDepth`: Boolean property to determine if the height of a pie item should be based on the area's depth.
- `Depth`: Float property representing the depth of the chart area.

#### Methods
- `ConfigureChart()`: Configures the chart based on the specified properties.

### Parameters
- **Name** | **Type** | **Description** | **Default** | **Required**
- `HeightByAreaDepth` | Boolean | Determines the height configuration based on area depth. | False | No
- `Depth` | Float | Specifies the depth of the chart area. | 0 | No

### Returns
- None.

### Exceptions
- **InvalidOperationException**: Thrown when the chart control is not initialized properly.

### Code Examples
#### Configuring a Pie Chart in C#
```csharp
using Syncfusion.Windows.Forms.Chart.Internal;

class ChartConfiguration
{
    public void ConfigureChart()
    {
        this.chartControl1.Series[0].ConfigItems.PieItem.HeightByAreaDepth = true;
        this.chartControl1.ChartArea.Depth = 25f;
    }
}
```

#### Configuring a Pie Chart in VB.NET
```vb.net
Imports Syncfusion.Windows.Forms.Chart.Internal

Class ChartConfiguration
    Public Sub ConfigureChart()
        Me.chartControl1.Series(0).ConfigItems.PieItem.HeightByAreaDepth = True
        Me.chartControl1.ChartArea.Depth = 25f
    End Sub
End Class
```

---

<!-- tags: [Syncfusion Winforms, Chart, Pie Chart, HeightByAreaDepth, Depth, Configuration] keywords: [chart, pie, height, area depth, depth configuration, C#, VB.NET, sample code, chart control, series, area, 2D_RdG_Dec19_Q2132192] -->
```