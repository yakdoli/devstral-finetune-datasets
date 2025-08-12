```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: tools
page_number: 091
page_id: tools#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:53Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the `RightToLeft` property of the CommandBarController.
- Discusses the themes and visual styles settings for the CommandBar control.

## Content

### CommandBarController Property

| CommandBarController Property | Description |
|-------------------------------|-------------|
| RightToLeft                   | Gets a value indicating whether the control's elements are aligned from right to left. |

```csharp
[C#]
this.commandBarController1.RightToLeft = true;
```

```vb.net
[VB.NET]
Me.commandBarController1.RightToLeft = True
```

#### 3.3.3.8 Themes And Visual Styles

This section discusses the themes and visual styles settings of the CommandBar control.

##### 3.3.3.8.1 Themes

Themes define the look and feel of the CommandBar control. They can be set using the property given below.

| CommandBarController Property | Description |
|-------------------------------|-------------|
| ThemesEnabled                 | Specifies whether XP themes should be used for the CommandBars. |

```csharp
[C#]
this.commandBarController1.ThemesEnabled = true;
```

```vb.net
[VB.NET]
Me.commandBarController1.ThemesEnabled = True
```

![Themed Appearance of CommandBar Control](https://example.com/image_url.png)
*Figure 35: Themed Appearance of CommandBar Control*

## API Reference
- `ThemesEnabled` property with description of its purpose.

## Code Examples
- Examples provided for both C# and VB.NET to demonstrate how to enable themes for the CommandBar control.

## Cross References
- Referenced sections include the installation and configuration of themes in WinForms applications.

<!-- tags: [Syncfusion, WinForms, CommandBar, Themes, Visual Styles, RightToLeft, ThemesEnabled] keywords: [CommandBar, Themes, Visual Styles, RightToLeft, ThemesEnabled, C#, VB.NET, Control, Appearance] -->
```