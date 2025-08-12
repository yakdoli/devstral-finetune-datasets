```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_744.jpeg
document_name: grid
page_number: 744
page_id: grid#page_744
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Sorting on specified columns can also be controlled by handling the `TableControlQueryAllowSortColumn` event. The event accepts an instance of `GridQueryAllowSortColumnEventArgs` as a parameter that contains the details of the column being affected. Using this instance, you can check for a particular column and cancel the sorting behavior.

The following code example prevents sorting on the `CompanyName` field.

## C#

```csharp
this.gridGroupingControl.TableControlQueryAllowSortColumn += new GridQueryAllowSortColumnEventHandler(gridGroupingControl_TableControlQueryAllowSortColumn);

private void gridGroupingControl_TableControlQueryAllowSortColumn(object sender, GridQueryAllowSortColumnEventArgs e)
{
    if (e.Column.GetName() == "CompanyName")
    {
        e.AllowSort = false;
    }
}
```

## VB.NET

```vb
AddHandler gridGroupingControl1.TableControlQueryAllowSortColumn, AddressOf gridGroupingControl1_TableControlQueryAllowSortColumn

Private Sub gridGroupingControl1_TableControlQueryAllowSortColumn(ByVal sender As Object, ByVal e As GridQueryAllowSortColumnEventArgs)
    If e.Column.GetName() = "CompanyName" Then
        e.AllowSort = False
    End If
End Sub
```

**Note:** For more details, refer the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Sort\Sort Method Demo
```

## Summaries

### 4.3.4.3.3 Summaries
```html
<!-- tags: [syncfusion, winforms, grid, tablecontrolqueryallowsortcolumn, gridqueryallowsortcolumneventargs, essential studio, 11.4.0.26, control properties, column sorting, event handlers, c#, vb.net, APIs, code examples] keywords: [sorting, grid control, windows forms, column names, event control, event handling, c# code, vb.net code, method demo, summarization] -->
```