```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_953.jpeg
document_name: grid
page_number: 953
page_id: grid#page_953
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Object, ByVal e As GridTableCellStyleInfoEventArgs)
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

## VB.NET

```vb
Dim parentTable As DataTable = GetParentTable()
Dim childTable As DataTable = GetChildTable()

' Add Summary row to parent table.
Dim gridSummaryColumnDescriptor As New GridSummaryColumnDescriptor()
gridSummaryColumnDescriptor.DisplayColumn = "GroupID"
gridSummaryColumnDescriptor.Format = " {Count} Records."
gridSummaryColumnDescriptor.Name = "SummaryColumn"
gridSummaryColumnDescriptor.SummaryType = SummaryType.Count
Me.gridGroupingControl1.TableDescriptor.SummaryRows.Add(New GridSummaryRowDescriptor("SummaryRow", New GridSummaryColumnDescriptor() {gridSummaryColumnDescriptor}))

' Manually specify relations in grouping engine.
Dim parentToChildRelationDescriptor As New GridRelationDescriptor()
parentToChildRelationDescriptor.ChildTableName = "MyChildTable" ' same as SourceListSetEntry.Name for childTable
parentToChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails
parentToChildRelationDescriptor.RelationKeys.Add("parentID", "ParentID")

' Add Summary Row to child table.
gridSummaryColumnDescriptor = New GridSummaryColumnDescriptor()
gridSummaryColumnDescriptor.DisplayColumn = "ChildGroupID"
gridSummaryColumnDescriptor.Format = " {Count} Records."
gridSummaryColumnDescriptor.Name = "SummaryColumn"
```

## Cross References
- See also: Essential Grid for Windows Forms, GridTableCellStyleInfoEventArgs, GridTableCellType, DisplayElement, TableDescriptor, Field, ParentRecord, SummaryRow, SummaryColumn, RelationDescriptor, RelationKind.

<!-- tags: [Syncfusion Winforms, Grid, TableCellStyle, PreviewCell, SummaryRow, RelationDescriptor] keywords: [GridTableCellStyleInfoEventArgs, GridTableCellType, DisplayElement, TableDescriptor, Field, ParentRecord, SummaryRow, SummaryColumn, RelationDescriptor, RelationKind] -->
```