```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_854.jpeg
document_name: tools
page_number: 854
page_id: tools#page_854
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:10Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the background and foreground settings for the MaskedEditBox control.
- Explains how to set and reset the background color of the MaskedEditBox control.
- Describes the methods associated with the `BackColor` property.
- Provides code examples in C# and VB.NET for setting `BackColor` and `ForeColor`.
- Highlights the installation path for the sample demonstrating these settings.

## Content

### Background Color for MaskedEditBox
The method associated with the `BackColor` property is given below:

```markdown
```vb
Me.maskedTextBox1.BackColor = System.Drawing.Color.PaleGoldenrod
```
```

**Figure 545**: Background Color set for MaskedEditBox

#### Method Description
| Method        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `ResetBackColor` | Resets the `BackColor` property to its default value. |

A sample demonstrating the Background Settings of MaskedEditBox control is available in the following sample installation path:

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls
```

### Foreground Settings
The foreground settings of the MaskedEditBox control are discussed below.

#### Foreground Color
The foreground color of the control can be set using the properties given below.

### MaskedEditBox Property Description
| MaskedEditBox Property | Description                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------|
| `ForeColor`            | Specifies the foreground color of this component, which is used to display text.               |

#### Code Examples
```csharp
this.maskedTextBox1.ForeColor = System.Drawing.Color.DarkMagenta;
```

```vb
Me.maskedTextBox1.ForeColor = System.Drawing.Color.DarkMagenta
```

## API Reference

### Properties
- **BackColor**: Gets or sets the background color of the control.
- **ForeColor**: Gets or sets the foreground color of the control.

## Code Examples
The code examples shown above illustrate how to set the `BackColor` and `ForeColor` properties for the MaskedEditBox control in both C# and VB.NET.

## Cross References
- See also:
  - [MaskedEditBox Control Documentation](#)
  - [Syncfusion WinForms Controls Overview](#)
  - [Essential Tools for Windows Forms](#)

<!-- tags: [syncfusion winforms, maskededitbox, background color, foreground color, properties, methods] keywords: [BackColor, ForeColor, MaskedEditBox, Syncfusion, Windows Forms, C#, VB.NET] -->
```