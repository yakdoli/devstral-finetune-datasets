```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_119.jpeg
document_name: edit
page_number: 119
page_id: edit#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:17Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Describes the functionality and use of the **Edit Control Border Enumerator** for specifying border styles and weights.
- Provides details on how to set and remove borders on specified text ranges in WinForms.

## Content

### WinForms-specific Border Control

The **Edit Control Border Enumerator** allows customization of text borders in Windows Forms applications.

#### Enumerations

| Edit Control Border Enumerator | Description |
| --- | --- |
| **FrameBorderStyle** | Specifies the style of border line. The options provided are: <br> - Dash<br> - DashDot<br> - Dot<br> - None<br> - Solid<br> - Wave |
| **BorderWeight** | Specifies the weight of the border line. The options provided are: <br> - Bold<br> - Double<br> - Thin |

### Code Examples

#### C#

```csharp
// Set borders for the specified text range.
this.editControl1.SetTextBorder(new Point(1, 13), new Point(15, 13), 
                                Color.Red, FrameBorderStyle.Wave, BorderWeight.Double);

// Remove borders from the specified text range.
this.editControl1.RemoveTextBorder(new Point(1, 13), new Point(15, 13));
```

#### VB.NET

```vb
' Set borders for the specified text range.
Me.editControl1.SetTextBorder(New Point(1, 13), New Point(15, 13), 
                              Color.Red, FrameBorderStyle.Wave, BorderWeight.Double)

' Remove borders from the specified text range.
Me.editControl1.RemoveTextBorder(New Point(1, 13), New Point(15, 13))
```

### Notes
- The `SetTextBorder` method sets a border with specified style, weight, and color for a text range defined by two points.
- The `RemoveTextBorder` method removes any borders applied to the specified text range.

<!--
tags: [edit, border control, windows forms, enumerator] keywords: [FrameBorderStyle, BorderWeight, SetTextBorder, RemoveTextBorder, color, text range, wave, bold, double, thin]
-->
```