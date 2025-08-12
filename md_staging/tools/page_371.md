```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_371.jpeg
document_name: tools
page_number: 371
page_id: tools#page_371
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page describes the properties and settings related to the appearance of a button control in Windows Forms.
- Focuses on the `FlatAppearance` and `FlatStyle` properties, providing examples in both C# and VB.NET.
- Demonstrates how to customize border colors, hover effects, and other appearance attributes.

## Content

### Button Appearance Properties

| Property           | Description                                                                                                                                                                                                                                                                                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FlatAppearance     | Represents the appearance of the border and the color for the check state and mouse over state. `FlatStyle` should be set to `Flat`, and `UseVisualStyleBackColor` should be set to `false` to make these settings effective.                                                                                                                 |
| FlatStyle          | Specifies the flat style for the button. The options are `Flat`, `Popup`, `Standard`, and `System`.                                                                                                                                                                                                                                                         |

### Code Examples

#### C#

```csharp
this.buttonEditChildButton5.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
this.buttonEditChildButton5.FlatAppearance.BorderColor = System.Drawing.Color.Crimson;
this.buttonEditChildButton5.FlatAppearance.MouseOverBackColor = System.Drawing.Color.Pink;
```

#### VB.NET

```vb
Me.buttonEditChildButton5.FlatStyle = System.Windows.Forms.FlatStyle.Flat
Me.buttonEditChildButton5.FlatAppearance.BorderColor = System.Drawing.Color.Crimson
Me.buttonEditChildButton5.FlatAppearance.MouseOverBackColor = System.Drawing.Color.Pink
```

### Figure: CrimsonRed Border Color with Pink MouseHover Color

![Figure 180: CrimsonRed Border Color with Pink MouseHover Color](https://i.imgur.com/4dbZy3F.png)

*Figure 180: CrimsonRed Border Color with Pink MouseHover Color*

### Style Settings

#### UseVisualStyleBackColor

Determines whether the background of a child button is drawn using visual style if the button supports visual styles.

#### Office2007ColorScheme

Specifies the office color scheme.

## RAG Annotations

<!-- tags: [Windows Forms, Button Control, Flat Appearance, Flat Style, C#, VB.NET, Visual Style, Office Color Scheme, Mouse Hover, Border Color]keywords: [FlatAppearance, FlatStyle, UseVisualStyleBackColor, Office2007ColorScheme, Crimson Color, Pink Color, Windows Forms, button, appearance customization, code examples, FlatStyle.Popup, FlatStyle.Standard, FlatStyle.System] -->
```