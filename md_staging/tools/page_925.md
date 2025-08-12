```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_925.jpeg
document_name: tools
page_number: 925
page_id: tools#page_925
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:42Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page describes how to use the FontComboBox control in a Windows Forms application.
- Provides both design-time and programmatic approaches to incorporating the FontComboBox control.
- Highlights the use of the Syncfusion.Windows.Forms.Tools namespace.

## Content

### See Also
- **Concepts and Features**
- **3.5.9.2.2 Creating FontComboBox**

To use a FontComboBox control in your application, all you need to do is drag and drop the FontComboBox control from the controls toolbox onto your form.

![Figure 590: FontComboBox in Toolbox](https://example.com/figure590.png)

It can be created programmatically as follows.

1. Include the required namespace.

   **[C#]**
   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   **[VB.NET]**
   ```vb
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. Create an instance of FontComboBox control. Specify its size and finally add that instance to that Form.

   **[C#]**
   ```csharp
   private Syncfusion.Windows.Forms.Tools.FontComboBox fontComboBox1;
   ```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Tools
- FontComboBox
  - Methods, Properties, and Events specific to FontComboBox are listed below.
  - This section would include detailed descriptions of each member, including parameters, types, and usage examples.

## Code Examples

### Design-Time Integration
1. Drag and drop the FontComboBox control from the toolbox onto your form.
2. Set its properties in the Properties window (e.g., Font, Size, Location).

### Programmatic Integration
1. Include the required Syncfusion namespace.
2. Create an instance of the FontComboBox control.
3. Set size and location properties.
4. Add the control to the form's Controls collection.

## Page-level Navigation/TOC (if applicable)
- Overview
- Content
  - See Also
  - Drag and Drop Approach
  - Programmatic Approach
- API Reference
- Code Examples

<!-- tags: [syncfusion, winforms, fontcombobox, tools, controls, .NET, C#, VB.NET, version:11.4.0.26] keywords: [FontComboBox, design-time, programmatic, toolbox, controls, namespace, Syncfusion, Windows Forms, drag and drop, programmatic integration] -->
```