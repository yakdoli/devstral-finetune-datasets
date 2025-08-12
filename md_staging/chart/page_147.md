```html
<!--  
source: image  
domain: syncfusion-sdk  
task: pdf-ocr-to-markdown  
language: en (keep original; do not translate)  
source_filename: page_147.jpeg  
document_name: chart  
page_number: 147  
page_id: chart#page_147  
product: Syncfusion Winforms  
version: 11.4.0.26  
timestamp: 2025-08-09T03:24:02Z  
fidelity: lossless  
-->  

## Doughnut Chart  

### DoughnutCoefficient  

PieCharts specified with a **DoughnutCoefficient** will be rendered as the Doughnut chart. By default, this value is set to `0.0` and hence the chart will be rendered as a full pie. The DoughnutCoefficient property specifies the fraction of radius occupied by the doughnut whole. Hence the value can range from `0.0` to `0.9`.  

```csharp
this.chartControl1.Series(0).ConfigItems.PieItem.DoughnutCoefficient=0.5f;
```  

```vb
Me.chartControl1.Series(0).ConfigItems.PieItem.DoughnutCoefficient=0.5f
```  

![Figure 82: Pie Chart with DoughnutCoefficient Property Set](https://i.imgur.com/U3uHjlt.png)

### HeightCoefficient  

When in 3D mode, the relative height of the pie chart can be specified via the **HeightCoefficient** property. Note that the **HeightByAreaDepth** property should be set as `false` for this to take effect. The valid values are `0.1f` to `0.5f`. This property is set to `0.2f` by default.  

```csharp
this.chartControl1.Series[0].ConfigItems.PieItem.HeightByAreaDepth = 
```  

## API Reference  

### DoughnutCoefficient  

- **Property:** `DoughnutCoefficient`
- **Type:** `float`
- **Description:** Specifies the fraction of radius occupied by the doughnut whole in the pie chart.
- **Range:** `0.0` to `0.9`
- **Default:** `0.0`

### HeightCoefficient  

- **Property:** `HeightCoefficient`
- **Type:** `float`
- **Description:** Specifies the relative height of the pie chart in 3D mode.
- **Range:** `0.1f` to `0.5f`
- **Default:** `0.2f`

### HeightByAreaDepth  

- **Property:** `HeightByAreaDepth`
- **Type:** `bool`
- **Description:** Determines whether the height of the pie segments is based on their area or depth.
- **Default:** `false`

## Code Examples  

### C#  

```csharp
// Setting the DoughnutCoefficient
this.chartControl1.Series(0).ConfigItems.PieItem.DoughnutCoefficient = 0.5f;

// Setting the HeightCoefficient
this.chartControl1.Series(0).ConfigItems.PieItem.HeightByAreaDepth = false;
this.chartControl1.Series(0).ConfigItems.PieItem.HeightCoefficient = 0.3f;
```  

### VB.NET  

```vb
' Setting the DoughnutCoefficient
Me.chartControl1.Series(0).ConfigItems.PieItem.DoughnutCoefficient = 0.5f

' Setting the HeightCoefficient
Me.chartControl1.Series(0).ConfigItems.PieItem.HeightByAreaDepth = False
Me.chartControl1.Series(0).ConfigItems.PieItem.HeightCoefficient = 0.3f
```  
```html
 <!-- tags: [Syncfusion, DoughnutCoefficient, HeightCoefficient, WinForms, Chart] keywords: [DoughnutCoefficient, HeightCoefficient, 3D mode, 3D pie chart, PieChart] --> 
```