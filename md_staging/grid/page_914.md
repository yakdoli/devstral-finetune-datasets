```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_914.jpeg
document_name: grid
page_number: 914
page_id: grid#page_914
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:49Z
fidelity: lossless
-->

## Overview
- The page excerpt describes the selection modes in the Essential Grid for Windows Forms control, focusing on various selection behaviors such as column, row, table, and mixed range selections.
- It explains how to customize the selection mode using `GridSelectionFlags` enums and provides example code in both C# and VB.NET to demonstrate setting multiple selection modes with alpha blending.

## Content

### Selection Modes in the Grid

The following table describes the different selection modes available in the Essential Grid:

| Column | Columns can be selected. |
| --- | --- |
| Row | Rows can be selected. |
| Table | Whole table can be selected. |
| Shift | Allows user to extend the existing selection by holding the Shift key and clicking a cell. |
| MixRangeType | Allows you to select multiple ranges by holding the CTRL key. |
| Multiple | Allows both rows and columns to be selected at the same time when GridSelectionFlags.Multiple is enabled. |
| Keyboard | Allows extend existing selection when user holds SHIFT+Arrow keys. |
| Any | Default behavior for selecting cells: Rows, Columns, Cells, Table, Multiple, Extends Shift Key support and alpha blending. |
| None | Disable selecting cells. |

### Combining Selection Flags

You can combine more than one flags to customize the current selection behavior.

#### Example

Following code example illustrates how to set the selection mode for selecting multiple rows with alpha blending.

In **C#**:

```csharp
this.gridGroupingControl1.TableOptions.AllowSelection =
GridSelectionFlags.AlphaBlend | GridSelectionFlags.Row |
GridSelectionFlags.Multiple;
```

In **VB.NET**:

```vb
Me.gridGroupingControl1.TableOptions.AllowSelection =
GridSelectionFlags.AlphaBlend Or GridSelectionFlags.Row Or
GridSelectionFlags.Multiple
```

## Page-level Navigation/TOC (if applicable)
- If this page contains a table of contents or local navigation, it should be documented here. Since no specific TOC is present in this cropped excerpt, this section is left as is.

## Cross References
- This page is part of the Essential Grid for Windows Forms documentation, which may refer to other related sections or controls within the Syncfusion framework. See the main documentation for complete navigation and API references.

## Tags and Keywords
<!-- tags: [grid, selection, Windows Forms, Syncfusion, custom selection behavior, alpha blending, multiple selection, row selection, column selection] keywords: [selection behavior, Essential Grid, Windows Forms, GridSelectionFlags, alpha blending, multiple selection mode, shift key, extend selection] -->
```