```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_955.jpeg
document_name: grid
page_number: 955
page_id: grid#page_955
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:24Z
fidelity: lossless
-->

## Content

### Handling Preview Rows in Grouping Grid

```vb
' Hook up this event to handle preview rows.
AddHandler gridGroupingControl1.QueryCellStyleInfo, AddressOf gridGroupingControl1_QueryCellStyleInfo

Private Sub gridGroupingControl1_QueryCellStyleInfo(sender As Object, e As GridTableCellStyleInfoEventArgs)
    If e.TableCellIdentity.TableCellType = GridTableCellType.RecordPreviewCell Then
        Dim el As Element = e.TableCellIdentity.DisplayElement
        e.Style.CellValue = "Preview notes for Record (" & el.ParentTableDescriptor.Fields(0).Name & ": " & el.ParentRecord.GetValue(el.ParentTableDescriptor.Fields(0).Name) & ")"
    End If
    If e.TableCellIdentity.TableCellType = GridTableCellType.GroupPreviewCell Then
        Dim el As Element = e.TableCellIdentity.DisplayElement
        e.Style.CellValue = "Preview notes for Group (" & el.ParentGroup.Name & ": " & el.ParentGroup.Category.ToString() & ")"
    End If
End Sub
```

### Setting Up Grouping Grid Excel Converter

Set up a Grouping Grid Excel Converter and choose the elements you want to export by setting the appropriate properties.

#### [C#]

```csharp
GroupingGridExcelConverterControl converter = new GroupingGridExcelConverterControl();
converter.ExportBorders = true;
converter.ExportGroupPlusMinus = true;
converter.ExportPreviewRows = true;
converter.ExportRecordPlusMinus = true;
converter.ExportStyle = true;
converter.HeaderBackColor = Color.Orange;
converter.CaptionBackColor = Color.Lavender;
```

#### [VB.NET]

```vb
Dim converter As GroupingGridExcelConverterControl = New GroupingGridExcelConverterControl()
converter.ExportBorders = True
converter.ExportGroupPlusMinus = True
converter.ExportPreviewRows = True
converter.ExportRecordPlusMinus = True
converter.ExportStyle = True
converter.HeaderBackColor = Color.Orange
```

<!-- tags: [product, GroupingGrid, ExcelConverter, PreviewRows, C#, VB.NET] keywords: [Grouping Grid, Excel Conversion, Preview Rows, Cell Styles, VB.NET, C#, Syncfusion Winforms] -->
```