```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_048.jpeg
document_name: QTP
page_number: 048
page_id: QTP#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:19Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Provides methods for interacting with Grid and Table elements in a WinForms application.
- Includes functions for collapsing and expanding groups, retrieving cell data, getting row and column counts, and managing grid details.

## Content

### WinForms Methods

The following table lists methods for working with Grid and Table elements:

| Method Name | Description |
|-------------|-------------|
| `CollapseGroup(object row)` | Collapses the group. |
| `ExpandGroup(object row)` | Expands the group. |
| `ExpandRecord(object record)` | Expands the record. |
| `FindRecordInGrid(string tableObject, string columnName, string data)` | Returns the first index of the searched data for the given column of the table, as located in the NestedDisplayElements. |
| `FindRecordInTable(string tableObject, string columnName, string data)` | Returns the first index of the searched data for the given column. |
| `GetAbsoluteRowIndex(int RowIndex)` | Retrieves the absolute RowIndex. |
| `GetBackColor(int row)` | Gets the backcolor of the record. |
| `GetCellBackColor(object row, object col)` | Gets the backcolor of the Cell. |
| `GetCellData(object row, object col)` | For the given Row and Column objects, the cell value of that cell can be obtained. |
| `GetChildCount(object row)` | Gets the child count for the given caption row and a record row. |
| `GetDescription(object row, object col)` | Gets the description of grid cells. |
| `GetColumnCount()` | Returns the sort order of the sorted column (Ascending or Descending). |
| `GetColSortOrder(int col)` | Returns the sort order of the sorted column (Ascending or Descending). |
| `GetColumnName(string tablename, int colindex)` | For a given table name and column index, the column name in which an element resides can be obtained. |
| `GetDetails()` | Gets details like table, record, and table descriptor. |
| `GetLevelByTableName(string name)` | Gets the level of table for the given table name. |
| `GetRowCount()` | Retrieves the number of rows used. |
| `GetRowElement(object row)` | Gets the row element. |
| `GetSelectedColIndex()` | Returns the Left column index of the selected |

## API Reference

### Methods

#### CollapseGroup(object row)
**Description**: Collapses the group.

#### ExpandGroup(object row)
**Description**: Expands the group.

#### ExpandRecord(object record)
**Description**: Expands the record.

#### FindRecordInGrid(string tableObject, string columnName, string data)
**Description**: Returns the first index of the searched data for the given column of the table, as located in the NestedDisplayElements.

#### FindRecordInTable(string tableObject, string columnName, string data)
**Description**: Returns the first index of the searched data for the given column.

#### GetAbsoluteRowIndex(int RowIndex)
**Description**: Retrieves the absolute RowIndex.

#### GetBackColor(int row)
**Description**: Gets the backcolor of the record.

#### GetCellBackColor(object row, object col)
**Description**: Gets the backcolor of the Cell.

#### GetCellData(object row, object col)
**Description**: For the given Row and Column objects, the cell value of that cell can be obtained.

#### GetChildCount(object row)
**Description**: Gets the child count for the given caption row and a record row.

#### GetDescription(object row, object col)
**Description**: Gets the description of grid cells.

#### GetColumnCount()
**Description**: Returns the sort order of the sorted column (Ascending or Descending).

#### GetColSortOrder(int col)
**Description**: Returns the sort order of the sorted column (Ascending or Descending).

#### GetColumnName(string tablename, int colindex)
**Description**: For a given table name and column index, the column name in which an element resides can be obtained.

#### GetDetails()
**Description**: Gets details like table, record, and table descriptor.

#### GetLevelByTableName(string name)
**Description**: Gets the level of table for the given table name.

#### GetRowCount()
**Description**: Retrieves the number of rows used.

#### GetRowElement(object row)
**Description**: Gets the row element.

#### GetSelectedColIndex()
**Description**: Returns the Left column index of the selected.

## Code Examples

### Example: Retrieving Cell Data
```csharp
object row = grid.Rows[0];
object col = grid.Columns[0];
string cellData = (string)grid.GetCellData(row, col);
```

### Example: Getting the Description of Grid Cells
```csharp
string description = grid.GetDescription(row, col);
```

## Page-level Navigation/TOC
- Methods for Grid and Table Interaction
- Description of each method

## Cross References
- Refer to the Grid and Table sections for more details on these elements.

## RAG Annotations
<!-- tags: Grid, Table, WinForms, QuickTest, Method, Property, Version: 11.4.0.26 -->
```