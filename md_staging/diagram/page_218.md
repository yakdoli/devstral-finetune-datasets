```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_218.jpeg
document_name: diagram
page_number: 218
page_id: diagram#page_218
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:22:04Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates the use of a simple flow diagram with the Vertex Changed Event.
- Explains the concept of pinpoint events and their triggers when changing a node's location.

## Content

### 4.6.8.2.2 PinPoint Events

When changing the node's location, the pinpoint of the node will be reset. The below table contains pinpoint events and descriptions.

#### Figure: Simple Flow Diagram

**Figure 135: Diagram with Vertex Changed Event**

![Simple Flow Diagram](https://i.imgur.com/unknown_image_url.png)
*Note: Placeholder image. Replace with actual diagram image if available.*

#### PinPoint Events Table

| DocumentEventSink          | Description                                            |
|----------------------------|--------------------------------------------------------|
| PinOffsetChanged           | Triggered after the offset of the pinpoint is reset.  |
| PinOffsetChanging          | Triggered when the offset of the pinpoint is changed. |

---

## Cross References
- Refer to Section 4.6.8.2 for related events and their handling.

<!-- tags: [Syncfusion Winforms, Diagram, Flow Diagram, Vertex Changed Event, Pinpoint Events] keywords: [simple flow diagram, vertex changed event, pinpoint events, node location, pinpoint offset] -->
```