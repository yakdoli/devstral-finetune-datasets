```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_444.jpeg
document_name: grid
page_number: 444
page_id: grid#page_444
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:17:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This page explains how to set the background image and text color for a grid in Windows Forms.

## Content

### Background Image for Grid

![Figure 169: Background Image set for Grid]( figures/Figure_169.png)

### TextColor

- The TextColor property specifies the color of the text in the grid.

#### Setting TextColor Property

The following code examples can be used to set this property:

##### Using C#

```csharp
[C#]
 
 // Set grid text color.
 this.gridControl1.TableStyle.TextColor = Color.MidnightBlue;
```

##### Using VB.NET

```vb.net
[VB.NET]
 
 ' Set grid text color.
 Me.gridControl1.TableStyle.TextColor = Color.MidnightBlue
```

### Visual Transformation

The following illustration shows how the Grid in "Figure 1" is transformed when the TableStyle.TextColor property is set to MidnightBlue.

## Code Examples

### C#

```csharp
// Set grid text color.
this.gridControl1.TableStyle.TextColor = Color.MidnightBlue;
```

### VB.NET

```vb.net
' Set grid text color.
Me.gridControl1.TableStyle.TextColor = Color.MidnightBlue
```

<!-- tags: [windowsforms, grid, textcolor, backgroundimage, tablestyle] keywords: [Essential Grid, Windows Forms, TextColor, Background Image, TableStyle, C#, VB.NET, MidnightBlue] -->
```