```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_663.jpeg
document_name: grid
page_number: 663
page_id: grid#page_663
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:14Z
fidelity: lossless
-->

## WinForms Grouping and Filtering with GridGroupingControl

### Overview

- The code demonstrates how to handle grouping and filtering options for a `GridGroupingControl` in a Windows Forms application.
- Two checkboxes, `checkBoxGrouping` and `checkBoxFilter`, are used to toggle grouping and filtering features.
- The `GridGroupingControl` is refreshed after modifying the grouping or filtering settings.

### Content

#### Grouping Option
The following snippet implements the grouping functionality for the `GridGroupingControl` when the `checkBoxGrouping` is checked or unchecked.

```csharp
// Grouping Option.
private void checkBoxGrouping_CheckedChanged(object sender, System.EventArgs e)
{
    if (this.checkBoxGrouping.Checked)
    {
        gridGroupingControl1.TableDescriptor.GroupedColumns.Clear();
        gridGroupingControl1.TableDescriptor.GroupedColumns.Add("1");
        this.gridGroupingControl1.Table.ExpandAllGroups();
    }
    else
    {
        gridGroupingControl1.TableDescriptor.GroupedColumns.Clear();
    }
    this.gridGroupingControl1.Refresh();
}
```

#### Filtering Option
The following snippet implements the filtering functionality for the `GridGroupingControl` when the `checkBoxFilter` is checked or unchecked. It retrieves the filter expression from a `TextBox`.

```csharp
// Filter Option.
private void checkBoxFilter_CheckedChanged(object sender, System.EventArgs e)
{
    if (this.checkBoxFilter.Checked)
    {
        gridGroupingControl1.TableDescriptor.RecordFilters.Clear();

        // Gets the filter expression from a Text Box.
        gridGroupingControl1.TableDescriptor.RecordFilters.Add(this.textBoxFilter.Text);
    }
    else
    {
        gridGroupingControl1.TableDescriptor.RecordFilters.Clear();
    }
    this.gridGroupingControl1.Refresh();
}
```

### Code Examples

#### C# Implementation

```csharp
// Grouping Option.
private void checkBoxGrouping_CheckedChanged(object sender, System.EventArgs e)
{
    if (this.checkBoxGrouping.Checked)
    {
        gridGroupingControl1.TableDescriptor.GroupedColumns.Clear();
        gridGroupingControl1.TableDescriptor.GroupedColumns.Add("1");
        this.gridGroupingControl1.Table.ExpandAllGroups();
    }
    else
    {
        gridGroupingControl1.TableDescriptor.GroupedColumns.Clear();
    }
    this.gridGroupingControl1.Refresh();
}

// Filter Option.
private void checkBoxFilter_CheckedChanged(object sender, System.EventArgs e)
{
    if (this.checkBoxFilter.Checked)
    {
        gridGroupingControl1.TableDescriptor.RecordFilters.Clear();

        // Gets the filter expression from a Text Box.
        gridGroupingControl1.TableDescriptor.RecordFilters.Add(this.textBoxFilter.Text);
    }
    else
    {
        gridGroupingControl1.TableDescriptor.RecordFilters.Clear();
    }
    this.gridGroupingControl1.Refresh();
}
```

#### VB.NET Implementation

```vb
' Sorting Option.
Private Sub checkBoxSorting_CheckedChanged(ByVal sender As Object, 
                                          ByVal e As System.EventArgs) Handles checkBoxSorting.CheckedChanged
    If Me.checkBoxSorting.Checked Then
        ' Sorting logic implementation
    Else
        ' Clear sorting
    End If
    Me.gridGroupingControl1.Refresh()
End Sub
```

### Conclusion

This section provides an example of how to dynamically apply grouping and filtering to a `GridGroupingControl` in a Windows Forms application. The example includes both C# and VB.NET implementations for toggling grouping and filtering based on checkbox selections.

<!-- tags: [grid, groupingcontrol, windowsforms, syncfusion] keywords: [GridGroupingControl, grouping, filtering, checkbox, checkedchanged, refresh] -->
```