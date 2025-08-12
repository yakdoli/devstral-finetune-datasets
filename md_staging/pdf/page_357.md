<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_357.jpeg
document_name: pdf
page_number: 357
page_id: pdf#page_357
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:58Z
fidelity: lossless
-->

# Essential PDF

## Content

You can span any number of columns with the help of the `BeginRowLayout` event handler and `ColumnSpan` property. `ColumnSpanMap` property of this event enables column spanning, which merges cells within a row. To specify the span, you should create an array of integers with size equal to the number of cells in a row, and assign it to the `ColumnSpanMap` property.

### Description of Map Values

The description of the map values are as follows:

- **0 or 1**: denotes an ordinary cell; 0 allows you to omit explicit specification of 1
- **Negatives**: denotes that the cell is covered by a merged cell; you should not specify these values
- **2 and more**: denotes how many cells should be merged

The following code example illustrates this.

### C# Example

```csharp
void table_BeginRowLayout(object sender, BeginRowLayoutEventArgs args)
{
    if (args.RowIndex == 1)
    {
        PdfLightTable table = (PdfLightTable)sender;
        int count = table.Columns.Count;

        int[] spanMap = new int[count];

        // Set just spanned cells. Other values are not important
        // Except negatives that are not allowed.
        spanMap[0] = 2;
        spanMap[2] = 3;

        args.ColumnSpanMap = spanMap;

        // Sets row height.
        args.MinimalHeight = 30f;
    }
}
```

### VB.NET Example

```vb.net
Private Sub table_BeginRowLayout(ByVal sender As Object, ByVal args As BeginRowLayoutEventArgs)
    If args.RowIndex = 1 Then
        Dim table As PdfLightTable = CType(sender, PdfLightTable)
        Dim count As Integer = table.Columns.Count
    End If
End Sub
```

## RAG Annotations

<!-- tags: [Syncfusion, Winforms,Essential PDF, BeginRowLayout, ColumnSpan, ColumnSpanMap] keywords: [column spanning, cells, row, event handler, map values, merging cells, array of integers, size, number of cells, specifying span, ordinary cell, covered cell, merged cell, negative values, row height, minimal height] -->