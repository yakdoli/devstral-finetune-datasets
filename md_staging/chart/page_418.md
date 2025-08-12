```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_418.jpeg
document_name: chart
page_number: 418
page_id: chart#page_418
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:10Z
fidelity: lossless
-->

## 3-D Related

### Overview
- Detailed properties that influence rendering of axis in 3-D mode.
- Explains how to enable 3-D rendering using the `Series3D` property.
- Describes various properties like `RealMode3D`, `Depth`, `Tilt`, `Rotation`, and more.
- Includes examples in both C# and VB.NET to demonstrate 3-D rendering configurations.

### Content

#### Chart Control Property and Description

| Chart Control Property | Description |
|-------------------------|-------------|
| Series3D               | Specifies if the chart should be rendered in 3-D mode. |
| RealMode3D             | Specifies if the chart should be rendered in a 3-D plane. |
| Depth                  | Specifies the depth of the axes in the z-coordinate. Default value is 50f. |
| Tilt                   | Specifies the tilt angle relative to the y-axis. Default value is 30f. |
| Rotation               | Specifies the angle of rotation relative to the x-axis. Default value is 30f. |
| ColumnDrawMode         | Specifies the mode of column drawing when in 3-D. |
|                         | - **PlaneMode**: Columns from different series are drawn with the same depth. |
|                         | - **InDepthMode**: Columns from different series are drawn with different depths. |
| EnableMouseRotation     | Enables rotation of the chart at runtime using middle/right mouse button. |

---

#### 3D Mode Sample

**C#**

```csharp
this.chartControl1.Series3D = true;
this.chartControl1.Depth = 55F;
this.chartControl1.Tilt = 55F;
this.chartControl1.Rotation = 60;
```

**VB.NET**

```vb
Me.chartControl1.Series3D = True
Me.chartControl1.Depth = 55F
```

## Page-level Navigation/TOC (if applicable)
- 4.6.11 3-D Related

## Cross References
- None explicitly mentioned in the current page content.

<!-- tags: [Syncfusion Winforms, chart, 3-D, axis rendering, Series3D, RealMode3D, Depth, Tilt, Rotation, ColumnDrawMode, EnableMouseRotation] keywords: [3-D rendering, axis properties, chart control,Series3D property, Solid plane draw mode, 3DMode Property] -->
```