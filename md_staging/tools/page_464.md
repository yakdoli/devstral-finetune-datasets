```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_464.jpeg
document_name: tools
page_number: 464
page_id: tools#page_464
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:24Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Image for DropDown

The existing dropdown icon can be replaced with a custom image using the below properties.

| DateTimePickerAdv Properties    | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| DropDownImage                   | Gets or Sets the Image for dropdown button.                              |
| StretchDropDownImage            | Specifies whether the image of the dropdown is stretched.                |

#### Code Examples

- **[C#]**
  ```csharp
  this.dateTimePickerAdv1.DropDownImage =
    ((System.Drawing.Image)(resources.GetObject("dateTimePickerAdv1.DropDownImage")));
  this.dateTimePickerAdv1.StretchDropDownImage = true;
  ```

- **[VB.NET]**
  ```vb
  Me.dateTimePickerAdv1.DropDownImage =
    DirectCast((resources.GetObject("dateTimePickerAdv1.DropDownImage")), System.Drawing.Image)
  Me.dateTimePickerAdv1.StretchDropDownImage = True
  ```

### Visual Examples

![Figure 262: Custom Image for DropDown Button](https://via.placeholder.com/200)

**Figure 262: Custom Image for DropDown Button**

![Figure 263: Stretched Custom Image](https://via.placeholder.com/200)

**Figure 263: Stretched Custom Image**

## See Also

- Checkbox, Text Field

### CheckBox

**3.5.3.2.3.1.2 CheckBox**

## Footer Navigation
© 2013 Syncfusion. All rights reserved. 464 | Page

<!-- tags: [DateTimePickerAdv, DropDownImage, StretchDropDownImage, Custom Image, CheckBox] keywords: [DateTimePickerAdv, DropDownImage, StretchDropDownImage, Custom Image, CheckBox] -->
```