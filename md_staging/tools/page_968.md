```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_968.jpeg
document_name: tools
page_number: 968
page_id: tools#page_968
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:24Z
fidelity: lossless
-->

## CheckBoxAdv Image Settings

### Overview

- Images can be set for the CheckBoxAdv control when it is in the Checked, Unchecked, or Indeterminate state.
- The CheckBoxAdv provides properties to display images based on its state.
- Key properties include ImageCheckBox, ImageCheckBoxSize, CheckedImage, UncheckedImage, IndeterminateImage, DisabledImage, and StretchImage.

### Content

The image settings of the CheckBoxAdv control have been discussed in this section.

**Images for CheckBoxAdv States**

Images can be set to the CheckBoxAdv when it is in the Checked, Unchecked, or Indeterminate state. The CheckBoxAdv allows us to set the following properties in order to display images.

| CheckBoxAdv Properties              | Description                                                                                                                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ImageCheckBox**                   | Indicates whether the CheckBox will be drawn using the images provided.                                                                                                                                     |
| **ImageCheckBoxSize**               | Gets / sets the size of the ImageCheckBox. <br> **Note**: The ImageCheckBox property must be set to 'True'.                                                                                                   |
| **CheckedImage**                    | Gets / sets the image used to draw the CheckBox when checked and the mouse is not over.                                                                                                                   |
| **UncheckedImage**                  | Gets / sets the image used to draw the CheckBox when unchecked and the mouse is not over.                                                                                                                |
| **IndeterminateImage**              | The image used to draw the CheckBox when indeterminate and the mouse is not over.                                                                                                                          |
| **DisabledImage**                   | Gets / sets the image used to draw the CheckBox when it is disabled.                                                                                                                                         |
| **StretchImage**                    | Indicates whether the state images of the CheckBox are stretched.                                                                                                                                          |

---

**Note**: Before setting the images, make sure the **ImageCheckBox** property is set to **'True'**.

### WinForms-specific Code Examples

```csharp
this.checkBoxAdv1.ImageCheckBox = true;
this.checkBoxAdv1.ImageCheckBoxSize = new System.Drawing.Size(15, 15);
this.checkBoxAdv1.CheckedImage =
    ((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.CheckedImage")));
this.checkBoxAdv1.UncheckedImage =
    ((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.UncheckedImage")));
this.checkBoxAdv1.IndeterminateImage =
```

### Cross References

- Refer to the section on CheckBoxAdv properties for more information on specific property settings.

<!-- tags: [Syncfusion Winforms, CheckBoxAdv, ImageCheckBox, WinForms, CheckBox Properties] keywords: [CheckBoxAdv, ImageCheckBox, CheckedImage, UncheckedImage, IndeterminateImage, DisabledImage, StretchImage] -->
```