```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_622.jpeg
document_name: tools
page_number: 622
page_id: tools#page_622
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Handling MultiColumnComboBox Selection Change in C#

This section demonstrates how to handle the `SelectedIndexChanged` event for a `MultiColumnComboBox` control in a Windows Forms application. The code snippet below updates `textBox1` and `textBox2` based on the selected row and column values from the grid within the `MultiColumnComboBox`.

```csharp
[C#]

private void MultiColumnComboBox1_SelectedIndexChanged(object sender, System.EventArgs e)
{
    for (int i = 1; i <= this.MultiColumnComboBox1.ListBox.Grid.RowCount; i++)
    {
        for (int j = 1; j <= this.MultiColumnComboBox1.ListBox.Grid.ColCount; j++)
        {
            this.textBox2.Text = this.MultiColumnComboBox1
                .ListBox.Grid.Model[this.MultiColumnComboBox1.SelectedIndex + 1, j].CellValue.ToString();

            textBox1.Text = this.MultiColumnComboBox1.ListBox.Grid.Model[this.MultiColumnComboBox1.SelectedIndex + 1, j - 1].CellValue.ToString();
        }
    }
}
```

### Handling MultiColumnComboBox Selection Change in VB.NET

The equivalent implementation in VB.NET for the `SelectedIndexChanged` event is shown below. This code updates the `textBox1` and `textBox2` controls based on the selected row and column values from the grid within the `MultiColumnComboBox`.

```vb
[VB.NET]

Private Sub MultiColumnComboBox1_SelectedIndexChanged(ByVal sender As Object, ByVal e As System.EventArgs)
    Dim i As Integer = 1

    Do While i <= Me.MultiColumnComboBox1.ListBox.Grid.RowCount
        Dim j As Integer = 1

        Do While j <= Me.MultiColumnComboBox1.ListBox.Grid.ColCount
            Me.textBox2.Text =
                Me.MultiColumnComboBox1.ListBox.Grid.Model(Me.MultiColumnComboBox1.SelectedIndex + 1, j).CellValue.ToString()

            textBox1.Text = Me.MultiColumnComboBox1.ListBox.Grid.Model(Me.MultiColumnComboBox1.SelectedIndex + 1, j - 1).CellValue.ToString()
            j += 1
        Loop
        i += 1
    Loop
End Sub
```

These code snippets illustrate how to programmatically interact with the grid model of a `MultiColumnComboBox` control, updating other elements of the form based on user selections. The `SelectedIndexChanged` event is particularly useful for linking grids or lists where selected items need to be updated elsewhere in the user interface.

## Page-level Navigation/TOC (if applicable)
- Essential Tools for Windows Forms
- Handling MultiColumnComboBox Selection Change in C#
- Handling MultiColumnComboBox Selection Change in VB.NET

<!-- tags: [product, Windows Forms, MultiColumnComboBox, SelectedIndexChanged, toolbox, versionality] keywords: [selecteditem, gridmodel, selectedindex, textbox, combobox] -->
```