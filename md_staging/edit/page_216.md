```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_216.jpeg
document_name: edit
page_number: 216
page_id: edit#page_216
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:27Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Describes the options for configuring gradient colors in EditControl.
- Explains the `GradientColors` property and its associated gradient styles.
- Shows examples in C# and VB.NET for setting a gradient background style.

## Content

### GradientColors

| GradientColors                     | Specifies the gradient colors. The options provided are as follows: |
| ----------------------------------- | ----------------------------------------------------------------------------------------- |
|                                    |                                                                                             |
|                                    | - ForwardDiagonal                                                                      |
|                                    | - BackwardDiagonal                                                                      |
|                                    | - Horizontal                                                                           |
|                                    | - Vertical                                                                             |
|                                    | - PathRectangle                                                                        |
|                                    | - PathEllipse                                                                          |
|                                    |                                                                                             |
|                                    | The first entry in this list will be the same as the backcolor property, and the last entry will be the same as the forecolor property. |

### Examples

#### [C#]

```csharp
this.editControl1.BackgroundColor = new
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.ForwardDiagonal,
    new System.Drawing.Color[] { System.Drawing.Color.LavenderBlush,
    System.Drawing.Color.AliceBlue, System.Drawing.Color.BlanchedAlmond });
```

#### [VB.NET]

```vbnet
Me.editControl1.BackgroundColor = New
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.ForwardDiagonal,
    New System.Drawing.Color() { System.Drawing.Color.LavenderBlush,
    System.Drawing.Color.AliceBlue, System.Drawing.Color.BlanchedAlmond })
```

## API Reference

### GradientColors

Represents the gradient colors used in the EditControl's background. This property specifies the color gradient styles.

### GradientStyle

Specifies the style of the gradient colors, including:

- ForwardDiagonal
- BackwardDiagonal
- Horizontal
- Vertical
- PathRectangle
- PathEllipse

### Usage Notes

- The `GradientColors` property uses the first entry as the background color and the last entry as the foreground color.

## Code Examples

The examples above demonstrate how to set a **ForwardDiagonal** gradient style using specific colors.

<!-- tags: [syncfusion, windowsforms, editcontrol, gradientstyle, gradientcolors] keywords: [gradient, editcontrol, windows forms, colors, style, forwarddiagonal] -->
```