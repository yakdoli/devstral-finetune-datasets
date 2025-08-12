```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_208.jpeg
document_name: grid
page_number: 208
page_id: grid#page_208
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:51Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates ButtonEdit cells in a grid.
- Explains embedding OLE objects in grid cells.
- Provides use case scenarios and sample code for implementation.

## Content

### Button Edit Cells

| A                 | B                     | C                      | D                     | E                    |
|-------------------|-----------------------|------------------------|-----------------------|----------------------|
| 1                 | ButtonEdit displaying common images             |                        |                      |                      |
| 2                 | ...                   | √                     | ▼                     | 🖼                   |
| 3                 |                        |                        |                      |                      |
| 4                 | Option to show the button to the Left side     |                        |                      |                      |
| 5                 | ...                   | √                     |                      |                      |
| 6                 |                        |                        |                      |                      |
| 7                 | Setting text, textcolor and text alignment for the |                      |                      |                      |
| 8                 | Sync                  | Sync                  | Sync                  | Sync                 |
| 9                 |                        |                        |                      |                      |
| 10                | Setting the width of button                    |                        |                      |                      |
| 11                |                        | ...                   |                      |                      |
| 12                |                        |                        |                      |                      |
| 13                | Setting the BackColor (In a themed application, |                      |                      |                      |
| 14                |                        | 🟩                    | 🟧                   | 🟦                   |

**Figure 107: Button Edit Cells**

### 4.1.4.4.2 Embedding OLE Objects in the Grid Cell

- OLE objects can be directly embedded to a grid's cell, which by default displays the icon of the file attached. Activating the cell will open the file through its default associated application.
- This custom cell type hosts the cell as an OLE container. The file address should be passed through the cell's `Style.Description` value.

#### Use Case Scenarios
- In a payroll application, the generated report can be attached to the grid and viewed directly. After viewing, the grid should be exported to Excel to reflect recent changes; otherwise, the document will not show the updates.

#### Sample Link
- Find examples in the following location:
  ```
  <Install Location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Grid.Windows\Samples\2.0\ Grid Controls / Grid Control / Concepts and Features\Custom Cell Types
  ```

### Adding OleContainer Cell to an Application

The following code illustrates how to set the cell type to `OleContainer`:

#### C#
```csharp
RegisterCellModel.GridCellType(this.gridControl1, CustomCellTypes.OleContainerCell);
this.gridControl1[rowIndex, colIndex].CellType = CustomCellTypes.OleContainerCell;
```

## Page-level Navigation/TOC (if applicable)
- 4.1.4.4.2 Embedding OLE Objects in the Grid Cell
- Use Case Scenarios
- Sample Link
- Adding OleContainer Cell to an Application

### Cross References
- See also: ButtonEdit cells, OLE embedding, grid controls, custom cell types.

<!-- tags: [Syncfusion Winforms, Grid, OLE embedding, Custom Cell Types, OleContainerCell] keywords: [OLE objects, grid cells, custom cell types, payroll application, Excel export, sample link] -->
```
