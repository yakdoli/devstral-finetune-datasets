```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_207.jpeg
document_name: diagram
page_number: 207
page_id: diagram#page_207
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:58Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates the use of a simple flow diagram in Windows Forms.
- Focuses on handling the "Tool Deactivated Event."
- Discusses origin events and their behavior.

## Content

### Simple Flow Diagram

The flow diagram illustrates a basic workflow:

- **START**: Initializes the process.
- **PROCESS**: Executes the main processing logic.
- **CHECK**: Performs a check operation.
- **END**: Marks the completion of the process.

**Figure 129: Tool Deactivated Event**

![Tool Deactivated Event](https://example.com/tool-deactivated-event.png)

This figure shows a message box indicating that the ZoomTool has been deactivated.

### 4.6.8.1.3 Origin Events

#### Description
The origin changes when the diagram window is scrolled either horizontally or vertically.

#### Origin Events
Origin events are as follows:

| DiagramViewerEventSink          | Description                                   |
|----------------------------------|-----------------------------------------------|
| **OriginChanged**               | Triggered when the origin is changed.         |

#### Data Retrieval and Setting
Data can be retrieved or set by using the following members.

## Page-level Navigation/TOC (if applicable)
- 4.6.8.1.3 Origin Events

## Cross References
See also:
- [Handling Scroll Events in Windows Forms](#scrolling-events-in-windows-forms)

## RAG Annotations
<!-- tags: [winforms, diagram, flow-diagram, origin-events, zoomtool, syncfusion-sdk] keywords: [origin, scroll, tool deactivated, event handling, synchronization, window origin] -->
```