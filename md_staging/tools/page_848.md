```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_848.jpeg
document_name: tools
page_number: 848
page_id: tools#page_848
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:31Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Me.maskedEditBox1.PasswordChar = "$"c
End Sub
```

---

## Overview
- Demonstrates the `PasswordChar` property of the `MaskedEditBox` control.
- Provides working sample code and path to a sample installation.

### Figure 540: '$' Character displayed Sequentially
- This figure shows the sequential display of the '$' character in the `MaskedEditBox`.

## Sample Availability
- A Sample which demonstrates the `PasswordChar` property of `MaskedEditBox` control is available in the below sample installation path:
  ```
  ..My Documents\Syncfusion\EssentialStudio\Version Number
  Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls
  ```

---

### 3.5.8.8.3.4 Culture Settings
This section discusses the culture settings of the `MaskedEditBox` control.

| MaskedEditBox Properties          | Description                                                                                   |
|-----------------------------------|-----------------------------------------------------------------------------------------------|
| **Culture**                       | Gets / sets the culture that is to be used for formatting the numeric display.              |
| **SpecialCultureValue**           | Gets / sets the mode for the cultures.                                                        |
|                                   | It includes the below given options:                                                          |
|                                   | None,                                                                                         |
|                                   | CurrentCulture,                                                                              |
|                                   | UiCulture and                                                                                |
|                                   | InstalledCulture.                                                                            |
| **UseUserOverride**               | Specifies if the `NumberFormatInfo` used for formatting will use the User Overrides for the culture. The default value is set to 'True'. |

---

### Code Example

```csharp
[C#]
this.maskedEditBox1.Culture = new System.Globalization.CultureInfo("ar-SA");
```

---

## Page-level Navigation/TOC (if applicable)
- This section describes the culture settings of the `MaskedEditBox` control, including relevant properties and their descriptions.

## Cross References
See also: 
- `PasswordChar` property
- `MaskedEditBox` control
- Sample installation path

## RAG Annotations
<!-- tags: [winforms, maskededitbox, culture, passwordchar, syncfusion, essentialsdk] keywords: [language, culture, passwordchar, maskededitbox, sample installation, numeric formatting, property description] -->
```