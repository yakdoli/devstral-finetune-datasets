```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_089.jpeg
document_name: diagram
page_number: 089
page_id: diagram#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:25Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Provides dynamic panning and zooming capabilities for diagrams.
- Features a view port window for modifying diagrams' origin and magnification.
- Important property is the Diagram property.

## Content

### 4.1.1 Overview Control

#### Overview of the Control

Overview Control provides a perspective view of a diagram model, and allows users to dynamically pan and zoom the diagrams. The control features a view port window that can be moved and / or resized using the mouse to modify the diagrams' origin and magnification properties at run-time.

The important property of the Overview Control is the Diagram property. The following are the list of properties of the Overview control.

| **Property**          | **Description**                                                                 |
|-----------------------|-----------------------------------------------------------------------------------|
| BackColor             | Background color of the component.                                              |
| AllowDrop             | Gets or sets a value indicating whether the control can accept the data that the user can drops on it. |
| BackgroundImage       | Background image of the component.                                              |
| BorderStyle           | Sets the border style for the component. It can be FixedSingle, Fixed3D or None. |
| Controls              | Indicates the collection of control within the component.                       |
| Enabled               | Indicates if the control is enabled.                                            |
| Dock                  | Indicates which control borders are docked to its parent control and determine how the control is resized with its parent. |
| Diagram               | Sets the corresponding diagram to the Overview Control.                         |
| Visible               | Sets the visibility of the control.                                             |

#### Important Events of Overview Control

The important events of Overview Control are listed below with their corresponding descriptions.

| **Event**                     | **Description**                                                                 |
|-------------------------------|-----------------------------------------------------------------------------------|
| Click                        | Occurs when the component is clicked.                                           |
| DoubleClick                  | Occurs when the component is double-clicked.                                    |
| ViewPortBoundsChanged        | Occurs when the controls viewport bounds is                                     |

## API Reference

### Properties

- **BackColor**: Background color of the component.
- **AllowDrop**: Indicates whether the control can accept the data that the user can drop on it.
- **BackgroundImage**: Background image of the component.
- **BorderStyle**: Sets the border style for the component (FixedSingle, Fixed3D, or None).
- **Controls**: Indicates the collection of controls within the component.
- **Enabled**: Indicates if the control is enabled.
- **Dock**: Indicates which control borders are docked to the parent control and how the control is resized with its parent.
- **Diagram**: Sets the corresponding diagram to the Overview Control.
- **Visible**: Sets the visibility of the control.

### Events

- **Click**: Occurs when the component is clicked.
- **DoubleClick**: Occurs when the component is double-clicked.
- **ViewPortBoundsChanged**: Occurs when the controls viewport bounds is changed.

## Code Examples

No specific code examples are provided in the text content.

## RAG Annotations

<!-- tags: [Syncfusion, Windows Forms, Diagram Control, Overview, Panning, Zooming, Runtime Properties, Event Handling] keywords: [Overview Control, Diagram property, Dynamic panning, Magnification, Viewport window, AllowDrop, BackgroundImage, BorderStyle, Controls, Enabled, Dock, ViewPortBoundsChanged, Click, DoubleClick] -->
```