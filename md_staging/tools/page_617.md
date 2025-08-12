```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_617.jpeg
document_name: tools
page_number: 617
page_id: tools#page_617
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:27Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Implements `MultiColumnComboBox` in VB.NET.
- Handles the `SelectedValueChange` event in Windows Forms.
- Demonstrates displaying and retrieving column values from a `MultiColumnComboBox`.

## Content

### SelectedValueChange Event

```vb
[VB.NET]
Private Sub multiColumnComboBox1_SelectedValueChanged(ByVal sender As Object, ByVal e As System.EventArgs)
    Dim c As ComboBoxBaseDataBound = CType(multiColumnComboBox1, ComboBoxBaseDataBound)
    If Not (c.SelectedIndex = -1) Then
        ' Sets the text of MultiColumnComboBox to the text in the first column of selected row.
        Dim drv As DataRowView = CType(c.Items(c.SelectedIndex), DataRowView)
        c.Text = drv.Row(1).ToString
    End If
End Sub
```

#### Figure: Second Column Value of the Selected Row Displayed in the ComboBox

The `MultiColumnComboBox` shows the second column value of the selected row in the dropdown.

### SelectedIndexChanged Event

This event is illustrated in the topic **[How to retrieve the columns other than Display and Value members in a MultiColumnComboBox?](#topic-ref)**.

#### Subsection: Frequently Asked Questions

This section provides solutions to task-based queries about the `MultiColumnComboBox` control.

##### Displaying Multiple Members in a MultiColumnComboBox

This section explains how to display multiple members in a `MultiColumnComboBox`. Follow the steps to achieve this.

## API Reference

This section includes reference information about the `MultiColumnComboBox` and its properties and methods relevant to the example.

## Code Examples

The code above demonstrates handling the `SelectedValueChanged` event to set text based on the selected column values in a `MultiColumnComboBox`.

## Cross References

See also: [How to retrieve the columns other than Display and Value members in a MultiColumnComboBox?](#topic-ref)

<!-- tags: [product, Syncfusion Winforms, MultiColumnComboBox, SelectedValueChange, Windows Forms] keywords: [Windows Forms, MultiColumnComboBox, SelectedValueChanged, VB.NET, ComboBoxBaseDataBound, DataRowView] -->
```