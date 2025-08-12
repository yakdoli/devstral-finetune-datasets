```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_203.jpeg
document_name: diagram
page_number: 203
page_id: diagram#page_203
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:46Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This page discusses the concept of node collection events in the context of a simple flow diagram.
- It showcases two types of events: `Node Collection Changing Event` and `Node Collection Changed Event`.
- These events are demonstrated using flow diagrams and corresponding dialog boxes.

## Content

### Simple Flow Diagram

#### Figure 126: Node Collection Changing Event
- **Diagram Description**: 
  - The flow diagram starts with a "START" node.
  - A message box appears indicating that the `NodeCollectionChanging event fired`.
  - The process node follows the start node.

#### Figure 127: Node Collection Changed Event
- **Diagram Description**:
  - A similar flow diagram is shown, with the "START" node leading to a "PROCESS" node.
  - A dialog box indicates that a "Node added" event has occurred.
  - The flow concludes with a "CHECK" node.

## API Reference

The diagram demonstrates two key events related to node collections in Diagrams:

### NodeCollectionChanging Event
- Triggered when the node collection is about to change. This can be used for validation or to prevent modifications.

### NodeCollectionChanged Event
- Triggered after a change has been made to the node collection. This can be used for updates or notifications.

## Page-level Navigation/TOC (if applicable)

- **Navigation**: 
  - This page focuses on the node collection events within the Diagram control of Syncfusion WinForms.
  - It is part of the larger section on Diagrams in the user guide.

<!-- tags: [Syncfusion, WinForms, Diagram, NodeCollectionChanging, NodeCollectionChanged] keywords: [node collection, event, start, process, check, dialog box, flow diagram] -->
```