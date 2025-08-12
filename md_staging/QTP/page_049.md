```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: QTP
page_number: 049
page_id: QTP#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:23Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Overview of various methods and properties related to grid controls.
- Functions to manipulate and query grid rows, columns, and ranges.
- Includes methods for resizing, selecting, grouping, and determining column and row states.

## Content

### Grid Control Methods

The following table lists the methods and their descriptions for grid controls:

| Method Name | Description |
|-------------|-------------|
| GetSelectedRowIndex() | Returns the top row index of the selected row. |
| GetSelectedRowRange() | Returns the Top and Bottom row of the selected row range. |
| GetTableName(object row) | Obtains the table name for a given Row. |
| GetTableNameByLevel(int level) | Gets the level of the table for the given table name. |
| GroupBy(string tablename, string column, string status) | Defines grouping and ungrouping of specified columns. |
| MouseDown(object row, object col, string button) | Raises the MouseDown. |
| MouseDownOnRowHeader(int row, int col, string button) | Raises the MouseDown on the RowHeader. |
| MoveColumn(string tablename, object fromColumn, object count, object target) | Moves a range of columns. |
| IsColSorted(int col) | Determines whether the column is sorted. |
| IsGroupExpanded(object row) | Determines whether the specified group is expanded. |
| IsGroupRow(object row) | Determines whether the specified row is a caption row or caption section. |
| IsRecord(object record) | Determines whether the specified row is a record. |
| IsRecordExpanded(object record) | Determines whether the specified record is expanded. |
| ResizeColumn(string tablename, int fromColumn, int to, int width) | Resizes the specified column. |
| ResizeRow(string tablename, int fromRow, int to, int height) | Resizes the specified rows. |
| SelectRange(string range, int top, int left, int bottom, int right) | Selects the range. |
| SelectRecord(object row, string status) | Selects a record for the GridGroupingControl. |

## API Reference

### Methods

#### GetSelectedRowIndex()
- **Returns**: The top row index of the selected row.

#### GetSelectedRowRange()
- **Returns**: The Top and Bottom row of the selected row range.

#### GetTableName(object row)
- **Parameters**:
  - `object row`: The row object for which the table name is obtained.
- **Returns**: The table name for the given Row.

#### GetTableNameByLevel(int level)
- **Parameters**:
  - `int level`: The level for which the table name is obtained.
- **Returns**: The level of the table for the given table name.

#### GroupBy(string tablename, string column, string status)
- **Parameters**:
  - `string tablename`: The name of the table to group.
  - `string column`: The column to group by.
  - `string status`: The status indicating grouping or ungrouping.
- **Description**: Defines grouping and ungrouping of specified columns.

#### MouseDown(object row, object col, string button)
- **Parameters**:
  - `object row`: The row object for the MouseDown event.
  - `object col`: The column object for the MouseDown event.
  - `string button`: The button type for the MouseDown event.
- **Description**: Raises the MouseDown event.

#### MouseDownOnRowHeader(int row, int col, string button)
- **Parameters**:
  - `int row`: The row number for the MouseDown event.
  - `int col`: The column number for the MouseDown event.
  - `string button`: The button type for the MouseDown event.
- **Description**: Raises the MouseDown event on the RowHeader.

#### MoveColumn(string tablename, object fromColumn, object count, object target)
- **Parameters**:
  - `string tablename`: The name of the table.
  - `object fromColumn`: The starting column to move.
  - `object count`: The number of columns to move.
  - `object target`: The target position for the moved columns.
- **Description**: Moves a range of columns.

#### IsColSorted(int col)
- **Parameters**:
  - `int col`: The column index to check.
- **Returns**: A boolean indicating whether the column is sorted.

#### IsGroupExpanded(object row)
- **Parameters**:
  - `object row`: The row object to check.
- **Returns**: A boolean indicating whether the specified group is expanded.

#### IsGroupRow(object row)
- **Parameters**:
  - `object row`: The row object to check.
- **Returns**: A boolean indicating whether the specified row is a caption row or caption section.

#### IsRecord(object record)
- **Parameters**:
  - `object record`: The record object to check.
- **Returns**: A boolean indicating whether the specified row is a record.

#### IsRecordExpanded(object record)
- **Parameters**:
  - `object record`: The record object to check.
- **Returns**: A boolean indicating whether the specified record is expanded.

#### ResizeColumn(string tablename, int fromColumn, int to, int width)
- **Parameters**:
  - `string tablename`: The name of the table.
  - `int fromColumn`: The starting column to resize.
  - `int to`: The ending column to resize.
  - `int width`: The new width for the columns.
- **Description**: Resizes the specified column.

#### ResizeRow(string tablename, int fromRow, int to, int height)
- **Parameters**:
  - `string tablename`: The name of the table.
  - `int fromRow`: The starting row to resize.
  - `int to`: The ending row to resize.
  - `int height`: The new height for the rows.
- **Description**: Resizes the specified rows.

#### SelectRange(string range, int top, int left, int bottom, int right)
- **Parameters**:
  - `string range`: The name of the range to select.
  - `int top`: The top boundary of the range.
  - `int left`: The left boundary of the range.
  - `int bottom`: The bottom boundary of the range.
  - `int right`: The right boundary of the range.
- **Description**: Selects the specified range.

#### SelectRecord(object row, string status)
- **Parameters**:
  - `object row`: The row object to select.
  - `string status`: The status for the GridGroupingControl.
- **Description**: Selects a record for the GridGroupingControl.

## Cross References
- See also: GridGroupingControl, Table operations, Row and Column manipulation.

<!-- tags: [Grid, Grouping, Control, Table, Row, Column, Select, Resize, MouseDown, GroupBy, Range, Record, Expand] keywords: [GridGroupingControl, table, row, column, select, resize, groupby, range, record, expand, collapse] -->
```