```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_541.jpeg
document_name: tools
page_number: 541
page_id: tools#page_541
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:38Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section discusses how to manage the Office2007 styles and custom colors for the ColorPickerUIAdv control.
- Instructions on turning off the Office2007 style and applying custom colors are provided.
- Examples in both C# and VB.NET are included.

## Content

### Customization of Office2007 Styles

**Figure 328: Blue, Silver and Black Color schemes of ColorPickerUIAdv**

The Office2007 Visual Styles can be turned off by setting the `UseOffice2007Style` property to false.

**Figure 329: ColorPickerUIAdv with Office2007 Style Turned Off**

#### Custom Colors

We can also apply custom colors to the `ColorPickerUIAdv` control by setting `Office2007Theme` to "Managed" and specifying the custom color through the `ApplyManagedColors` method as follows.

#### Code Examples

##### C#

```csharp
this.colorPickerUIAdv1.Office2007Theme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Orange);
```

##### VB.NET

```vb
Me.colorPickerUIAdv1.Office2007Theme = Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(Me, Color.Orange)
```

## API Reference

### Properties
- **`Office2007Theme`**: Determines the theme of the Office2007 styles.
  - **Type**: `Office2007Theme`
  - **Description**: Options include `Managed`, `Silver`, `Black`, and `Blue`.

### Methods
- **`ApplyManagedColors`**: Applies custom colors to the control.
  - **Parameters**:
    - `control`: The control to which the custom color is applied.
    - `color`: The custom color to be applied.
  - **Returns**: None.

## RAG Annotations
- **Tags**: [ColorPickerUIAdv, Office2007Theme, ApplyManagedColors, Custom Colors]
- **Keywords**: [visual styles, custom colors, managed theme, C#, VB.NET, Syncfusion Windows Forms, Office2007, ColorPicker]

```