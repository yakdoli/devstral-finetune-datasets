```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_461.jpeg
document_name: chart
page_number: 461
page_id: chart#page_461
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:07Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

To restrict the zoom-in factor to a certain level on the x and y axis use the `MinZoomFactorX` and `MinZoomFactorY` properties. The value can be in between 0 and 1. 1 means not zoomed.

## Zooming via Keyboard

Essential Chart also enables users to use keyboard shortcuts to enable zooming. Enable this feature through the `KeyZoom` property.

Using the following properties the zooming action can be mapped to specific keys.

| Chart control Property | Description |
| --- | --- |
| ZoomCancel | Specifies the keyboard shortcut to control Zoom cancel. The default value is ESCAPE. |
| ZoomDown | Specifies the keyboard shortcut to control Zoom Down. The default value is DOWN arrow. |
| ZoomIn | Specifies the keyboard shortcut to control Zoom In. The default value is ADD key. |
| ZoomLeft | Specifies the keyboard shortcut to control Zoom Left. The default value is LEFT arrow. |
| ZoomOut | Specifies the keyboard shortcut to control Zoom Out. The default value is SUBTRACT. |
| ZoomRight | Specifies the keyboard shortcut to control Zoom Right. The default value is RIGHT arrow. |
| ZoomUp | Specifies the keyboard shortcut to control Zoom Up. The default value is UP arrow. |

## Panning Support for Zoomed Chart

Now, you will be able to pan a chart when it is zoomed. Set the `ChartControl.MouseAction` to 'Panning' to enable this feature. Set the `MouseAction` to 'None' to disable this feature. The panning action can be controlled using the `ZoomActions` property that is available for individual axis.

| Chart Axes Property | Description |
| --- | --- |
| ZoomActions | Specifies the zoom action on the corresponding axis. The options are, |

<!-- tags: [chart, Essential Chart for Windows Forms, zooming, keyboard shortcuts, panning, WinForms] keywords: [MinZoomFactorX, MinZoomFactorY, KeyZoom, ESCAPE, ADD, SUBTRACT, LEFT, RIGHT, UP, DOWN, zoom cancel, zoom in, zoom out, zoom left, zoom right, MouseAction, Panning, None, ZoomActions] -->
```