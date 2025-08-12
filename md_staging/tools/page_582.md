```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_582.jpeg
document_name: tools
page_number: 582
page_id: tools#page_582
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:08Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```vb.net
Me.Gon AccManager2.List = Me.accImageList
Me.ComboBoxAdv1.ListItem.LoadImageIndex.Add(New Syncfusion.Windows.Forms.Tools.QomboBoxAdv.ListItem("Pointer", 0))
```

### Image in TextBox

The following code snippet is used to show the images together with the selected text in the TextArea of the ComboBoxAdv control.

**C#:**
```csharp
// Show the images in the TextArea.
this.comboBoxAdv1.ShowImageInTextBox = true
```

**VB.NET:**
```vb.net
// Show the images in the TextArea.
Me.comboBoxAdv1.ShowImageInTextBox = True
```

![](./image.png)

*Figure 361: TextArea with Image*

#### 3.5.5.2.3.4.5 Customizable ComboBoxAdv height

ComboBoxAdv allows to customize the height of the Display area, making more space to display larger images and text items by setting the `TextBoxHeight` property of the ComboBox.

**C#:**
```csharp
// Sets the height of the ComboBox.
this.comboBoxAdv1.TextBoxHeight = 80;
```

---

© 2013 Syncfusion. All rights reserved.
582 | Page
```