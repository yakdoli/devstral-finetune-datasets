```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_600.jpeg
document_name: tools
page_number: 600
page_id: tools#page_600
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:22Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Prevent Dropdown from Closing

#### C#

```csharp
// Avoids the closing of dropdown.
private void comboBoxBasel_DropDownCloseOnClick(object sender, Syncfusion.Windows.Forms.Tools.MouseClickCancelEventArgs args)
{
    args.Cancel = true;
}
```

#### VB.NET

```vb
' Avoids the closing of dropdown.
Private Sub comboBoxBasel_DropDownCloseOnClick(ByVal sender As Object, ByVal args As Syncfusion.Windows.Forms.Tools.MouseClickCancelEventArgs)
    args.Cancel = True
End Sub
```

### Handle `SelectedIndexChanged` Event of the `CheckedListBox`

#### C#

```csharp
// Sets the corresponding selected text in the ComboBoxBase TextBox.
private void checkedListBox1_SelectedIndexChanged(object sender, System.EventArgs e)
{
    comboBoxBasel.TextBox.Text = "";
    foreach (object s in checkedListBox1.CheckedItems)
        comboBoxBasel.TextBox.Text += s.ToString();
}
```

#### VB.NET

```vb
' Sets the corresponding selected text in the ComboBoxBase TextBox.
Private Sub checkedListBox1_SelectedIndexChanged(ByVal sender As Object, ByVal e As System.EventArgs)
    comboBoxBasel.TextBox.Text = ""
    For Each s In checkedListBox1.CheckedItems
        comboBoxBasel.TextBox.Text += s.ToString()
    Next
End Sub
```

---
© 2013 Syncfusion. All rights reserved.
Page
```