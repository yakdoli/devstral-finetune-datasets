```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_524.jpeg
document_name: tools
page_number: 524
page_id: tools#page_524
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:33Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- ColorPickerButton displaying ColorUIControl at run time
- Customization settings for ColorPickerButton

## Content

### Figure 309: ColorPickerButton Displaying ColorUIControl at Run Time

**See Also**

- [Appearance and Behavior Settings](Appearance and Behavior Settings)
- [3.5.4.4.3 Customization Settings](3.5.4.4.3 Customization Settings)

#### **3.5.4.4.3 Customization Settings**

ColorPickerButton displays the ColorUIControl as its dropdown. ColorPickerButton has properties to customize the ColorUIControl. Refer the [User Guide](User Guide) for ColorUIControl. The size for the dropdown, i.e., ColorUIControl can be set using the `ColorUISize` property.

---

### C#

```csharp
this.colorPickerButton1.ColorUISize = new System.Drawing.Size(250, 280);
```

---

### VB.NET

```vb
Me.colorPickerButton1.ColorUISize = New System.Drawing.Size(250, 280)
```

---

### Figure 310: ColorUISize-Width = 250, Height = 280

**ColorPicker Appearance**

## API Reference (if applicable)

- **ColorPickerButton** properties:
  - `ColorUISize`: Sets the size of the dropdown ColorUIControl.

## Code Examples

#### C#

```csharp
this.colorPickerButton1.ColorUISize = new System.Drawing.Size(250, 280);
```

#### VB.NET

```vb
Me.colorPickerButton1.ColorUISize = New System.Drawing.Size(250, 280)
```

---

### Summary

- Customizing the size of the ColorUIControl in ColorPickerButton.
- Setting the size using the `ColorUISize` property.

## Page-level Navigation/TOC (if applicable)

- [3.5.4.4.3 Customization Settings](3.5.4.4.3 Customization Settings)
- See Also: [Appearance and Behavior Settings](Appearance and Behavior Settings)

## RAG Annotations

<!-- tags: [syncfusion, winforms, colorpickerbutton, coloui, customization, ui] keywords: [ColorPickerButton, ColorUIControl, ColorUISize, customization, appearance, behavior, user guide, size, run time display, C#, VB.NET, default colors, palette] -->
```