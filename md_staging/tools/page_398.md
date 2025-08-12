```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_398.jpeg
document_name: tools
page_number: 398
page_id: tools#page_398
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:21Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to configure the Calculator control's themes and button styles in a Windows Forms application.
- Demonstrates disabling themes and enabling button styles with code examples in C# and VB.NET.
- Lists supported button styles for the Calculator control.

## Content

### Themes for the Calculator control

**Themes for the Calculator control** is themed by default. To disable themes, set the `ThemesEnabled` property to `false`.

#### Example Code: Disabling Themes

##### C#
```csharp
this.calculatorControl1.ThemesEnabled = false;
```

##### VB.NET
```vb.net
Me.calculatorControl1.ThemesEnabled = False
```

#### Figure 200: Calculator Control Without Themes
![](Figure 200: Calculator Control Without Themes)

**Button Styles**

The Calculator control supports different button styles. The `UseVisualStyle` property should be set to `true` to enable button styles for the control.

- Classic (default)
- Office2000
- WindowsXP
- OfficeXP
- Office2003
- Office2007

<!-- tags: [syncfusion, winforms, calculator control, themes, button styles, visual styles, interface customization] keywords: [themesEnabled, useVisualStyle, classic, office2000, windowsXP, officeXP, office2003, office2007] -->
``` 
