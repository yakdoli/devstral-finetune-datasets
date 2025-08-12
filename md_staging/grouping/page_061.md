```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: grouping
page_number: 061
page_id: grouping#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:41Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Implements custom grouping calculations using custom functions.
- Demonstrates how to add and use custom functions in Expression columns.
- Provides examples in both C# and VB.NET.

### Custom Function Implementation

#### C# Example

```csharp
string[] ss = s.Split(comma);
if (ss.GetLength(0) != 2)
    throw new ArgumentException("Requires 2 arguments.");

double arg1, arg2;
if (double.TryParse(ss[0], System.Globalization.NumberStyles.Any, null, out arg1)
    && double.TryParse(ss[1], System.Globalization.NumberStyles.Any, null, out arg2))
{
    return Math.Abs(arg1 - 2 * arg2).ToString();
}
return "";
```

#### VB.NET Example

```vb
' Step 1
' Add function named Func that uses a delegate named ComputeFunc to define a custom calculation.
Dim evaluator As ExpressionFieldEvaluator =
    Me.groupingEngine.TableDescriptor.ExpressionFieldEvaluator
evaluator.AddFunction("Func", New
    ExpressionFieldEvaluator.LibraryFunction(ComputeFunc))

' Sample usage in an Expression column.
Me.groupingEngine.TableDescriptor.ExpressionFields.Add("test")
Me.groupingEngine.TableDescriptor.ExpressionFields("test").Expression = "Func([Col1], [Col2])"

' Step 2
' Define ComputeFunc that returns the absolute value of the 1st arg minus 2 * the 2nd arg.
Public Function ComputeFunc(ByVal s As String) As String

    ' Get the list delimiter (for en-us, it is a comma).
    Dim comma As Char =
        Convert.ToChar(Me.gridGroupingControl1.Culture.TextInfo.ListSeparator)
    Dim ss As String() = s.Split(comma)
    If ss.GetLength(0) <> 2 Then
        Throw New ArgumentException("Requires 2 arguments.")
    End If

    Dim arg1, arg2 As Double
    If Double.TryParse(ss(0), System.Globalization.NumberStyles.Any, Nothing, arg1) _
       AndAlso _
       Double.TryParse(ss(1), System.Globalization.NumberStyles.Any, Nothing, arg2) Then
        Return Math.Abs((arg1 - 2 * arg2)).ToString()
    End If
    Return ""
End Function
```

## Code Examples

### C# Implementation of Custom Function
The provided C# code defines a custom function that parses two arguments from a string, checks if they are valid doubles, and calculates the absolute difference between the first argument and twice the second argument.

### VB.NET Implementation of Custom Function
The VB.NET example demonstrates the addition of a custom function named `Func` to the `ExpressionFieldEvaluator`. It also includes the implementation of the `ComputeFunc` delegate, which performs a similar calculation as the C# example.

## See also
- [Expression Calculator](#expression-calculator)
- [TableDescriptor](#tabledescriptor)

<!-- tags: [Syncfusion, Winforms, Grouping, ExpressionCalculator, ExpressionFieldEvaluator] keywords: [custom functions, C#, VB.NET, grouping, expressions, calculations, delegates, tryParse, Math.Abs] -->
```