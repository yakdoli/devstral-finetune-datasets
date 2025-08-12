```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_170.jpeg
document_name: grid
page_number: 170
page_id: grid#page_170
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:58:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### 4.1.4.1.14 Rich Text

The Rich Text control will allow you to display and edit Rich Text in grid cells. The control enables you to optionally drop down an editable Rich Text window using which you can modify the Rich Text in the cell.

The following code example illustrates how to set the cell type to RichText.

#### C#

```csharp
// Create a Rich Text Format.
string rtf =
@"{\rtf1\ansi\deff0\deflang1033\deftab720
{\fonttbl{\f0\fswiss MS Sans Serif;}{\f1\froman\fcharset2 Symbol;}{\f2\fswiss\fcharset0 System;}{\f3\fswiss\fcharset0 Arial;}{\f4\froman\fcharset0 Bookman Old Style;}}
{\colortbl;\red0\green0\blue0;\red255\green0\blue0;}
\pard\par\fs20\par
{\plain\f0\fs16\cf0 * Change the "{\plain\f4\fs24\cf0\b\i<ul font \plain\f3\fs16\cf0 or "{\plain\f4\fs24\cf0\b\ul color\plain\f3\fs16\cf0 }" for individual characters.\par}
}";

// Set up a Rich Text Cell.
gridControl1[rowIndex, 1].CellType = "RichText";
gridControl1[rowIndex, 1].Text = rtf;
gridControl1.RowHeights[rowIndex] = 50;
gridControl1.CoveredRanges.Add(GridRangeInfo.Cells(rowIndex, 1, rowIndex, 5));
```

#### VB.NET

```vb
' Create a Rich Text Format.
Dim rtf As String = "{\rtf1\ansi\deff0\deflang1033\deftab720
{\fonttbl{\f0\fswiss MS Sans Serif;}" _
+ "{\f1\froman\fcharset2 Symbol;}" _
+ "{\f2\fswiss\fcharset0 System;}" _
+ "{\f3\fswiss\fcharset0 Arial;}" _
+ "{\f4\froman\fcharset0 Bookman Old Style;}}}" _
+ "{\colortbl;\red0\green0\blue0;\red255\green0\blue0;}" _
+ "\par\pard\par\fs20\par
{\plain\f0\fs16\cf0 * Change the "{\plain\f4\fs24\cf0\b\i\ul font \plain\f3\fs16\cf0}\plain\f4\fs24\cf0\b\i\ul or "{\plain\f4\fs24\cf0\b\ul color\plain\f3\fs16\cf0}" for individual characters.\par
}"
```

## API Reference

### Methods
- `CellType`: Sets the cell's display and editing behavior.
- `Text`: Sets or retrieves the text content of the cell.
- `RowHeights`: Allows setting the height of individual rows in the grid.
- `CoveredRanges`: Allows specifying areas in the grid covered by custom editors or styles.

### Properties
- `RichText`: A cell type that allows Rich Text formatting and editing.

## Code Examples

The above examples demonstrate how to configure a grid cell to display and edit Rich Text using the Rich Text control. By setting the `CellType` to "RichText" and specifying the content using an RTF string, the grid can handle formatted text effectively. Adjusting the `RowHeights` ensures that the content is displayed properly, and the use of `CoveredRanges` can further customize the interaction with the cell.

<!-- tags: [Syncfusion Winforms, Rich Text, Grid, CellType, RowHeights, CoveredRanges, RichText Control] keywords: [Rich Text, CellType, RowHeights, CoveredRanges, RTF, Cell Editing, Custom Editors, Grid, GridControl, Windows Forms] -->
```