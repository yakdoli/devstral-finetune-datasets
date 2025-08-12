```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_478.jpeg
document_name: tools
page_number: 478
page_id: tools#page_478
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:15:57Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Details configuration of the DateTimePickerAdv control's background image.
- Demonstrates setting border styles for DateTimePickerAdv in 2D or 3D modes.

## Content
### Setting Background Image for DateTimePickerAdv
- **C#**
  ```csharp
  this.dateTimePickerAdv2.BackgroundImage = 
  ((System.Drawing.Image)(resources.GetObject("dateTimePickerAdv2.BackgroundImage")));
  ```
- **VB.NET**
  ```vb
  Me.dateTimePickerAdv2.BackgroundImage = 
  DirectCast((resources.GetObject("dateTimePickerAdv2.BackgroundImage")), 
  System.Drawing.Image)
  ```
  ![Background Image for DateTimePickerAdv](https://example.com/placeholder_image.png)
  *Figure 276: Background Image for DateTimePickerAdv*

### Border Styles
#### 3.5.3.2.3.4.2 Border Styles
- The DateTimePickerAdv control offers various border options when in 2D or 3D mode.
- The table below illustrates the border settings.

| DateTimePickerAdv Properties | Description |
|------------------------------|-------------|
| **BorderStyle**              | Specifies whether the DateTimePickerAdv should have a border and if it is 2D or 3D border. The options are, |
|                              | - None      |
|                              | - FixedSingle |
|                              | - Fixed3D(Default) |
| **Border3DStyle**            | Specifies the 3D border style of the DateTimePickerAdv. The options are, |

## See Also
- **Border Styles**

## API Reference
- Namespace: Syncfusion.Windows.Forms.Tools
- Class: DateTimePickerAdv
- Properties:
  - **BorderStyle**
    - **Description**: Specifies whether the DateTimePickerAdv should have a border and if it is 2D or 3D border.
    - **Options**: None, FixedSingle, Fixed3D (Default)
  - **Border3DStyle**
    - **Description**: Specifies the 3D border style of the DateTimePickerAdv.

### Code Examples
- Sample C# code for setting **BorderStyle**:
  ```csharp
  this.dateTimePickerAdv2.BorderStyle = BorderStyle.Fixed3D;
  ```

### Cross References
- Related section: **3.5.3.2.3.4.2 Border Styles**

<!-- tags: [Syncfusion Winforms, DateTimePickerAdv, Border Styles, 2D, 3D] keywords: [Background Image, Border Style, DateTimePicker, Syncfusion, WinForms, Styles] -->
``` 
