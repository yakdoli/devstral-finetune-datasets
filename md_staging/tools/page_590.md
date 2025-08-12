```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_590.jpeg
document_name: tools
page_number: 590
page_id: tools#page_590
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:33Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Code Example

```csharp
this.comboBoxAdv1.UseBackColor = true;
this.comboBoxAdv1.BackColor = Color.Red;
```

```vbnet
Me.comboBoxAdv1.UseBackColor = true
Me.comboBoxAdv1.BackColor = Color.Red
```

#### 3.5.5.3 ComboBoxBase

The flexible **ComboBoxBase control** is an alternative to the standard combo box control. It separates the edit portion from the drop-down list portion thereby making this architecture powerful and flexible. However, due to this separation, the object model of this control is different from that of the combo box.

There is however, a ComboBoxAdv, which is based on the ComboBoxBase and provides an identical object model to that of the framework combo box. You can also get a framework combo box like look-and-feel (without a similar object model) by attaching a list box control to the ComboBoxBase.

Note that Essential Grid comes with a **ListControl-derived GridListControl**, which you can place in the drop-down area to get a multi-column drop-down combo.

---

### References

- Essential Grid
- ListControl
- GridListControl
- ComboBox
- ComboBoxBase
- ComboBoxAdv

---

### API Reference

#### Essential Grid

- **GridListControl**: Subclass of ListControl used for multi-column drop-downs.
- **ComboBoxBase**: Control that separates edit and drop-down list portions.
- **ComboBoxAdv**: Control based on ComboBoxBase with a similar object model to the framework combo box.

#### Properties and Methods

- **UseBackColor**: Boolean property to enable custom background color.
- **BackColor**: Property to set the color of the background.

---

### Cross References

- For more details on GridListControl, see the Essential Grid documentation.
- For additional information on ComboBoxBase and ComboBoxAdv, refer to the respective sections in the WinForms Toolkit documentation.

<!-- tags: [syncfusion, windows forms, combobox, comboboxbase, comboboxadv, essential grid, gridlistcontrol] keywords: [comboboxbase, comboboxadv, gridlistcontrol, listcontrol, multicoloumdropdown] -->
```