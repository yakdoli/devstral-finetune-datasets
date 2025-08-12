```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_987.jpeg
document_name: tools
page_number: 987
page_id: tools#page_987
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:47:26Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Describes the properties and alignment options for `RadioButtonAdv` in Syncfusion Winforms.
- Focuses on configuring text alignment and alignment settings for `RadioButtonAdv`.

## Content

### RadioButtonAdv Properties

#### TextContentAlignment

The `TextContentAlignment` property indicates the alignment of the text. The default value is set to 'MiddleLeft'. The options included are as follows:

- `TopLeft`
- `TopCenter`
- `TopRight`
- `MiddleLeft`
- `MiddleCenter`
- `MiddleRight`
- `BottomLeft`
- `BottomCenter`
- `BottomRight`

Note: The `WrapText` property must be set to 'False'. Refer to Text Settings for more information.

**Example: Setting `TextContentAlignment` to `MiddleCenter`**

- **C#**
  ```csharp
  this.radioButtonAdv1.TextContentAlignment =
      System.Drawing.ContentAlignment.MiddleCenter;
  ```

- **VB.NET**
  ```vb
  Me.radioButtonAdv1.TextContentAlignment =
      System.Drawing.ContentAlignment.MiddleCenter
  ```

**Figure 637: Text aligned to "MiddleRight"**

![Radio Button Alignment](https://via.placeholder.com/200x50?text=radioButtonAdv1)

### RadioButton Alignment

## APIs and Code Examples

### Setting TextContentAlignment Property
The `TextContentAlignment` property can be configured programmatically as shown in the examples above.

### References
- Refer to Text Settings for details on configuring text properties.

<!-- tags: [syncfusion, windowsforms, textalignment, radiobuttonadv] keywords: [textcontentalignment, alignment options, middlecenter, topleft, topcenter, topright, middleleft, middleright, bottomleft, bottomcenter, bottomright, wraptext] -->
``` 
