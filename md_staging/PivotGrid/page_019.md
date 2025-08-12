```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: PivotGrid
page_number: 019
page_id: PivotGrid#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:43Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- Demonstrates how to implement a custom `IComparer` for sorting Pivot Grid data in descending order.
- Includes C# and VB.NET code examples for adding `PivotItem` with custom `FieldMappingName`, `TotalHeader`, and `Comparer`.
- Explains the functionality of the `ReverseOrderComparer` class.

## Content

### Implementing a Custom Comparer

#### C# Code Example

```csharp
#region IComparer Members

public int Compare(object x, object y)
{
    if (x == null && y == null)
        return 0;
    else if (y == null)
        return 1;
    else if (x == null)
        return -1;
    else
        return -x.ToString().CompareTo(y.ToString());
}

#endregion
}
```

#### VB.NET Code Example

```vb
' Adding Pivot Rows to Grid with FieldMappingName, TotalHeader and Comparer
Me.PivotGridControl1.PivotRows.Add(New PivotItem With
{
    .FieldMappingName = "Product", .TotalHeader = "Total", .Comparer = New ReverseOrderComparer()
})

''' <summary>
''' Reverse Order Comparer for sorting data in Descending order
''' </summary>
public class ReverseOrderComparer : IComparer
    ' #Region "IComparer Members"

    public Integer Compare(Object x, Object y)
        If x Is Nothing AndAlso y Is Nothing Then
            Return 0
        ElseIf y Is Nothing Then
```

## API Reference

### Classes

- **ReverseOrderComparer**
  - Implements `IComparer` for sorting in descending order.
  - **Parameters:**
    - `x`: The first object to be compared.
    - `y`: The second object to be compared.
  - **Returns:** An integer indicating the relative order of the two objects.

### Properties and Methods

- **`PivotItem.FieldMappingName`**
  - Type: `String`
  - Description: The field mapping name for the Pivot Grid.
- **`PivotItem.TotalHeader`**
  - Type: `String`
  - Description: The header name for the total row.
- **`PivotItem.Comparer`**
  - Type: `IComparer`
  - Description: The custom comparer used for sorting.

## Code Examples

### C# Example

```csharp
// Adding a PivotItem with custom settings
pivotGridControl1.PivotRows.Add(new PivotItem
{
    FieldMappingName = "Product",
    TotalHeader = "Total",
    Comparer = new ReverseOrderComparer()
});
```

### VB.NET Example

```vb
' Adding a PivotItem with custom settings
Me.PivotGridControl1.PivotRows.Add(New PivotItem With
{
    .FieldMappingName = "Product",
    .TotalHeader = "Total",
    .Comparer = New ReverseOrderComparer()
})
```

## Cross References
- See also: [Syncfusion PivotGrid Documentation](https://help.syncfusion.com/windowsforms/pivotgrid)

<!-- tags: [PivotGrid, WindowsForms, CustomComparer, SyncfusionWinforms, Sorting, IComparer, ReverseOrderComparer] keywords: [PivotItem, FieldMappingName, TotalHeader, CustomComparer, ReverseOrder, DescendingSort] -->
```