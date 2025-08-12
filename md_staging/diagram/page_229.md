```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_229.jpeg
document_name: diagram
page_number: 229
page_id: diagram#page_229
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:22:56Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Illustrates the sequence of events for the `Z-Order Changing Event` and `Z-Order Changed Event`.
- Explains the `Connections And Ports Events` triggered during the creation of connections between nodes.

## Content

### Diagram Flow for Z-Order Events

#### Figure 142: Z-Order Changing Event

The diagram shows the process flow for handling the `Z-Order Changing Event`:

- **START**: Initiates the process.
- **PROCESS**: Handles the underlying logic for detecting changes.
- **CHECK**: Validates the new `ZOrder` value.
- **END**: Concludes the process.

#### Figure 143: Z-Order Changed Event

- Displays a dialog indicating that the `ZOrderChanged event is fired`, with the new `ZOrder` value shown as `6`.

### Connections And Ports Events

#### Section 4.6.8.2.5: Connections And Ports Events

**Description:**  
The following events are triggered while the connection is created between two nodes.

**Table Explanation:**  
The table below explains the `Connections` and `Ports` events.

| DocumentEventSink         | Description                          |
|---------------------------|--------------------------------------|
| ConnectionsChanged        | Triggered after the connection is changed. |
| PortsChanged              | Triggered when ports are added or changed. |

## Page-level Navigation/TOC (if applicable)

- **4.6.8.2.5 Connections And Ports Events**
  - Events triggered during the creation of connections between nodes.
  - Explanation of the `Connections` and `Ports` events.

<!-- tags: [syncfusion, winforms, z-order, events, connections, ports, version: 11.4.0.26] keywords: [diagram, process flow, z-order changing, z-order changed, event handling, connections changed, ports changed] -->
```