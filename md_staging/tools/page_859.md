```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_859.jpeg
document_name: tools
page_number: 859
page_id: tools#page_859
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:40:12Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the Border Settings of MaskedEditBox control.
- Discusses the Layout Settings for the MaskedEditBox control.
- Explains how to set the size of the MaskedEditBox control using properties.

## Content

### Border Settings of MaskedEditBox Control

Figure 547 illustrates the MaskedEditBox with Border Set.

**Figure 547: MaskedEditBox with Border Set**

A sample demonstrating the Border Settings of the MaskedEditBox control is available in the following sample installation path:

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls
```

### Layout Settings of MaskedEditBox Control

The layout settings of the MaskedEditBox control are discussed in this section. The size of the MaskedEditBox control can be set according to the needs of the user using the properties listed below.

#### MaskedEditBox Properties and Description

| MaskedEditBox Properties | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| MaximumSize              | Gets / sets the maximum size for the control.                            |
| MinimumSize              | Gets / sets the minimum size for the control.                            |

#### Code Examples

```csharp
[C#]

this.maskedEditBox1.MaximumSize = new System.Drawing.Size(150, 20);
this.maskedEditBox1.MinimumSize = new System.Drawing.Size(150, 20);
```

```vb
[VB.NET]

Me.maskedEditBox1.MaximumSize = New System.Drawing.Size(150, 20)
Me.maskedEditBox1.MinimumSize = New System.Drawing.Size(150, 20)
```

**Figure 548: Size of the MaskedEditBox control Set**

## API Reference

### MaskedEditBox Properties
- **MaximumSize**: Gets or sets the maximum size for the control.
- **MinimumSize**: Gets or sets the minimum size for the control.

## Code Examples

The code examples demonstrate how to set the `MaximumSize` and `MinimumSize` properties for the MaskedEditBox control in both C# and VB.NET.

### Summary

This section provides a comprehensive overview of setting the Border and Layout properties of the MaskedEditBox control in Syncfusion's WinForms tools. The examples and properties outlined aid in customizing the control according to specific requirements.

<!-- tags: [Syncfusion Winforms, MaskedEditBox, Border Settings, Layout Settings, MaximumSize, MinimumSize] keywords: [MaskedEditBox, Border Settings, Layout, Size, MaximumSize, MinimumSize] -->
```