```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_846.jpeg
document_name: grid
page_number: 846
page_id: grid#page_846
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:47:22Z
fidelity: lossless
-->

## Overview

- Explains the GridStyleInfo properties and their precedence in determining grid cell appearance.
- Describes how theme coloring can interfere with the intended visual effects on Windows XP-like systems.
- Demonstrates the inheritance hierarchy of Appearance properties and how specificity affects the final cell appearance.

## Content

### Appearance Properties

**Figure 327: Appearance Properties**

To understand exactly what is going on here, let's consider three of these GridStyleInfo properties: **AnyCell**, **AnyRecordFieldCell**, and **AnyAlternateRecordFieldCell**. Say we set `AnyCell.BackColor = Color.LightBlue`. This will color any grid cell light blue.

**Note:** If you are using a **Themed Operating** system, like Windows XP, turn the `GridGroupingControl.ThemesEnabled` property off so that the theme coloring does not affect things like header cell buttons. Otherwise, this will interfere with illustrating the concepts we are trying to communicate in this section.

Next, if we set `AnyRecordFieldCell.BackColor = Color.Azure`, we will see the color of any record field cell change to azure. If we then set `AnyAlternateRecordFieldCell.BackColor = Color.LightGreen`, we will see alternate records being displayed with a green background. Below is a picture illustrating the look of the grid after setting each property in order.

### Inheritance Hierarchy of Appearance Properties

There is an inheritance hierarchy that is associated with the **Appearance** properties. The general rule is that, if present, the more specific property takes precedence over the less specific property. This means that `AnyCell.BackColor` is overridden by setting the `AnyRecordFieldCell.BackColor`, which is again overridden by setting even more specific `AnyAlternateRecordFieldCell.BackColor`.

## API Reference

**Properties**
- **BackColor**
  - **Type:** Color
  - **Description:** Specifies the background color of the grid cell.
  - **Default:** System default.
  - **Required:** No

### Code Examples

```csharp
// Setting the AnyCell.BackColor property
grid.StyleInfo.AnyCell.BackColor = Color.LightBlue;

// Setting the AnyRecordFieldCell.BackColor property
grid.StyleInfo.AnyRecordFieldCell.BackColor = Color.Azure;

// Setting the AnyAlternateRecordFieldCell.BackColor property
grid.StyleInfo.AnyAlternateRecordFieldCell.BackColor = Color.LightGreen;
```

## Cross References

### Related Topics

- [Managing Grid Appearances](#managing-grid-appearances)
- [Theming and Appearance in Grids](#theming-and-appearance-in-grids)

## RAG Annotations

<!-- tags: [winforms, grid, gridstyleinfo, appearance, colorproperties, inheritance] keywords: [anycell, anyrecordfieldcell, anyalternaterecordfieldcell, backcolor, lightblue, azure, lightgreen, theme, windowsxp] -->
```