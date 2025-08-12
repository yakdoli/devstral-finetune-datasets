```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_522.jpeg
document_name: grid
page_number: 522
page_id: grid#page_522
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to use the `CopyTextToClipboard` method to copy text from a specified range of cells in a grid.
- Explains the `CopyCellsToClipboard` method to copy cell styles and settings to the clipboard.
- Provides code examples in both C# and VB.NET for implementation.

## Content

The selection starts from the cell (1,2) – with row index 1 and column index 2 to the cell (1,4) – with row index 1 and column index 4 of the grid.

### Using C#

The following code examples show how to call the `CopyTextToClipboard` method:

```csharp
this.gridControl1.Model.CutPaste.CopyTextToClipboard(GridRangeInfo.Cells(1, 2, 1, 4));
```

### Using VB.NET

```vb.net
Me.gridControl1.Model.CutPaste.CopyTextToClipboard(GridRangeInfo.Cells(1, 2, 1, 4))
```

#### CopyCellsToClipboard(GridRangeInfoList list, bool bLoadBaseStyles)
This method copies the style information of a specified range of cells to the clipboard. The range of cells to be copied is given to the method as the first parameter. The second parameter represents a Boolean value. The base style will be copied along with default settings, if it is set to true. Only the default settings that were initialized to the cell are copied if it is set to false.

### Code Examples

#### Using C#

```csharp
GridRangeInfoList list = new GridRangeInfoList();
list.Add(GridRangeInfo.Cell(2, 2));
this.gridControl1.Model.CutPaste.CopyCellsToClipboard(list, true);
```

#### Using VB.NET

```vb.net
Dim list As New GridRangeInfoList()
list.Add(GridRangeInfo.Cell(2, 2))
Me.gridControl1.Model.CutPaste.CopyCellsToClipboard(list, True)
```

## API Reference

### Methods
- **CopyTextToClipboard**:
  - Parameters:
    - `GridRangeInfo` - Specifies the range of cells to copy.
  - Description: Copies the text content of the specified range of cells to the clipboard.

- **CopyCellsToClipboard**:
  - Parameters:
    - `GridRangeInfoList` - A list of `GridRangeInfo` objects representing the range of cells to copy.
    - `bool bLoadBaseStyles` - A boolean indicating whether to copy the base style along with the cell settings.
  - Description: Copies the style information of the specified range of cells to the clipboard.

## Code Examples

The document provides code examples in both C# and VB.NET for both `CopyTextToClipboard` and `CopyCellsToClipboard` methods.

<!-- tags: [Syncfusion, GridControl, WinForms, Copy, Clipboard, Cell Styles, User Guide] keywords: [GridRangeInfo, GridRangeInfoList, CopyTextToClipboard, CopyCellsToClipboard, C#, VB.NET, Cell Styles, Clipboard, WinForms] -->
```