```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_993.jpeg
document_name: tools
page_number: 993
page_id: tools#page_993
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:46:47Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Properties Related to ImageCheckBox

The following table describes properties related to ImageCheckBox in a RadioButton:

| Property Name          | Description                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------|
|                       | ImageCheckBox property must be set to 'True'.                                                   |
| CheckedImage          | Gets / sets the image used to draw the RadioButton when checked and mouse not over.            |
| UncheckedImage        | Gets / sets the image used to draw the RadioButton when unchecked and mouse not over.          |
| DisabledImage         | Gets / sets the image used to draw the RadioButton when disabled.                             |
| StretchImage          | Indicates whether the state images of the RadioButton are stretched.                          |

#### Note: Before setting the images, make sure the ImageCheckBox property is set to 'True'.

### C# Code Example

```csharp
thisadioButtonAdv1.ImageCheckBox = true;
thisadioButtonAdv1.ImageCheckBoxSize = new System.Drawing.Size(15, 15);
thisadioButtonAdv1.CheckedImage =
    (System.Drawing.Image)(resources.GetObject("checkBoxAdv1.CheckedImage"));
thisadioButtonAdv1.UncheckedImage =
    (System.Drawing.Image)(resources.GetObject("checkBoxAdv1.UncheckedImage"));
thisadioButtonAdv1.DisabledImage =
    (System.Drawing.Image)(resources.GetObject("checkBoxAdv1.DisabledImage"));
thisadioButtonAdv1.StretchImage = false;
```

### VB.NET Code Example

```vb
Me.radioButtonAdv1.ImageCheckBox = True
Me.radioButtonAdv1.ImageCheckBoxSize = New System.Drawing.Size(15, 15)
Me.radioButtonAdv1.CheckedImage =
    CType(Resources.GetObject("checkBoxAdv1.CheckedImage"), System.Drawing.Image)
Me.radioButtonAdv1.UncheckedImage =
    CType(Resources.GetObject("checkBoxAdv1.UncheckedImage"), System.Drawing.Image)
```

## Page-level Navigation/TOC (if applicable)
- **Properties Related to ImageCheckBox**
- **C# Code Example**
- **VB.NET Code Example**
  
## Cross References
- **See also:** Additional resources on ImageCheckBox and related concepts in Syncfusion Winforms documentation.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, ImageCheckBox, RadioButton, C#, VB.NET, properties, version: 11.4.0.26] keywords: [ImageCheckBox, RadioButton, CheckedImage, UncheckedImage, DisabledImage, StretchImage, C#, VB.NET, property settings, version] -->
```