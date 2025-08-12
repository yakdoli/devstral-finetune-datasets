```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_469.jpeg
document_name: grid
page_number: 469
page_id: grid#page_469
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the functionality of hiding rows and columns in the `GridControl`.
- Shows the default grid setup with all rows and columns visible.
- Explains how to hide specific rows and columns.
- Guides through setting the number of header rows and columns using properties.

---

### GridDisplay

#### Figure 178: Default Grid With No Hidden Rows or Columns
![](Figure 178.png)

---

#### Figure 179: Grid with the Column Headers, Row 5 and Column 4 Hidden
![](Figure 179.png)

---

## Content

### Header Rows and Columns

#### Section: 4.1.4.14.2 Header Rows and Columns

We have seen in the previous section that it is possible to hide both the row and column headers. Additionally, we can have more than one header row and/or more than one header column. The properties that control the number of header rows and columns are `GridControl.Rows.HeaderCount` and `GridControl.Cols.HeaderCount`. The `HeaderCount` property is the index of the last header row or column. To have a total of three column header rows, set `Rows.HeaderCount` to two.

---

## API Reference

#### Properties
- `GridControl.Rows.HeaderCount`: Controls the number of header rows.
- `GridControl.Cols.HeaderCount`: Controls the number of header columns.

---

## Code Examples

Example: Setting the number of header rows and columns in C#:
```csharp
gridControl.Rows.HeaderCount = 2;
gridControl.Cols.HeaderCount = 1;
```

---

## Page-level Navigation/TOC
- 4.1.4.14.2 Header Rows and Columns

---

## Tags and Keywords
<!-- tags: [Essential Grid, Windows Forms, Header Rows, Header Columns, GridControl, Syncfusion Winforms, HeaderCount] keywords: [GridControl, HeaderCount, Rows, Columns, WinForms, Row Headers, Column Headers, Syncfusion] -->
```