```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_906.jpeg
document_name: tools
page_number: 906
page_id: tools#page_906
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:17Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Sets maximum and minimum sizes for `textBoxExt1`.
- Explains the use of ThemesEnabled to define the control's appearance.
- Lists events relating to `TextBoxExt` and their explanations.

## Content

### Setting Maximum and Minimum Sizes

```csharp
this.textBoxExt1.MaximumSize = new System.Drawing.Size(150, 20);
this.textBoxExt1.MinimumSize = new System.Drawing.Size(150, 20);
```

```vb
Me.textBoxExt1.MaximumSize = New System.Drawing.Size(150, 20)
Me.textBoxExt1.MinimumSize = New System.Drawing.Size(150, 20)
```

**Figure 581: Size of the TextBoxExt control Set**

### Applying Themes

The ThemesThemes property defines the look and feel of the control. This can be enabled using the following property.

**Property Table:**

| TextBoxExt Property       | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| ThemesEnabled             | Specifies whether or not to use XP themes when BorderStyle is set to 'Fixed3D'. |

#### Code Examples

```csharp
this.textBoxExt1.ThemesEnabled = true;
```

```vb
Me.textBoxExt1.ThemesEnabled = True
```

**Figure 582: ThemesEnabled property Set**

### TextBoxExt Events

The list of events and a detailed explanation about each of them is given in the following sections.

---

## API Reference (if applicable)

No specific API information is provided in this section.

## Code Examples (multi-language supported)

Refer to the code examples in the [C# and VB.NET] sections above.

## Page-level Navigation/TOC (if applicable)

No local Table of Contents is provided on this page.

## Cross References

No explicit cross-references are provided on this page.

## RAG Annotations

<!--
tags: [windows forms, textbox, size, themes, events, windows presentation foundation]
keywords: [ThemesEnabled, TextBoxExt, size set, maximum size, minimum size, fixed3D, XP themes, event handling]
-->
```