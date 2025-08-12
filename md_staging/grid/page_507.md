```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_507.jpeg
document_name: grid
page_number: 507
page_id: grid#page_507
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates different selection modes available in Essential Grid for Windows Forms.
- Explains how to activate various selection modes using GridSelectionFlags options.

## Content

### Selection Modes Overview
The image shows the **Selection Mode Demo** window, displaying various selection modes with corresponding checkboxes. The grid section lists contact information with columns for **Contact Name**, **Company Name**, and **Address**.

#### Figure 195: Selection Mode

The figure illustrates different selection modes with their corresponding descriptions:

- **AlphaBlend**:
  - Alpha blending to highlight selected cells can be achieved using `GridSelectionFlags.AlphaBlend` or by selecting the **AlphaBlend** checkbox under Selection Modes.
- **Any**:
  - The default behavior for selecting cells, rows, columns, tables, multiple extending SHIFT key support, and alpha blending can be achieved using `GridSelectionFlags.Any` or by selecting the **Any** checkbox under Selection Modes.
- **Column**:
  - Column selection can be achieved using `GridSelectionFlags.Column` or by selecting the **Column** checkbox under Selection Modes.
- **Row**:
  - Row selection can be achieved using `GridSelectionFlags.Row` or by selecting the **Row** checkbox under Selection Modes.
- **Keyboard**:
  - An existing selection can be extended when a user holds the SHIFT key and uses the arrow keys by using `GridSelectionFlags.Keyboard` or by selecting the **Keyboard** checkbox under Selection Modes.
- **MixRangeType**:
  - Selection of both rows and columns simultaneously when multiple selection is enabled can be achieved using `GridSelectionFlags.MixRangeType` or by selecting the **MixRangeType** checkbox under Selection Modes.
- **Table**:
  - Selection of the entire table can be achieved using `GridSelectionFlags.Table` or by selecting the **Table** checkbox under Selection Modes.

### Grid Selection Example

The screenshot shows the grid with the following entries:

| Contact Name     | CompanyName                     | Address                             |
|------------------|----------------------------------|-------------------------------------|
| Maria Anders     | Alfreds Futterkiste             | Obere Str. 57                      |
| Ana Trujillo     | Ana Trujillo Emparedados y helados | Avda. de la Constitución 2222     |
| Antonio Moreno   | Antonio Moreno Taquería          | Mataderos 2312                     |
| Thomas Hardy     | Around the Horn                 | 120 Hanover Sq.                    |
| Christina Berglund | Berglunds snabbköp             | Berguvsvägen 8                     |
| Hanna Moos      | Blauer See Delikatessen         | Forsterstr. 57                    |
| Frédérique Citeaux | Blondel père et fils           | 24, place Kléber                  |
| Martín Sommer    | Bólido Comidas preparadas       | C/ Araquil, 67                    |
| Laurence Lebihan | Bon app'                        | 12, rue des Bouchers               |
| Elizabeth Lincoln | Bottom-Dollar Markets           | 23 Tsawassen Blvd.                |
| Victoria Ashworth | B's Beverages                   | Fauntleroy Circus                 |

## API Reference

### Selection Modes

#### GridSelectionFlags

- **AlphaBlend**:
  - Highlighting selected cells with alpha blending.
- **Any**:
  - Default behavior for selecting various elements with SHIFT support.
- **Column**:
  - Selecting entire columns.
- **Row**:
  - Selecting entire rows.
- **Keyboard**:
  - Extending selection using keyboard input.
- **MixRangeType**:
  - Simultaneous selection of rows and columns.
- **Table**:
  - Selecting the entire table.

## Code Examples

The selection modes can be programmatically controlled using the following C# code:

```csharp
gridModel.SelectionFlags = GridSelectionFlags.Row | GridSelectionFlags.AlphaBlend;
```

## Page-level Navigation/TOC
- [Selection Modes Overview](#selection-modes-overview)
- [Grid Selection Example](#grid-selection-example)
- [API Reference](#api-reference)
- [Code Examples](#code-examples)

## Cross References
- See also: Essential Grid documentation for more detailed information on selection modes and customization.

### RAG Annotations
<!-- tags: [syncfusion, essentialgrid, windowsforms, selectionmodes, gridselectionflags] keywords: [grid, selection, modes, alphablend, any, column, row, keyboard, mixrangetype, table, windows forms, essential grid] -->
```
