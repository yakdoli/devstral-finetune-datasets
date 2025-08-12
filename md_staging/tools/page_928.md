<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_928.jpeg
document_name: tools
page_number: 928
page_id: tools#page_928
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:05Z
fidelity: lossless
-->

## Overview

- FontComboBox provides properties to control the appearance and behavior of the dropdown, including DropDownStyle, DropDownHeight, DropDownWidth, and MaxDropDownItems. These properties determine the style, dimensions, and list visibility of the dropdown.

## Content

FontComboBox has properties to control the appearance and behavior of the dropdown.

### Properties and Their Descriptions

| Properties          | Description                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------------------|
| DropDownStyle       | Specifies the style of the dropdown. The options are:<br><br> - DropDownList - The user cannot directly edit the text portion. The user must click the arrow button to display the list portion.<br> - DropDown (default) - The user can directly edit the text portion. The user must click the arrow button to display the list portion.<br> - Simple - The text portion is editable. The list portion is always visible. |
| DropDownHeight      | Specifies the height of the dropdown combo box in pixels.                                                  |
| DropDownWidth       | Specifies the width of the dropdown combo box in pixels.                                                    |
| MaxDropDownItems    | Indicates the maximum number of entries to display in the dropdown list.                                    |

### Code Examples

#### C#

```csharp
this.fontComboBox2.DropDownHeight = 107;
this.fontComboBox2.DropDownStyle = 
    System.Windows.Forms.ComboBoxStyle.DropDownList;
this.fontComboBox2.DropDownWidth = 154;
this.fontComboBox2.MaxDropDownItems = 10;
```

#### VB.NET

```vb
Me.fontComboBox2.DropDownHeight = 107
Me.fontComboBox2.DropDownStyle = 
    System.Windows.Forms.ComboBoxStyle.DropDownList
Me.fontComboBox2.DropDownWidth = 154
Me.fontComboBox2.MaxDropDownItems = 10
```

## RAG Annotations

<!-- tags: [FontComboBox, dropdown, WinForms] keywords: [DropDownStyle, DropDownHeight, DropDownWidth, MaxDropDownItems] -->