```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: QTP
page_number: 063
page_id: QTP#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:09Z
fidelity: lossless
-->

## 4.4 Essential Schedule

The following are the recorded methods and their corresponding descriptions for Essential Schedule:

### Schedule Control

| Method                              | Description                                              |
|-------------------------------------|----------------------------------------------------------|
| `DblClick(int row, int col)`       | Double-click a schedule row.                            |
| `RightClick(int row, int col)`     | Right-click a schedule row.                             |
| `TimeDrag(int row, int col, object newStartTime, object newEndTime)` | Adjust the timeline for an appointment. |
| `ItemDrag(int row, int col, object newStartTime, object newEndTime)` | Move appointment to some other timeline. |
| `Scroll(int value)`                | Scroll the schedule control.                             |

## 4.5 Essential Diagram

The following are the recorded methods and their corresponding descriptions for Essential Diagram:

### Diagram Control

| Method                                  | Description                                             |
|-----------------------------------------|---------------------------------------------------------|
| `ConnectNodes(string startNode, string endNode, string connector)` | Connects the specified nodes using the connector. |
| `SelectNode(string name)`              | Selects a diagram node.                                 |
| `DblClick(string name)`               | Double-clicks a diagram node.                           |
| `RotateNode(string node, float offset)` | Rotates a diagram node to the given offset.           |
| `ResizeNode(string node, float offsetX, float OffsetY)` | Resizes a diagram node to the given offset. |
| `MoveNode(string node, float offsetX, float OffsetY)` | Moves a diagram node to a new location. |
| `Zoom(float magnification)`           | Zoom the diagram view.                                   |
```