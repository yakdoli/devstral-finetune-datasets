```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_366.jpeg
document_name: tools
page_number: 366
page_id: tools#page_366
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page covers setting up ForeColor for ButtonEdit controls, pointing out child button settings, and modifying text casing with ButtonEdit properties.
- Demonstrates how to achieve custom styling and functionality for ButtonEdit controls in the Windows Forms environment.

## Content

### Foreground Settings for ButtonEdit
```csharp
Me.buttonEdit3.ForeColor = Color.SteelBlue
```

**Note**: Foreground settings for the child buttons can be specified using `ButtonEditChildButton.Font` and `ButtonEditChildButton.ForeColor` properties.

![Figure 176: Foreground Text of Child Button Overriding ButtonEdit Foreground Settings](https://example.com/image.png)

**Figure 176: Foreground Text of Child Button Overriding ButtonEdit Foreground Settings**

### Case Settings

#### Using `ButtonEdit.CharacterCasing` Property
Using the `ButtonEdit.CharacterCasing` property, we can specify whether the case of the character can be modified as they are typed. The values are:
- `Upper`
- `Lower`
- `Normal`

```csharp
[C#]
this.buttonEdit3.Font = new System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Regular);
this.buttonEdit3.ForeColor = Color.SteelBlue;
```

```vbnet
[VB.NET]
Me.buttonEdit3.Font = New System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Regular)
Me.buttonEdit3.ForeColor = Color.SteelBlue
```

**Note**: This case setting can be overridden by the `TextBox.CharacterCasing` property.

### See Also
- **TextBox Settings for ButtonEdit**
- **3.5.2.2.3.2 Child Button Customization**

The child buttons in a ButtonEdit control are normal Windows buttons, but they support additional features within our ButtonEdit control. These features are discussed in the following topics:

#### 3.5.2.2.3.2.1 Button Types and Border Styles
- **Button Types**: The ButtonEdit control supports various types of buttons, including custom styles and appearances.
- **Border Styles**: The button borders can be customized to fit different design needs.

---

## API Reference

- **Properties**
  - **ButtonEdit.CharacterCasing**: Specifies the casing for the text entered in the control.
  - **ButtonEdit.ChildButton**:
    - **ButtonEditChildButton.Font**: Gets or sets the font of the child button.
    - **ButtonEditChildButton.ForeColor**: Gets or sets the foreground color of the child button.

## Code Examples

### C# Example
```csharp
buttonEdit3.Font = new System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Regular);
buttonEdit3.ForeColor = Color.SteelBlue;
```

### VB.NET Example
```vbnet
Me.buttonEdit3.Font = New System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Regular)
Me.buttonEdit3.ForeColor = Color.SteelBlue
```

---

## Page-level Navigation/TOC
- **Foreground Settings for ButtonEdit**
- **Case Settings**
  - Using `ButtonEdit.CharacterCasing` Property
- **See Also**
  - TextBox Settings for ButtonEdit
  - Child Button Customization
  - Button Types and Border Styles

## Cross References
- **Related Topics**:
  - Child Button Customization
  - Button Types and Border Styles

<!-- tags: [Syncfusion Winforms, ButtonEdit, Foreground Settings, CharacterCasing, TextBox, ChildButton, Button Styles] keywords: [Windows Forms, ButtonEdit, ForeColor, ChildButton, CharacterCasing, TextBox, Button Styles] -->
```
