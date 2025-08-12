```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_562.jpeg
document_name: tools
page_number: 562
page_id: tools#page_562
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:02Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
' Closes the dropdown and changes the text.
Private Sub button1_Click(ByVal sender As Object, ByVal e As EventArgs)
    comboDropDown.Text = comboBox1.Text + " works in " + comboBox2.Text
    comboDropDown1.DroppedDown = False
End Sub
```

![Figure 346: Editing ComboDropDown text using another two Comboboxes](https://i.imgur.com/placeholder.png)

## 3.5.5.1.5.2 How to remove the current selection in ComboDropDown control?

We can derive custom ComboDropDown control and override DrawListModeEditPortion property to remove the selection as follows.

### [C#]

```csharp
public class CustomComboDropDown : ComboDropDown
{
    public CustomComboDropDown()
    {
    }

    protected override void DrawListModeEditPortion(PaintEventArgs e, Color highlightBG, Color highlightText, bool drawFocusRect)
    {
        // Set the highlightBG to Color.Transparent to draw transparent selection.
        // Set drawFocusRect to false to hide the focus rectangle.
        base.DrawListModeEditPortion(e, Color.Transparent, highlightText, false);
    }
}
```
```