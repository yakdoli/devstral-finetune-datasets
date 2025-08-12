```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_346.jpeg
document_name: tools
page_number: 346
page_id: tools#page_346
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:10Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

Text for the ButtonAdv can be customized using the below properties.

## Customizing ButtonAdv Text

### Properties Table

| Properties         | Description                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------|
| Text              | Sets the text for the ButtonAdv control.                                                         |
| TextAlign         | Sets the alignment of the text in the control. The options are, <br/> <br/> TopLeft, <br/> TopCenter, <br/> TopRight, <br/> MiddleLeft, <br/> MiddleCenter, <br/> MiddleRight, <br/> BottomLeft, <br/> BottomCenter and <br/> BottomRight. |
| TextImageRelation | Sets the relative location of the image to the text. The options are, <br/> <br/> Overlay, <br/> ImageBeforeText, <br/> TextBeforeImage, <br/> ImageAboveText and <br/> TextAboveImage. |
| Font              | Sets the font style for the control's text.                                                      |
| ForeColor         | Sets the fore color for the control's text.                                                     |

### Code Example

```csharp
[C#]

this.buttonAdv1.Text = "Image above Text";
this.buttonAdv4.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
this.buttonAdv4.TextImageRelation = TextImageRelation.ImageAboveText;
```

## API Reference

### Properties

- **Text**: Sets the text for the ButtonAdv control.
- **TextAlign**: Sets the alignment of the text in the control. The alignment options are:
  - TopLeft
  - TopCenter
  - TopRight
  - MiddleLeft
  - MiddleCenter
  - MiddleRight
  - BottomLeft
  - BottomCenter
  - BottomRight
- **TextImageRelation**: Sets the relative location of the image to the text. The options are:
  - Overlay
  - ImageBeforeText
  - TextBeforeImage
  - ImageAboveText
  - TextAboveImage
- **Font**: Sets the font style for the control's text.
- **ForeColor**: Sets the fore color for the control's text.

## Page-level Navigation/TOC

- **Text Customization for ButtonAdv**
  - Properties
  - Code Example

### Cross References

- See also:
  - [General Button Configuration] (examples outside this page)
  - [Advanced Styling Techniques] (examples outside this page)

<!-- tags: [WinForms, ButtonAdv, TextCustomization, PropertyOverview] keywords: [ButtonAdv, Text, TextAlign, TextImageRelation, Font, ForeColor, C# Demo] -->
```