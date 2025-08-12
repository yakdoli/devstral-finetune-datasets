```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_191.jpeg
document_name: XlsIO
page_number: 191
page_id: XlsIO#page_191
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:44Z
fidelity: lossless
-->

## Overview

- Examples of methods for showing columns and rows.
- Demonstration of a worksheet with a hidden row.
- Methods to focus on specific rows and columns upon opening.

## Content

The following code examples demonstrate how to control the visibility of specific rows and columns in a worksheet:

```csharp
sheet.ShowColumn(5, True)
sheet.ShowRow(2, True)
```

**Figure 66: Worksheet with a hidden row**

![Worksheet with a hidden row](./images/XlsIO#page_191/figure66.png)

XlsIO also provides options to provide focus to a particular row/column when it is opened by using the `TopVisibleRow` and `LeftVisibleColumn` properties respectively.

### Focus on Specific Rows and Columns

The following code snippets illustrate how to set focus on specific rows or columns when a worksheet is opened:

#### C#
```csharp
// Scrolls to 40th row
sheet.TopVisibleRow = 40;

// Scrolls to 7 column when opening
sheet.LeftVisibleColumn = 7;
```

#### VB.NET
```vb
' Scrolls to 40th row
sheet.TopVisibleRow = 40

' Scrolls to 7 column when opening
sheet.LeftVisibleColumn = 7
```

### API Reference

- **ShowColumn(5, True)**: Shows the 5th column.
- **ShowRow(2, True)**: Shows the 2nd row.
- **TopVisibleRow**: Property to specify the top visible row.
- **LeftVisibleColumn**: Property to specify the leftmost visible column.

### Code Examples

The provided examples show how to manipulate the visibility and focus of rows and columns in a worksheet using the XlsIO library.

#### C#
```csharp
// Example: Show specific columns and rows and set focus
sheet.ShowColumn(5, True);
sheet.ShowRow(2, True);
sheet.TopVisibleRow = 40;
sheet.LeftVisibleColumn = 7;
```

#### VB.NET
```vb
' Example: Show specific columns and rows and set focus
sheet.ShowColumn(5, True)
sheet.ShowRow(2, True)
sheet.TopVisibleRow = 40
sheet.LeftVisibleColumn = 7
```

### Notes

- The `ShowColumn` and `ShowRow` methods are used to make specific columns and rows visible.
- The `TopVisibleRow` and `LeftVisibleColumn` properties control the initial visible rows and columns when the worksheet is opened.

<!-- tags: [XlsIO, worksheets, row-column visibility, focus, TopVisibleRow, LeftVisibleColumn] keywords: [rows, columns, hidden, visible, focus, worksheet] -->
```