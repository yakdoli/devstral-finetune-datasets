```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_248.jpeg
document_name: grid
page_number: 248
page_id: grid#page_248
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
}
```

[VB.NET]

```vb
' Implement your Method.
Public Function ComputeSumPosNums(args As String) As String
    Dim model As GridFormulaCellModel = 
        Me.gridControl1.CellModels("FormulaCell")

    If Not (model Is Nothing) Then
        Dim engine As GridFormulaEngine = model.Engine
        Dim sum As Double = 0.0
        Dim d As Double
        Dim s1 As String

        ' Loop through arguments and sum up the positive values.
        Dim r As String
        For Each r In args.Split(New Char() {","c})

            ' Cell Range.
            If r.IndexOf(":"c) > -1 Then
                Dim s As String
                For Each s In engine.GetCellsFromArgs(r)

                    ' s is a cell line a21 or c3...
                    Try
                        s1 = engine.GetValueFromArg(s)
                    Catch ex As Exception
                        Return ex.Message
                    End Try
                    If s1 <> "" Then

                        ' Add only if positive.
                        If Double.TryParse(s1, NumberStyles.Number, Nothing, d) And d > 0 Then
                            sum += d
                        End If
                    End If
                Next s
            Else
                Try
                    s1 = engine.GetValueFromArg(r)
                Catch ex As Exception
                    Return ex.Message
                End Try
            End If
        Next r
    End If
    Return sum.ToString()
End Function
```

## API Reference

### Namespace: GridFormulaEngine

#### Methods

- **ComputeSumPosNums(args As String) As String**
  - **Parameters:**
    - `args` As String: A comma-separated list of arguments.
  - **Returns:**
    - `String`: A string representation of the sum of positive numeric values.

### GridFormulaCellModel

#### Properties

- **gridControl1.CellModels("FormulaCell")**: Reference to the GridFormulaCellModel for the specified grid control.

#### Methods

- **GetCellsFromArgs(args As String) As IEnumerable(Of String)**: Retrieves a collection of cells from the specified arguments.
- **GetValueFromArg(arg As String) As String**: Retrieves the value of a specific argument.

### String

#### Methods

- **Split(separators As Char()) As String()**: Splits a string into substrings based on the specified separators.

### Double

#### Methods

- **TryParse(input As String, styles As NumberStyles, provider As IFormatProvider, result As Double) As Boolean**: Attempts to convert the string representation of a number to its corresponding Double value.

## Code Examples

### Example 1: Implementation of `ComputeSumPosNums`

```vb
Public Function ComputeSumPosNums(args As String) As String
    ' Implementation as described in the section above.
End Function
```

### Example 2: Usage of `ComputeSumPosNums`

```vb
Dim result As String = ComputeSumPosNums("A1, A2, A3")
' result will contain the sum of positive values from cells A1, A2, and A3.
```

## Cross References

See also:
- [GridFormulaEngine Documentation](https://<link>)
- [GridFormulaCellModel Documentation](https://<link>)

<!-- tags: [Windows Forms, Grid, FormulaCell, CustomMethods, Computation, PositiveNumbers, Version: 11.4.0.26] keywords: [GridFormulaEngine, GetCellsFromArgs, GetValueFromArg, ComputeSumPosNums, PositiveValues, Custom Method, WindowsForms, GridControl] -->
```