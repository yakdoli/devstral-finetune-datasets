```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_873.jpeg
document_name: grid
page_number: 873
page_id: grid#page_873
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:26Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- 1. Explains how to apply dynamic merging in GridGrouping control using MergeCellsLayout.
- 2. Describes the functionality and use of BaseStyles in GridStyleInfo objects to enhance cell appearance.
- 3. Provides code examples in C# and VB to illustrate the implementation of dynamic cell merging within a grid.

## Content

### 4.3.4.5.1 Merging Cells Dynamically in a Grid
To apply dynamic merging in the GridGrouping control, the MergeCellsLayout needs to be applied along with the existing code to merge the cells in the grid.

#### Code Example in C#
```csharp
// Existing code to set merge cells.
this.gridGroupingControl1.TableDescriptor.Columns[colName].Appearance.AnyRecordFieldCell.MergeCell = GridMergeCellDirection.Both;
this.gridGroupingControl1.TableModel.Options.MergeCellsMode = GridMergeCellsMode.OnDemandCalculation ;

// To set the range of cells.
this.gridGroupingControl1.TableModel.Options.MergeCellsLayout = GridMergeCellsLayout.Grid;
```

#### Code Example in VB
```vb
' Existing code to set merge cells.
Me.gridGroupingControl1.TableDescriptor.Columns(colName).Appearance.AnyRecordFieldCell.MergeCell = GridMergeCellDirection.Both
Me.gridGroupingControl1.TableModel.Options.MergeCellsMode = GridMergeCellsMode.OnDemandCalculation

' To set the range of cells
Me.gridGroupingControl1.TableModel.Options.MergeCellsLayout = GridMergeCellsLayout.Grid
```

### 4.3.4.5.6 BaseStyles
In addition to the parent styles discussed in the previous topics, Essential Grid supports one other parent-type style which, can contribute to a cell's appearance, they are BaseStyles of GridStyleInfo objects which, can be associated with an arbitrary collection of cells.

BaseStyles provide the way to create StyleTemplates that can be applied to the cells. It allows you to apply styles with ease and in faster manner. For example, in a word processing software, there is the common task of defining a particular style (such as style Header1 representing a bold, 20-point Helvetica font) and then using it repeatedly in your document whenever you need a 'Header1' type.

## RAG Annotations
<!-- tags: [Essential Grid, Windows Forms, GridGrouping, BaseStyles, MergeCellsLayout, syncfusion-sdk, GridStyleInfo, cell styling] keywords: [dynamic merging, cell merging, grid grouping control, base styles, style templates, appearance, cell range, GridMergeCellDirection, OnDemandCalculation, GridMergeCellsLayout, GridStyleInfo] -->
```