```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_296.jpeg
document_name: edit
page_number: 296
page_id: edit#page_296
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:50Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb
Private Sub editControl1_ReadOnlyChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles editControl1.ReadOnlyChanged
    edit = CType(sender, StreamEditControl)
End Sub

Private Sub MenuItem9_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MenuItem9.Click
    edit.ShowCodeSnippets()
End Sub
```

## 5.17 How To Set Different Background Colors For the Lines In the Edit Control

Edit Control provides support for custom coloring the background of the lines in the Edit Control. The following code snippet illustrates how to set the back color for the entire line and selected text.

```csharp
private IBackgroundFormat RegisterFormat()
{
    Color background = Color.Empty, foreground = Color.Empty;
    if (radioButton1.Checked)
        background = radioButton1.BackColor;
    else if (radioButton2.Checked)
        background = radioButton2.BackColor;
    else if (radioButton3.Checked)
        background = radioButton3.BackColor;
    if (radioButton6.Checked)
        foreground = radioButton6.BackColor;
    else if (radioButton5.Checked)
        foreground = radioButton5.BackColor;
    else if (radioButton4.Checked)
        foreground = radioButton4.BackColor;
    bool bUseHatchFille = comboBox1.SelectedIndex > 0;
    HatchStyle style = (bUseHatchFille) ? 
        (HatchStyle)Enum.Parse(typeof(HatchStyle), 
            comboBox1.SelectedItem.ToString()) :
        HatchStyle.Min;
    IBackgroundFormat format =
}
```

## API Reference (if applicable)
- **Namespace:** Syncfusion.Windows.Forms.Edit
- **Class:** EditControl
- **Methods:**
  - `RegisterFormat()`
- **Properties:**
  - `BackColor`
  - `ForeColor`
  - `HachStyle`

## Code Examples (multi-language supported)
- **C#:**
  ```csharp
  private IBackgroundFormat RegisterFormat()
  {
      Color background = Color.Empty, foreground = Color.Empty;
      if (radioButton1.Checked)
          background = radioButton1.BackColor;
      else if (radioButton2.Checked)
          background = radioButton2.BackColor;
      else if (radioButton3.Checked)
          background = radioButton3.BackColor;
      if (radioButton6.Checked)
          foreground = radioButton6.BackColor;
      else if (radioButton5.Checked)
          foreground = radioButton5.BackColor;
      else if (radioButton4.Checked)
          foreground = radioButton4.BackColor;
      bool bUseHatchFille = comboBox1.SelectedIndex > 0;
      HatchStyle style = (bUseHatchFille) ? 
          (HatchStyle)Enum.Parse(typeof(HatchStyle), 
              comboBox1.SelectedItem.ToString()) :
          HatchStyle.Min;
      IBackgroundFormat format =
  }
  ```

## Page-level Navigation/TOC (if applicable)
- 5.17 How To Set Different Background Colors For the Lines In the Edit Control

## Cross References
- See also: LineBackgroundFormatting

<!-- tags: [Syncfusion Winforms, edit control, background color customization] keywords: [edit, background color, line formatting, control, example, registration] -->
```