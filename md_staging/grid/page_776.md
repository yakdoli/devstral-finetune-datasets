```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_776.jpeg
document_name: grid
page_number: 776
page_id: grid#page_776
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:40Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to handle special characters in filter expressions within the `gridGroupingControl`.
- Discusses replacing special characters like `[`, `#`, `*`, and `?` with their escaped equivalents.
- Explains the process of adding records, applying filters, and retrieving filtered records.

## Content

### Handling Special Characters in Filter Expressions

#### Code Example: C#
```csharp
// Take caution while replacing the pattern and ensure that only the intended pattern is modified.
pattern = pattern.Replace("[", "[[]]");
pattern = pattern.Replace("#", "[#]");
pattern = pattern.Replace("*", "[*]");
pattern = pattern.Replace("?", "[?]");
return pattern;
}
```

#### Code Example: VB.NET
```vb
[Vb.NET]

Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    Dim rank As New ArrayList()
    Dim rankData As New RankData("aaa")
    rank.Add(rankData)
    rankData = New RankData("bbb#")
    rank.Add(rankData)
    gridGroupingControl1.DataSource = rank
    Dim filter As String = ""
    Dim rfd As RecordFilterDescriptor = Nothing
    Dim r As Record = Nothing

    For Each a As RankData In rank
        filter = "[WellName] like '" & ReplaceSpcChar(a.WellName) & "'"
        rfd = New RecordFilterDescriptor(filter)
        gridGroupingControl1.TableDescriptor.RecordFilters.Add(rfd)
        Dim cont As Integer =
        gridGroupingControl1.Table.FilteredRecords.Count
        r = New Record(gridGroupingControl1.Table)

        ' Exception will be thrown here if special characters are not enclosed in square brackets.
        r = gridGroupingControl1.Table.FilteredRecords(0)
        rankData = TryCast(r.GetData(), RankData)
        gridGroupingControl1.TableDescriptor.RecordFilters.Clear()
        Next a
    End Sub

Private Function ReplaceSpcChar(ByVal pattern As String) As String

    ' Take caution while replacing the pattern and ensure that only the intended pattern is modified.
    pattern = pattern.Replace("[", "[[]]")
    pattern = pattern.Replace("#", "[#]")
    pattern = pattern.Replace("*", "[*]")
    pattern = pattern.Replace("?", "[?]")
End Function
```

### Explanation
- The code demonstrates how to handle special characters in filter expressions to avoid exceptions.
- The `ReplaceSpcChar` function ensures that any special characters like `[`, `#`, `*`, and `?` in the filter pattern are escaped correctly.
- The `gridGroupingControl1` is populated with `rankData` objects, and filters are applied dynamically based on the `WellName` property.
- Filtered records are retrieved, and the special characters in the filter are handled using the `ReplaceSpcChar` function.

### Notes
- It is crucial to replace special characters in filter expressions to prevent unexpected behavior or exceptions.
- The example showcases both C# and VB.NET implementations for clarity.

## API Reference

- **Methods**
  - `ReplaceSpcChar(pattern As String) As String`
    - **Parameters**: 
      - `pattern`: The input string pattern to be processed.
    - **Returns**: A modified string with special characters escaped.
    - **Description**: Escapes special characters `[`, `#`, `*`, and `?` in the input pattern to ensure correct filtering behavior.

## Code Examples (Reiterated)

### C#
```csharp
// Escaping special characters in filter patterns
pattern = pattern.Replace("[", "[[]]");
pattern = pattern.Replace("#", "[#]");
pattern = pattern.Replace("*", "[*]");
pattern = pattern.Replace("?", "[?]");
```

### VB.NET
```vb
'The same escaping logic in VB.NET
pattern = pattern.Replace("[", "[[]]")
pattern = pattern.Replace("#", "[#]")
pattern = pattern.Replace("*", "[*]")
pattern = pattern.Replace("?", "[?]")
```

### See also:
- [Grid Grouping Control Documentation](https://help.syncfusion.com/windowsforms/gridgroupingcontrol)
- [Filtering Data in Grids](https://help.syncfusion.com/windowsforms/gridgroupingcontrol/filtering)

<!-- tags: [syncfusion, winforms, grid, filter, special characters, escape, gridGroupingControl] keywords: [Essential Grid, Windows Forms, filter, ReplaceSpcChar, special characters, escaping, gridGroupingControl] -->
```