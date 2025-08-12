```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_081.jpeg
document_name: calculate
page_number: 081
page_id: calculate#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:34Z
fidelity: lossless
-->

# Essential Calculate

```vb
Me.dataGrid1(2, 2) = "= A1 + A3"

' 1) Reset static members of CalcEngine.
Syncfusion.Calculate.CalcEngine.ResetSheetFamilyID()

' 2) Create a CalcEngine object and tie it to the DataGrid that
' implements ICalcData.
engine = New Syncfusion.Calculate.CalcEngine(Me.dataGrid1)

' 3) Set the CalcEngine to track dependencies required for auto
updating.
    engine.UseDependencies = True

' 4) Call RecalculateRange so any formulas in the data can be
' initially computed.
    engine.RecalculateRange(RangeInfo.Cells(1, 1, dt.Rows.Count, 
dt.Columns.Count), Me.dataGrid1)

' SingleDataGridForm_Load
End Sub
```

## Overview
- **Goal**: Explains the usage of the `CalcEngine` to compute formulas within a DataGrid and enable automatic updates based on cell dependencies.

### Key Points
- Initializes the `CalcEngine` for a single DataGrid.
- Configures the engine to track dependencies.
- Automatically recalculates formulas as cell values are updated.

## Content

### Explanation of the Code
The following is an explanation of the preceding code.

1. **ResetSheetFamilyID**  
   Clears any static members of the `CalcEngine` class and sets the engine state to operate with a single `ICalcData` object.

2. **Creates an instance of the CalcEngine object**  
   Instantiates the `CalcEngine` object and associates it with the `DataGrid` that implements `ICalcData`.

3. **Sets the engine object to track calculation dependencies**  
   Configures the engine to track dependencies so that cells can be automatically updated as other cell values change.

4. **RecalculateRange**  
   Processes the existing cell contents to calculate any formulas for the initial display.

#### Subsection: 4.1.2.2 Using Several CalcDataGrids in a Workbook

- **Feature**: Essential Calculate supports cross-references among several `ICalcData` objects.
- **Usage**: Allows the creation of a workbook with multiple `CalcDataGrids` using a Windows Forms `Tab` control.
- **Reference**: Based on the `Calculation\Samples\DataGridCalculator` sample that ships with the product.

## API Reference

### Methods
- **ResetSheetFamilyID**  
  Clears static members and initializes the `CalcEngine` for a single `ICalcData` object.

- **CalcEngine Constructor**  
  Creates an instance of the `CalcEngine` and associates it with a specific `DataGrid`.

- **UseDependencies Property**  
  Enables or disables dependency tracking for automatic cell updates.

- **RecalculateRange Method**  
  Evaluates formulas in a specified range for the initial display.

## Code Examples

### VB.NET Example
```vb
Me.dataGrid1(2, 2) = "= A1 + A3"

Syncfusion.Calculate.CalcEngine.ResetSheetFamilyID()

engine = New Syncfusion.Calculate.CalcEngine(Me.dataGrid1)
engine.UseDependencies = True

engine.RecalculateRange(RangeInfo.Cells(1, 1, dt.Rows.Count, dt.Columns.Count), Me.dataGrid1)
```

## See also
- `CalcEngine`
- `ICalcData`
- `RangeInfo`
- `DataGridCalculator` sample

<!-- tags: [Syncfusion Winforms, CalcEngine, ICalcData, DataGridCalculator] keywords: [calculation engine, dependencies, auto updating, formula evaluation, range recalculation] -->
```