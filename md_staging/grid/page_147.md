```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_147.jpeg
document_name: grid
page_number: 147
page_id: grid#page_147
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:58:07Z
fidelity: lossless
--> 

## Overview
- You will learn to add special controls to grid cells.
- Derive a cell control and populate Essential Grid.
- Use Grid control and GridStyleInfo classes.
- Work with Read-only attributes, Undo/Redo, rows, and columns.
- Create code for making the current row bold.
- Derive a GridPrintDocument.

## Content
Also, it discusses the following topics.

### 4.1.4.1 Adding Special Controls to Grid Cells

The GridStyleInfo property, `CellType`, lets you add special controls such as a check box or a combo box to a grid cell. Since the `CellType` is a member of GridStyleInfo, you can use it on a cell basis, row basis, column basis, or on a table basis, simply by setting this `CellType` property on the appropriate style. If you want the entire grid to be a combo box, then you simply have to set the grid's `CellValue` property to use combo boxes. You can derive your own controls to implement additional cell types. For more details, see *deriving a cell control*.

#### Table: Cell Types Supported in Essential Grid

The following table lists the cell types supported in Essential Grid.

| Grid Cell Control   | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Check Box          | Displays a check box in the cell.                                          |
| Color Edit         | Displays a color selection and allows editing color choices.               |
| Combo Box          | Displays a combo box in the cell.                                           |
| Control            | Displays a `System.Windows.Forms.Control` in a cell.                       |
| Currency Edit      | Displays a currency value and allows editing of it.                        |
| Formula Cell       | Displays calculation from a formula entered in the cell.                   |
| Grid List Control  | Displays a multicolumn list control as a drop                              |

#### Key Points:
- The `CellType` property is crucial for customizing grid cells.
- You can customize controls on different levels: individual cells, rows, columns, or tables.
- Deriving custom controls is possible for implementing additional cell types.

### API Reference (if applicable)
No specific API reference details are provided in this section.

### Code Examples (if applicable)
No code examples are provided in this section.

#### Cross References
See also:
- *deriving a cell control*

## RAG Annotations
<!-- tags: [essential grid, syncfusion winforms, grid, cell controls, types] keywords: [CellType, GridStyleInfo, Check Box, Color Edit, Combo Box, Control, Currency Edit, Formula Cell, Grid List Control, custom controls, cell customization, deriving a cell control] -->
```