```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: QTP
page_number: 044
page_id: QTP#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:59Z
fidelity: lossless
-->

## QuickTest Professional Grid Functions

### Overview

- **Grid Functions** for modifying and interacting with grid cells.
- Includes methods for setting cell values, checkbox states, radio buttons, current cell location, and scroll positions.
- Helper functions to manage grid editing, retrieve cell types, column counts, and extract formatted cell text.
- Methods to check if a cell contains a formula and retrieve its computed value.
- Functions to insert, remove, and manipulate rows and columns dynamically.

### Content

#### Grid Interaction Functions

- **SetCellData(int row, int col, string str)**
  - Sets the cell value of the cell.
- **SetCellCheckBox(int row, int col, string str)**
  - Sets the cell value of the check box cell.
- **SetCellRadioButton(int row, int col, string str)**
  - Sets the cell value of the radio button cell.
- **SetCurrentCell(int row, int col)**
  - Sets the location of the current cell.
- **SetScrollPosition(int vScrollPosition, int hScrollPosition)**
  - Sets the scroll position.

#### Helper Functions

- **BeginEdit(int row, int col)**
  - Brings the editing cursor in the specified grid cell.
- **EndEdit(int row, int col)**
  - Finishes the editing mode of the cell specified.
- **string GetCellType(int row, int col)**
  - Retrieves the CellType for the given cell coordinates.
- **int GetColumnCount()**
  - Retrieves the number of columns used.
- **int GetColumnlndex(string name)**
  - Finds the column index for the given column name, returns 0 if search fails.
- **string GetFormattedText(int row, int col)**
  - Retrieves the formatted cell format.
- **bool IsFormulaCell(int row, int col, out string formula, out string computedValue)**
  - For a given row and column index, IsFormulaCell points to the formula used in that cell and the result of the formula. This also returns "false" if this cell is not a formula cell.
- **object GetCellData(int row, int col)**
  - For the given Row and Column objects, the cell value of that cell can be obtained.
- **int GetRowCount()**
  - Retrieves the number of rows used.
- **InsertColumn(int insertAt, int count)**
  - Inserts a range of columns from the specified location.
- **InsertRow(int insertAt, int count)**
  - Inserts a range of rows from the specified location.
- **RemoveColumn(int from, int to)**
  - Removes a range of columns specified for the Grid.

#### RAG Annotations

- This section provides a comprehensive list of functions related to grid manipulation and interaction in the Syncfusion Winforms environment. These functions allow developers to programmatically modify grid contents, manage scroll positions, and perform various cell and grid-level operations efficiently.

### Tags and Keywords
<!-- tags: [grid, winforms, syncfusion, gridfunctions, cellinteraction, helperfunctions, datamanipulation, scrolling] keywords: [SetCellData, SetCellCheckBox, SetCellRadioButton, SetCurrentCell, SetScrollPosition, BeginEdit, EndEdit, GetCellType, GetColumnCount, GetColumnlndex, GetFormattedText, IsFormulaCell, GetCellData, GetRowCount, InsertColumn, InsertRow, RemoveColumn] -->
```