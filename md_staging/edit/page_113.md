```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: edit
page_number: 113
page_id: edit#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:05Z
fidelity: lossless
-->

## Overview

- The page explains the word wrap margin properties and their functionalities for the Syncfusion WinForms library.
- It provides descriptions and examples for configuration in both C# and VB.NET.

### Edit Control Properties

| Edit Control Property                | Description                                                               |
|---------------------------------------|---------------------------------------------------------------------------|
| `WordWrapMarginVisible`              | Gets / sets value indicating whether the word wrap margin should be visible. |
| `WordWrapMarginLineStyle`            | Specifies style of line that is drawn at the border of the word wrap margin. The options provided are:  <br> - Solid <br> - Dash <br> - Dot <br> - DashDot <br> - DashDotDot <br> - Custom <br> The default value is **Solid**. |
| `WordWrapMarginLineColor`            | Sets custom color for the line that is drawn at the border of the word wrap margin. |
| `WordWrapMarginBrush`                | Gets / sets BrushInfo object that is used when the area situated after the text area is drawn. |

### C#

```csharp
// Specifies whether the word wrap margin should be visible.
this.editControl.WordWrapMarginVisible = true;

// Specifies the line style of the word wrap margin.
this.editControl.WordWrapMarginLineStyle = DashStyle.Dash;

// Specifies the line color of the word wrap margin.
this.editControl.WordWrapMarginLineColor = Color.Green;

// Specifies the BrushInfo object that is used when the area situated after the text area is drawn.
this.editControl.WordWrapMarginBrush = new
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal,
System.Drawing.Color.White, System.Drawing.Color.LightSalmon);
```

### VB.NET

```vb
' Specifies whether the word wrap margin should be visible.
Me.editControl.WordWrapMarginVisible = True

' Specifies the line style of the word wrap margin.
```

## Parameters

- `WordWrapMarginVisible`: Boolean indicating visibility.
- `WordWrapMarginLineStyle`: Enum defining line style.
- `WordWrapMarginLineColor`: Color for the line.
- `WordWrapMarginBrush`: BrushInfo object for area rendering.

## See also

- [Syncfusion WinForms Documentation](https://www.syncfusion.com/documentation/windows-forms/)
- WinForms properties reference

<!-- tags: [product, syncfusion, winforms, controls, properties, wordwrap] keywords: [word wrap margin, line style, line color, brush info, edit control, visible margin] -->
```