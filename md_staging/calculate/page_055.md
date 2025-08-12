```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_055.jpeg
document_name: calculate
page_number: 055
page_id: calculate#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:36Z
fidelity: lossless
-->

# Essential Calculate

```vbnet
'/<summary>
'// Gets the value into either the double array or column vector or row vector.
'//</summary>
'//<param name="row">One-based row index.</param>
'//<param name="col">One-based column index.</param>
'//<returns>The value.</returns>
'//<remarks> By convention, ICalcData uses one-based indexes.</remarks>
Public Function GetValueRowCol(ByVal row As Integer, ByVal col As Integer) _
    As Object Implements Syncfusion.Calculate.ICalcData.GetValueRowCol
    If row = rowCount Then
        Return colSums((col - 1))
    Else
        If col = colCount Then
            Return rowSums((row - 1))

        Else
            Return Me.dValues(row - 1, col - 1)
        End If
    End If
End Function
```

## Overview

- The `GetValueRowCol` method is used to retrieve the value at a specified row and column index.

## Content

1. **Retrieve Value Using `GetValueRowCol`**
   - The `GetValueRowCol` function retrieves the value at a specified row and column index from a data structure.
   - **Parameters:**
     - `row` (One-based row index)
     - `col` (One-based column index)
   - **Returns:**
     - The value at the specified index.
   - **Details:**
     - If the specified row is the last row, it returns the sum of the specified column.
     - If the specified column is the last column, it returns the sum of the specified row.
     - Otherwise, it returns the value from the double array `dValues` at the adjusted zero-based row and column indices.

2. **Set Value Using `SetValueRowCol`**
   - The `SetValueRowCol` method is used to set the value at a specified row and column index.
   - **Usage:**
     - It can trigger calculations when values are entered or modified.
     - The `CalcEngine` listens to the `ValueChanges` event raised by this method to manage calculations.
     - This event ensures that calculations are triggered whenever values are set or changed.

   Here is the code for the `SetValueRowCol` method:

   ```csharp
   /// <summary>
   /// Sets the value into either the double array or column vector or row vector.
   /// </summary>
   /// <param name="row">One-based row index.</param>
   /// <param name="col">One-based column index.</param>
   /// <param name="value">The value to be set.</param>
   /// <remarks>This setter raises the ICalcData.ValueChanged event which,
   /// is listened to by the CalcEngine to manage the calculations.
   ///</remarks>
   /// By convention, ICalcData uses one-based indexes.
   ```

## Code Examples

The `GetValueRowCol` method's implementation demonstrates how to access values based on one-based indices, handling edge cases like row and column sums. The `SetValueRowCol` method, while not fully shown, is described as the reverse process, setting a value and raising the `ValueChanges` event.

## Cross References

- **Related Methods:**
  - `SetValueRowCol`
  - `CalcEngine`
  - `ICalcData`
  - `ValueChanges` event

<!-- tags: [Syncfusion, Winforms, ICalcData, GetValueRowCol, SetValueRowCol, CalcEngine, ValueChanges event] keywords: [getValueRowCol, setValueRowCol, one-based indexing, row sums, column sums, value changes event, calcEngine, ICalcData] -->
```