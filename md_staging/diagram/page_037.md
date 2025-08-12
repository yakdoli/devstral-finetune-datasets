```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: diagram
page_number: 037
page_id: diagram#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:09:56Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

### Overview
- This section provides a guide on programmatically adding and configuring a PaletteGroupBar control in a .NET Windows Forms application.
- It explains the step-by-step procedure for creating a PaletteGroupBar control both design-time and code-wise.
- The document includes visual examples and code snippets for integrating the PaletteGroupBar control.

## Content

### Figure 16: Designer Form Window Added with PaletteGroupBar Control

This figure illustrates the Designer Form Window with a PaletteGroupBar control added. Key components highlighted include:
- **PaletteGroupBar:** A control group that allows the user to organize buttons or controls into logical groups.
- **Smart Tag:** A feature that provides quick access to common properties and tasks for the control.
- **Diagram:** Visual representation and configuration settings of the PaletteGroupBar in the application.

#### 3.2.2.2 Creating a PaletteGroupBar Control through code
This section details the step-by-step procedure to create a PaletteGroupBar control programmatically in a .NET Windows Forms application.

**Instructions:**
To create a PaletteGroupBar control using code:
1. **Create a new Windows Forms application.**
   - Begin by setting up a new Windows Forms project in your Integrated Development Environment (IDE).
2. **Add the following basic dependent Syncfusion assemblies to the project:**
   - **Syncfusion.Core.dll**
   - **Syncfusion.Diagram.Base.dll**
   - **Syncfusion.Diagram.Windows.dll**
   - **Syncfusion.Shared.Base.dll**
     - These assemblies are necessary for leveraging the Syncfusion controls and functionalities within your application.
3. **Create a PaletteGroupBar control using the following code:**
   - Code examples will be provided in the subsequent sections to demonstrate the implementation.

## API Reference

### Namespace
- `Syncfusion.Windows.Forms.Diagram.Controls`

### Class
- `PaletteGroupBar`

### Properties (示例)
- `Name`: The name of the PaletteGroupBar control (e.g., `paletteGroupBar1`).
- `Items Collection`: The collection of items/grouped controls assigned to the PaletteGroupBar.
- `Layout.Dock`: Configures how the PaletteGroupBar is docked in the form (e.g., `Left`).
- `Appearance.VisualStyle`: Sets the visual style of the PaletteGroupBar (e.g., `OfficeXP`).
- `Behavior.PopUpResizeMode`: Defines the resize mode for the palette (e.g., `Both`).

## Code Examples

The detailed code example will demonstrate how to programmatically create and configure the PaletteGroupBar control. The section will include:
- Instantiating the PaletteGroupBar control.
- Setting its properties such as Dock, Appearance, and Behavior.
- Adding controls to the PaletteGroupBar items collection.

## Page-level Navigation/TOC
- **Step-by-step procedure to create a PaletteGroupBar control through code.**
- **Reference to essential SDK assemblies required for a successful implementation.**
- **Explanation of key properties and methods relevant to the PaletteGroupBar control.**

### Cross References
- Refer to the related sections or external documentation for a deeper understanding of configuring Smart Tags and Diagrams in Windows Forms.
- For advanced configurations, see the Syncfusion documentation or relevant tutorials.

<!-- tags: [syncfusion, winforms, palettegroupbar, control, api, essential diagram, .NET] keywords: [palettegroupbar, windows forms, smart tag, diagram, design-time, code] -->
```