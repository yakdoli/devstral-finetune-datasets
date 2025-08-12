```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_537.jpeg
document_name: tools
page_number: 537
page_id: tools#page_537
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:23Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Focuses on adjusting the appearance of color group headers in Windows Forms applications.
- Details the properties used to modify the header height, text, alignment, and font.

## Content

### 3.5.4.5.3.1.2.3 Header Settings

The below properties are used to change the default appearance of the color group headers.

#### Color Group Properties

| Color Group Properties | Description |
|-------------------------|-------------|
| HeaderHeight           | Sets the height for the color group header. Default value is 20. |
| Name                   | Sets the name of the color group, i.e., the header text. |

#### ColorPickerUIAdv Property

| ColorPickerUIAdv Property | Description |
|-----------------------------|-------------|
| TextAlignment              | Sets the header text alignment of all the color groups. By default it is set to MiddleLeft. |
| Font                       | Sets the font for the header text. |

#### C#

```csharp
//Sets header height for Theme group
this.colorPickerUIAdv1.ThemeGroup.HeaderHeight = 25;
//Sets header text for Theme group
this.colorPickerUIAdv1.ThemeGroup.Name = "Recent Colors";
//Sets text alignment of the color group headers
this.colorPickerUIAdv1.TextAlign = 
System.Drawing.ContentAlignment.MiddleCenter;
//Sets the font style for the header text
this.colorPickerUIAdv1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Bold);
```

#### VB.NET

```vbnet
' Sets header height for Theme group
Me.colorPickerUIAdv1.ThemeGroup.HeaderHeight = 25
' Sets header text for Theme group
Me.colorPickerUIAdv1.ThemeGroup.Name = "Recent Colors"
' Sets text alignment of the color group headers
Me.colorPickerUIAdv1.TextAlign = 
System.Drawing.ContentAlignment.MiddleCenter
' Sets the font style for the header text
Me.colorPickerUIAdv1.Font = New System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Bold)
```

### Page-level Navigation/TOC (if applicable)
- This page is focused on the customization of color group headers in WinForms using properties and examples in both C# and VB.NET.

### Cross References
- See also: Related sections on advanced color picker UI elements and customization options in the full user guide.

## RAG Annotations

<!-- tags: [WinForms, ColorPickerUIAdv, HeaderCustomization, UIProperties] keywords: [HeaderHeight, Name, TextAlignment, Font, ThemeGroup] -->
```