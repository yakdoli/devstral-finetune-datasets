```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_929.jpeg
document_name: grid
page_number: 929
page_id: grid#page_929
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:24Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
' Code for None option.
Private Sub RadioButton6_CheckedChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles RadioButton6.CheckedChanged
    If Me.RadioButton6.Checked Then
        Me.GridGroupingControl1.TableModel.Options.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.HideAlways
    Else
        Me.GridGroupingControl1.TableModel.Options.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.GrayWhenLostFocus
    End If
End Sub
```

## Overview

- Handle the behavior of table cell borders when options are selected or deselected.
- Refresh the table control when the selection type is changed to update the display accordingly.

## Content

### Handling Border Behavior

The VB.NET code snippet demonstrates how to adjust the current cell border behavior based on the state of a radio button (`RadioButton6`). The `CheckedChanged` event is used to toggle between two border behaviors:

- **HideAlways**: Hides the current cell border permanently.
- **GrayWhenLostFocus**: Displays the current cell border in gray when the cell loses focus.

### Refreshing the Table Control

#### Refreshing on Selection Change

When the selection type is changed, the table control needs to be refreshed to reflect the new selection. This can be achieved by handling the `CheckedChanged` event for the relevant radio buttons (`RadioButton2`, `RadioButton3`, `RadioButton4`, and `RadioButton5`). The `Refresh()` method of the `TableControl` property is called to update the display.

#### Using the `CurrentCellActivating` Event

Alternatively, you can handle the `TableControlCurrentCellActivating` event to refresh the table control when the current cell is activated. This ensures a consistent user experience by updating the display dynamically as the user interacts with the table.

```csharp
private void RadioButton2_CheckedChanged(object sender, System.EventArgs e)
{
    this.GridGroupingControl1.TableControl.Refresh();
}

private void RadioButton3_CheckedChanged(object sender, System.EventArgs e)
{
    this.GridGroupingControl1.TableControl.Refresh();
}

private void RadioButton4_CheckedChanged(object sender, System.EventArgs e)
{
    this.GridGroupingControl1.TableControl.Refresh();
}

private void RadioButton5_CheckedChanged(object sender, System.EventArgs e)
{
    this.GridGroupingControl1.TableControl.Refresh();
}

void TableControl_CurrentCellActivating(object sender, ...
```

<!-- tags: [syncfusion, winforms, grid, table, selection, currentcell, borderbehavior, refresh, event] keywords: [gridgroupingcontrol, tablemodel, showcurrentcellborderbehavior, radio button, checked changed, refresh, currentcellactivating] -->
```