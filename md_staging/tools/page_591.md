```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_591.jpeg
document_name: tools
page_number: 591
page_id: tools#page_591
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
The ComboBoxBase control is an advanced ComboBox that allows you to plug in any ListControl-derived class as the list for the combo box. It provides several improvements over the standard ComboBox control and contains various advanced features.

## Content

### ComboBoxBase Control
![Figure 363: ComboBoxBase Control](image_description_for_Figure_363.png)

- **Functionality**: With the ComboBoxBase, you can plug in any ListControl-derived class as the list for the list portion of the combo box using the ListControl property.
- **Customization**: This version of ComboBoxBase does not support any kind of owner drawing to customize painting. However, you could still use a ListControl that supports owner drawing.

#### See also
- [ComboBoxAdv](#)

### 3.5.5.3.1 Features

#### Overview
ComboBoxBase is an advanced ComboBox control that provides many improvements over the standard ComboBox control and contains the following features:

- **Any ListControl-derived controls can be displayed in the drop-down portion of ComboBoxBase.**
- **Supports AutoComplete.**
- **We can specify the external data source for ComboBoxBase control.**
- **It provides a FlatStyle mode that lets users draw the control flat or use XP Themes.**

## API Reference
This section provides a detailed reference of the key APIs related to the ComboBoxBase control.

### Namespace
- **Syncfusion.Windows.Forms.Tools**

### Class Members
- **ListControl Property**: Used to specify the ListControl-derived class for the list portion of the combo box.
- **FlatStyle Property**: Specifies whether the control should be drawn in a flat style or use XP Themes.

## Code Examples
Here are some example code snippets demonstrating the use of the ComboBoxBase control.

### Example 1: Binding a ListControl to ComboBoxBase
```csharp
// Creating an instance of the ComboBoxBase
ComboBoxBase comboBoxBase = new ComboBoxBase();

// Setting the ListControl property
ListControl listControl = new ListControl();
comboBoxBase.ListControl = listControl;
```

### Example 2: Specifying the External Data Source
```csharp
// Creating an instance of the ComboBoxBase
ComboBoxBase comboBoxBase = new ComboBoxBase();

// Setting the data source
comboBoxBase.DataSource = myExternalDataSource;
```

### Example 3: Enabling FlatStyle Mode
```csharp
// Creating an instance of the ComboBoxBase
ComboBoxBase comboBoxBase = new ComboBoxBase();

// Enabling FlatStyle mode
comboBoxBase.FlatStyle = FlatStyle.Flat;
```

## Page-level Navigation/TOC
- **_comboBoxBase Control**
  - Overview
  - Features
  - API Reference
  - Code Examples

## Cross References
- **Related Documentation**
  - ComboBoxAdv

<!-- tags: [ComboBoxBase, ListControl, FlatStyle, AutoComplete, Windows Forms, ComboBox, Data Source] keywords: [ComboBoxBase, ListControl integration, flat style mode, auto-complete, dropdown list, external data source] -->
```