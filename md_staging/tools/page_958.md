```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_958.jpeg
document_name: tools
page_number: 958
page_id: tools#page_958
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:15Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses CheckBoxAdv Values and Image Settings in Windows Forms.
- Focuses on associating values with different check states of a CheckBoxAdv control.
- Details properties for handling integer and string values for checked, unchecked, and indeterminate states.
- Includes sample C# code demonstrating the setup of these properties.

## Content

### 3.5.11.1.3.1.2 CheckBoxAdv Values

This section discusses how values can be associated with the various check states.

Both integer and string values can be associated with the check states as follows.

| **CheckBoxAdv Properties** | **Description** |
|----------------------------|-----------------|
| CheckedInt                | Specifies the integer value when checked. |
| CheckedString             | Specifies the string value when checked. |
| IndeterminateInt          | Specifies the integer value when indeterminate. |
| IndeterminateString       | Specifies the string value when indeterminate. |
| UncheckedInt              | Specifies the integer value when Unchecked. |
| UncheckedString           | Specifies the string value when Unchecked. |
| StringValue               | Gets or sets the string value. |
| BoolValue                 | Gets / sets a value indicating the check state. This property can be set to use bool values for databinding. Refer Frequently Asked Questions section. |
| IntValue                  | Gets / sets the int value. Refer Frequently Asked Questions section. |

### Code Examples

```csharp
this.checkBoxAdv1.CheckedInt = 3;
this.checkBoxAdv1.CheckedString = "CheckBoxAdv is Checked";
this.checkBoxAdv1.IndeterminateInt = 5;
this.checkBoxAdv1.IndeterminateString = "CheckBoxAdv is Indeterminate";
this.checkBoxAdv1.UncheckedInt = 3;
this.checkBoxAdv1.UncheckedString = "CheckBoxAdv is Unchecked";
this.checkBoxAdv1.StringValue = "String";
this.checkBoxAdv1.IntValue = 5;
this.checkBoxAdv1.BoolValue = true;
```

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [Windows Forms, CheckBoxAdv, checked, unchecked, indeterminate, checkedint, checkedstring, Boolean values, integer values, String values, Syncfusion] -->
```