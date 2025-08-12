```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_956.jpeg
document_name: grid
page_number: 956
page_id: grid#page_956
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:57Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
converter.CaptionBackColor = Color.Lavender
```

### Handling the QueryExportPreviewRowInfo Event

1. **Objective**: Customize the preview rows before export.
   
#### Implementation in C#

```csharp
converter.QueryExportPreviewRowInfo += new
GroupingGridExcelConverterControl.GroupingGridExportPreviewRowQueryInfo
EventHandler(converter_QueryExportPreviewRowInfo);

void converter_QueryExportPreviewRowInfo(object sender,
GroupingGridExportPreviewRowQueryInfoEventArgs e)
{
    if (e.Element.Kind == DisplayElementKind.GroupPreview)
    {
        Element el = e.Element;
        e.Style.CellValue = "Preview notes for Group (" +
            el.ParentGroup.Name + ": " + el.ParentGroup.Category.ToString() + ")";
        e.Style.BackColor = Color.MistyRose;
        e.Handled = true;
    }
    if (e.Element.Kind == DisplayElementKind.RecordPreview)
    {
        Element el = e.Element;
        e.Style.CellValue = "Preview notes for Record (" +
            el.ParentTableDescriptor.Fields[0].Name + ": " +
            el.ParentRecord.GetValue(el.ParentTableDescriptor.Fields[0].Name) + ")";
        e.Style.BackColor = Color.MistyRose;
        e.Handled = true;
    }
}
```

#### Implementation in VB.NET

```vbnet
AddHandler converter.QueryExportPreviewRowInfo, AddressOf
converter_QueryExportPreviewRowInfo

Private Sub converter_QueryExportPreviewRowInfo(ByVal sender As Object,
ByVal e As GroupingGridExportPreviewRowQueryInfoEventArgs)
    If e.Element.Kind = DisplayElementKind.GroupPreview Then
        Dim el As Element = e.Element
        e.Style.CellValue = "Preview notes for Group (" &
            el.ParentGroup.Name & ": " & el.ParentGroup.Category.ToString() &
            ")"
        e.Style.BackColor = Color.MistyRose
    End If
End Sub
```

## Summary

Customizing the export preview rows in the Essential Grid for Windows Forms can be achieved by handling the `QueryExportPreviewRowInfo` event. This allows developers to modify the appearance and content of the preview rows, enhancing the export functionality to suit specific needs.

## Cross References

- See also: [Grid Export Overview](#grid-export-overview)
- Refer to: [Customizing Export Formats](#customizing-export-formats)

<!-- tags: [essential-grid, windows-forms, export, preview, customization] keywords: [queryexportpreviewrowinfo, grid, export, preview rows, customization] -->
```