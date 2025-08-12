```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_571.jpeg
document_name: tools
page_number: 571
page_id: tools#page_571
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:48Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Explains the configuration and usage of the ComboBoxAdv control.
- Demonstrates setting properties like `DropDownWidth`, `MaxDropDownItems`, and `Sorted`.
- Provides guidance on data settings and dropdown styles.

## Content

### Properties Configuration

#### Figure 351: DropDownWidth = "150"; MaxDropDownItems = "6"; Sorted = "True"

![](attachment://image.png)
*Figure 351: DropDownWidth = "150"; MaxDropDownItems = "6"; Sorted = "True"*

#### Notes

- **Note:** Data for the dropdown can be set using the `Items` property. Refer to **Data Settings** for details.
  
  ```markdown
  Data Settings
  ```

- **Note:** To know about different dropdown styles available for the control, see the **ReadOnly Settings** section in the **TextBox** topic.

  ```markdown
  ReadOnly Settings in TextBox topic.
  ```

## See Also

- **TextBox, Image Settings**
- **3.5.5.2.3.2 Data Settings**

## Data Settings for ComboBoxAdv

Data for the ComboBoxAdv is added through the String Collection Editor, which is invoked through the `ComboBoxAdv.Items` property.

## API Reference

### Properties
- **ComboBoxAdv.Items**
  - **Type:** String Collection
  - **Description:** Used to add items to the ComboBoxAdv control.
  - **Invocation:** Invoked through the `ComboBoxAdv.Items` property.

## Code Examples

### Example 1: Configuring ComboBoxAdv

```csharp
// Example code for configuring ComboBoxAdv
ComboBoxAdv comboBox = new ComboBoxAdv();
comboBox.DropDownWidth = 150;
comboBox.MaxDropDownItems = 6;
comboBox.Sorted = true;

// Adding items using the Items property
comboBox.Items.Add("April");
comboBox.Items.Add("August");
comboBox.Items.Add("December");
comboBox.Items.Add("February");
comboBox.Items.Add("January");
comboBox.Items.Add("July");
```

## RAG Annotations

```plaintext
tags: [ComboBoxAdv, Data Settings, ReadOnly Settings, Windows Forms] 
keywords: [DropDownWidth, MaxDropDownItems, Sorted, Textbox, Image Settings]
```
```