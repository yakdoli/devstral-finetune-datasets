```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_927.jpeg
document_name: tools
page_number: 927
page_id: tools#page_927
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

| AutoCompleteSource            | Specifies the source of the complete strings used for auto completion. DropDownStyle property should be set to "DropDown" to make this setting effective. |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AutoCompleteCustomSource      | Represents the collection of string for the custom source, when AutoCompleteSource is set to CustomSource.                                                                                          |

## Overview

- Explains how to configure the auto-complete feature for combo boxes in Windows Forms.
- Demonstrates setting properties like `AutoCompleteMode`, `AutoCompleteSource`, and `AutoCompleteCustomSource`.
- Provides code examples in both C# and VB.NET.

## Content

### AutoComplete Feature Configuration

#### C#

```csharp
// Enables AutoComplete feature.
this.fontComboBox1.UseAutoComplete = true;
this.fontComboBox2.AutoCompleteCustomSource.AddRange(new string[] { 
    "Calibri", "Cambria", "Candara" 
});
this.fontComboBox2.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.SuggestAppend;
this.fontComboBox2.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.CustomSource;
```

#### VB.NET

```vb
' Enables AutoComplete feature.
Me.fontComboBox1.UseAutoComplete = True
Me.fontComboBox2.AutoCompleteCustomSource.AddRange(New String() { 
    "Calibri", "Cambria", "Candara" 
})
Me.fontComboBox2.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.SuggestAppend
Me.fontComboBox2.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.CustomSource
```

### Example Screenshot

![Figure 592: AutoCompleteMode = "SuggestAppend"; AutoCompleteSource = "CustomSource"](attachment://screenshot.png)

---

## Cross References

- [DropDown Settings]

---

<!-- tags: [syncfusion, windows forms, combobox, auto-complete, suggestsappend, customsource] keywords: [AutoCompleteMode, AutoCompleteSource, AutoCompleteCustomSource, C#, VB.NET] -->
```