```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_134.jpeg
document_name: pdf
page_number: 134
page_id: pdf#page_134
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:47Z
fidelity: lossless
-->

## Essential PDF

### Event-Based Table Generation

This section details the process of creating a table using event handlers in the Essential PDF library. It demonstrates how to populate table data dynamically by handling events that query column count, row count, and row data.

#### Code Example: C#

```csharp
void pdfLightTable_QueryNextRow(object sender, QueryNextRowEventArgs args)
{
    if (args.RowIndex < datastring.Length)
        args.RowData = new string[] { datastring[args.RowIndex][0], datastring[args.RowIndex][1], datastring[args.RowIndex][2] };
}
```

#### Code Example: VB.NET

```vb
Public datastring(1)() As String

' Giving it some column arrays
Private datastring(0) = New String() { "111", "Maxim", "100" }
Private datastring(1) = New String() { "222", "Calvin", "95" }

' Creating PdfLightTable
Private pdfLightTable As New PdfLightTable()

pdfLightTable.QueryColumnCount += New QueryColumnCountEventHandler(AddressOf pdfLightTable_QueryColumnCount)
pdfLightTable.QueryNextRow += New QueryNextRowEventHandler(AddressOf pdfLightTable_QueryNextRow)
pdfLightTable.QueryRowCount += New QueryRowCountEventHandler(AddressOf pdfLightTable_QueryRowCount)

' Drawing the PdfLightTable
pdfLightTable.Draw(page, PointF.Empty)

' Getting the number of columns
Private Sub pdfLightTable_QueryColumnCount(ByVal sender As Object, ByVal args As QueryColumnCountEventArgs)
    args.ColumnCount = 3
End Sub

' Getting the number of rows
Private Sub pdfLightTable_QueryRowCount(ByVal sender As Object, ByVal args As QueryRowCountEventArgs)
    args.RowCount = 2
End Sub

' Getting row data
Private Sub pdfLightTable_QueryNextRow(ByVal sender As Object, ByVal args As QueryNextRowEventArgs)
    If args.RowIndex < datastring.Length Then
        args.RowData = New String() { datastring(args.RowIndex)(0), datastring(args.RowIndex)(1), datastring(args.RowIndex)(2) }
    End If
End Sub
```

### Summary
- Implements a table generation mechanism using event-based callbacks.
- Demonstrates handling events to define column count, row count, and row data dynamically.
- Provides examples in both C# and VB.NET, showing how to populate a table with predefined data arrays.

#### Cross References
- Refer to the **PdfLightTable** class documentation for more details on table rendering and event handling.
- For further examples, see the section on creating static tables without using event handlers.

<!-- tags: [Essential PDF, WinForms, PdfLightTable, event handlers, table generation] keywords: [column count, row count, row data, C#, VB.NET, dynamic table, data arrays] -->
```