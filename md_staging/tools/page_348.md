```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_348.jpeg
document_name: tools
page_number: 348
page_id: tools#page_348
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:06Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Lists various settings available for the ButtonAdv control in the Tasks window.
- Detailed explanation of each setting and its functionality.
- Guides on how to configure and customize ButtonAdv control properties using the Smart Tag feature.

## Content

### Tasks Window for ButtonAdv

#### Figure 159: Tasks Window accessed using Smart Tag of ButtonAdv
![Image Description](https://example.com/image.png)

**The various settings through this window is as follows:**

- **Name** - Lets you edit the control text.
- **UseVisualStyle** - Enables visual style settings.
- **KeepFocusRectangle** - Specifies whether to show focus rectangle or not.
- **Appearance** - Lets you to set the Visual style for the control.
- **ButtonType** - Lets you to set the button type.
- **BorderStyles** - Lets you to set the border styles for the control.
- **Image** - Lets you to set the image for the ButtonAdv control.
- **ImageAlign** - Sets the image alignment within the control.
- **Text** - Sets the text for button.
- **Text Alignment** - Sets the alignment of the text.

### Image Settings

#### ButtonAdv supports two types of images. They are:
- BackgroundImage
- Image

#### BackgroundImage

### WinForms-specific conventions
- The **ButtonAdv** control allows customization of various properties through the Smart Tag window.
- These properties include visual style, border types, image alignment, and text formatting.

### Code Examples

#### Example: Configuring ButtonAdv with Smart Tag
```csharp
// Using Smart Tag to configure ButtonAdv properties
private void ConfigureButtonAdv() {
    ButtonAdv buttonAdv = new ButtonAdv();
    
    // Set properties using Smart Tag settings
    buttonAdv.Name = "MyButton";
    buttonAdv.UseVisualStyle = true;
    buttonAdv.KeepFocusRectangle = true;
    buttonAdv.Appearance = ButtonAdvAppearance.Normal;
    buttonAdv.ButtonType = ButtonAdvType.Normal;
    buttonAdv.BorderStyles = Border3DStyle.Default;
    
    // Image settings
    buttonAdv.Image = new Bitmap("image.png");
    buttonAdv.ImageAlign = ContentAlignment.MiddleCenter;
    
    // Text settings
    buttonAdv.Text = "Click Me";
    buttonAdv.TextAlignment = ContentAlignment.MiddleCenter;
}
```

## API Reference

### ButtonAdv Properties

#### Properties
- **Name**
  - Type: String
  - Description: Sets the name of the ButtonAdv control.
- **UseVisualStyle**
  - Type: Boolean
  - Description: Enables visual style settings for the control.
- **KeepFocusRectangle**
  - Type: Boolean
  - Description: Controls whether a focus rectangle is displayed when the control is focused.
- **Appearance**
  - Type: ButtonAdvAppearance
  - Description: Sets the visual style for the control.
- **ButtonType**
  - Type: ButtonAdvType
  - Description: Defines the type of the button.
- **BorderStyles**
  - Type: Border3DStyle
  - Description: Sets the border style for the control.
- **Image**
  - Type: Image
  - Description: Sets the image for the ButtonAdv control.
- **ImageAlign**
  - Type: ContentAlignment
  - Description: Sets the alignment of the image within the control.
- **Text**
  - Type: String
  - Description: Sets the text for the button.
- **TextAlignment**
  - Type: ContentAlignment
  - Description: Sets the alignment of the text.

### Image Settings

#### BackgroundImage
- свойства, связанные с фоновыми изображениями.

## Cross References
- See also: ButtonAdv documentation for detailed configuration options.

<!-- tags: [Syncfusion Winforms, ButtonAdv, Smart Tag, Image Settings, Appearance, BorderStyles, ButtonAdvType] keywords: [ButtonAdv, Smart Tag, configure, settings, visual style, image alignment, text formatting] -->
```