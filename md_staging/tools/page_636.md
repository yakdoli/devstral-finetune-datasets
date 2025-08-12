```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_636.jpeg
document_name: tools
page_number: 636
page_id: tools#page_636
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:25Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Adding TextBox and Button controls to the PopupControlContainer.
- Displaying the Popup on a RichTextBox using a code snippet.
- Handling the BeforePopup event.

## Content

### Adding Controls and Displaying the Popup

![](https://via.placeholder.com/150)

**Figure 388: TextBox and Button controls added to the PopupControlContainer**

#### Display the Popup on the RichTextBox

1. **Using the following code snippet:**

   **[C#]**

   ```csharp
   private void richTextBox1_MouseUp(object sender, System.Windows.Forms.MouseEventHandler e)
   {
       this.popupControlContainer1.ShowPopup(Point.Empty);
   }
   ```

   **[VB.NET]**

   ```vb
   Private Sub richTextBox1_MouseUp(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventHandler)
       Me.popupControlContainer1.ShowPopup(Point.Empty)
   End Sub
   ```

#### Handling the BeforePopup event

2. **Handle BeforePopup event.**

   **[C#]**

   ```csharp
   private void popupControlContainer1_BeforePopup(object sender, System.ComponentModel.CancelEventArgs e)
   {
       // Set the text of richTextBox to the textBox
       this.textBox1.Text = this.richTextBox1.Text;
   }
   ```

   **[VB.NET]**

   ```vb
   Private Sub popupControlContainer1_BeforePopup(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs)
       ' Set the text of richTextBox to the textBox
   ```

## Page-level Navigation/TOC (if applicable)
- No TOC provided in the image.

## Cross References
- None provided in the image.

<!-- tags: [Syncfusion, Winforms, PopupControlContainer, TextBox, Button, RichTextBox, BeforePopup] keywords: [PopupControlContainer, TextBox, Button, RichTextBox, BeforePopup, MouseUp] -->
```
