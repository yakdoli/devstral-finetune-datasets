```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_540.jpeg
document_name: tools
page_number: 540
page_id: tools#page_540
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:19:26Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page outlines the properties and their descriptions for the `ColorPickerUIAdv` control.
- Demonstrates how to enable and customize the Office 2007 style and theme using code examples in C# and VB.NET.

## Content

### Properties of ColorPickerUIAdv

| ColorPickerUIAdv Properties                  | Description                                                                 |
|----------------------------------------------|-----------------------------------------------------------------------------|
| **UseOffice2007Style**                       | Office 2007 style can be enabled or disabled using this property. By default it is true. |
| **Office2007Theme**                         | Sets the color scheme for the Office2007 Style.                              |

### Enabling and Customizing Office 2007 Style

#### C#
```csharp
colorPickerUIAdv1.UseOffice2007Style = true;

// Sets Office2007 Black color Theme
colorPickerUIAdv1.Office2007Theme =
Syncfusion.Windows.Forms.Office2007Theme.Black;
```

#### VB.NET
```vb
colorPickerUIAdv1.UseOffice2007Style = True

' Sets Office2007 Black color Theme
Private colorPickerUIAdv1.Office2007Theme =
Syncfusion.Windows.Forms.Office2007Theme.Black
```

### Visual Representation

The following images depict different themes available for the `ColorPickerUIAdv` control:

- **Office 2007 Light Theme**:
- **Office 2007 Black Theme**:
- **Standard Colors**:

![Theme Colors for ColorPickerUIAdv](https://raw.githubusercontent.com/syncfusion-demos/windows-forms-samples/main/images/office-themes.png)

<!-- tags: [ColorPickerUIAdv, Office 2007 Style, Windows Forms, Syncfusion, Theme, Control, Version 11.4.0.26] keywords: [ColorPickerUIAdv, Office2007Style, Office2007Theme, C#, VB.NET, Windows Forms, Syncfusion, Office 2007, Theme, Control Properties] -->
```