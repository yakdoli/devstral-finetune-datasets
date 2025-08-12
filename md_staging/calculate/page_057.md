```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: calculate
page_number: 057
page_id: calculate#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:07Z
fidelity: lossless
-->
# Essential Calculate

```vb
Dim e1 As New ValueChangedEventArgs(row, col, value.ToString())
RaiseEvent ValueChanged(Me, e1)

' SetValueRowCol
End Sub
```

## Overview
- Adding an indexer definition to the class for monitoring user changes.
- Forcing users to go through GetValueRowCol and SetValueRowCol methods for array-like access.
- Code examples for C# and VB.NET implementing the indexer using ICalcData interface.

## Content

### Adding an Indexer Definition

10. You have to add an indexer definition to the class for two reasons: it is a straightforward way to force the user to go through the GetValueRowCol and SetValueRowCol methods, allowing the CalcEngine to monitor these changes. It also makes your ArrayCalcData class look like an array.

Here is the code you must use. It is just a Get and Set implementation that goes through the ICalcData interface methods.

### C# Code Example

```csharp
/// <summary>
/// Gets / sets the value of this ArrayCalcData object.
/// </summary>
/// <remarks>
/// Since this class wraps a double array, the indexing is zero-based but,
/// the ICalcData methods requires one-based indexing by convention. So,
/// one is added to the indexes when the ICalcData methods are called.
/// </remarks>
public object this[int row, int col]
{
    get { return GetValueRowCol(row + 1, col + 1); }
    set { SetValueRowCol(value, row + 1, col + 1); }
}
```

### VB.NET Code Example

```vb
' <summary>
' Gets / sets the value of this ArrayCalcData object.
' </summary>
' <remarks>
' Since this class wraps a double array, the indexing is zero-based but,
' the ICalcData methods requires one-based indexing by convention. So,
' one is added to the indexes when the ICalcData methods are called.
' </remarks>
Default Public Property Item(ByVal row As Integer, ByVal col As Integer) As Object
    Get
        Return GetValueRowCol(row + 1, col + 1)
    End Get
    Set(ByVal Value As Object)
```

## Code Examples

The indexer implementation in both C# and VB.NET demonstrates how to bridge the one-based indexing convention of the ICalcData interface with the zero-based array indexing typically used in .NET. This ensures proper integration with the CalcEngine and other related components.

### References
- VB.NET indexer implementation.
- C# indexer implementation using the ICalcData interface.

<!-- tags: [syncfusion-sdk, winforms, arraycalcdata, indexer, calcengine] keywords: [indexer, getvaluecolrow, setvaluecolrow, icalcdata, one-based indexing, zero-based array, adapter, binding, calcengine] -->
```