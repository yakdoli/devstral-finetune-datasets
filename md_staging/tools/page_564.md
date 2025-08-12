```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_564.jpeg
document_name: tools
page_number: 564
page_id: tools#page_564
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:00Z
fidelity: lossless
-->

## Overview

- This section introduces ComboBoxAdv, an advanced ComboBox control with various features, including 3D and flat styles, image display, AutoComplete functionality, external data binding, and customizable visual styles.
- Describes how to create and configure ComboBoxAdv both visually through the designer and programmatically using code samples.
- Highlights the flexibility and enhanced functionality of ComboBoxAdv over standard ComboBox controls in Windows Forms.

## Content

### Features

**ComboBoxAdv** is an advanced ComboBox control and contains the following features:

- We can set 3D border styles and flat styles for the ComboBoxAdv control.
- We can set images for ComboBoxAdv control items.
- AutoComplete functionality can be provided.
- We can bind the ComboBoxAdv to any external datasource. See **DataBinding**.
- You can set visual styles to enrich your application with the standard look and feel.

**See Also**

- [Concepts and Features](Concepts and Features)

### Creating ComboBoxAdv

**[3.5.5.2.2 Creating ComboBoxAdv]**

ComboBoxAdv is available to the designer by just dragging and dropping from the toolbox onto the form.

![Figure 348: ComboBoxAdv in Toolbox](https://i.imgur.com/INSERT_IMAGE_URL.png)

**It can be created programmatically as follows.**

1. **Include the required namespace.**

    ```csharp
    using Syncfusion.Windows.Forms.Tools;
    ```

    ```vb.net
    [VB.NET]
    ```

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Tools
- **Control:** ComboBoxAdv
- **Features:**
    - **Border Styles:** 3D and flat styles.
    - **Images:** Support for images in control items.
    - **AutoComplete:** Provider functionality for dropdown items.
    - **DataBinding:** Integration with external datasources.
    - **Visual Styles:** Customizable themes for a standardized look and feel.

## Code Examples

### Programmatic Creation

```csharp
using Syncfusion.Windows.Forms.Tools;

// Example of creating ComboBoxAdv programmatically
ComboBoxAdv comboBoxAdv = new ComboBoxAdv();
form.Controls.Add(comboBoxAdv);
comboBoxAdv.DropDownStyle = ComboBoxStyle.DropDown;
comboBoxAdv.Items.Add("Item 1");
comboBoxAdv.Items.Add("Item 2");
comboBoxAdv.AutoCompleteSource = AutoCompleteSource.ListItems;
comboBoxAdv.AutoCompleteMode = AutoCompleteMode.SuggestAppend;
```

<!-- tags: [winforms, comboboxadv, advanced combobox, visual studio toolbox, data binding, autocomplete, syncfusion, version 11.4.0.26] keywords: [comboxadv, winforms, visual styles, programmatically, data binding, auto complete] -->
```