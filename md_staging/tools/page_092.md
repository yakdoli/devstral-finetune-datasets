```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_092.jpeg
document_name: tools
page_number: 092
page_id: tools#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to enhance the appearance of the CommandBar control using visual styles.
- Demonstrates setting the visual style of the CommandBar using the `Style` property.
- Provides examples in both C# and VB.NET for enabling themes and setting the style.

## Content

### 3.3.3.8.2 Visual Styles

Visual Styles enhance the appearance of the CommandBar control and can be set using the property given below.

| **CommandBarController Property** | **Description**                                                                 |
|------------------------------------|--------------------------------------------------------------------------------|
| Style                             | Specifies the visual style of the CommandBar. It includes the options given below. <br> <br> - OfficeXP, <br> - Office2003, <br> - Office2007, <br> - VS2005 and <br> - Office2007Outlook. |

#### C#

```csharp
this.commandBarController1.ThemesEnabled = true;
this.commandBarController1.Style = Syncfusion.Windows.Forms.VisualStyle.OfficeXP;
```

#### VB.NET

```vb
Me.commandBarController1.ThemesEnabled = True
Me.commandBarController1.Style = Syncfusion.Windows.Forms.VisualStyle.OfficeXP
```

<!-- tags: [windows forms, commandbar, visual styles] keywords: [commandbarcontroller, themes, visualstyle, office, outlook] -->
```