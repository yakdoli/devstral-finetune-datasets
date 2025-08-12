```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: QTP
page_number: 050
page_id: QTP#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:11Z
fidelity: lossless
-->

## Overview
- Describes various methods applicable to grid controls, highlighting functionality for setting cell values, managing scroll positions, and performing operations like sorting and resizing.
- Explains methods specific to `GridListControl` for resizing columns and rows, selecting ranges, and retrieving the control name.
- Lists the `GetName()` method for `TabBarSplitterControl`, indicating functionality to retrieve the name of the `TabBarControl`.

## Content

| Method                              | Description                                    |
|-------------------------------------|------------------------------------------------|
| SetCellData(object row, object col, string str) | Sets the cell value of the cell.              |
| SetCellCheckBox(object row, object col, string str) | Sets the cell value of the check box cell.  |
| SetCellRadioButton(object row, object col, string str) | Sets the cell value of the radio button cell. |
| SetCurrentCell(object row, object col) | Sets the location of current cell.            |
| SetScrollPosition(int vScrollPosition, int hScrollPosition) | Sets the scroll position.                 |
| SortColumn(string tablename, object col, string sortBehavior, bool cntrl) | Sorts the column.                      |
| SelectRecords(object row, object count) | Selects multiple records for the GridGroupingControl.                                      |
| ScrollToColumn(string tablename, object col) | The grid will scroll to the given column.    |
| ScrollToRow(int row)               | The grid will scroll to the given row.        |
| AddNewRow(string objn)             | A new row will be added.                      |
| string GetFormattedText(int row, int col) | Retrieves the formatted cell value.         |
| string GetName()                   | Gets the name of the Grid control object.     |

### GridListControl

| Method                              | Description                                    |
|-------------------------------------|------------------------------------------------|
| ResizeColumn(object fromColumn, int to, int width) | Resizes the specified columns.             |
| ResizeRow(int fromRow, int to, int height) | Resizes the specified rows.                 |
| SelectRow(int top, int bottom)     | Selects the range.                            |
| string GetName()                   | Gets the name of the GridListControl object    |

### TabBarSplitterControl

| Method                              | Description                                    |
|-------------------------------------|------------------------------------------------|
| GetName()                          | Gets the name of the TabBarControl.            |

## API Reference (if applicable)

The table above lists various methods and their descriptions relevant to grid controls, `GridListControl`, and `TabBarSplitterControl` in Syncfusion Winforms. These methods provide functionality for setting and retrieving values, managing grid views, and interacting with control elements.

## Code Examples (multi-language supported)

While no explicit code examples are provided in the image, the methods listed can be used in code as follows:

```csharp
// Example usage of SetCellData
grid.SetCellData(row, col, "newValue");

// Example usage of ResizeColumn
listControl.ResizeColumn("columnName", 50, 100);

// Example usage of GetName
string controlName = tabSplitterControl.GetName();
```

These examples illustrate how the methods described can be integrated into a C# application.

## Page-level Navigation/TOC (if applicable)

This page provides comprehensive documentation for grid-related controls in Syncfusion Winforms, focusing on methods applicable to grid manipulation and control management.

## Cross References

See also:
- Documentation for other grid-related controls and functionalities in Syncfusion Winforms.
- Additional API references and examples for Syncfusion Winforms controls.

<!-- tags: [syncfusion-sdk, syncfusion-winforms, grid-controls, gridlistcontrol, tabbarsplittercontrol, api-reference] keywords: [setcelldata, scrollposition, sortcolumn, resizecolumn, resizerow, selectrow, getname, gridcontrols, winforms] -->
```