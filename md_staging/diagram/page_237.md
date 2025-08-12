```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_237.jpeg
document_name: diagram
page_number: 237
page_id: diagram#page_237
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:23Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Describes the flow of events in a property changed scenario.
- Details events related to labels and layers in the diagram.

## Content

### Property Changed Event

#### Workflow

- **START**: Initiates the event sequence.
- **PROCESS**: Implements the property change logic.
- **CHECK**: Validates the new property value.
- **END**: Concludes the event process.
- **PropertyChanging Event**: Indicates that a property is about to be changed.
  - **Property Name**: `LineStyle.LineColor`
  - **New Value**: `Color [DarkBlue]`
- **PropertyChange Event**: Confirms the property has been changed.

![Figure 147: Property Changed Event](https://example.com/property-changed-event.png)

### Labels And Layers Events

#### Overview

The following events are triggered when adding or removing labels and layers to or from the diagram:

#### Label Events

| DocumentEventSink         | Description                                      |
|---------------------------|--------------------------------------------------|
| LabelsChanged             | Triggered when labels are added.                |
| LayersChanged             | Triggered when layers are added to the model.  |

#### Data Retrieval And Setting

Data can be retrieved or set using the following members.

## API Reference

- **Events**:
  - `LabelsChanged`
  - `LayersChanged`

## See also

- Relevant cross-references and additional documentation.

<!-- tags: [property-changed-event, labels-events, layers-events, diagram-control, syncfusion-winforms, windows-forms] keywords: [propertychanging, propertychange, labels, layers, event-handling, event-registration, event-triggers, winforms-diagram, syncfusion-tools] -->
```