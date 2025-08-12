```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_245.jpeg
document_name: diagram
page_number: 245
page_id: diagram#page_245
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:47Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

To view a sample:

1. Open the Syncfusion Dashboard.
2. Click the Windows Forms drop-down list and select Run Locally Installed Samples.
3. Navigate to Diagram Samples > Product Showcase > Diagram Builder.

### 4.6.11 Preview for Symbol Palette Item

Essential Diagram for Windows Forms provides preview support for Symbol Palette. When you drag an item from Symbol Palette to Diagram View, Preview of the dragged item will be displayed. You can enable or disable the preview support.

#### Use Case Scenario

This feature displays a preview of the item you drag from Symbol Palette, thus enables you to identify the item you are dragging from the symbol palette to Diagram view.

#### Properties

| Property               | Description                                                                                     | Type | Data Type | Reference links |
|------------------------|-------------------------------------------------------------------------------------------------|------|-----------|-----------------|
| ShowDragNodeCue       | Gets or sets a value indicating whether preview is visible. The default value is true.         | NA   | Boolean    | NA              |
| DragNodeCueEnabled    | Gets or sets a value indicating whether preview is enabled. The default value is true.         | NA   | Boolean    | NA              |

#### Enabling Preview Support

To enable preview for the dragged item from Symbol Palette, set the `DragNodeCueEnabled` property of `PaletteGroupBar/PaletteGroupView` to `true`. To disable preview set this to `false`. By default this is set to `true`.

<!-- tags: [Windows Forms, Diagram Builder, Symbol Palette, Preview Support] keywords: [preview, drag, drop, enable, disable, dragNodeCueEnabled, shownodeseue, properties, feature, windows forms, diagram builder, essential diagram] -->
```