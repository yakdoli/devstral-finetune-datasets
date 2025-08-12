```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_274.jpeg
document_name: chart
page_number: 274
page_id: chart#page_274
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:56Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

This section provides details about implementing histogram charts in Windows Forms applications. It includes code samples and examples to help users create and configure histogram charts effectively.

### Setting Intervals for Histogram Charts

#### C# Code Example

```csharp
// Set the desired number of intervals required for the histogram chart.
series.NumberOfHistogramIntervals = 20;
```

#### VB.NET Code Example

```vb.net
' Set the desired number of intervals required for the histogram chart.
series.NumberOfHistogramIntervals = 20
```

### Example of Histogram Chart

The following figure illustrates a histogram chart with the interval set to 20.

![Histogram Chart with Interval set to 20](chart_image.png)  
**Figure 163: Histogram Chart with Interval set to 20**

---

### See Also
- [Histogram Chart](Histogram_Chart_Link)

---

## 4.5.1.49 OpenCloseDrawMode

### Overview
This section describes the `OpenCloseDrawMode` property in the HiloOpenClose chart.

### Property Description
- **Name**: OpenCloseDrawMode
- **Description**: Gets or sets the open, close draw mode to the HiloOpenClose chart.

---

### API Reference

- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: HiloOpenClose

#### Members
- **OpenCloseDrawMode**
  - **Type**: Enumeration
  - **Purpose**: Specifies the drawing mode for open and close values in a HiloOpenClose chart.

#### Example Usage

```csharp
// Set the draw mode for open and close values
chart.Series[0].OpenCloseDrawMode = OpenCloseDrawMode.OpenClose;
```

---

### See also
- [OpenCloseDrawMode](OpenCloseDrawMode_Link)

---

<!-- Page-level Navigation/TOC -->
- [Histogram Chart](Histogram_Chart_Link)
- [OpenCloseDrawMode](OpenCloseDrawMode_Link)

---

<!-- tags: [Windows Forms, Histogram Chart, HiloOpenClose, Chart, Syncfusion Winforms, 11.4.0.26] keywords: [Histogram, Intervals, OpenCloseDrawMode, HiloOpenClose, Chart, DrawMode] -->
```