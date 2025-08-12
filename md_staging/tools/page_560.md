```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_560.jpeg
document_name: tools
page_number: 560
page_id: tools#page_560
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:20:49Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
this.comboDropDown1.PopupContainer.Popup += new
EventHandler(this.AfterDropDownPopup);

private void AfterDropDownPopup(object sender, EventArgs e)
{
    // Tree takes focus on dropdown.
    this.treeView1.Focus();
}
```

```vb.net
Private Me.comboDropDown1.PopupContainer.Popup += New
EventHandler(Me.AfterDropDownPopup)

Private Sub AfterDropDownPopup(ByVal sender As Object, ByVal e As EventArgs)
    ' Tree takes focus on dropdown.
    Me.treeView1.Focus()
End Sub
```

![Figure 345: AfterDropDownPopup Event Illustrated](attachment:AfterDropDownPopup_Example.png)

## 3.5.5.1.5 Frequently Asked Questions

This section illustrates the solutions for various task-based queries about the control.

### 3.5.5.1.5.1 Using ComboBoxes inside ComboDropDown

This section deals on how to use two comboboxes within the dropdown area of a ComboDropDown. The panel contains two ComboBoxes and a Button. The text will change only after the Button had pressed.

The steps are as follows:

1. Create the ComboBoxes and OK button.
2. Populate the ComboBoxes.

---

© 2013 Syncfusion. All rights reserved.
```

```html
<!-- tags: [Windows Forms, ComboDropDown, Event Handling, frequently asked questions, control, version] keywords: [ComboBox, button, dropdown area, text change, task-based queries] -->
```