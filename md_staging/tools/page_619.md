```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_619.jpeg
document_name: tools
page_number: 619
page_id: tools#page_619
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to configure a MultiColumnComboBox with hidden and resized columns.
- Explains handling the `DropDown` event to set hidden and resized columns.
- Details handling the `SelectedIndexChanged` event to display the entire row in the GridListControl.

## Content

### Configuring MultiColumnComboBox

```vb
Private Sub multiColumnComboBox1_DropDown(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Hide a column.
    Me.multiColumnComboBox1.ListBox.Grid.Model.Cols.Hidden(1) = True

    ' Resize columns.
    Me.multiColumnComboBox1.ListBox.Grid.Model.ColWidths(3) = Me.multiColumnComboBox1.Bounds.Width / 2
    Me.multiColumnComboBox1.ListBox.Grid.Model.ColWidths(4) = Me.multiColumnComboBox1.Bounds.Width / 2

    Me.afterDropDown = True
End Sub
```

#### Displaying the Entire Row

CAL#
```csharp
private void multiColumnComboBox1_SelectedIndexChanged(object sender, System.EventArgs e)
{
    if (this.afterDropDown == true)
    {
        for (int i = 1; i <= this.multiColumnComboBox1.ListBox.Grid.ColCount; i++)
        {
            if (i == 1)
            {
                // do nothing for the hidden columns
            }
            else
            {
                str += this.multiColumnComboBox1.ListBox.Grid[this.multiColumnComboBox1.SelectedIndex, i].Text + " ";
            }
        }

        Console.WriteLine(str);
        this.multiColumnComboBox1.Text = str;
    }
}
```

### Explanation

3. To display the contents of the entire row in the `GridListControl` within the `MultiColumnComboBox`, instead of just the `DisplayMember`, handle the `MultiColumnComboBox`'s `SelectedIndexChanged` event as shown above.

### Code Snippet Overview

The VB code snippet demonstrates setting a column to hidden and resizing two other columns in the `MultiColumnComboBox`. The C# snippet illustrates filling the `MultiColumnComboBox` with the entire row data when the `SelectedIndexChanged` event is triggered, ensuring the hidden column is skipped.

## API Reference

- **Namespaces**: Used namespaces include those for handling events and grid functionalities in the `MultiColumnComboBox`.

## Code Examples

### VB Example
```vb
Private Sub multiColumnComboBox1_DropDown(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Code for configuring MultiColumnComboBox.
End Sub
```

### C# Example
```csharp
private void multiColumnComboBox1_SelectedIndexChanged(object sender, System.EventArgs e)
{
    // Code for handling SelectedIndexChanged event.
}
```

<!-- tags: [syncfusion, windows forms, multicolumncombobox, gridlistcontrol, dropdown event, selectedindexchanged event, columns configuration] keywords: [column, hidden, resize, grid, event, display member, row data, selected index changed] -->
```