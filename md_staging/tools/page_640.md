```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_640.jpeg
document_name: tools
page_number: 640
page_id: tools#page_640
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:38Z
fidelity: lossless
-->

## Content

We can also display the popup at a particular location.

### Code Example: C#

```csharp
[C#]

this.popupControlContainer1.ShowPopup(new Point(100, 100));
```

### Code Example: VB.NET

```vb
[VB.NET]

Private Sub richTextBox1_MouseUp(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventArgs)
    Me.popupControlContainer1.ShowPopup(Point.Empty)
End Sub
```

At run time, right-click on the RichTextBox, and the popup will be shown below the RichTextBox as in the following image:

![Figure 390: PopupControlContainer as popup for RichTextBox Editor](./image.png)

**Figure 390: PopupControlContainer as popup for RichTextBox Editor**

### 3.5.6.1.5.4 When Two PopUpControl Containers are Opened at the Same Time Controls like the ComboDropDown Close by Itself.

### 3.5.6.1.5.5 How to Get Around this Behavior?

In order to work around this behavior, you can set a boolean flag and cancel the BeforeCloseUp event as shown below.

## Footer

© 2013 Syncfusion. All rights reserved. 640 | Page
```

<!-- tags: [syncfusion winforms, rich text box, popup control container, combo dropdown, beforecloseup event, workaround] keywords: [popup, rich text box, combo dropdown, boolean flag, beforecloseup] -->
