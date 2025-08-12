```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_589.jpeg
document_name: tools
page_number: 589
page_id: tools#page_589
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:36Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates handling the DropDown event of the ComboBoxAdv control.
- Explains how to select multiple items in the dropdown.
- Describes how to change the BackColor for a disabled `ComboBoxAdv` control.

## Content
### Handling DropDown Event of ComboBoxAdv
You can handle the DropDown event of the `ComboBoxAdv` control and set it as shown in the following code snippet.

#### C#
```csharp
private void comboBoxAdv1_DropDown(object sender, System.EventArgs e)
{
    this.comboBoxAdv1.ListBox.SelectedItem = this.comboBoxAdv1.TextBox.Text;
}
```

#### VB.NET
```vb.net
Private Sub comboBoxAdv1_DropDown(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.comboBoxAdv1.ListBox.SelectedItem = Me.comboBoxAdv1.TextBox.Text
End Sub
```

### Selecting Multiple Items in the Dropdown
#### 3.5.5.2.5.1 How to select multiple items in the dropdown
In order to perform multiple selection, we can use our `ComboBoxAdv` or `MultiColumnComboBox` controls, which internally contains a normal `ListBox` that allows you to select multiple items.

#### C#
```csharp
this.comboBoxAdv1.ListBox.SelectionMode = SelectionMode.MultiExtended;
this.multiColumnComboBox1.ListBox.SelectionMode = SelectionMode.MultiExtended;
```

#### VB.NET
```vb.net
Me.comboBoxAdv1.ListBox.SelectionMode = SelectionMode.MultiExtended
Me.multiColumnComboBox1.ListBox.SelectionMode = SelectionMode.MultiExtended
```

### Changing BackColor for a Disabled ComboBoxAdv Control
#### 3.5.5.2.5.3 How to change the BackColor for a disabled ComboBoxAdv control
Previously, once the `ComboBoxAdv` control was disabled, the `BackColor` property of the control could not be changed. This was due to the fact that, by default, all the properties of the control were disabled once the control was disabled.

Now, you can set the `BackColor` for the `ComboBoxAdv` control even in its disabled state by using the `UseBackColor` property.

## Footer
© 2013 Syncfusion. All rights reserved. 

<!-- tags: [Syncfusion Winforms, ComboBoxAdv, DropDown event, multiple selection, BackColor, UseBackColor] keywords: [ComboBoxAdv, DropDown, SelectionMode.MultiExtended, BackColor, UseBackColor] -->
```