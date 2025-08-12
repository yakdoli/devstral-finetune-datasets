<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: PivotGrid
page_number: 030
page_id: PivotGrid#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:21Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- Demonstrates disabling sorting in the Grouping Bar.
- Explains cell selection in PivotGrid for Windows Forms and how it can be customized.
- Provides code examples in C# and VB.

## Content

The following code example illustrates how to disable sorting in the Grouping Bar.

### Disabling Sorting

#### C#
```csharp
[C#]
// Disabling Sorting.
pivotGridControl1.AllowSorting = false;
```

#### VB
```vb
[VB]
// Disabling Sorting.
pivotGridControl1.AllowSorting = False
```

### 4.7 Cell Selection

The PivotGrid for Windows Forms supports cell selection, similar to Microsoft Excel. On cell selection, an event called `PivotGridSelectionChanged` will be triggered, and the `PivotGridSelectionChangedEventArgs` will return an `IEnumerable` collection of column, row, and value of the corresponding selected cell.

#### Use Case Scenarios
Using the cell selection support, you can select cells that can be copied to clipboard or notepad. You can perform custom operations on cell selection and also bind any control based on the selected cell values.

#### Adding Cell Selection
The following code snippets show how to create a PivotGrid and specify cell selection.

```csharp
[C#]
// Instantiating PivotGridControl
PivotGridControl pivotGridControl1 = new PivotGridControl();
// Adding PivotRows
pivotGridControl1.PivotRows.Add(new PivotItem { FieldHeader = "Product" });
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "Date" });
// Adding PivotColumns
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = 
```

## Page-level Navigation/TOC (if applicable)

## RAG Annotations
<!-- tags: [PivotGrid, WindowsForms, Sorting, CellSelection] keywords: [Disable Sorting, Grouping Bar, PivotGridSelectionChanged, IEnumerable, Custom Operations, Cell Selection, Clipboard, Notepad, PivotGridControl, PivotRows, PivotColumns, FieldHeader] -->