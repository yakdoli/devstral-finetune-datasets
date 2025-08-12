```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_877.jpeg
document_name: grid
page_number: 877
page_id: grid#page_877
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:42Z
fidelity: lossless
-->

## Overview
- This section describes how to set base styles for the grid using code.
- Provides examples in both C# and VB.NET for creating and applying multiple base styles to a grouping grid.

## Content

### Setting Base Styles Programmatically

Base styles can also be set through code. The following code example illustrates how to create and apply the above styles to the grouping grid.

#### C# Example

```csharp
GridTableBaseStyle style1 = new GridTableBaseStyle("BaseStyle 1");
style1.Name = "BaseStyle 1";
style1.StyleInfo.Font.Facename = "Verdana";
style1.StyleInfo.Interior = new BrushInfo(Color.FromArgb(255, 128, 0));

GridTableBaseStyle style2 = new GridTableBaseStyle("BaseStyle 2");
style2.Name = "BaseStyle 2";
style2.StyleInfo.Font.Facename = "Arial";
style2.StyleInfo.Interior = new BrushInfo(Color.FromArgb(192, 192, 255));

gridGroupingControl1.BaseStyles.AddRange(new GridTableBaseStyle[] { style1, style2 });

gridGroupingControl1.Appearance.AlternateRecordFieldCell.BaseStyle = "BaseStyle 1";
gridGroupingControl1.Appearance.AnyCell.BaseStyle = "BaseStyle 2";
```

#### VB.NET Example

```vb
Dim style1 As GridTableBaseStyle = New GridTableBaseStyle("BaseStyle 1")
style1.Name = "BaseStyle 1"
style1.StyleInfo.Font.Facename = "Verdana"
style1.StyleInfo.Interior = New BrushInfo(Color.FromArgb(255, 128, 0))

Dim style2 As GridTableBaseStyle = New GridTableBaseStyle("BaseStyle 2")
style2.Name = "BaseStyle 2"
style2.StyleInfo.Font.Facename = "Arial"
style2.StyleInfo.Interior = New BrushInfo(Color.FromArgb(192, 192, 255))
```

## API Reference

### Namespaces and Classes
- `GridTableBaseStyle`
- `StyleInfo`
- `Font`
- `Facename`
- `BrushInfo`
- `Color`

### Methods and Properties
- `AddRange`: Adds a range of base styles to the grid.
- `BaseStyle`: Property to assign a specific base style to elements like `AlternateRecordFieldCell` and `AnyCell`.

## Code Examples

### Example: Creating and Applying Base Styles

The above examples demonstrate:
1. Creating two base styles (`BaseStyle 1` and `BaseStyle 2`) with different font and interior settings.
2. Adding these styles to the grid using `BaseStyles.AddRange`.
3. Assigning the base styles to specific grid elements.

## Page-level Navigation/TOC
- [Introduction](#introduction)
- [Setting Base Styles Programmatically](#setting-base-styles-programmatically)
- [Code Examples](#code-examples)

## Tags and Keywords
<!-- tags: [Syncfusion Winforms, Grid, Base Styles, C#, VB.NET, Example] keywords: [GridTableBaseStyle, Font, Facename, BrushInfo, BaseStyles, AlternateRecordFieldCell, AnyCell] -->
```