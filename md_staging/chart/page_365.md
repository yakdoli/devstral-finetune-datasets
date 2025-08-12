```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_365.jpeg
document_name: chart
page_number: 365
page_id: chart#page_365
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:13Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### 4.5.1.93 ZOrder

Specifies the order in which the objects are arranged and controls the visibility when one is placed over the other. 

By default, the ZOrder for series are assigned based on the order in which they are added to the Series collection.

| **Details**           |                                                                              |
|-----------------------|------------------------------------------------------------------------------|
| **Possible Values**   | Any integer value                                                           |
| **Default Value**     | The order that we add the series in the chart control.                    |
| **2D / 3D Limitations** | No                                                                     |
| **Applies to Chart Element** | Any Series                                                         |
| **Applies to Chart Types** | Gantt Chart, Histogram chart, Tornado Chart, Combination Chart, Box and Whisker Chart, Area Charts, Polar And Radar Chart, BarCharts, Column Charts, Bubble Charts, Candle Charts, Hilo Charts, Hilo Open Close Chart |

Here is sample code snippet using ZOrder.

- **[C#]**  
```csharp
this.chartControl1.Series[0].ZOrder = 0;
this.chartControl1.Series[1].ZOrder = 1;
```

- **[VB.NET]**  
```vbnet
Private Me.chartControl1.Series(0).ZOrder = 0
Private Me.chartControl1.Series(1).ZOrder = 1
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Chart

#### Property: ZOrder

- **Type:** `int`

- **Description:** Represents the z-order of the chart series. Specifies the drawing order of the series.

- **Default:** The order that we add the series in the chart control.

- **Parameters:** None

- **Returns:** An integer value representing the z-order.

## Code Examples

### C# Example

```csharp
this.chartControl1.Series[0].ZOrder = 0;
this.chartControl1.Series[1].ZOrder = 1;
```

### VB.NET Example

```vbnet
Private Me.chartControl1.Series(0).ZOrder = 0
Private Me.chartControl1.Series(1).ZOrder = 1
```

<!-- tags: [Syncfusion, Winforms, Chart, ZOrder, Series, Order, Visibility, Control, API, Version] keywords: [zorder, chart series, drawing order, visibility, control order, chart control, syncfusion windows forms] -->
```