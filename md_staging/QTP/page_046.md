```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: QTP
page_number: 046
page_id: QTP#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:54Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Methods

| **Method**                                      | **Description**                                           |
|-------------------------------------------------|-----------------------------------------------------------|
| ResizeColumn(int fromColumn, int to, int width)| Resizes the specified columns.                           |
| ResizeRow(int fromRow, int to, int height)     | Resizes the specified rows.                              |
| SelectRange(string range, int top, int left, int bottom, int right)| Selects the range.                |
| SetCellData(int row, int col, string str)      | Sets the cell value of the cell.                         |
| SetCellCheckBox(int row, int col, string str)  | Sets the cell value of the check box cell.              |
| SetCellRadioButton(int row, int col, string str)| Sets the cell value of the radio button cell.           |
| SetCurrentCell(int row, int col)               | Sets the location of current cell.                       |
| SetScrollPosition(int vScrollPosition, int hScrollPosition)| Sets the scroll position.                  |
| SortColumn(int col, string sortBehavior)       | Sorts the column.                                        |

## Helper Functions

| **Function**                                  | **Description**                                           |
|-----------------------------------------------|-----------------------------------------------------------|
| BeginEdit(int row, int col)                  | Brings the editing cursor in the specified grid cell.    |
| string GetCellType(int row, int col)         | Retrieves the CellType for the given cell coordinates.    |
| string GetCellBackColor(int row, int col)    | Retrieves the Back color for the given cell coordinates.  |
| int GetColumnCount()                         | Retrieves the number of columns used.                    |
| int GetVisibleColumnCount()                  | Retrieves the number of visible columns.                 |
| int GetColumnIndex(string name)              | Finds the column index for the given column name, returns 0 if search fails.  |
| Int GetCurrentCellImageIndex(int row, int col)| Gets the image index of the current cell.                |
| string GetFormattedText(int row, int col)    | Retrieves the formatted cell value.                     |
| bool IsColumnVisible(int col)                | Checks if the column is visible.                        |
| bool IsFormulaCell(int row, int col, out string formula, out string computedValue)| For a given row and column index, IsFormulaCell points to the formula used in that cell and the result |

## Cross References
See also:
- [Syncfusion documentation](https://www.syncfusion.com/documentation)

<!-- tags: [syncfusion, winforms, quicktest professional, api, methods, helper functions] keywords: [resizecolumn, resizerow, selectrange, setcelldata, setcellcheckbox, setcellradiobutton, setcurrentcell, setscrollposition, sortcolumn, beginedit, getcelltype, getcellbackcolor, getcolumncount, getvisiblecolumncount, getcolumnindex, getcurrentcellimageindex, getformattedtext, iscolumnvisible, isformulacell] -->
```