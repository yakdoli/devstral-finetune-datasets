```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_626.jpeg
document_name: tools
page_number: 626
page_id: tools#page_626
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## 3.5.6.1.2 Creating Simple Popup

This section deals with creating a simple popup with the help of `PopupControlContainer` control.

### Creating `PopupControlContainer`

The `PopupControlContainer` control provides full support for the Windows Forms designer. To use a `PopupControlContainer` control in your application, all you need to do is drag and drop the `PopupControlContainer` control from the controls toolbox onto your form.

![PopupControlContainer in the Toolbox](image.png)

**Figure 385: PopupControlContainer in the Toolbox**

The `PopupControlContainer` can be created programmatically as follows.

1. Include the Shared.Base assembly reference to Reference folder.
2.
3. Create an instance of `PopupControlContainer` and add to the Form.

```csharp
private Syncfusion.Windows.Forms.PopupControlContainer popupControlContainer1;
this.popupControlContainer1 = new Syncfusion.Windows.Forms.PopupControlContainer();
this.Controls.Add(this.popupControlContainer1);
```

```vb.net
Private popupControlContainer1 As Syncfusion.Windows.Forms.PopupControlContainer
```
```html
<!-- tags: [windows forms, popup, popupcontrolcontainer, essential tools, designer, toolbox, windows forms, syncfusion sdk] keywords: [popupcontrolcontainer, windows forms, essential tools, designer, toolbox, programmatically] -->
```