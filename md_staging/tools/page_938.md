```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_938.jpeg
document_name: tools
page_number: 938
page_id: tools#page_938
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:44:02Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page discusses the customization of spacing and positioning for the AutoLabel control in Windows Forms.
- Highlights the properties that allow precise control over the placement of labels relative to their associated controls.
- Provides examples in both C# and VB.NET for setting spacing and positioning.

## Content

### **3.5.10.1.3.2 Spacing**

The space between the AutoLabel control and the labeled control can be customized using the properties given below. When using relative positioning, you can also specify the gap between the label and the control.

| AutoLabel Properties | Description                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------------------|
| DX                   | The effective horizontal distance between the left of the AutoLabel and its labeled control.      |
| DY                   | The effective vertical distance between the top of the AutoLabel and its labeled control.        |
| Gap                  | Specifies the horizontal and vertical gap to use when computing the relative position.           |

#### Code Examples

- **[C#]**
```csharp
this.autoLabel1.DX = -80;
this.autoLabel1 DY = 3;
this.autoLabel1.Gap = 10;
```

- **[VB.NET]**
```vb
Me.autoLabel1.DX = -80
Me.autoLabel1.DY = 3
Me.autoLabel1.Gap = 10
```

![Space Settings of AutoLabel](https://via.placeholder.com/300x200?text=Figure+601%3A+Space+Settings+of+AutoLabel)

### **3.5.10.1.3.3 Position**

The AutoLabel control can be positioned relative to the top, left, bottom, or right of the labeled control. You can do this using the below given property.

#### Figure: AutoLabel Sample

NOTE: The description of the figure is not fully provided in the given text, so additional context is needed for a complete explanation.

---

## API Reference

### Properties
- **DX**
- **DY**
- **Gap**

### Methods (if any, detail to be added)

### Events (if any, detail to be added)

---

## Code Examples

The examples provided above demonstrate how to set the `DX`, `DY`, and `Gap` properties using C# and VB.NET.

---

## Page-level Navigation/TOC (if applicable)
- 3.5.10.1.3.2 Spacing
- 3.5.10.1.3.3 Position

---

## Cross References

See also: [Related Features in Windows Forms]

---

<!-- tags: [AutoLabel, Windows Forms, Spacing, Positioning, C#, VB.NET] keywords: [AutoLabel Properties, DX, DY, Gap, Relative Positioning, Essential Tools, Windows Forms, Software Development] -->
```