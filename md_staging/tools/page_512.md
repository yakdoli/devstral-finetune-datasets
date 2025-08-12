```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_512.jpeg
document_name: tools
page_number: 512
page_id: tools#page_512
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:17:47Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section explains how to set the default tab text of the ColorGroups in a Windows Forms application using the ColorUIControl properties.
- Provides methods to customize and reset the tab names for Custom, Standard, System, and User colors.

## Content

### 3.5.4.1.3.2 Tab Text

The default tab text of the ColorGroups can be set using the below properties.

| ColorUIControl Properties | Description |
|---------------------------|-------------|
| CustomTabName            | Set the text displayed on the custom colors tab. The tab name can be reset using ResetCustomTabName() method. |
| StandardTabName          | Set the text displayed on the Standard colors tab. The tab name can be reset using ResetStandardTabName() method. |
| SystemTabName           | Set the text displayed on the System colors tab. The tab name can be reset using ResetSystemTabName() method. |
| UserTabName             | Set the text displayed on the User colors tab. The tab name can be reset using ResetUserTabName() method. |

#### Code Examples

**[C#]**
```csharp
this.colorUIControl1.StandardTabName = "Web Layout";
this.colorUIControl1.SystemTabName = "System Colors";
this.colorUIControl1.UserTabName = "User Defined";
this.colorUIControl1.CustomTabName = "Palettes";
```

**[VB.NET]**
```vb
Me.colorUIControl1.StandardTabName = "Web Layout"
Me.colorUIControl1.SystemTabName = "System Colors"
Me.colorUIControl1.UserTabName = "User Defined"
Me.colorUIControl1.CustomTabName = "Palettes"
```

## API Reference

- **CustomTabName**: Property to set the text displayed on the custom colors tab.
- **StandardTabName**: Property to set the text displayed on the Standard colors tab.
- **SystemTabName**: Property to set the text displayed on the System colors tab.
- **UserTabName**: Property to set the text displayed on the User colors tab.
- **ResetCustomTabName()**: Method to reset the custom tab name.
- **ResetStandardTabName()**: Method to reset the Standard tab name.
- **ResetSystemTabName()**: Method to reset the System tab name.
- **ResetUserTabName()**: Method to reset the User tab name.

<!-- tags: [Syncfusion Winforms, colorUIControl, tabText, tab customization] keywords: [CustomTabName, StandardTabName, SystemTabName, UserTabName, ResetCustomTabName(), ResetStandardTabName(), ResetSystemTabName(), ResetUserTabName()] -->
```