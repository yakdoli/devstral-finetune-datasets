```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_886.jpeg
document_name: tools
page_number: 886
page_id: tools#page_886
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses themes and visual styles settings of the NumericUpDowExt control.
- Explains the use of the ThemesEnabled property to define the look and feel of the control.
- Provides examples in C# and VB for setting ThemesEnabled to true.

## Content

### 3.5.8.9.3.9 Themes and Visual Styles

This section discusses themes and visual styles settings of the NumericUpDowExt control.

#### Themes

Themes define the look and feel of the NumericUpDowExt control. They can be set using the property given below.

| NumericUpDowExt Property | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| ThemesEnabled             | Specifies whether XP Themes (visual styles) should be used for this control when available. |

#### Code Examples

[C#]

```csharp
this.numericUpDowExt1.ThemesEnabled = true;
```

[VB]

```vb
Me.numericUpDowExt1.ThemesEnabled = True
```

#### Visual Representation

Figure 562: Themes set for Office 2007 (Blue) Visual Style

![Themes set for Office 2007 (Blue) Visual Style](https://i.imgur.com/1vqJc9S.png)

## API Reference

- **Property**: ThemesEnabled  
  - **Type**: Boolean
  - **Description**: Specifies whether XP Themes (visual styles) should be used for the control when available.

## Code Examples

The following code demonstrates how to set the ThemesEnabled property.

### C#

```csharp
this.numericUpDowExt1.ThemesEnabled = true;
```

### VB

```vb
Me.numericUpDowExt1.ThemesEnabled = True
```

### Figure: Themes Enabled

The figure below shows the control with ThemesEnabled set to `False` and `True`.

## RAG Annotations

<!-- tags: [NumericUpDowExt, ThemesEnabled, Visual Styles, Control Appearance] keywords: [Themes, Visual Styles, NumericUpDowExt, XP Themes, Control Appearance] -->
```