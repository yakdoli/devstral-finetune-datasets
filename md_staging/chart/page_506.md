```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_506.jpeg
document_name: chart
page_number: 506
page_id: chart#page_506
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:19Z
fidelity: lossless
-->

## Chart Title Positioning and Appearance in Windows Forms

### Overview
- Modifying chart title positioning using `ChartTitle` properties: `Position`, `Alignment`, and `Behavior`.
- Customizing the look and feel of the chart title with various appearance options.

### Chart Title Property Overview

| ChartTitle Property | Description                                                                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Position**         | Specifies the position relative to the chart at which to render the chart title panel. <br> <ul> <li>**Top** - above the chart (Default setting)</li> <li>**Left** - left of the chart</li> <li>**Right** - right of the chart</li> <li>**Bottom** - below the chart</li> <li>**Floating** - will not be docked to any specific location. Can be docked manually by dragging the title panel.</li> </ul> |
| **Alignment**        | When docked to a side, this property specifies how the title panel should be aligned with respect to the chart boundaries. <br> <ul> <li>**Center** - will be aligned to center. Default setting.</li> <li>**Far** - will be aligned Far.</li> <li>**Near** - will be aligned Near.</li> </ul> |
| **Behavior**         | Specifies the docking behavior of the title. <br> <ul> <li>**Docking** - It is dockable on all four sides.</li> <li>**Movable** - It is movable.</li> <li>**All** - It is movable and dockable.</li> <li>**None** - It is neither movable nor dockable.</li> </ul> |

### Title Look and Feel
There are several appearance options that can be applied on the `ChartTitle` instance as illustrated in this `ChartTitle` Collection Editor.

<!-- tags: [Syncfusion, WinForms, Chart, ChartTitle, Chart properties, appearance] keywords: [ChartTitle, Position, Alignment, Behavior, Charttitle properties, appearance options, Charttitle editor] -->
```