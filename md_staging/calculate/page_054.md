```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_054.jpeg
document_name: calculate
page_number: 054
page_id: calculate#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:52Z
fidelity: lossless
-->

# Essential Calculate

```vb
Public Sub SetValueRowCol(ByVal value As Object, ByVal row As Integer, ByVal –
            col As Integer) Implements
Syncfusion.Calculate.ICalcData.SetValueRowCol
End Sub

Public Sub WireParentObject() Implements
Syncfusion.Calculate.ICalcData.WireParentObject
End Sub

Public Event ValueChanged(ByVal sender As Object, ByVal e As _
    Syncfusion.Calculate.ValueChangedEventArgs) Implements _
        Syncfusion.Calculate.ICalcData.ValueChanged
```

## Overview
- Implements methods for setting values in a table, wiring parent objects, and event handling for value changes.
- Focuses specifically on the `SetValueRowCol`, `WireParentObject`, and `ValueChanged` event handling required for Syncfusion's calculation API.

## Content

### Retrieving Values Based on Row and Column Indices

1. **Purpose of `GetValueRowCol`**:
   - The `GetValueRowCol` method should return the value for a given row and column index. The indexes are one-based by convention.

2. **Logic for Handling Different Scenarios**:
   - If the last column is requested, the value in the `colSums` array is returned.
   - If the last row is requested, the value in the `rowSums` array is returned.
   - Otherwise, the value in the double array is returned.

```csharp
/// <summary>
/// Gets the value into either the double array or column vector or row
/// vector.
/// </summary>
/// <param name="row">One-based row index.</param>
/// <param name="col">One-based column index.</param>
/// <returns>The value.</returns>
/// <remarks>By convention, ICalcData uses one-based indexes.</remarks>
public object GetValueRowCol(int row, int col)
{
    if (row - 1 == rowCount)
    {
        return colSums[col - 1];
    }
    else if (col - 1 == colCount)
    {
        return rowSums[row - 1];
    }
    else
    {
        return this.dValues[row - 1, col - 1];
    }
}
```

### Implementation Details
- **Parameters**:
  - `row`: One-based row index.
  - `col`: One-based column index.
- **Return Value**:
  - The method returns the appropriate value based on the row and column indices.
- **Edge Cases**:
  - If the requested row or column is out of bounds, the method appropriately handles the scenario by referencing the `rowSums` or `colSums` arrays.

## API Reference

### Methods
- **`SetValueRowCol`**:
  - Sets a value at a specific row and column in the data table.
  - Parameters:
    - `value`: The value to set.
    - `row`: One-based row index.
    - `col`: One-based column index.
  
- **`WireParentObject`**:
  - Connects the data object with its parent object, facilitating communication and synchronization.

- **`GetValueRowCol`**:
  - Gets the value at a specific row and column.
  - Parameters:
    - `row`: One-based row index.
    - `col`: One-based column index.

## Code Examples

### C#

```csharp
// Example of implementing GetValueRowCol
public object GetValueRowCol(int row, int col)
{
    if (row - 1 == rowCount)
    {
        return colSums[col - 1];
    }
    else if (col - 1 == colCount)
    {
        return rowSums[row - 1];
    }
    else
    {
        return this.dValues[row - 1, col - 1];
    }
}
```

### VB.NET

```vb
' Example of implementing GetValueRowCol
Public Function GetValueRowCol(ByVal row As Integer, ByVal col As Integer) As Object
    If row - 1 = rowCount Then
        Return colSums(col - 1)
    ElseIf col - 1 = colCount Then
        Return rowSums(row - 1)
    Else
        Return Me.dValues(row - 1, col - 1)
    End If
End Function
```

## Cross References
- Refer to the documentation on `Syncfusion.Calculate.ICalcData` for more details on the API and its usage.

<!-- tags: [syncfusion, calculate, irowcolumn, data manipulation, winforms, syncfusion windows forms] keywords: [rowsums, colsums, GetValueRowCol, one-based indexing, setValueRowCol, ICALCDATA] -->
```