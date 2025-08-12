```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_465.jpeg
document_name: tools
page_number: 465
page_id: tools#page_465
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

By default the DateTimePicker control has a checkbox in checked state. This checkbox can be hidden using **ShowCheckBox** property and the state can be unchecked through designer, using **Checked** property.

## Content

```csharp
this.dateTimePickerAdv1.ShowCheckBox = false;
this.dateTimePickerAdv5.Checked = false;
```

```vb.net
Me.dateTimePickerAdv1.ShowCheckBox = False
Me.dateTimePickerAdv5.Checked = False
```

![Figure 264: Unchecked State of the CheckBox](https://i.imgur.com/unchecked_checkbox.png)

**Figure 264: Unchecked State of the CheckBox**

### See Also

- **Text Field, UpDown and DropDown Buttons**
- **3.5.3.2.3.1.3 Text Field**

#### This section discusses the properties related to Checkbox and text field in the DateTimePicker control.

##### CheckBox

By default the DateTimePicker control has a checkbox in checked state. This checkbox can be hidden using **ShowCheckBox** property and the state can be unchecked through designer, using **Checked** property.

```csharp
this.dateTimePickerAdv1.ShowCheckBox = false;
this.dateTimePickerAdv5.Checked = false;
```

```vb.net
Me.dateTimePickerAdv1.ShowCheckBox = False
```

<!-- tags: [Windows Forms, DateTimePicker, CheckBox, ShowCheckBox, Checked, Designer, Control, WinForms] keywords: [DateTimePicker, CheckBox, ShowCheckBox, Checked, Designer, Control, datetime, state, checked, unchecked, properties] -->
```