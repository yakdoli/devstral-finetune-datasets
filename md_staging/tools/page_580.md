```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_580.jpeg
document_name: tools
page_number: 580
page_id: tools#page_580
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:05Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the application of predefined and custom colors to `ComboBoxAdv` controls using Office2007ColorTheme.
- Provides details on overriding theme backgrounds with `BackColor` using the `IgnoreThemeBackground` property.

## Content

### Figure 358: Blue, Silver and Black OfficeColorSchemes
![](image.png)

#### Custom Colors
We can also apply custom colors to the `ComboBoxAdv` control by setting `Office2007ColorTheme` to "Managed" and specifying the custom color through the `ApplyManagedColors` method as follows.

- **C#**
```csharp
this.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyResources(this, Color.Orchid);
```
- **VB.NET**
```vb
Me.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyResources(Me, Color.Orchid)
```

#### Figure 359: Custom Color = "Orchid"
![](image.png)

### 3.5.5.2.3.4.3 Background Settings

When `ComboBoxAdv` control is set with some style, theme background will be drawn. We can override this background with `BackColor` property using the `IgnoreThemeBackground` property. When this `IgnoreThemeBackground` is set to `true`, the control will ignore the theme background and draw the backcolor as the background.

- **C#**
```csharp
// Code snippet to represent the background setting override
```

### Footer
© 2013 Syncfusion. All rights reserved.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms
- **Class:** `ComboBoxAdv`
- **Properties:**
  - `Office2007ColorTheme`: Manages the color theme applied to the control.
  - `BackColor`: Sets the background color of the control.
  - `IgnoreThemeBackground`: Boolean property to override the theme background.

### Code Examples
- **Setting Custom Colors**
  ```csharp
  this.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
  Office2007Colors.ApplyResources(this, Color.Orchid);
  ```

- **Overriding Background with BackColor**
  ```csharp
  this.comboBoxAdv1.IgnoreThemeBackground = true;
  this.comboBoxAdv1.BackColor = Color.CustomColor;
  ```

## RAG Annotations
<!-- tags: WinForms, ComboBoxAdv, Office2007ColorTheme, Managed, ApplyManagedColors, BackColor, IgnoreThemeBackground, SyncfusionWinForms, version:11.4.0.26 keywords: CustomColors, BackgroundSettings, colorTheme, themeOverride, controlCustomization -->
```
