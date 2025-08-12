```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_128.jpeg
document_name: diagram
page_number: 128
page_id: diagram#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:38Z
fidelity: lossless
-->


# Essential Diagram for Windows Forms

## Overview
- Describes properties related to text formatting and label positioning in Windows Forms.
- Focuses on properties like FitBlackBox, LineLimit, MeasureTrailingSpaces, NoClip, OffsetX, and OffsetY.
- Types are specified as either Boolean or float, providing control over text layout and visibility.

## Content

### Text Formatting Properties

The following table outlines the properties that control text formatting and label positioning:

| Property Name       | Description                                                                                       | Default Value | Type     | Default |
|---------------------|---------------------------------------------------------------------------------------------------|---------------|----------|---------|
| FitBlackBox         | Gets or sets a value indicating whether no part of any glyph overhangs the label bounds.            | NA            | Boolean  | NA      |
| LineLimit           | Gets or sets a value indicating whether only entire lines are laid out in the formatting rectangle. | NA            | Boolean  | NA      |
| MeasureTrailingSpaces | Gets or sets a value indicating whether space at the end of each line in calculations that measure the size of the text. | NA            | Boolean  | NA      |
| NoClip              | Gets or sets a value indicating whether overhanging parts of glyphs and unwrapped text reaching outside the formatting rectangle are allowed to show. | NA            | Boolean  | NA      |
| OffsetX             | Gets or sets the label offset x in percent relative to node's width from node's top left point.     | NA            | float    | NA      |
| OffsetY             | Gets or sets the label offset y in percent relative to node's width from node's top left point.     | NA            | float    | NA      |

### Description of Properties

- **FitBlackBox**: Ensures that no part of any text glyph extends beyond the specified label bounds.
- **LineLimit**: Ensures that only complete text lines are displayed within the formatting rectangle.
- **MeasureTrailingSpaces**: Indicates whether trailing spaces at the end of lines should be considered in text size calculations.
- **NoClip**: Allows overhanging parts of text and unwrapped text to be visible outside the formatting rectangle.
- **OffsetX / OffsetY**: Specifies the x and y offsets of the label in percent relative to the node's width and height, starting from the top-left point.

## API Reference

### Members

#### Properties
- **FitBlackBox**
  - Type: Boolean
  - Description: Controls whether text glyphs overhang the label bounds.
- **LineLimit**
  - Type: Boolean
  - Description: Controls whether only complete text lines are displayed.
- **MeasureTrailingSpaces**
  - Type: Boolean
  - Description: Controls whether trailing spaces are considered in text size calculations.
- **NoClip**
  - Type: Boolean
  - Description: Controls whether overhanging text is visible.
- **OffsetX**
  - Type: float
  - Description: Specifies the horizontal offset in percent relative to the node's width.
- **OffsetY**
  - Type: float
  - Description: Specifies the vertical offset in percent relative to the node's height.

---

<!-- tags: [diagram, windows forms, text formatting, label positioning, fitblackbox, linelimit, measuretrailingspaces, noclip, offsetx, offsety] keywords: [text layout, glyph overhang, line formatting, space measurements, unwrapped text visibility, label offsets, percentage offsets] -->
```