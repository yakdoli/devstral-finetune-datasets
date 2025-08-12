```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_970.jpeg
document_name: tools
page_number: 970
page_id: tools#page_970
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### CheckBoxAdv Hover Images

[C#]
```csharp
this.checkBoxAdv1.MouseOverCheckedImage = 
    ((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.MouseOverCheckedImage")));
this.checkBoxAdv1.MouseOverIndeterminateImage =
    ((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.MouseOverIndeterminateImage")));
this.checkBoxAdv1.MouseOverUncheckedImage =
    ((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.MouseOverUncheckedImage")));
```

[VB.NET]
```vb.net
Me.checkBoxAdv1.MouseOverCheckedImage = 
    CType(Resources.GetObject("checkBoxAdv1.MouseOverCheckedImage"), System.Drawing.Image)
Me.checkBoxAdv1.MouseOverIndeterminateImage =
    CType(Resources.GetObject("checkBoxAdv1.MouseOverIndeterminateImage"), System.Drawing.Image)
Me.checkBoxAdv1.MouseOverUncheckedImage =
    CType(Resources.GetObject("checkBoxAdv1.MouseOverUncheckedImage"), System.Drawing.Image)
```

![Figure: Image displayed for Unchecked State of CheckBoxAdv during Mouse Hover](./images/ferro确认.jpg)

**Figure 625: Image displayed for Unchecked State of CheckBoxAdv during Mouse Hover**

A Sample which demonstrates the ImageCheckBox property of CheckBoxAdv is available in the below sample installation path.

```
..My Documents\Syncfusion\EssentialStudio\<Version Number>\Windows\Tools.Windows\Samples\2.0\Editors Package\OptionControls
```

### 3.5.11.1.3.8 Themes and Visual Styles

This section discusses the themes and visual style settings that are supported by the CheckBoxAdv control.

#### Themes

The CheckBoxAdv can be provided with a themed appearance using the below given property.

## API Reference

### CheckBoxAdv Properties

The CheckBoxAdv control supports the following properties related to themes and visual styles:
- **ImageCheckBox**: Allows customization of images for check, uncheck, and indeterminate states.

## Code Examples

[C#]
```csharp
// Example of setting images for CheckBoxAdv
this.checkBoxAdv1.ImageCheckBox = true;
this.checkBoxAdv1.MouseOverCheckedImage = 
    ((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.MouseOverCheckedImage")));
this.checkBoxAdv1.MouseOverIndeterminateImage =
    ((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.MouseOverIndeterminateImage")));
this.checkBoxAdv1.MouseOverUncheckedImage =
    ((System.Drawing.Image)(resources.GetObject("checkBoxAdv1.MouseOverUncheckedImage")));
```

[VB.NET]
```vb.net
' Example of setting images for CheckBoxAdv
Me.checkBoxAdv1.ImageCheckBox = True
Me.checkBoxAdv1.MouseOverCheckedImage = 
    CType(Resources.GetObject("checkBoxAdv1.MouseOverCheckedImage"), System.Drawing.Image)
Me.checkBoxAdv1.MouseOverIndeterminateImage =
    CType(Resources.GetObject("checkBoxAdv1.MouseOverIndeterminateImage"), System.Drawing.Image)
Me.checkBoxAdv1.MouseOverUncheckedImage =
    CType(Resources.GetObject("checkBoxAdv1.MouseOverUncheckedImage"), System.Drawing.Image)
```

## RAG Annotations

<!-- tags: [WinForms, CheckBoxAdv, Themes, Visual Styles, ImageCheckBox] keywords: [CheckBoxAdv, ImageCheckBox, Themes, Visual Styles, MouseOverCheckedImage, MouseOverIndeterminateImage, MouseOverUncheckedImage, ImageCheckBox property] -->
```