```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_928.jpeg
document_name: grid
page_number: 928
page_id: grid#page_928
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:05Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Configures selection mode for the `ListBoxSelectionMode` in WinForms.
- Demonstrates how to set `SelectionMode.One` or `SelectionMode.None` for a `Table` control.
- Includes clearing selected records when transitioning between options.

### Selection Mode Configuration

The following snippets demonstrate how to configure the `ListBoxSelectionMode` for a grid control and how to handle clearing selections based on the chosen selection mode.

#### C# Code Example

```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.One;
else
this.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.None;
    foreach (Table t in
this.gridGroupingControl1.Engine.EnumerateTables())
this.gridGroupingControl1.GetTable(t.TableDescriptor.Name).SelectedRecords.Clear();
}
```

#### VB.NET Code Example

```vb
' Code for Default option.
 Private Sub radioButton1_CheckedChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles radioButton1.CheckedChanged
    If Me.radioButton1.Checked Then
        Me.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.One
    Else
        Me.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.None
    End If
    Dim t As Table
    For Each t In Me.gridGroupingControl1.Engine.EnumerateTables()
        Me.gridGroupingControl1.GetTable(t.TableDescriptor.Name).SelectedRecords.Clear()
    Next t
End Sub
```

### Disable Selection

Below is the code for None option that disables the selection.

#### C# Code Example

```csharp
// Code for None option.
private void radioButton6_CheckedChanged(object sender, System.EventArgs e)
{
    if (this.radioButton6.Checked)
        this.gridGroupingControl1.TableModel.Options.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.HideAlways;
    else
        this.gridGroupingControl1.TableModel.Options.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.GrayWhenLostFocus;
}
```

### Relevant Resources
- Syncfusion Documentation: [WinForms Grid Overview](https://help.syncfusion.com/windowsforms/grid)
- API Reference: `GridGroupingControl`, `TableOptions`, `ListBoxSelectionMode`, `SelectedRecords`

### Usage Scenarios
- Enable single or no selection for list boxes within a grid control dynamically.
- Handle selection changes based on user input or application logic.

## Summary
The provided code examples illustrate how to configure the `ListBoxSelectionMode` in a WinForms Grid control and manage selection behaviors based on user input. This is particularly useful for creating responsive and interactive grid applications with synchronized selection options.

<!-- tags: [winforms, grid, selectionmode, tableoptions, listboxselection, none] keywords: [syncfusion, gridgroupingcontrol, selectionmode, listbox, clearselection, userinput, dynamicselection] -->
```