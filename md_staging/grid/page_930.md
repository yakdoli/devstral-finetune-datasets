```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_930.jpeg
document_name: grid
page_number: 930
page_id: grid#page_930
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to handle events in the `GridCurrentCellActivatingEventArgs` class.
- Focuses on refreshing the grid table control upon various events.

## Content

### Code Examples

#### C#
```csharp
GridCurrentCellActivatingEventArgs e)
{
    this.gridGroupingControl1.TableControl.Refresh();
}
```

#### VB.NET
```vb
Private Sub radioButton2_CheckedChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles radioButton2.CheckedChanged
    Me.gridGroupingControl1.TableControl.Refresh()
End Sub

Private Sub radioButton3_CheckedChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles radioButton3.CheckedChanged
    Me.gridGroupingControl1.TableControl.Refresh()
End Sub

Private Sub radioButton4_CheckedChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles radioButton4.CheckedChanged
    Me.gridGroupingControl1.TableControl.Refresh()
End Sub

Private Sub radioButton5_CheckedChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles radioButton5.CheckedChanged
    Me.gridGroupingControl1.TableControl.Refresh()
End Sub

Private Sub TableControl_CurrentCellActivating(ByVal sender As Object, ByVal e As GridCurrentCellActivatingEventArgs)
    Me.gridGroupingControl1.TableControl.Refresh()
End Sub
```

### Sample Output Description
Here is a sample output that focuses the current row and column.

## API Reference

### Members
- `GridCurrentCellActivatingEventArgs`: Represents event data specific to grid cell activation events.
- `gridGroupingControl1`: Represents the grid grouping control used in this example.
- `TableControl.Refresh()`: Method to refresh the grid table control.

---

### Tags and Keywords
<!-- tags: [syncfusion, windows forms, grid, event handling, gridcurrentcellactivatingeventargs, refreshtablecontrol] keywords: [grid, event args, refresh, current cell, table control] -->
``` 
