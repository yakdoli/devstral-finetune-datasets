```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_382.jpeg
document_name: grid
page_number: 382
page_id: grid#page_382
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:55Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Introduction

The Essential Grid for Windows Forms is a powerful tool that provides advanced functionalities for managing grids in Windows-based applications. This page focuses on the creation and usage of named ranges within Grid controls.

### Figure 136: Named Ranges in Grid Control

The figure illustrates the concept of named ranges within a Grid control. It shows an example of how named ranges can be used to reference specific cells or ranges of cells for easier formula management and calculations.

## Example

The following example demonstrates the creation and usage of named ranges in Grid controls.

You can call the `AddNamedRange` method by using an instance of Grid Formula Engine and pass two parameters—`Name` and `Value`—to be set for the range.

### Code Example

#### C#

```csharp
GridFormulaEngine engine;
this.engine = ((GridFormulaCellModel)gridCashFlow.Model.CellModels["FormulaCell"]).Engine;
this.engine.AddNamedRange("Car", "300");
```

#### VB.NET

```vb
Dim engine As GridFormulaEngine
Me.engine = (CType(grid_cashFlow.Model.CellModels("FormulaCell"), GridFormulaCellModel)).Engine
Me.engine.AddNamedRange("Car", "300")
```

### Explanation

- **GridFormulaEngine**: This class is responsible for managing formulas in the Grid control. It provides various methods to handle named ranges and expressions.
- **AddNamedRange**: This method is used to add a named range to the Grid formula engine. It takes two parameters:
  - `Name`: The name of the range, which can be used in formulas.
  - `Value`: The value associated with the named range.

This example demonstrates how to create a named range called "Car" with a value of "300" in the Grid control.

---

## API Reference

### Methods

#### `AddNamedRange`

- **Description**: Adds a named range to the Grid formula engine.
- **Parameters**:
  - `Name`: A `string` representing the name of the range.
  - `Value`: A `string` representing the value associated with the range.
- **Returns**: None.
- **Exceptions**:
  - `ArgumentNullException`: If the `Name` or `Value` parameter is null.

## Code Examples

The examples above showcase how to create and use named ranges in a Grid control. These examples are provided in both C# and VB.NET, demonstrating the flexibility and interoperability of the Syncfusion Grid control.

---

## See also

- **Grid Formula Engine Documentation**: For more detailed information on managing formulas and named ranges.
- **Grid Control Overview**: An overview of the features and functionalities provided by the Essential Grid for Windows Forms.

<!-- tags: [grid, windows forms, named ranges, grid control, syncfusion] keywords: [named range, addnamedrange, grid formula engine, c#, vb.net, windows forms] -->
```