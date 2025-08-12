```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_389.jpeg
document_name: chart
page_number: 389
page_id: chart#page_389
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:40Z
fidelity: lossless
--> 

## Essential Chart for Windows Forms

```csharp
layout1.Axes.Add(axis);
layout1.Axes.Add(axis0);
layout1.Axes.Add(axis1);
```

```vb
// Added the layout into ChartArea.
chartControl1.ChartArea.YLayouts.Add(layout1);
```

### [VB.NET]

```vb
' Created chart axes:

Dim axis As ChartAxis = Me.chartControl1.PrimaryYAxis
Dim axis0 As New ChartAxis(ChartOrientation.Vertical)
Dim axis1 As New ChartAxis(ChartOrientation.Vertical)

' Added chart axes into the chart:

chartControl1.Axes.Add(axis0)
chartControl1.Axes.Add(axis1)

' Created chart axis layout using ChartAxisLayout class: (New class)

Dim layout1 As New ChartAxisLayout()

' Added the axes to this layout including the primary axis:

layout1.Axes.Add(axis)
layout1.Axes.Add(axis0)
layout1.Axes.Add(axis1)

' Added the layout into ChartArea.

chartControl1.ChartArea.YLayouts.Add(layout1)
```

> **Note:** All the axes with the same orientation must be added to `ChartAxisLayout` (PrimaryAxis as well) as illustrated in the above code snippet.

### 4.6.5 Axis Value Type

You can set the value type for an axis using the `Axes.ValueType` property. You can set any of the following value types, of which the default is `double`.

## Page-level Navigation/TOC (if applicable)
- None

## Cross References
- None

<!-- tags: [Syncfusion Winforms, Chart, Axis Layout, Value Type, 11.4.0.26] keywords: [layout1, Axes, ChartArea, ChartAxis, PrimaryYAxis, Axis Orientation, double, ChartAxisLayout] -->
```