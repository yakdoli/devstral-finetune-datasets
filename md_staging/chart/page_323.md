```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_323.jpeg
document_name: chart
page_number: 323
page_id: chart#page_323
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:42Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page discusses the configuration and behavior of chart labels in Syncfusion Winforms.
- It introduces the `SmartLabels` feature, which controls how chart labels are rendered to avoid overlapping.

## Content

### Chart Labels Configuration

#### Figure 203: ShowTicks = "False"

![Figure: ShowTicks = "False"](image.jpg)  
**Figure 203: ShowTicks = "False"**

- This figure illustrates the distribution of various expenses as percentages in a donut chart. The labels are shown without tick marks (`ShowTicks = "False"`).

#### See Also
- [Pie Chart](Pie Chart)

### 4.5.1.73 SmartLabels

#### Specification of Label Behavior
Specifies the behavior of the labels. If set to true, the labels will be rendered to avoid overlap with other labels.

| **Details**       |                                                                 |
|--------------------|-----------------------------------------------------------------|
| **Possible Values**| • True - Enables smart labels                                <br>• False - Disables smart labels |
| **Default Value**   | False                                                          |
| **2D / 3D Limitations** | No                                                           |
| **Applies to Chart Element** | Any Series                                            |
| **Applies to Chart Types** | All chart types                                        |

## API Reference

### Properties
- **SmartLabels**: A property that controls the rendering behavior of labels to prevent overlap.

### Usage
```csharp
// Enable smart labels in a chart
Chart chart = new Chart();
chart.SmartLabels = true;
```

## Code Examples

### Enabling SmartLabels in a Chart
```csharp
using Syncfusion.Windows.Forms.Chart;

Chart chart = new Chart();
chart.SmartLabels = true;
```

## Cross References
- [Pie Chart](Pie Chart)

### Footnotes
- © 2013 Syncfusion. All rights reserved.

<!-- tags: [chart, winforms, smartlabels, labels, overlap, syncfusion] keywords: [smartlabels, labels, overlap, chart properties, winforms] -->
```