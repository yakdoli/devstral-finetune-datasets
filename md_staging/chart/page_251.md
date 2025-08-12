```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_251.jpeg
document_name: chart
page_number: 251
page_id: chart#page_251
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:51Z
fidelity: lossless
-->

Essential Chart for Windows Forms

Bar Charts, Pie Chart, Funnel Chart, Pyramid Chart, Bubble Chart, Column Chart, Area Chart, Stacking Area Chart, Stacking Area100 Chart, Line Charts, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar And Radar Chart, Hi Lo Chart, Hi Lo Open Close Chart

### 4.5.1.37 HitTestRadius

HitTestRadius property controls the circle around this point, which will be considered within the bounds of this point for hit-testing purposes. The ChartRegion events such as ChartRegionClick, ChartRegionMouseDown, ChartRegionMouseHover, ChartRegionMouseLeave, ChartRegionMouseMove, and ChartRegionMouseEnter, are being affected by this property.

| **Details**             |
|--------------------------|
| **Possible Values**     | A double values                  |
| **Default Value**       | 7.5                             |
| **2D / 3D Limitations**| None                            |
| **Applies to Chart Element** | All series             |
| **Applies to Chart Types** | Line Chart and Step Line Chart |

Here is some sample code.

```csharp
// Specifies the circle radius around the point for HitTest
this.chartControl1.Series[0].Style.HitTestRadius = 20;

// ChartClick Event will be fired if clicked within the above circle
void chartControl1_ChartRegionClick(object sender,
Syncfusion.Windows.Forms.Chart.ChartRegionMouseEventArgs e)
{
    // Message appears when User hits the test radius region
    if (e.Region.IsChartPoint)
    {
        MessageBox.Show("Point is Hit");
    }
}
```

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

<!-- tags: [WinForms, Chart, HitTestRadius] keywords: [HitTestRadius, ChartRegionClick, ChartRegionMouseEvents, LineChart, StepLineChart, HitTesting, SampleCode] -->
```