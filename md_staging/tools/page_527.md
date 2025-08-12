```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_527.jpeg
document_name: tools
page_number: 527
page_id: tools#page_527
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section focuses on getting started with the **ColorPickerUIAdv** control in **Windows Forms**.
- Describes how to create the **ColorPickerUIAdv** control both visually (using the designer) and programmatically.
- Lists the steps to include the required namespace and create an instance of the control.

## Content

### 3.5.4.5.2 Creating ColorPickerUIAdv

#### Overview
This section will help you to get started with using the **ColorPickerUIAdv** control.

#### Drag-and-Drop Method
The **ColorPickerUIAdv** can be easily created in the designer by dragging-and-dropping from the toolbox onto the Windows application form.

#### Visual Representation
"Figure 313: ColorPickerUIAdv Control in Toolbox"

![Figure 313: ColorPickerUIAdv Control in Toolbox](https://i.imgur.com/1jkmRQI.png)

#### Programmatic Addition
It can be added programmatically by performing the following steps:

1. **Include the namespace for the Tools Package.**

   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   ```vbnet
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. **Create an instance of ColorPickerUIAdv and add it to the Windows Form.**

   ```csharp
   private Syncfusion.Windows.Forms.Tools.ColorPickerUIAdv colorPickerUIAdv1;
   ColorPickerUIAdv cpa = new ColorPickerUIAdv();
   cpa.Size = new Size(200, 180);
   ```

## API Reference

### Namespaces and Classes
- `Syncfusion.Windows.Forms.Tools`
  - `ColorPickerUIAdv`
    - **Properties**
      - `Size`: Specifies the size of the control.
    - **Methods**
      - `Constructor`: Initializes a new instance of the `ColorPickerUIAdv` class.

## Code Examples

### C#
```csharp
using Syncfusion.Windows.Forms.Tools;

private Syncfusion.Windows.Forms.Tools.ColorPickerUIAdv colorPickerUIAdv1;
ColorPickerUIAdv cpa = new ColorPickerUIAdv();
cpa.Size = new Size(200, 180);
```

### VB.NET
```vbnet
Imports Syncfusion.Windows.Forms.Tools

Private colorPickerUIAdv1 As Syncfusion.Windows.Forms.Tools.ColorPickerUIAdv
Dim cpa As New ColorPickerUIAdv()
cpa.Size = New Size(200, 180)
```

## Page-level Navigation/TOC
- 3.5.4.5.2 Creating ColorPickerUIAdv
  - Drag-and-Drop Method
  - Programmatic Addition

### Cross References
- See also: [Windows Forms Controls](#windows-forms-controls)

<!-- tags: [windows-forms, colorpickeruiadv, design-time, runtime, toolbox] keywords: [syncfusion, windows forms, tools package, color picker, programmatic addition, designer, toolbox, namespace, instance, size, properties, methods] -->
```
