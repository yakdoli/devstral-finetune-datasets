```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_561.jpeg
document_name: tools
page_number: 561
page_id: tools#page_561
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:19:52Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Add controls to a Panel.
- Set the `PopupControl` property of the ComboDropDown to the same Panel.
- Handle the `SelectedIndexChanged` event of both ComboBoxes to keep the DropDown showing.

## Content

### Step-by-Step Instructions

1. **Add Controls to the Panel**
   
   Add these controls to the Panel.

2. **Set the `PopupControl` Property**
   
   Set the `PopupControl` property of the `ComboDropDown` to the same Panel.

3. **Handle `SelectedIndexChanged` Event**
   
   To avoid closing the `ComboDropDown` after selecting an item in the `ComboBox`, handle the `SelectedIndexChanged` event of both `ComboBoxes` and keep the DropDown showing.

   **C#**
   ```csharp
   // Indicates whether the combo box is displaying its drop-down portion.
   private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
   {
       comboDropDown1.DroppedDown = true;
   }

   private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
   {
       comboDropDown1.DroppedDown = true;
   }
   ```

   **VB.NET**
   ```vb
   ' Indicates whether the combo box is displaying its drop-down portion.
   Private Sub comboBox1_SelectedIndexChanged(ByVal sender As Object, ByVal e As EventArgs)
       comboDropDown1.DroppedDown = True
   End Sub

   Private Sub comboBox2_SelectedIndexChanged(ByVal sender As Object, ByVal e As EventArgs)
       comboDropDown1.DroppedDown = True
   End Sub
   ```

4. **Close DropDown and Change Text**
   
   In the button click event of the Button inside the panel, insert these codes to close the DropDown and change the text of `ComboDropDown`.

   **C#**
   ```csharp
   // Closes the dropdown and changes the text.
   private void button1_Click(object sender, EventArgs e)
   {
       comboDropDown.Text = comboBox1.Text + " " + comboBox2.Text;
       comboDropDown1.DroppedDown = false;
   }
   ```

   **VB.NET**
   ```vb
   ' Closes the dropdown and changes the text.
   Private Sub button1_Click(ByVal sender As Object, ByVal e As EventArgs)
       comboDropDown.Text = comboBox1.Text + " " + comboBox2.Text
       comboDropDown1.DroppedDown = False
   End Sub
   ```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: ComboDropDown
- **Event**: `SelectedIndexChanged`
- **Property**: `DroppedDown`
- **Methods**:
  - `CloseDropDown()`
  - `SetSelectedText()`

## Code Examples

### C#
```csharp
private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
{
    comboDropDown1.DroppedDown = true;
}

private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
{
    comboDropDown1.DroppedDown = true;
}

private void button1_Click(object sender, EventArgs e)
{
    comboDropDown.Text = comboBox1.Text + " " + comboBox2.Text;
    comboDropDown1.DroppedDown = false;
}
```

### VB.NET
```vb
Private Sub comboBox1_SelectedIndexChanged(ByVal sender As Object, ByVal e As EventArgs)
    comboDropDown1.DroppedDown = True
End Sub

Private Sub comboBox2_SelectedIndexChanged(ByVal sender As Object, ByVal e As EventArgs)
    comboDropDown1.DroppedDown = True
End Sub

Private Sub button1_Click(ByVal sender As Object, ByVal e As EventArgs)
    comboDropDown.Text = comboBox1.Text + " " + comboBox2.Text
    comboDropDown1.DroppedDown = False
End Sub
```

## Cross References

- See also: [ComboDropDown Documentation](#ComboDropDownDocumentation)

<!-- tags: [Syncfusion Winforms, ComboDropDown, SelectedIndexChanged, DroppedDown] keywords: [ComboBox, DropDown, Panel, SelectedIndexChanged, DroppedDown, C#, VB.NET, ComboDropDown] -->
```