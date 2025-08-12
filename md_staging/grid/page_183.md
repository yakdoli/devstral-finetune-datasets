```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_183.jpeg
document_name: grid
page_number: 183
page_id: grid#page_183
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## GridBaseStyle Collection Editor

The following code example illustrates how to create a BaseStyle. When you define a BaseStyle, you can apply it to any cell (or row or column) by just setting the `GridStyleInfo.BaseStyle` for that cell to the name used to define the BaseStyle.

### Figure 101: GridBaseStyle Collection Editor

The figure above shows the GridBaseStyle Collection Editor, which includes options to manage BaseStyles, such as adding, removing, and editing their properties.

## Creating a BaseStyle

### Example: Adding and Applying a BaseStyle

#### C#

```csharp
// Add a new base style.
GridBaseStyle gridBaseStyle1 = new GridBaseStyle("BackColorTest", false);
gridBaseStyle1.StyleInfo.BackColor = Color.SkyBlue;
gridBaseStyle1.StyleInfo.TextColor = Color.RosyBrown;
gridControl1.BaseStylesMap.AddRange(new GridBaseStyle[] { gridBaseStyle1 });

// Apply this base style to a couple of cells.
gridControl1[1, 2].BaseStyle = "BackColorTest";
gridControl1[4, 2].BaseStyle = "BackColorTest";
```

#### VB.NET

```vb
' Add a new base style.
Dim gridBaseStyle1 As GridBaseStyle = New GridBaseStyle("BackColorTest", False)
gridBaseStyle1.StyleInfo.BackColor = Color.SkyBlue
gridBaseStyle1.StyleInfo.TextColor = Color.RosyBrown
gridControl1.BaseStylesMap.AddRange(New GridBaseStyle() { gridBaseStyle1 })

' Apply this base style to a couple of cells.
gridControl1(1, 2).BaseStyle = "BackColorTest"
gridControl1(4, 2).BaseStyle = "BackColorTest"
```

## Summary

This page demonstrates how to define and apply a `BaseStyle` in the Essential Grid for Windows Forms. By creating a `BaseStyle` and assigning it to specific cells, you can easily manage the appearance of cells, rows, or columns across the grid.

## Code Examples (Reformatted)

### C#

Here is the restructured version of the C# code example:

```csharp
// Add a new base style.
GridBaseStyle gridBaseStyle1 = new GridBaseStyle("BackColorTest", false);
gridBaseStyle1.StyleInfo.BackColor = Color.SkyBlue;
gridBaseStyle1.StyleInfo.TextColor = Color.RosyBrown;
gridControl1.BaseStylesMap.AddRange(new GridBaseStyle[] { gridBaseStyle1 });

// Apply this base style to specific cells.
gridControl1[1, 2].BaseStyle = "BackColorTest";
gridControl1[4, 2].BaseStyle = "BackColorTest";
```

### VB.NET

Here is the restructured version of the VB.NET code example:

```vb
' Add a new base style.
Dim gridBaseStyle1 As GridBaseStyle = New GridBaseStyle("BackColorTest", False)
gridBaseStyle1.StyleInfo.BackColor = Color.SkyBlue
gridBaseStyle1.StyleInfo.TextColor = Color.RosyBrown
gridControl1.BaseStylesMap.AddRange(New GridBaseStyle() { gridBaseStyle1 })

' Apply this base style to specific cells.
gridControl1(1, 2).BaseStyle = "BackColorTest"
gridControl1(4, 2).BaseStyle = "BackColorTest"
```

## Page Footer

© 2013 Syncfusion. All rights reserved.  
Page 183
```

<!-- tags: [grid, basestyle, windowsforms, editor, csharp, vb.net] keywords: [GridBaseStyle, BaseStyle, GridStyleInfo.BaseStyle, gridcontrol, cell styling, style editor, windows forms, syncfusion] -->