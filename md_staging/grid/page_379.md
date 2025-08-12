```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_379.jpeg
document_name: grid
page_number: 379
page_id: grid#page_379
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:30Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

![Form with Multiple Grids](#)
**Figure 134: Form with Multiple Grids**

## Example

### Overview
- Implements the feature with two sheets: 'Display' and 'Calculations'.
- The 'Display' sheet accepts parameters like Salary details, Insurance Policy details, Loan details, and computes the annual income of the employee.
- The 'Calculations' sheet computes tax deductions for an insurance policy and personal loan.

### Detailed Explanation

This process is explained in the following steps:

#### Step 1: Register the grid controls for cross-reference

The grid controls are registered as shown in the following code so that they can be referenced using a formula.

```csharp
// Registering grid controls as separate sheets for cross-reference.
int sheetFamilyID = GridFormulaEngine.CreateSheetFamilyID();
GridFormulaEngine.RegisterGridAsSheet("Display", this.gridDisplay.Model, sheetFamilyID);
GridFormulaEngine.RegisterGridAsSheet("Calculate", this.gridCalculations.Model, sheetFamilyID);
```

```vb.net

```

## API Reference

- **GridFormulaEngine.CreateSheetFamilyID()**: Creates an ID for organizing sheets in a family structure.
- **GridFormulaEngine.RegisterGridAsSheet(sheetName, model, familyID)**: Registers a grid control as a sheet within a specified family.

## Code Examples

- **C# Example**: Demonstrates registering grid controls for cross-reference.
- **VB.NET Example**: Placeholder for VB.NET equivalent code.

## Related Topics

- Referenced controls: `gridDisplay.Model`, `gridCalculations.Model`.
- For more information on grid functionalities, see the documentation on "Grid Controls."

<!-- tags: [grid, windows forms, grid formula engine, display calculate, tax deductions, loan details, salary details] keywords: [GridFormulaEngine, RegisterGridAsSheet, sheetFamilyID, grid models, salary, insurance, tax, loan] -->
```