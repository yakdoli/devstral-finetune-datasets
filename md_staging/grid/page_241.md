```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_241.jpeg
document_name: grid
page_number: 241
page_id: grid#page_241
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:05Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Properties

### Table 2: Property Table

| Property                 | Description                                                                                   | Type      | Data Type | Reference links |
|--------------------------|-----------------------------------------------------------------------------------------------|-----------|-----------|------------------|
| UnHideColsOnDblClick    | Indicates whether to allow unhide the hidden columns when double click the row.               | Property   | Boolean   | N/A.             |

### Sample Link

A demo of this feature is available in the following location:

```
..\..\AppData\Local\Syncfusion\EssentialStudio\{Installed Version}\Windows\Grid.Windows\Samples\2.0\Grid Layout\Hide Rows and Columns Demo
```

### Disabling Unhide Column by Double-Clicking

To disable unhide column by double-clicking, set the `UnHideColsOnDblClick` property to `false`. By default, this is set to `true`.

#### C#

```csharp
// Disables unhide column when double clicking as found in Excel.
this.gridControl1.UnHideColsOnDblClick = true;
```

#### VB

```vb
' Disables unhide column when double clicking as found in Excel.
Me.gridControl1.UnHideColsOnDblClick = True
```

### 4.1.4.5.9 Highlighting Row and Column Headers

This feature is used to highlight the corresponding row and column headers of one or more cells that you selected. Using the `MarkRowHeader` and `MarkColHeader` properties, you can enable highlighting the row and column headers of the selected cells.

---

© 2013 Syncfusion. All rights reserved.
<!-- tags: [winforms, essentialgrid, gridlayout, unhidere Ondblclick, markrowheader, markcolheader, highlighting, syncfusion, 11.4.0.26] keywords: [UnHideColsOnDblClick, MarkRowHeader, MarkColHeader, row header, column header, double-click, highlighting, property table, grid, windows forms] -->
```