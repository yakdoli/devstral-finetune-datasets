```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_786.jpeg
document_name: tools
page_number: 786
page_id: tools#page_786
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the Border and Size settings of the PercentTextBox control in Syncfusion WinForms.
- Includes code examples in C# and VB.NET for configuring border properties.
- Explains how to set the border style and size of the PercentTextBox control.

## Content

### Border Settings

The `Border3DStyle`, `BorderColor`, `BorderSides`, and `BorderStyle` properties can be set for the `PercentTextBox` control. The available options are `Etched` for `Border3DStyle`, `Color.Orange` for `BorderColor`, `All` for `BorderSides`, and `FixedSingle` for `BorderStyle`.

#### Code Examples

##### C#
```csharp
this.percentTextBox1.Border3DStyle =
System.Windows.Forms.Border3DStyle.Etched;
this.percentTextBox1.BorderColor = System.Drawing.Color.Orange;
this.percentTextBox1.BorderSides =
System.Windows.Forms.Border3DSide.All;
this.percentTextBox1.BorderStyle =
System.Windows.Forms.BorderStyle.FixedSingle;
```

##### VB.NET
```vb.net
Me.percentTextBox1.Border3DStyle =
System.Windows.Forms.Border3DStyle.Etched
Me.percentTextBox1.BorderColor = System.Drawing.Color.Orange
Me.percentTextBox1.BorderSides = System.Windows.Forms.Border3DSide.All
Me.percentTextBox1.BorderStyle =
System.Windows.Forms.BorderStyle.FixedSingle
```

#### Border Visualization

![PercentTextBox with Border Set](image.png)

**Figure 500: PercentTextBox with Border Set**

A sample demonstrating the border settings of the PercentTextBox control is available at the following installation path:

```
..My Documents\Syncfusion\EssentialStudio\<Version Number>\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls
```

### Size Settings

The size of the PercentTextBox control can be set according to the needs of the user using the properties discussed below.

#### Size Properties

| **PercentTextBox Properties** | **Description**                                                                 |
|--------------------------------|--------------------------------------------------------------------------------|
| MaximumSize                   | Gets / sets the maximum size for the control.                                  |

## Page-level Navigation/TOC (if applicable)
- **Border Settings**
  - Code Examples
  - Border Visualization
- **Size Settings**

## Code Examples (multi-language supported)
- C# and VB.NET examples for configuring Border and Size properties.

## RAG Annotations
<!-- tags: [Windows Forms, User Guide, PercentTextBox, Border Settings, Size Settings, C#, VB.NET] keywords: [Syncfusion, Border3DStyle, BorderColor, BorderSides, BorderStyle, PercentTextBox, MaximumSize, Windows Forms, User Guide] -->
```