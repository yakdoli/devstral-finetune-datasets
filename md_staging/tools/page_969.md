<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_969.jpeg
document_name: tools
page_number: 969
page_id: tools#page_969
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:21Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Configuring images for various states of the `CheckBoxAdv` control.
- Setting properties for checked, unchecked, indeterminate, and disabled states.
- Exploring mouse hover behavior and corresponding images.

## Content

### Checkbox Images

```csharp
((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.IndeterminateImage")));
this.checkBoxAdv1.DisabledImage = 
((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.DisabledImage")));
this.checkBoxAdv1.StretchImage = false;
```

```vb
Me.checkBoxAdv1.ImageCheckBox = True
Me.checkBoxAdv1.ImageCheckBoxSize = New System.Drawing.Size(15, 15)
Me.checkBoxAdv1.CheckedImage = 
(CType(Resources.GetObject("checkBoxAdv1.CheckedImage"), System.Drawing.Image))
Me.checkBoxAdv1.UncheckedImage = 
(CType(Resources.GetObject("checkBoxAdv1.UncheckedImage"), System.Drawing.Image))
Me.checkBoxAdv1.IndeterminateImage = 
(CType(Resources.GetObject("checkBoxAdv1.IndeterminateImage"), System.Drawing.Image))
Me.checkBoxAdv1.DisabledImage = 
(CType(Resources.GetObject("checkBoxAdv1.DisabledImage"), System.Drawing.Image))
Me.checkBoxAdv1.StretchImage = False
```

**Figure 624: Image displayed for Checked State of CheckBoxAdv**

### Images displayed during Mouse Hover

Images can also be set when the mouse is hovered over the `CheckBoxAdv` control.

### CheckBoxAdv Properties and Descriptions

| CheckBoxAdv Properties       | Description                                                                                                           |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `MouseOverCheckedImage`      | Gets / sets the image used to draw the CheckBox when checked and mouse over.                                      |
| `MouseOverDisabledImage`     | Gets / sets the image used to draw the CheckBox when indeterminate and mouse over.                                 |
| `MouseOverUncheckedImage`    | Gets / sets the image used to draw the CheckBox when unchecked and mouse over.                                     |

## Page-level Navigation/TOC (if applicable)
- [Essential Tools for Windows Forms](#essential-tools-for-windows-forms)
  - [Checkbox Images](#checkbox-images)
  - [Images displayed during Mouse Hover](#images-displayed-during-mouse-hover)

## Cross References
- See also: [Syncfusion WinForms documentation](https://help.syncfusion.com/windowsforms)

<!-- tags: [winforms, checkboxadv, checkbox, images, states, hover] keywords: [essential tools, windows forms, checked, unchecked, indeterminate, disabled, mouse hover, checkboxadv, images, properties, config] -->