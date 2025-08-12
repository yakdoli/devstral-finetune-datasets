<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_175.jpeg
document_name: grid
page_number: 175
page_id: grid#page_175
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:00:19Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the cell type architecture of the Essential Grid.
- Details the use of GridStyleInfo objects to manage cell appearance and behavior.
- Highlights the inheritance process of GridStyleInfo objects from parent styles.

## Content

### 4\.1\.4\.2 Cell Style Architecture

The Essential Grid's cell style architecture plays an integral role in almost every aspect of Essential Grid. A basic understanding of this layered cell style architecture will help you understand and learn the grid behavior. This is particularly important when you are trying to modify or extend some existing functionality.

#### 4\.1\.4\.2\.1 GridStyleInfo Class Overview

Grid control can be thought of as a rectangular table of grid cells. Each cell contains distinct information and can be displayed independently of other cells. EssentiGrid uses `GridStyleInfo` objects to store state information about the appearance of a grid cell. So attributes like `font`, `backcolor`, `cellvalue`, and `celltype` are all reflected in a single `GridStyleInfo` object.

Every cell in a grid may have such an object associated with it, giving the individual cell its unique appearance. It is not necessary that all cells should require fully populated `GridStyleInfo` objects stored in memory to function. And, for a given `GridStyleInfo` object, not all possible properties need to be populated in the object. So for example, a particular cell may or may not have a stored `GridStyleInfo` object, and if it does, this `GridStyleInfo` object may, or may not, contain a particular property such as `Font`.

In general, when Essential Grid needs a cell's state information, usually to draw the cell, it uses an inheritance process to generate a `GridStyleInfo` from several parent styles. The following parent styles are `GridStyleInfo` objects associated with particular grid entities:

- `TableStyle` is a single `GridStyleInfo` object that is associated with the entire grid.
- `RowStyles` are `GridStyleInfo` objects that are associated with each row.
- `ColumnStyles` are `GridStyleInfo` objects that are associated with each column.

These three `GridStyleInfo` objects may not be fully populated, meaning that some properties may not have been set. However, there is a fourth parent style referred to as the `StandardStyle`, which is a fully populated style object, meaning every property has a setting in the `StandardStyle`.

## Code Examples

```csharp
gridControl1(rowIndex, colIndex).CellType = "TextBox";
gridControl1(rowIndex, colIndex + 1).ImageIndex = 1;
```

### Figure 93: Text Box Cells
![Figure 93: Text Box Cells](43.png)

```html
<Figure: Text Box Cells>
<image src="43.png" alt="Figure 93: Text Box Cells" />
</Figure>
```

<!-- tags: [Essential Grid, Windows Forms, Cell Style Architecture, GridStyleInfo, TableStyle, RowStyles, ColumnStyles, StandardStyle, font, backcolor, cellvalue, celltype] -->
