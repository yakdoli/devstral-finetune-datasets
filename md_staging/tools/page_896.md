```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_896.jpeg
document_name: tools
page_number: 896
page_id: tools#page_896
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section discusses the usage and features of the TextBoxExt control in Windows Forms.
- It covers the creation and customization of the TextBoxExt control.
- Includes a visual representation of the TextBoxExt control as shown in Figure 569.

## Content

### 4. Run the application
Run the application to view the TextBoxExt control in your form. After creating the TextBoxExt, it can be used similarly to the Windows Forms' TextBox control.

#### Figure 569: TextBoxExt created Through Code

![Figure 569: TextBoxExt created Through Code](https://example.com/figure569.jpg)

### 3.5.8.10.3 Concepts and Features

#### 3.5.8.10.3.1 Text Settings
This section discusses the text settings of the TextBoxExt control.

The text associated with the TextBoxExt control can be set and customized using the following settings:

| TextBoxExt Properties     | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Text                      | Specifies the text associated with the control.                            |
| CharacterCasing           | Gets / sets the case of characters as they are typed.                    <br> <br> Includes the following options: <br> - Normal, <br> - Upper, <br> - Lower. |
| TextAlign                 | Indicates how the text should be aligned for edit controls.               |
| RightToLeft               | Indicates whether the component should draw right to left for RTL languages. |
| SelectedText              | Gets / sets a value indicating the currently selected text.                |

## API Reference
This section provides an overview of the properties and their descriptions as listed in the table above.

## Code Examples
Example code for utilizing the TextBoxExt properties can be written using C# syntax:

```csharp
// Example: Setting the text and alignment properties
TextBoxExt textBoxExt1 = new TextBoxExt();
textBoxExt1.Text = "Sample Text";
textBoxExt1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
textBoxExt1.CharacterCasing = System.Windows.Forms.CharacterCasing.Lower;
```

## Cross References
- For more information on Windows Forms and control customization, refer to the respective sections in the documentation.

<!-- tags: [Windows Forms, TextBoxExt, Text Settings, CharacterCasing, TextAlign, RightToLeft, SelectedText] keywords: [TextBoxExt, controls, customization, text alignment, character casing, selected text, run application, figure 569, concepts and features] -->
```