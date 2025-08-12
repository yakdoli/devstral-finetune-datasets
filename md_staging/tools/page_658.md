```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_658.jpeg
document_name: tools
page_number: 658
page_id: tools#page_658
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:57Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Facilitates expand and collapse options for the GradientPanelExt, with image provisions.
- Allows images to be placed along any of the panel borders with gradient background.
- Enables text inclusion in the GradientPanelExt's borders.
- Supports placement of any Windows Forms or custom .NET Control along the panel borders.

## Content

### GradientPanelExt Primitives

- **Collapse Primitive**: Facilitates expand and collapse option for the GradientPanelExt, with image provisions.
- **Image Primitive**: Images can be placed along any of the panel borders with gradient background.
- **Text Primitive**: Text can be included in the GradientPanelExt's borders.
- **Host Primitive**: Any Windows Forms or custom .NET Control can be placed along the panel borders.

The primitives for the GradientPanelExt can be included using the **GradientPanelExt PrimitiveCollection Editor**, which can be opened using the **primitives** property.

### PrimitiveCollection Editor Interface

The **GradientPanelExt PrimitiveCollection Editor** allows configuration of various properties for each primitive added to the GradientPanelExt. Below is an example configuration:

#### Interface Layout

- **Left Panel**:
  - Lists the primitives currently added to the GradientPanelExt.
  - Example primitives: `hostPrimitive1`, `hostPrimitive2`, `textPrimitive1`, `textPrimitive2`.

- **Right Panel**:
  - Displays properties for the selected primitive in the left panel.
  - **Appearance**:
    - `BackColor`: White
    - `BorderColor`: Black
    - `PrimitiveBorderStyle`: None
  - **Behavior**:
    - `HostControl`: button1
    - `Visible`: True
  - **Data**: Placeholder for data settings.
  - **Design**:
    - `(Name)`: hostPrimitive1
    - `GenerateMember`: True
    - `Modifiers`: Private
  - **Layout**:
    - `Alignment`: Top
    - `Position`: 0
    - `Size`: 60, 20

#### Control Actions
- **Types of primitive**: A dropdown to select the type of primitive to add (e.g., Collapse).
- **Add**: Adds a new primitive to the list.
- **Remove**: Removes the selected primitive from the list.
- **OK**: Applies changes and closes the editor.
- **Cancel**: Closes the editor without applying changes.

**Figure 405: GradientPanelExt Primitive Collection Editor**

<!-- tags: [syncfusion, winforms, gradientpanel, primitives, tools, editor] keywords: [gradientpanel, primitives, expand/collapse, image placement, text inclusion, host controls, primitive collection editor, appearance properties, behavior properties, design properties, layout properties, collapse primitive, image primitive, text primitive, host primitive] -->
```