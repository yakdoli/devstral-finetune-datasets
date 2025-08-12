```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_139.jpeg
document_name: edit
page_number: 139
page_id: edit#page_139
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:28Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates the usage of the Syncfusion EditControl in a Windows Forms application.
- Explains how to use the Find, Replace, and Goto functionalities within the EditControl.
- Details the various methods provided for text search and replacement operations.

## Content

### 4.6.4 Find, Replace and Goto

The Edit Control supports text search and replace functionalities through the use of the `FindText` and `ReplaceText` methods. There are also other useful methods like `FindCurrentText`, `FindNext`, and `ReplaceAll` that assist in this purpose.

#### Code Example

```csharp
using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using System.IO;

using Syncfusion.Windows.Forms.Edit;
using Syncfusion.Windows.Forms.Edit.Dialogs;
using Syncfusion.Windows.Forms.Edit.Implementation;
using Syncfusion.Windows.Forms.Edit.Interfaces;
using Syncfusion.Windows.Forms.Edit.Enums;

namespace EditControlDemo
{
    // ...
}
```

#### Table: Edit Control Methods and Descriptions

| Edit Control Method | Description |
| --- | --- |
| FindText | Finds the first occurrence of the specified text as per the conditions specified like match case, match whole word, search hidden text, and search up. |
| FindRange | Searches for the given string in the text of the control and returns the text range of the first found occurrence. |
| FindRegex | Looks for the specified expression in the text. |
| ReplaceText | Replaces the first occurrence of the specified text with the replacement text as per the conditions specified like match case, match whole word, search hidden text, and search up. |

### Summary

This section introduces the `EditControlDemo` namespace and highlights the essential methods for performing text search and replacement operations within the Edit Control. It provides a brief overview of the available functionalities and their purposes, helping developers to effectively utilize the Syncfusion Edit Control for advanced text manipulation tasks in Windows Forms applications.

#### Page-level Navigation/TOC (Local)
- 4.6.4 Find, Replace and Goto

### Cross References
- See also: FindText, ReplaceText, FindCurrentText, FindNext, ReplaceAll, Syncfusion Edit Control

### Code Examples
- Demonstrates usage of namespaces and imports necessary for working with the Syncfusion Edit Control in a Windows Forms application.

### RAG Annotations
<!-- tags: [windows-forms, edit-control, find-replace, syncfusion, version:11.4.0.26] keywords: [editcontrol, findtext, replacetext, findrange, findregex, findcurrenttext, findnext, replaceall, windows forms] -->
```