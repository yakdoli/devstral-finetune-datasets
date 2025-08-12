```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_881.jpeg
document_name: tools
page_number: 881
page_id: tools#page_881
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:48Z
fidelity: lossless
-->

## Numerical Input Alignment in WinForms

### Overview
- Describes how to align text and up/down buttons in numeric input controls in Windows Forms.
- Includes programming examples in C# and VB.NET for text alignment.
- Explains the `UpDownAlign` property for button alignment.

### Text Alignment

This section explains how to align the text in a numeric input control, specifically for center alignment.

#### Code Examples

```csharp
this.numericUpdownExt1.TextAlign =
    System.Windows.Forms.HorizontalAlignment.Center;
```

```vb
Me.numericUpdownExt1.TextAlign =
    System.Windows.Forms.HorizontalAlignment.Center
```

![Figure: Text Aligned to the "Center"](image.png)

**Figure 558: Text Aligned to the "Center"**

### UpDownAlign

#### Setting Up and Down Button Alignment

The alignment of the up and down buttons can be configured using the `UpDownAlign` property.

| NumericUpdownExt Property | Description |
|---------------------------|-------------|
| UpDownAlign               | Gets / sets the alignment of the up and down buttons. The default value is set to 'Right'. It includes the below given options: Left and Right. |

#### Code Examples

```csharp
this.numericUpdownExt1.UpDownAlign =
    System.Windows.Forms.LeftRightAlignment.Left;
```

```vb
Me.numericUpdownExt1.UpDownAlign =
    System.Windows.Forms.LeftRightAlignment.Left
```

### Conclusion
This guide covers the essential tools and properties for text and button alignment in numeric input controls in Windows Forms, demonstrating the use of `TextAlign` and `UpDownAlign` properties with examples in C# and VB.NET.

<!-- tags: [winforms, numericinput, alignment, textalign, updownalign, csharp, vbnet, syncfusionwinforms, 11.4.0.26] keywords: [text alignment, button alignment, numeric input, windows forms, numericUpDown, TextAlignment] -->
``` 
