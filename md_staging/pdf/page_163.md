```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_163.jpeg
document_name: pdf
page_number: 163
page_id: pdf#page_163
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:02Z
fidelity: lossless
-->

### PDFGrid: Cell Customization and Nesting

#### Overview
- Demonstrates how to set and customize cell values in a `PdfGrid`.
- Includes samples for setting nested tables within cells.
- Explains the use of properties to style cell content and appearance.

### Content

```csharp
{
    row.Cells[j].Value = String.Format("Cell [{0} {1}]", j, i);
}
}

// Set the value as another PdfGrid in a cell.
parentGrid.Rows[0].Cells[1].Value = childPdfGrid;
```

#### [VB.NET]
```vb
' Set the value to the specific cell.
parentPdfGrid.Rows(0).Cells(0).Value = "Nested Table"
parentPdfGrid.Rows(0).Cells(1).RowSpan = 2
parentPdfGrid.Rows(0).Cells(1).ColumnSpan = 2

Dim childPdfGrid As New PdfGrid()
childPdfGrid.Columns.Add(5)
For i As Integer = 0 To 4
    Dim row As PdfGridRow = childPdfGrid.Rows.Add()
    For j As Integer = 0 To 4
        row.Cells(j).Value = String.Format("Cell [{0} {1}]", j, i)
    Next j
Next i

' Set the value as another PdfGrid in a cell.
parentGrid.Rows(0).Cells(1).Value = childPdfGrid
```

### Style
PdfGrid provides various options to customize the cell content, text color, background color, and more. The following properties can be used for this purpose.

#### Properties

| Name                 | Description                                      | Data Type     |
|----------------------|--------------------------------------------------|---------------|
| BackgroundBrush      | Gets or sets background brush for the cell.     | PdfBrush      |
| BackgroundImage      | Gets or sets background image for the cell.     | PdfImage      |
| Borders              | Gets or sets the borders                          | PdfBorders    |

### References
- See the Syncfusion Winforms documentation for more examples and detailed information.

<!-- tags: [PdfGrid, cell styling, nesting tables, properties, customization] keywords: [PdfGrid, cell, background, borders, styles, nested tables, VB.NET] -->
```