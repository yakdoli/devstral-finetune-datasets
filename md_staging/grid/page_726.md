```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_726.jpeg
document_name: grid
page_number: 726
page_id: grid#page_726
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```html
el.ParentGroup.Name + ": " + el.ParentGroup.Category.ToString() + ")");
        }
    }
```

## Overview

This page discusses how to control the appearance of different group elements in the Grid control using the `Appearance` property. It provides code examples in C# and VB.NET to customize the style and appearance of group headers, footers, and preview cells.

## Content

### Handling Group Cell Styles

The following VB.NET code demonstrates how to handle `QueryCellStyleInfo` to customize the appearance of group footer and header section cells.

```vb.net
[VB.NET]

Private Sub gridGroupingControl1_QueryCellStyleInfo(ByVal sender As Object, ByVal e As GridTableCellStyleInfoEventArgs) Handles gridGroupingControl1.QueryCellStyleInfo

    If e.TableCellIdentity.TableCellType = GridTableCellType.GroupFooterSectionCell OrElse
       e.TableCellIdentity.TableCellType = GridTableCellType.GroupHeaderSectionCell Then
        e.Style.Enabled = False
        If e.TableCellIdentity.TableCellType = GridTableCellType.GroupFooterSectionCell Then
            e.Style.Text = "The details in the footer can be placed by enabling ShowGroupFooter and handling QueryCellStyleInfo"
        End If
        If e.TableCellIdentity.TableCellType = GridTableCellType.GroupHeaderSectionCell Then
            e.Style.Text = "The details in the header can be placed by enabling ShowGroupHeader and handling QueryCellStyleInfo"
        End If
    End If

    If e.TableCellIdentity.TableCellType = GridTableCellType.GroupPreviewCell Then
        Dim el As Element = e.TableCellIdentity.DisplayElement
        e.Style.CellValue = "Preview notes for Group (" & el.ParentGroup.Name & ": " & el.ParentGroup.Category.ToString() & ")"
    End If
End Sub
```

### Controlling Group Appearance Using `Appearance` Property

You can control the appearance of different group elements by using the `Appearance` property. Here is an example in C# to customize the appearance:

```csharp
[C#]

this.gridGroupingControl1.Appearance.AddNewRecordFieldCell.Interior = new BrushInfo(Color.FromArgb(255, 255, 192));
this.gridGroupingControl1.Appearance.GroupCaptionCell.Interior = new BrushInfo(SystemColors.Control);
this.gridGroupingControl1.Appearance.GroupCaptionCell.TextColor = Color.FromArgb(192, 64, 0);
this.gridGroupingControl1.Appearance.GroupFooterSectionCell.Interior =
```

## Summary

This section explains how to customize the style and appearance of group elements in the Grid control by handling `QueryCellStyleInfo` and using the `Appearance` property. The provided code examples show how to modify the visual representation of group headers, footers, and preview cells.

<!-- tags: [Syncfusion, WinForms, Grid, Group, Appearance, QueryCellStyleInfo] keywords: [grid grouping control, group header, group footer, preview cell, appearance property, custom styling, group elements, VB.NET, C#] -->
```