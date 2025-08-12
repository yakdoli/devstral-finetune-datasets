```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: calculate
page_number: 051
page_id: calculate#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:17Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Implements row and column sum formulas for a grid.
- Integrates the `ICalcData` interface with minimal method implementations.
- Demonstrates the use of named events for value changes in grid operations.

## Content

### Calculating Row and Column Sums

```vb
colSums = New Object(colCount + 1) {}

' Initializes the formulas for the row sums.
' eg. "=Sum(A5:D5)" to sum row 5
Dim row As Integer
For row = 0 To rowCount - 1
    rowSums(row) = String.Format("=Sum(A{1}:{0}{1})", _
                                 RangeInfo.GetAlphaLabel(colCount - 1), row + 1)
Next

' Initializes the formulas for the column sums.
' eg. "=Sum(B1:B5)" to sum column 2
Dim col As Integer
For col = 0 To colCount - 1
    colSums(col) = String.Format("=Sum({0}1:{0}{1})", _
                                 RangeInfo.GetAlphaLabel((col + 1)), rowCount - 1)
Next

' New
End Sub
```

### Implementing the ICalcData Interface

6. Now you can add the code stubs for implementing the `ICalcData` interface. For the implementation, you only need to add the code to the first two methods in the interface. `WireParentObject` will not be used in our code. `ValueChanged` is an event that you will raise in the `SetValueRowCol` implementation.

### Adding Method Stubs Using Visual Studio 2003

7. Using Visual Studio 2003 with C#, add a colon after the class name in the class declaration and type `ICalcData`. Pressing the tab key will add the method stubs. Given below is a picture showing this technique.

## API Reference

- **Interface Name**: ICalcData
- **Methods**:
  - `WireParentObject`: Not used in this implementation.
  - `ValueChanged`: Event to raise in the `SetValueRowCol` method.
- **Events**:
  - `ValueChanged`: Triggered when a value changes.

## Code Examples

### VB.NET Example

```vb
' Example code snippet demonstrating the use of ICalcData interface
```

### C# Example

```csharp
// Example code snippet demonstrating the use of ICalcData interface
```

## Page-level Navigation/TOC
- [Creating Row and Column Sum Formulas](#creating-row-and-column-sum-formulas)
- [Implementing ICalcData Interface](#implementing-icalcdata-interface)
- [Adding Method Stubs Using Visual Studio 2003](#adding-method-stubs-using-visual-studio-2003)

<!-- tags: [Syncfusion Winforms, ICalcData, Grid Calculations, Value Changed Event] keywords: [row sums, column sums, ICalcData interface, method stubs, Visual Studio 2003] -->
```
