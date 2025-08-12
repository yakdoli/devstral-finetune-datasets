```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_996.jpeg
document_name: grid
page_number: 996
page_id: grid#page_996
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:54:47Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Custom Categorizer Implementation (VB.NET)

```vb
' Defines custom categorizer.
Public Class CustomCategorizer
    Implements Syncfusion.Grouping.IGroupByColumnCategorizer

    ' Defines a group and returns a group category object (here returns 1 through 5).
    Public Shared Function GetCategory(ByVal i As Integer) As Integer
        Dim ret As Integer = 0
        If i < 10 Then
            ret = 1
        ElseIf i >= 10 AndAlso i < 20 Then
            ret = 2
        ElseIf i >= 20 AndAlso i < 30 Then
            ret = 3
        ElseIf i >= 30 AndAlso i < 40 Then
            ret = 4
        Else
            ret = 5
        End If
        Return ret
    End Function

    Public Function GetGroupByCategoryKey(ByVal column As SortColumnDescriptor, ByVal isForeignKey As Boolean, ByVal record As Record) As Object Implements IGroupByColumnCategorizer.GetGroupByCategoryKey
        Return GetCategory(Integer.Parse(record.GetValue(column).ToString()))
    End Function

    Public Function CompareCategoryKey(ByVal column As SortColumnDescriptor, ByVal isForeignKey As Boolean, ByVal category As Object, ByVal record As Record) As Integer Implements IGroupByColumnCategorizer.CompareCategoryKey
        Return GetCategory(Integer.Parse(record.GetValue(column).ToString())) - Fix(category)
    End Function
End Class
```

### Defining a Custom Comparer

3. Define a custom `Comparer` to ensure that the integer values are sorted as integers instead of strings.

### Code Example in C#

```csharp
// [C# Code to be provided here]
```

## Page-level Navigation/TOC

- **Custom Categorizer Implementation (VB.NET)**: Explains how to define and implement a custom categorizer for categorizing data into groups.
- **Defining a Custom Comparer**: Describes the process of defining a custom `Comparer` to sort integer values correctly.

## API Reference

- **Namespace**: Syncfusion.Grouping
- **Class**: IGroupByColumnCategorizer
- **Methods**:
  - `GetCategory(i As Integer) As Integer`: Defines and returns a group category object.
  - `GetGroupByCategoryKey(column As SortColumnDescriptor, isForeignKey As Boolean, record As Record) As Object`: Implements the logic to determine the group category key for a record.
  - `CompareCategoryKey(column As SortColumnDescriptor, isForeignKey As Boolean, category As Object, record As Record) As Integer`: Implements the logic to compare category keys for sorting purposes.

## Code Examples

### VB.NET Example

```vb
' Implementation of the Custom Categorizer in VB.NET
Public Class CustomCategorizer
    Implements Syncfusion.Grouping.IGroupByColumnCategorizer

    Public Shared Function GetCategory(ByVal i As Integer) As Integer
        Dim ret As Integer = 0
        ' ... [rest of the implementation]
    End Function

    ' ... [other methods]
End Class
```

### C# Example

```csharp
// Implementation of the Custom Categorizer in C#
public class CustomCategorizer : IGroupByColumnCategorizer
{
    public object GetGroupByCategoryKey(SortColumnDescriptor column, bool isForeignKey, Record record)
    {
        // ... [implementation]
    }

    public int CompareCategoryKey(SortColumnDescriptor column, bool isForeignKey, object category, Record record)
    {
        // ... [implementation]
    }
}
```

## Cross References

- **See also**: `IGroupByColumnCategorizer`, `Syncfusion.Grouping`, `Record`, `SortColumnDescriptor`.

<!-- tags: [grid, categorizer, comparer, sorting, groupbycolumncategorizer, winforms, syncfusion, version 11.4.0.26] keywords: [custom categorizer, integer sorting, group categories, VB.NET, C#, compare category key, syncfusion grid] -->
```