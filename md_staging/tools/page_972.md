```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_972.jpeg
document_name: tools
page_number: 972
page_id: tools#page_972
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:40Z
fidelity: lossless
-->

## WinForms - Essential Tools for Windows Forms

### CheckBoxAdv Style Customization

The CheckBoxAdv control offers several styling options, including:
- Managed,
- Blue,
- Silver and
- Black.

The Style property should be set to "Office2007".

#### Code Examples

**C#**
```csharp
this.checkBoxAdv1.Style =
    Syncfusion.Windows.Forms.Tools.CheckBoxAdvStyle.Office2007;
this.checkBoxAdv1.Office2007ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Blue;
```

**VB**
```vb
Me.checkBoxAdv1.Style =
    Syncfusion.Windows.Forms.Tools.CheckBoxAdvStyle.Office2007
Me.checkBoxAdv1.Office2007ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Blue
```

### Visual Representation

![Figure 627: CheckBoxAdv Styles](checkerbox_styles.png)

**Figure 627: CheckBoxAdv Styles**

This figure illustrates the difference between the default style and the Office 2007 style for the CheckBoxAdv control.

## API Reference

### Properties
- **Style**: Determines the visual style of the CheckBoxAdv.
  - Type: `CheckBoxAdvStyle`
  - Default: `Default`
  - Values: Framework, Office2007, Office2007ColorScheme
  - Office2007ColorScheme: Blue, Silver, Black

### Methods
- **ApplyTheme**: Applies the specified theme to the CheckBoxAdv control.
  - Parameters: 
    - `theme`: The Office2007Theme (Blue, Silver, Black)

### Events
- **StyleChanged**: Triggered when the style of the CheckBoxAdv control changes.

## Page-level Navigation/TOC
- Overview
- CheckBoxAdv Style Customization
- Visual Representation
- API Reference

## Cross References
See also:
- [Syncfusion Windows Forms Controls](#)
- [Syncfusion Office Themes](#)

<!-- tags: [Syncfusion Winforms, CheckBoxAdv, Office2007, Style, ColorScheme, VB, C#] keywords: [checkboxadv, office2007, style, colorscheme, theme, managed, blue, silver, black] -->
```