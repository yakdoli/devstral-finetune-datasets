```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: grouping
page_number: 034
page_id: grouping#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:38Z
fidelity: lossless
-->

### Essential Grouping

```csharp
{
    Console.WriteLine(obj);
}
Console.WriteLine("--");
else if (g.Groups != null && g.Groups.Count > 0)
{
    // Iterating through the groups.
    foreach (Group g1 in g.Groups)
    {
        // Recursive call
        ShowRecordsUnderGroup(g1);
    }
}
```

```
Public Sub ShowRecordsUnderGroup(ByVal g As Group)
    If Not (g.Records Is Nothing) And g.Records.Count > 0 Then
        Dim rec As Record
        
        ' Displaying the data for all the records in each group.
        For Each rec In g.Records
            Dim obj As MyObject = CType(rec.GetData(), MyObject)
            If Not (obj Is Nothing) Then
                Console.WriteLine(obj)
            End If
        Next rec
        Console.WriteLine("--")
    Else
        If Not (g.Groups Is Nothing) And g.Groups.Count > 0 Then
            Dim g1 As Group
            
            ' Iterating through the groups.
            For Each g1 In g.Groups
            
                ' Recursive call
                ShowRecordsUnderGroup(g1)
            Next g1
        End If
    End If
    ' ShowRecordsUnderGroup
End Sub
```

## API Reference

### Methods
- **ShowRecordsUnderGroup**  
  - **Parameters:**
    - `g` (`Group`): The group to display records for.
  - **Description:**
    - Recursively displays all records under a group and iterates through subgroups if present.

## Code Examples

### C#
```csharp
void ShowRecordsUnderGroup(Group g)
{
    if (g.Records != null && g.Records.Count > 0)
    {
        foreach (Record rec in g.Records)
        {
            MyObject obj = (MyObject)rec.GetData();
            if (obj != null)
            {
                Console.WriteLine(obj);
            }
        }
        Console.WriteLine("--");
    }
    else if (g.Groups != null && g.Groups.Count > 0)
    {
        foreach (Group g1 in g.Groups)
        {
            ShowRecordsUnderGroup(g1);
        }
    }
}
```

### VB.NET
```vb
Private Sub ShowRecordsUnderGroup(ByVal g As Group)
    If Not (g.Records Is Nothing) And g.Records.Count > 0 Then
        Dim rec As Record
        
        For Each rec In g.Records
            Dim obj As MyObject = CType(rec.GetData(), MyObject)
            If Not (obj Is Nothing) Then
                Console.WriteLine(obj)
            End If
        Next rec
        Console.WriteLine("--")
    Else
        If Not (g.Groups Is Nothing) And g.Groups.Count > 0 Then
            Dim g1 As Group
            
            For Each g1 In g.Groups
                ShowRecordsUnderGroup(g1)
            Next g1
        End If
    End If
End Sub
```

## Cross References
- [See also: Hierarchical Data Display]
- [See also: Grouping Techniques]

<!-- tags: [essential grouping, records, recursive, iteration, grouping techniques] keywords: [group, records, iteration, recursion, hierarchical data display, grouping methods] -->
```