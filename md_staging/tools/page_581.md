```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_581.jpeg
document_name: tools
page_number: 581
page_id: tools#page_581
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:03Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of the `ComboBoxAdv` control in Windows Forms.
- Explains how to set the background color using `BackColor` and ignore theme background properties.
- Outlines image settings and associated properties for the `ComboBoxAdv` control.

## Content

### Setting the Background Color

The `BackColor` property is used to set the background color of the `ComboBoxAdv` control, and the `IgnoreThemeBackground` property ensures that the theme background is ignored.

```csharp
this.comboBoxAdv1.BackColor = System.Drawing.SystemColors.Info;
this.comboBoxAdv1.IgnoreThemeBackground = true;
```

```vb
Me.comboBoxAdv1.BackColor = System.Drawing.SystemColors.Info
Me.comboBoxAdv1.IgnoreThemeBackground = True
```

#### Figure 360: Background set using BackColor
![Figure 360: Background set using BackColor](https://i.imgur.com/example_image.png)

**Legend:**
- **Left:** Theme Background
- **Right:** BackColor

### Image Settings

Images can be easily associated with the items of the `ComboBoxAdv` control using the following properties:

#### Table: ComboBoxAdv Properties

| ComboBoxAdv Properties          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| **ImageList**                    | Specifies the imagelist that is used for the ComboBoxAdv control.         |
| **ShowImageInTextBox**           | It sets the selected image in the textbox of the ComboBoxAdv control.      |
| **ItemsImageIndexes**           | Invokes an editor and lets you to set image index for individual dropdown items. |

#### C# Code Example

```csharp
this.comboBoxAdv1.ImageList = this.imageList1;
this.comboBoxAdv1.ItemsImageIndexes.Add(new
Syncfusion.Windows.Forms.Tools.ComboBoxAdv.ImageIndexItem(this.comboBoxAdv1, "Pointer", 0));
```

## API Reference

### ComboBoxAdv Properties
- **ImageList**: Type: `ImageList`  
  Specifies the imagelist that is used for the ComboBoxAdv control.

- **ShowImageInTextBox**: Type: `Boolean`  
  Sets the selected image in the textbox of the ComboBoxAdv control.

- **ItemsImageIndexes**: Type: `ComboBoxAdv.ImageIndexItem`  
  Invokes an editor to set the image index for individual dropdown items.

## Code Examples

### Setting ImageList
```csharp
this.comboBoxAdv1.ImageList = this.imageList1;
```

### Adding Image Index Items
```csharp
this.comboBoxAdv1.ItemsImageIndexes.Add(new
Syncfusion.Windows.Forms.Tools.ComboBoxAdv.ImageIndexItem(this.comboBoxAdv1, "Pointer", 0));
```

### Complete Example
```csharp
this.comboBoxAdv1.ImageList = this.imageList1;
this.comboBoxAdv1.ItemsImageIndexes.Add(
    new Syncfusion.Windows.Forms.Tools.ComboBoxAdv.ImageIndexItem(
        this.comboBoxAdv1, "Pointer", 0
    )
);
```

## Cross References

- See also:  
  - [ComboBoxAdv Documentation](https://help.syncfusion.com/windowsforms/combo-box-adv)
  - [ImageList Documentation](https://help.syncfusion.com/windowsforms/imagemanager)

<!-- tags: [windowsforms, comboboxadv, imagelist, version:11.4.0.26] keywords: [backgroundColor, image settings, comboboxadv, imagelist, theme background, ignoreThemeBackground, imageIndexItem] -->
```