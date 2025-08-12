```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_246.jpeg
document_name: grid
page_number: 246
page_id: grid#page_246
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Define a method with a specific signature for custom formula implementation.
- Implement the method to sum only positive numbers from specified cell ranges or lists.

## Content

### Defining the Method Signature

1. First, define a method that has this signature.

#### C#
```csharp
// Define a method whose name is the FormulaName.
public string MyLibraryFormulaName(string args)
```

#### VB.NET
```vbnet
' Define a method whose name is the FormulaName.
Public Function MyLibraryFormulaName(ByVal args As String) As String
```

- The name `MyLibraryFormulaName` must be a valid and unused name in the Function Library, consisting only of letters and digits.
- If you want to replace an existing formula with the same name, remove the existing formula using the `GridFormulaEngine.RemoveFunction` method before adding the new formula.

### Implementing the Method

2. Then, write an implementation for your method. Here's an example that sums only positive numbers in the specified ranges or lists.

#### C#
```csharp
// Implement your method.
public string ComputeSumPosNums(string args)
{
    GridFormulaCellModel model =
        this.gridControl1.CellModels["FormulaCell"] as GridFormulaCellModel;
    if (model != null)
    {
        GridFormulaEngine engine = model.Engine;
        double sum = 0d;
        double d;
        string s1;

        // Loop through arguments and sum up the positive values.
        foreach (string r in args.Split(new char[] { ',', ' ' }))
        {
            // Cell Range.
            if (r.IndexOf(':') > -1)
            {
                foreach (string s in engine.GetCellsFromArgs(r))
```

### Technical Notes
- The `ComputeSumPosNums` method processes the input `args` to sum only positive numbers. It uses the `FormulaEngine` helper methods `GetCellsFromArgs` and `GetValueFromArg` to extract and evaluate values from specified cell ranges or lists.
- The implementation iterates through the arguments, handling both cell ranges (e.g., A1:A5) and individual cell references (e.g., A1, A4, A10), ensuring only positive values are summed.

## API Reference

### Methods
- `GridFormulaEngine.RemoveFunction`
  - Removes a specified formula from the Function Library.
  - **Parameters**:
    - `formulaName`: The name of the formula to be removed.
  - **Returns**: `bool` - Indicates whether the removal was successful.

- `GridFormulaEngine.GetCellsFromArgs`
  - Extracts an array of cells from a specified range or list of cells.
  - **Parameters**:
    - `args`: A string representing the cell range or list.
  - **Returns**: `string[]` - An array of cell addresses.

- `GridFormulaEngine.GetValueFromArg`
  - Retrieves the value from a specified cell.
  - **Parameters**:
    - `cellAddress`: A string representing the cell address.
  - **Returns**: `double` - The value of the specified cell.

## Code Examples

#### Summing Positive Numbers Example (C#)
```csharp
public string ComputeSumPosNums(string args)
{
    GridFormulaCellModel model =
        this.gridControl1.CellModels["FormulaCell"] as GridFormulaCellModel;
    if (model != null)
    {
        GridFormulaEngine engine = model.Engine;
        double sum = 0d;
        double d;
        string s1;

        foreach (string r in args.Split(new char[] { ',', ' ' }))
        {
            if (r.IndexOf(':') > -1)
            {
                foreach (string s in engine.GetCellsFromArgs(r))
                {
                    // Handle each cell value here.
                }
            }
            else
            {
                // Handle individual cell reference.
            }
        }

        return sum.ToString();
    }
    return "0";
}
```

#### Summing Positive Numbers Example (VB.NET)
```vbnet
Public Function ComputeSumPosNums(ByVal args As String) As String
    Dim model As GridFormulaCellModel =
        TryCast(Me.gridControl1.CellModels("FormulaCell"), GridFormulaCellModel)
    If model IsNot Nothing Then
        Dim engine As GridFormulaEngine = model.Engine
        Dim sum As Double = 0
        Dim d As Double
        Dim s1 As String

        For Each r As String In args.Split(New Char() {",", " "c})
            If r.IndexOf(":") > -1 Then
                For Each s As String In engine.GetCellsFromArgs(r)
                    ' Handle each cell value here.
                Next
            Else
                ' Handle individual cell reference.
            End If
        Next

        Return sum.ToString()
    End If
    Return "0"
End Function
```

### Cross References
- See also: `GridFormulaCellModel`, `GridFormulaEngine`, `FormulaEngine`

<!-- tags: [syncfusion, winforms, grid, custom-formulas, function-library, version:11.4.0.26] keywords: [compute-sum-positive, gridformulaengine, cell-model, custom-function-implementation] -->
```