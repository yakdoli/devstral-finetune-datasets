```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_971.jpeg
document_name: tools
page_number: 971
page_id: tools#page_971
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:46:28Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### CheckBoxAdv Property

| CheckBoxAdv Property | Description |
|-----------------------|-------------|
| ThemesEnabled         | Specifies whether themes are enabled for CheckBoxAdv. |

### ThemesEnabled Property Example

- **C#[ ]**

  ```csharp
  this.checkBoxAdv1.ThemesEnabled = true;
  ```

- **VB[ ]**

  ```vb
  Me.checkBoxAdv1.ThemesEnabled = True
  ```

#### Visual Representation

![Figure 626: ThemesEnabled property Set](./checkboxadv_themes_set.png)
*Figure 626: ThemesEnabled property Set*

### Visual Styles

The appearance of the CheckBoxAdv control can be customized using the various options provided by the following properties.

#### CheckBoxAdv Properties

| CheckBoxAdv Properties | Description |
|-------------------------|-------------|
| Style                   | Gets / sets an advanced appearance for the CheckBoxAdv. <br><br> The options included are as follows. <br><br> `Default` <br> `Office2007` |
| Office2007ColorScheme   | Gets / sets Office 2007 color scheme. <br><br> The options included are as follows. |

---

## API Reference

### Style Property

- **Description**: Gets / sets an advanced appearance for the CheckBoxAdv.
- **Options**: 
  - `Default`
  - `Office2007`

### Office2007ColorScheme Property

- **Description**: Gets / sets Office 2007 color scheme.
- **Options**: To be determined.

---

## Code Examples

### Example for Style Property (C#)

```csharp
// Setting the advanced appearance to Office2007
this.checkBoxAdv1.Style = Syncfusion.Windows.Forms.Tools.CheckBoxAdvStyle.Office2007;
```

### Example for Office2007ColorScheme Property (C#)

```csharp
// Setting the Office 2007 color scheme
this.checkBoxAdv1.Office2007ColorScheme = Syncfusion.Windows.Forms.Tools.Office2007Schemes.BlueMetallic;
```

---

<!-- tags: [WinForms, CheckBoxAdv, Themes, Style, Office2007ColorScheme] keywords: [Syncfusion Winforms, CheckBoxAdv, ThemesEnabled, Office2007, visual styles, appearance customization, Office 2007 theme] -->
```