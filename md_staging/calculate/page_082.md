```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_082.jpeg
document_name: calculate
page_number: 082
page_id: calculate#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:02Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- The page focuses on using DataGrids with calculation support in Syncfusion WinForms.
- It explains how to register ICalcData objects with the CalcEngine to enable cross-references among multiple worksheets.
- Examples of formulas and cell reference syntax are provided, demonstrating how to use formulas in a DataGrid.

## Content

### Using DataGrids with Calculation Support

Figure 35 shows a workbook with multiple DataGrids (DG1, DG2, DG3, DG4, DG5) displaying numerical data.

#### Figure 35: Workbook

---
![Workbook Screenshot](#image)  
---

---

To support cross-references among several ICalcData objects, you must register the objects with a single instance of the CalcEngine. Part of the information provided during registration includes names associated with each ICalcData object. To reference a particular cell in an ICalcData object, you need to use its name along with the column and row to determine the proper reference. For example, say, in an ICalcData object whose name is `Sales`, to reference column 5, row 3, you must use `Sales!E3`. The name is separated from the column and row reference by an exclamation point. In the above screenshot, the formula `= DG2!A5 + 6` would add 6 to the value in row 5, column 1 in sheet DG2.

### FormLoad Method Implementation

Here is the implementation of the FormLoad method for the sample screenshot depicted above. Using the designer, a TabControl is dropped on a form and five TabPages are added. The pages are named `DG1`, `DG2`, ..., `DG5`. On each TabPage, a CalcDataGrid is set with the DockStyle set to `Fill`. This is all done through the designer.

#### Code Example

```csharp
Syncfusion.Calculate.CalcEngine engine;

private void DataGridWorkBookForm_Load(object sender, System.EventArgs e) {
    // Additional code for loading and interacting with CalcDataGrids
}
```

## Page-Level Navigation/TOC
- **Overview**
  - Using DataGrids with Calculation Support
  - FormLoad Method Implementation

## Cross References
- For more information on the CalcEngine and its features, refer to the CalcEngine documentation.

<!-- tags: [syncfusion, winforms, calcengine, icalldata, datagrid, workbook, calculation support] keywords: [DataGrid, CalcEngine, ICalcData, FormLoad, TabControl, TabPages, DockStyle, fill, formula, cell reference] -->
```