```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_517.jpeg
document_name: grid
page_number: 517
page_id: grid#page_517
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:29Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Code Example
```vb
GridQueryCellInfoEventArgs)
    If e.RowIndex > 0 AndAlso e.ColIndex > 0 Then
        e.Style.CellValue = externalData(e.RowIndex - 1).Items(e.ColIndex - 1)
        If e.ColIndex = 1 Then
            e.Style.CellType = "TreeCell"
            e.Style.Tag = externalData(e.RowIndex - 1).IndentLevel
            e.Style.ImageIndex = CInt(Fix(externalData(e.RowIndex - 1).ExpandState))
        End If
    End If
    e.Handled = True
End Sub
```

### Implementation Details

The implementation uses a `CollapsibleDataSource` class. This class makes use of a custom collection to hold a list of `SampleData` objects (Consider each of these objects as a row in the underlying grid). Each row carries information on a specific folder. Each `SampleData` object has an `IndentValue` property, an `ExpandState` property, and an `Items` string array that holds the different column values for this row. The column values display the folder details like the name of the folder, folder size, and so on. This class also contains the `InsertData` method which retrieves the data of the inner subtree and inserts the data into the collection when a node is expanded.

<!-- tags: [essential grid, windows forms, collapsibledatasource, syncfusion winforms, gridquerycellinfoeventargs] keywords: [cellvalue, treecell, indentlevel, imageindex, expandstate, rowindex, colindex, handled] -->
```