```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_573.jpeg
document_name: tools
page_number: 573
page_id: tools#page_573
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:20:39Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### ComboBoxAdv Control Features

#### Overview
- Discusses the dropdown items for the ComboBoxAdv control.
- Explains how to set images for dropdown items.
- Describes advanced features such as auto-complete support and external data binding.

### ComboBoxAdv Control Dropdown Items

**Figure 353: DropDown Items for ComboBoxAdv Control**

Note: ComboBoxAdv can also be bound to an external Data source like Data Table. Refer Databinding topic.

#### Setting Images for Dropdown Items
To set images for dropdown items, refer to the **Image settings** topic.

### Advanced Features

#### 3.5.5.2.3.3 Advanced Features
This section will discuss the auto-complete support available for the ComboBoxAdv control and databinding using an external source.

#### 3.5.5.2.3.3.1 AutoComplete Support

**AutoComplete Support**

The ComboBoxAdv has built-in support for auto-completion of the text entered in the control. This feature is automatically enabled for the control. To disable, set the `ComboBoxAdv.AutoComplete` property to `false`.

#### ComboBoxAdv Properties

| ComboBoxAdv Properties                  | Description                                                                                                                                                                                                                                                                                  |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CaseSensitiveAutoComplete               | Specifies whether the search in the AutoComplete is case sensitive.                                                                                                                                                                  |
| MatchFirstCharacterOnly                | Specifies the AutoComplete behavior in the dropdown mode. When set to `true`, it will match the first character in the drop list and returns the matching result. |

#### Code Examples

##### C#

```csharp
this.comboBoxAdv1.AutoComplete = true;
this.comboBoxAdv1.CaseSensitiveAutocomplete = true;
this.comboBoxAdv1.MatchFirstCharacterOnly = true;
```

##### VB.NET

No VB.NET code example provided.

---

### Footer

© 2013 Syncfusion. All rights reserved.

Page 573
```