```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_604.jpeg
document_name: tools
page_number: 604
page_id: tools#page_604
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:32Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to create and use a MultiColumnComboBox control in Windows Forms.
- Details the design-time setup and programming methods for the control.
- Provides examples in C# and VB.NET.

## Content

### 3.5.5.4.2 Creating MultiColumnComboBox

The **MultiColumnComboBox** control provides full support for the Windows Forms designer. To use a MultiColumnComboBox control in your application, all you need to do is drag-and-drop the MultiColumnComboBox control from the toolbox onto your form. You can then set any of its properties through the property grid.

#### Design-Time Setup

1. **Drag-and-Drop** the MultiColumnComboBox control from the toolbox onto your Windows Form.

**Figure 373: MultiColumnComboBox in the Toolbox**

![Figure 373: MultiColumnComboBox in the Toolbox](image: MultiColumnComboBox toolbox image)

#### Programmatic Creation

The MultiColumnComboBox can be created programmatically through code as detailed below.

1. **Include the required namespace.**

   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   ```vb
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. **Create an instance of MultiColumnComboBox. Add that instance to the Form.**

   ```csharp
   private Syncfusion.Windows.Forms.Tools.MultiColumnComboBox multiColumnComboBox1;
   this.multiColumnComboBox1 = new
   ```

## API Reference (if applicable)

- Namespace: **Syncfusion.Windows.Forms.Tools**
- Class: **MultiColumnComboBox**
- Properties, Methods, Events: Refer to the official Syncfusion documentation for complete details.

## Code Examples (multi-language supported)

The snippets provided above demonstrate the initialization and inclusion of a MultiColumnComboBox control in a Windows Forms application using both C# and VB.NET.

## Page-level Navigation/TOC (if applicable)

- [3.5.5.4.2 Creating MultiColumnComboBox]
- Design-Time Setup
- Programmatic Creation
- API Reference
- Code Examples

<!-- tags: [Syncfusion, Windows Forms, MultiColumnComboBox, Toolbox, Design-Time, Programmatic, Control] keywords: [MultiColumnComboBox, toolbox, designer, property grid, Windows Forms, Syncfusion, Windows, UI controls, dropdownlist] -->
```