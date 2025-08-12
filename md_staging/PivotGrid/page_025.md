```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: PivotGrid
page_number: 025
page_id: PivotGrid#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:51Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

```vb
#endregion
}
```

### Adding Pivot Rows to Grid with FieldMappingName, TotalHeader and Comparer

```vb
[VB]
' Adding Pivot Rows to Grid with FieldMappingName, TotalHeader and Comparer
Me.PivotGridControl1.PivotRows.Add(New PivotItem With
{.FieldMappingName = "Product", .TotalHeader = "Total", .Comparer = New ReverseOrderComparer()})
'''

''' <summary>
''' Reverse Order Comparer for sorting data in Descending order
''' </summary>
public class ReverseOrderComparer : IComparer
'    #Region "IComparer Members"

    public Integer Compare(Object x, Object y)
        If x Is Nothing AndAlso y Is Nothing Then
            Return 0
        ElseIf y Is Nothing Then
            Return 1
        ElseIf x Is Nothing Then
            Return -1
        Else
            Return -x.ToString().CompareTo(y.ToString())
        End If
'
'    #End Region
```

## API Reference
- **Class**: ReverseOrderComparer
  - Implements: IComparer
  - **Method**:
    - **Compare(Object x, Object y)**:
      - **Parameters**:
        - `x`: Object
        - `y`: Object
      - **Return**: Integer
      - **Description**: Compare method for sorting data in descending order.

## Code Examples

### VB.NET Example

```vb
' Adding Pivot Rows with Custom Comparer
Me.PivotGridControl1.PivotRows.Add(New PivotItem With
{.FieldMappingName = "Product", .TotalHeader = "Total", .Comparer = New ReverseOrderComparer()})
```

### ReverseOrderComparer Class

```vb
public class ReverseOrderComparer : IComparer
    ' Implementation of Compare method
    public Integer Compare(Object x, Object y)
        If x Is Nothing AndAlso y Is Nothing Then
            Return 0
        ElseIf y Is Nothing Then
            Return 1
        ElseIf x Is Nothing Then
            Return -1
        Else
            Return -x.ToString().CompareTo(y.ToString())
        End If
```

<!-- tags: PivotGrid, WindowsForms, Fields, Mapping, TotalHeader, Comparer keywords: PivotGrid, WindowsForms, ReverseOrderComparer, TotalHeader, FieldMappingName, IComparer, Compare -->
```