```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_860.jpeg
document_name: tools
page_number: 860
page_id: tools#page_860
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:11Z
fidelity: lossless
-->

## Overview
- Explains the application of Themes to the MaskedEditBox control.
- Describes how to enable or disable XP themes for the MaskedEditBox control based on the BorderStyle property.
- Provides details about the MaskedEditBox control's events related to its stylistic properties.
- Includes code examples in C# and VB.NET for enabling themes in the MaskedEditBox control.

## MaskedEditBox Control Themes

### Applying Themes

Themes can be applied to the MaskedEditBox control using the property given below.

| MaskedEditBox Property   | Description                                                                                   |
|--------------------------|-----------------------------------------------------------------------------------------------|
| ThemesEnabled            | Specifies whether or not to use XP themes when BorderStyle property is set to 'Fixed3D'. |

#### Note: Refer Border Settings topic to know about the BorderStyle property.

**C#**
```csharp
this.maskedEditBox1.ThemesEnabled = true;
```

**VB.NET**
```vbnet
Me.maskedEditBox1.ThemesEnabled = true
```

### Figure 549: Themes Applied to MaskedEditBox Control

![Themes Applied to MaskedEditBox Control](https://example.com/imageplaceholder.png)

## MaskedEditBox Events

The list of events and a detailed explanation about each of them is given in the following sections.

### Events and Their Descriptions

| MaskedEditBox Events       | Description                                                  |
|----------------------------|--------------------------------------------------------------|
| Border3DStyleChanged       | This event occurs when the Border3DStyle property is changed. |
| BorderColorChanged         | This event occurs when the BorderColor property is changed.   |
| BorderSidesChanged         | This event occurs when the BorderSides property is changed.   |
| BorderStyleChanged         | This event occurs when the Style property is changed.        |

## Additional Information
- The provided examples demonstrate how to enable ThemesEnabled in both C# and VB.NET.
- The events listed indicate changes to specific properties of the MaskedEditBox control.

### Localization and Accessibility
- The MaskedEditBox control supports localization through its properties.
- Ensure accessibility features are observed when customizing the control.

### See also:
- Border Settings
- MaskedEditBox Control Properties
- MaskedEditBox Design-Time Customization

<!-- tags: [toolkit, winforms, maskededitbox, event-handling, themes, application, control] keywords: [themesenabled, borderstyle, events, csharp, vb.net, syncfusion, 11.4.0.26] -->
```