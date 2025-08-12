```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_985.jpeg
document_name: tools
page_number: 985
page_id: tools#page_985
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:46:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Demonstrates the usage of the `TextShadow` property of the `RadioButtonAdv` control.
- Provides a sample installation path for viewing the demonstration.
- Includes details on alignment settings and behavior adjustments for the `RadioButtonAdv` control.

---

## Content

### RadioButtonAdv with Shadow Text

**Figure 636: RadioButtonAdv with Shadow Text**

A sample which demonstrates the `TextShadow` property of `RadioButtonAdv` is available in the below sample installation path.

..My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\OptionControls

#### See Also

- [Alignment Settings](#alignment-settings)
- [3.5.11.2.3.3 Appearance and Behavior Settings](#appearance-and-behavior-settings)

---

### Appearance Settings

#### DrawFocusRectangle

The focus rectangle can be hidden or made visible using the below given property.

| `RadioButtonAdv` Property          | Description                                                                                     |
|------------------------------------|-------------------------------------------------------------------------------------------------|
| DrawFocusRectangle                 | Determines if the focus rectangle is visible when it gets the focus. The default value is set to 'True'. |

**Example Code:**

```csharp
this.radioButtonAdv1.DrawFocusRectangle = true;
```

```vb
Me.radioButtonAdv1.DrawFocusRectangle = True
```

---

### Alignment Settings

---

### 3.5.11.2.3.3 Appearance and Behavior Settings

This section discusses the appearance and behavior settings of the `RadioButtonAdv` control.

---

## API Reference

#### Properties

- **DrawFocusRectangle**
  - **Type:** Boolean
  - **Description:** Determines whether the focus rectangle is visible when the control gets the focus.
  - **Default:** `True`

---

## Code Examples

### C#

```csharp
this.radioButtonAdv1.DrawFocusRectangle = true;
```

### VB.NET

```vb
Me.radioButtonAdv1.DrawFocusRectangle = True
```

---

## Page-level Navigation/TOC (if applicable)

- [Appearance Settings](#appearance-settings)
- [DrawFocusRectangle](#drawfocusrectangle)
- [Alignment Settings](#alignment-settings)
- [3.5.11.2.3.3 Appearance and Behavior Settings](#appearance-and-behavior-settings)

---

## Cross References

- `RadioButtonAdv`
- `TextShadow` property
- `DrawFocusRectangle` property

---

<!-- tags: [WinForms, Syncfusion, RadioButtonAdv, TextShadow, DrawFocusRectangle] keywords: [alignment, behavior, appearance, focus rectangle, property settings] -->
```