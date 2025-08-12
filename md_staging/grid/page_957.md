```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_957.jpeg
document_name: grid
page_number: 957
page_id: grid#page_957
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:19Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
e.Handled = True
End If
If e.Element.Kind = DisplayElementKind.RecordPreview Then
    Dim el As Element = e.Element
    e.Style.CellValue = "Preview notes for Record (" & _
                        el.ParentTableDescriptor.Fields(0).Name & ":" & _
                        el.ParentRecord.GetValue(el.ParentTableDescriptor.Fields(0).Name) & _
                       ")"
    e.Style.BackColor = Color.MistyRose
    e.Handled = True
End If
End Sub
```

6. Export the grouping grid to an Excel file.

### Code Example: C#

```csharp
converter.GroupingGridToExcel(this.gridGroupingControl1, 
                              "ExcelGrid.xls", 
                              ConverterOptions.Default);
```

### Code Example: VB.NET

```vb
converter.GroupingGridToExcel(Me.gridGroupingControl1, 
                              "ExcelGrid.xls", 
                              ConverterOptions.Default)
```

7. Here are screen shots showing grouping grid and the exported grid in Excel file.
```