```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_875.jpeg
document_name: grid
page_number: 875
page_id: grid#page_875
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstration of the GridTableBaseStyle Collection Editor for configuring cell styles in a Windows Forms application.
- Explanation of how to assign different base styles to alternate record field cells and other grid cells.

## Content

### Configuring Base Styles for Grid Cells

#### GridTableBaseStyle Collection Editor

![](Figure 340: GridTableBaseStyle Collection Editor)

Your next step is to set the base styles created above to the grid cells as required. Suppose if you want to set BaseStyle1 for alternate record field cells and BaseStyle2 for the remaining cells, then this can be specified by setting `Appearance.AlternateRecordFieldCell.BaseStyle` property to `BaseStyle1` and `Appearance.AnyCell.BaseStyle` property to `BaseStyle2` as shown in the image below.

## API Reference (if applicable)

### Properties

- **Appearance**
  - **AlternateRecordFieldCell.BaseStyle**: Specifies the style for alternate record field cells.
  - **AnyCell.BaseStyle**: Specifies the base style for any cell in the grid.

## Code Examples

An example of setting base styles:

```csharp
// Assuming BaseStyle1 and BaseStyle2 are already defined
grid.Grouping(Appearance.AlternateRecordFieldCell.BaseStyle, BaseStyle1);
grid.Grouping(Appearance.AnyCell.BaseStyle, BaseStyle2);
```

## Page-level Navigation/TOC (if applicable)

- GridTableBaseStyle Collection Editor
- Configuring Base Styles for Grid Cells

## Cross References

See also:
- [GridGroupingControl Properties and Methods](#)
- [Appearance API Reference](#)

<!-- tags: [Syncfusion Winforms, GridGroupingControl, BaseStyles, Appearance] keywords: [GridTableBaseStyle, Collection Editor, AlternateRecordFieldCell, BaseStyle1, BaseStyle2] -->
```