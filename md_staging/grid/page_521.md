```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_521.jpeg
document_name: grid
page_number: 521
page_id: grid#page_521
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:40Z
fidelity: lossless
-->

## Grid Control Cut, Copy, and Paste Methods

### Overview
- Introduces methods to handle clipboard operations in the `GridControl`.
- Discusses the `Copy`, `CopyRange`, and `CopyTextToClipboard` methods for copying grid cell contents to the clipboard.

### Content

#### Copy Method
- **Purpose**: Copies the contents of selected cells and the current cell's contents to the clipboard.
- **Code Examples**:
  - **Using C#**
    ```csharp
    [C#]
    this.gridControl1.Model.CutPaste.Copy();
    ```
  - **Using VB.NET**
    ```vb
    [VB.NET]
    Me.gridControl1.Model.CutPaste.Copy()
    ```

#### CopyRange Method
- **Signature**: `CopyRange(GridRangeInfo range)`
- **Purpose**: Copies the contents of a specified range of cells to the clipboard.
- **Parameter**: `GridRangeInfo range` - Defines the range of cells to be copied.
- **Example**: If `GridRangeInfo.Cell(2, 2)` is specified, only the cell at row index 2 and column index 2 is copied.
- **Code Examples**:
  - **Using C#**
    ```csharp
    [C#]
    this.gridControl1.Model.CutPaste.CopyRange(GridRangeInfo.Cell(2, 2));
    ```
  - **Using VB.NET**
    ```vb
    [VB.NET]
    Me.gridControl1.Model.CutPaste.CopyRange(GridRangeInfo.Cell(2, 2))
    ```

#### CopyTextToClipboard Method
- **Signature**: `CopyTextToClipboard(GridRangeInfo range)`
- **Purpose**: Copies the formatted text of a specified range of cells to the clipboard.
- **Parameter**: `GridRangeInfo range` - Defines the range of cells to be copied.
- **Example**: If `GridRangeInfo.Cell(1, 1, 4)` is specified, the formatted text from the specified range is copied to the clipboard.

### API Reference

#### Methods
- `Copy()`
  - Copies the contents of selected cells and the current cell to the clipboard.
- `CopyRange(GridRangeInfo range)`
  - Copies the contents of a specified range of cells to the clipboard.
- `CopyTextToClipboard(GridRangeInfo range)`
  - Copies the formatted text of a specified range of cells to the clipboard.

### Code Examples

#### C# Example
```csharp
// Copy all selected cells
this.gridControl1.Model.CutPaste.Copy();

// Copy a specific cell
this.gridControl1.Model.CutPaste.CopyRange(GridRangeInfo.Cell(2, 2));
```

#### VB.NET Example
```vb
' Copy all selected cells
Me.gridControl1.Model.CutPaste.Copy()

' Copy a specific cell
Me.gridControl1.Model.CutPaste.CopyRange(GridRangeInfo.Cell(2, 2))
```

### Cross References
- For more information on grid control properties, see the Grid API documentation.
- Related topics: Clipboard Operations, Cell Selection, GridRangeInfo.

<!-- tags: [grid, clipboard, copy, cutpaste, winforms, syncfusion] keywords: [gridcontrol, gridrangeinfo, copy, cut, paste, clipboard, cell, range, selection] -->
```
