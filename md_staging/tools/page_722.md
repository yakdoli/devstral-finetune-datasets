```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_722.jpeg
document_name: tools
page_number: 722
page_id: tools#page_722
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:48Z
fidelity: lossless
-->



## Introduction to Office2007 Visualization Styles for Windows Forms

Syncfusion provides extensive theming options for Windows Forms, allowing developers to customize the appearance of controls to match Office 2007 themes or XP themes. This guide walks through setting different Office 2007 theme color schemes and enabling XP themes for the `DomainUpDownExt` control.

### Setting Office2007 Themes

#### C# Code Example

```csharp
this.domainUpDownExt1.ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Silver;
// To set Black Color scheme.
this.domainUpDownExt1.ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Black;
```

#### VB.NET Code Example

```vb
' Sets the Office2007 Visual Style.
Me.domainUpDownExt1.ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Silver
' To set Black Color scheme.
Me.domainUpDownExt1.ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Black
```

#### Available Themes

- **Silver**
- **Blue**
- **Black**

### Setting Office2007 Color Schemes

Figure 452: DomainUpDownExt Office 2007 Themes

![Figure 452: DomainUpDownExt Office 2007 Themes](https://i.imgur.com/image452.png)

It also provides support for XP Themes look and feel.

#### C# Code Example

```csharp
// Enable Themes.
this.domainUpDownExt1.ThemesEnabled = true;
```

#### VB.NET Code Example

```vb
' Enable Themes.
Me.domainUpDownExt1.ThemesEnabled = True
```

### XP Theme Support

Figure 453: DomainUpDownExt XP Themes

![Figure 453: DomainUpDownExt XP Themes](https://i.imgur.com/image453.png)

#### Available XP Themes

- **XP Themes - Blue**
- **XP Themes - Silver**
- **XP Themes - Olive Green**

### Summary of XP Themes

It also provides support for XP Themes look and feel, with additional themes available for customization.

#### Available XP Themes

- **Blue**
- **Silver**
- **Olive Green**
```

<!-- tags: [syncfusion, windowsforms, theming, controls, office2007theme, xpthemes] keywords: [domainupdownext, office2007, theming, themes, user interface design, customization, silver, blue, black, xp themes, styling] -->
```