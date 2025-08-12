```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_310.jpeg
document_name: chart
page_number: 310
page_id: chart#page_310
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:01Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Specifies the appearance of the chart series using the `ShadingMode` property.

## Content

### 4.5.1.67 ShadingMode

Specifies the appearance of the chart series.

| **Details** |  |
|-------------|----------|
| **Possible Values** | • **FlatRectangle** - Displays in a flat rectangular format.<br/>• **PhongCylinder** - Displays in a cylindrical format. |
| **Default Value** | PhongCylinder |
| **2D / 3D Limitations** | No |
| **Applies to Chart Element** | All Series |
| **Applies to Chart Types** | Column Chart, BarCharts, Candle Chart, HiLO Chart, HiLOOpenClose Chart, Tornado chart, BoxandWhisker chart, Gantt Chart, Histogram Chart, Polar and Radar Chart |

Here is sample code snippet using ShadingMode.

#### C#
```csharp
this.chartControl1.Series[0].ConfigItems.ColumnItem.ShadingMode = ChartColumnShadingMode.FlatRectangle;
```

#### VB.NET
```vb
Private Me.chartControl1.Series(0).ConfigItems.ColumnItem.ShadingMode = ChartColumnShadingMode.FlatRectangle
```

## API Reference (if applicable)
- **Property**: ShadingMode
- **Description**: Specifies the appearance of the chart series.
- **Possible Values**:
  - FlatRectangle
  - PhongCylinder
- **Default Value**: PhongCylinder
- **Applies to**: All Series

## Code Examples (multi-language supported)
### C#
```csharp
this.chartControl1.Series[0].ConfigItems.ColumnItem.ShadingMode = ChartColumnShadingMode.FlatRectangle;
```

### VB.NET
```vb
Private Me.chartControl1.Series(0).ConfigItems.ColumnItem.ShadingMode = ChartColumnShadingMode.FlatRectangle
```

## Cross References
- See also: Chart Series, Series Appearance, Chart Types

<!-- tags: [Syncfusion Winforms, Chart, Series, Appearance, ShadingMode, version: 11.4.0.26] keywords: [chart control, series appearance, shading mode, flat rectangle, phong cylinder, series config items, column chart, bar charts, candle chart, hi-lo chart, tornado chart, boxandwhisker chart, gantt chart, histogram chart, polar chart, radar chart] -->
```