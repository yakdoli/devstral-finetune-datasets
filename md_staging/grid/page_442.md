```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_442.jpeg
document_name: grid
page_number: 442
page_id: grid#page_442
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:16:43Z
fidelity: lossless
-->

## Overview
- Discusses the `Grid` control in Windows Forms, particularly focusing on the `GridLineColor` property and its functionality.
- Provides examples in C# and VB.NET to demonstrate setting the `GridLineColor` property.
- Explains the effects on the Grid when `GridLineColor` is set.

## Content

### Grid Line Color Example

The GridLineColor property specifies the color for the grid lines, such as the active border. The default value is set to `GrayText`.

#### Example in C#

```csharp
// Specify the color for the grid lines.
this.gridControl1.Properties.GridLineColor = 
System.Drawing.Color.IndianRed;
```

#### Example in VB.NET

```vb
' Specify the color for the grid lines.
Me.gridControl1.Properties.GridLineColor = 
System.Drawing.Color.IndianRed
```

The illustration below shows how the Grid in "Figure 1" is transformed when the `Properties.GridLineColor` property is set to `IndianRed`.

---

## API Reference

### Properties

- **GridLineColor**: Specifies the color for the grid lines.
  - **Type**: System.Drawing.Color
  - **Default**: GrayText

---

## Code Examples

The following are code snippets demonstrating how to set the `GridLineColor` property in both C# and VB.NET.

### C# Example

```csharp
this.gridControl1.Properties.GridLineColor = System.Drawing.Color.IndianRed;
```

### VB.NET Example

```vb
Me.gridControl1.Properties.GridLineColor = System.Drawing.Color.IndianRed
```

---

## RAG Annotations
<!-- tags: [syncfusion winforms, gridlinecolor, c#, vb.net, windows forms, api reference, example code] keywords: [Grid, GridLineColor, C#, VB.NET, GridControl, System.Drawing, Color, GrayText, IndianRed] -->
```