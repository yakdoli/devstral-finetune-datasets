```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: calculate
page_number: 056
page_id: calculate#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:33Z
fidelity: lossless
-->

# Essential Calculate

## Content

Below is the `SetValueRowCol` method in C# and VB.NET along with its documentation.

### C# Method

```csharp
/// </remarks>
public void SetValueRowCol(object value, int row, int col)
{
    if (row - 1 == rowCount)
    {
        colSums[col - 1] = value;
    }
    else if (col - 1 == colCount)
    {
        rowSums[row - 1] = value;
    }
    else
        this.dValues[row - 1, col - 1] = double.Parse(value.ToString());

    ValueChangedEventArgs el = new ValueChangedEventArgs(row, col, value.ToString());
    ValueChanged(this, el);
}
```

### VB.NET Method

```vb
''' <summary>
''' Sets the value into either the double array or column vector or row vector.
''' </summary>
''' <param name="row">One-based row index.</param>
''' <param name="col">One-based column index.</param>
''' <param name="value">The value to be set.</param>
''' <remarks> This setter raises the ICalcData.ValueChanged event which,
''' is listened to by the CalcEngine to manage the calculations.
''' By convention, ICalcData uses one-based indexes.
''' </remarks>
Public Sub SetValueRowCol(ByVal value As Object, ByVal row As Integer, ByVal col As Integer) Implements Syncfusion.Calculate.ICalcData.SetValueRowCol

    If row = rowCount Then
        colSums(col - 1) = value
    Else
        If col = colCount Then
            rowSums(row - 1) = value
        Else
            Me.dValues(row - 1, col - 1) = Double.Parse(value.ToString())
        End If
    End If
End Sub
```

## Page-level Navigation/TOC (if applicable)

- **C# Method**: Explanation and implementation of the `SetValueRowCol` method.
- **VB.NET Method**: Equivalent implementation of the `SetValueRowCol` method in VB.NET.

## Cross References

See also: 
- [ICalcData Interface](#)
- [CalcEngine Class](#)

<!-- tags: [Syncfusion Winforms, Calculate, ICalcData, ICalcData.SetValueRowCol, CalcEngine, RowColVector, ValueChangedEventArgs] keywords: [SetValueRowCol, row, col, value, one-based index, rowSums, colSums, ValueChangedEventArgs, C#, VB.NET] -->
```