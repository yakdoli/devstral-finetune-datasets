```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_380.jpeg
document_name: grid
page_number: 380
page_id: grid#page_380
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to set up cross-references between grids for calculations.
- Register grids as separate sheets for cross-referencing using the GridFormulaEngine.
- Set values for the Display Grid to compute values for the Calculations Grid using cross-sheet references.

## Content

### Step 1-Registering Grids for Cross-Reference

```csharp
' Registering grid as separate sheets for cross-reference.
Dim sheetFamilyID As Integer = GridFormulaEngine.CreateSheetFamilyID()
GridFormulaEngine.RegisterGridAsSheet("Display", Me.gridDisplay.Model, sheetFamilyID)
GridFormulaEngine.RegisterGridAsSheet("Calculate", Me.gridCalculations.Model, sheetFamilyID)
```

### Step 2-Set Values for the Display Grid

#### [C#]

```csharp
this.gridDisplay[12, 1].Text = "Policy Premium Amount";
this.gridDisplay[12, 2].Text = "2,000";
this.gridDisplay[13, 1].Text = "Personal Loan Monthly Due";
this.gridDisplay[13, 2].Text = "1,500";
```

#### [VB.NET]

```vb.net
Me.gridDisplay(12, 1).Text = "Policy Premium Amount"
Me.gridDisplay(12, 2).Text = "2,000"
Me.gridDisplay(13, 1).Text = "Personal Loan Monthly Due"
Me.gridDisplay(13, 2).Text = "1,500"
```

### Step 3-Compute the Values for the Calculations Grid by Using the Values in the Display Grid

#### [C#]

```csharp
// Cross Sheet References.
this.gridCalculations[row, col].CellType = GridCellTypeName.FormulaCell;
this.gridCalculations[row, col].Text = "=Display!B12";
this.gridCalculations[row, col + 1].CellType = GridCellTypeName.FormulaCell;
this.gridCalculations[row, col + 1].Text = "=Display!B13";
```

#### [VB.NET]

```vb.net
' Cross Sheet References.
Me.gridCalculations(row, col).CellType = GridCellTypeName.FormulaCell
Me.gridCalculations(row, col).Text = "=Display!B12"
Me.gridCalculations(row, col + 1).CellType = GridCellTypeName.FormulaCell
Me.gridCalculations(row, col + 1).Text = "=Display!B13"
```

## Page-level Navigation/TOC (if applicable)
- This section details the process of setting up grids for calculations in Syncfusion WinForms.

## Cross References
See also: other sections detailing GridFormulaEngine and grid controls for more advanced functionalities.

<!-- tags: [syncfusion, winforms, grid, gridformulaengine, cross-reference] keywords: [Essential Grid, Display Grid, Calculations Grid, GridFormulaEngine, cross-sheet references, computation] -->
```