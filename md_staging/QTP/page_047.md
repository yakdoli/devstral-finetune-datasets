```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_047.jpeg
document_name: QTP
page_number: 047
page_id: QTP#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:12Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Provides a list of methods and properties for interacting with grid controls.
- Includes functionalities for retrieving cell values, managing grid visibility, sorting columns, and more.
- Focuses on GridControl and GridGroupingControl interactions.

## Content

### GridControl Methods

| Method                              | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| object GetCellData(int row, object col) | For the given Row and Column objects, the cell value of that cell can be obtained. |
| int GetRowCount()                  | Retrieves the number of rows used.                                      |
| ScrollToCell(int rowIndex, int colIndex) | Scrolls the grid so as the cell to be visible for replay.                    |
| HideRow(int from, int to)          | Hides a range of rows specified for the GridControl.                     |
| HideCol(int from, int to)          | Hides a range of columns specified for the GridControl.                   |
| int GetSelectedRowIndex()          | Returns the top row index of the selected row.                            |
| int GetSelectedColIndex()          | Returns the column index of the selected column.                         |
| int GetSelectedRowCount()          | Returns the number of selected rows.                                     |
| int GetSelectedColCount()          | Returns the number of selected columns.                                  |
| string GetSelectedRowRange()       | Returns the Top and Bottom row of the selected row range.                 |
| string GetSelectedColRange()       | Returns the left and right column of the selected column range.          |
| bool IsColSorted(int col)          | Determines whether the column is sorted.                                 |
| string GetColSortOrder(int col)    | Returns the sort order of the sorted column (Ascending or Descending).    |
| string GetName()                   | Gets the name of the Grid DataBoundGrid object.                          |

### GridGroupingControl Methods

| Method                         | Description                     |
|--------------------------------|----------------------------------|
| CellButtonClick(object row, object col) | Raises the cell button click. |
| CellDoubleClick(object row, object col) | Raises the cell double-click. |
| CollapseRecord(object record) | Collapses the record.           |

## Page-level Navigation/TOC (if applicable)
- The page provides detailed information about the methods available for managing grid controls.
- The content is structured to help users understand how to interact with GridControl and GridGroupingControl effectively.

<!-- tags: [Syncfusion, QuickTest Professional, GridControl, GridGroupingControl, WinForms] keywords: [GetCellData, GetRowCount, ScrollToCell, HideRow, HideCol, GetSelectedRowIndex, GetSelectedColIndex, GetSelectedRowCount, GetSelectedColCount, GetSelectedRowRange, GetSelectedColRange, IsColSorted, GetColSortOrder, GetName, CellButtonClick, CellDoubleClick, CollapseRecord] -->
```