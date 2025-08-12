```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_340.jpeg
document_name: tools
page_number: 340
page_id: tools#page_340
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:37Z
fidelity: lossless
-->

## ButtonAdv Control Button Types and Custom Images

### Overview
- This page explains how to define button types for ButtonAdv controls in Windows Forms. It covers predefined button types and the option to set custom images when the ButtonType is set to Normal.

### WinForms-specific conventions
- The ButtonAdv control allows configuring various button types with specific images to enhance user interaction.

### Content

#### Predefined Button Types
The following are the predefined button types available for the ButtonAdv control:

| Button Type | Description |
|-------------|-------------|
| Right | Right image is used. |
| Redo | Redo image is used. |
| Undo | Undo image is used. |
| Check | Check image is used. |
| Browse | Browse image is used. |
| LeftEnd | Left end image is used. |
| RightEnd | Right end image is used. |

#### Specifying Custom Images
- You can specify your own image for the ButtonAdv by using the `Image` property. This will only take effect when `ButtonType` is set to `Normal`.
- For more details, see **Image Settings**.

#### Code Examples

##### C#
```csharp
// Setting Calculator button type
this.ButtonAdvControl.ButtonType = Syncfusion.Windows.Forms.Tools.ButtonTypes.Calculator;
```

##### VB.NET
```vbnet
' Setting Calculator button type
Me.ButtonAdvControl.ButtonType = Syncfusion.Windows.Forms.Tools.ButtonTypes.Calculator
```

### Figure: Button Types for ButtonAdv Control
![Figure 152: Button Types for ButtonAdv Control](https://drive.google.com/uc?id=1Q9876543210fghjk)

### Page-level Navigation/TOC (if applicable)
- This page contains a structured explanation of how to configure different button types and use custom images effectively.

### Cross References
- See **Image Settings** for more information on customizing images for ButtonAdv controls.

### RAG Annotations
<!-- tags: [syncfusion-sdk, windows-forms, buttonadv, button-type, button-image, custom-image, predefined-button-types] keywords: [ButtonType, Image property, Calculator, Undo, Redo, LeftEnd, RightEnd, ButtonAdvControl, Syncfusion Windows Forms, customizing images] -->
``` 
