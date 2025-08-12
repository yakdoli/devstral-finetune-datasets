```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_184.jpeg
document_name: grid
page_number: 184
page_id: grid#page_184
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:26Z
fidelity: lossless
-->
# Essential Grid for Windows Forms

```csharp
gridBaseStyle1.StyleInfo.TextColor = Color.RosyBrown
gridControl1.BaseStylesMap.AddRange(New GridBaseStyle() {gridBaseStyle1})

' Apply this base style to a couple of cells.
gridControl1(1, 2).BaseStyle = "BackColorTest"
gridControl1(4, 2).BaseStyle = "BackColorTest"
```

### 4.1.4.2.3 GridRangeInfo

This class is used extensively to specify a collection of grid cells that are to be used as parameters for other method calls. `GridRangeInfo` class contains static methods that will allow you to specify a single cell, a rectangular range of cells, a row or rows, a column or columns, or the entire table.

| GridRangeInfo Method              | Description                                                                 |
|------------------------------------|----------------------------------------------------------------------------|
| GridRangeInfo.Cell(int row, int col) | Returns the GridRangeInfo object with cell row, col.               |
| GridRangeInfo.Cells(int top, int left, int bottom, int right) | Returns a GridRangeInfo object containing a rectangular collection of cells with top left cell (top, left) and bottom right cell (bot, right). |
| GridRangeInfo.Row(int row)         | Returns GridRangeInfo object with row = row.                         |
| GridRangeInfo.Rows(int fromRow, int toRow) | Returns a GridRangeInfo object containing rows fromRow through toRow. |
| GridRangeInfo.Col(int col)         | Returns GridRangeInfo object with column col.                        |
| GridRangeInfo.Cols(int fromCol, int toCol) | Returns a GridRangeInfo object containing columns fromCol through toCol. |
| GridRangeInfo.Table()             | Returns a GridRangeInfo object containing the whole table.             |

Note: For a complete description of the GridRangeInfo class, see the Essential Grid Class Reference.

<!-- tags: [product, module, control, api, version?] keywords: [GridRangeInfo, grid cells, method calls, parameters, static methods, GridRangeInfo.Cell, GridRangeInfo.Cells, GridRangeInfo.Row, GridRangeInfo.Rows, GridRangeInfo.Col, GridRangeInfo.Cols, GridRangeInfo.Table] -->
```