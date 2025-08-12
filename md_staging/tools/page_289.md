```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_289.jpeg
document_name: tools
page_number: 289
page_id: tools#page_289
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:03:21Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### AutoComplete Properties

| **AutoComplete Properties**   | **Description**                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------------------|
| AutoAddItem                   | Specifies whether the current item in the target control is to be automatically added during validation, when the ENTER key is pressed. |

**Note:** The header will be shown only for the text that is saved at run time. Set AutoCompleteMode and AutoCompleteSource properties to None.

#### C#

```csharp
this.autoCompletel.AutoAddItem = true;
this.autoComplete2.ShowColumnHeader = true;
this.autoCompleteDataColumnInfo1.ColumnHeaderText = "Contents";
```

#### VB.NET

```vb.net
Me.autoCompletel.AutoAddItem = True
Me.autoComplete2.ShowColumnHeader = True
Me.autoCompleteDataColumnInfo1.ColumnHeaderText = "Contents"
```

**Fig 122:** DropDownItem with ColumnHeaderText = "Contents"

**Note:** You can also set multiple columns. Refer **Multiple Columns** to know more.

### Close Button and Gripper Settings

Visibility of close button and the gripper in the popup can be determined by ShowCloseButton and ShowGripper properties.

| **AutoComplete Properties** | **Description**                                                                 |
|---------------------------|-------------------------------------------------------------------------------|
| ShowCloseButton            | Specifies whether to show the CloseButton at the bottom right of the DropDownContainer. |

## Footer

Ⓒ 2013 Syncfusion. All rights reserved.
<!-- tags: [Syncfusion Winforms, AutoComplete, AutoComplete Properties, DropDownItem, Close Button, Gripper, ColumnHeaderText, Multiple Columns, ShowCloseButton, ShowGripper] keywords: [AutoAddItem, AutoComplete, CloseButton, Gripper, ColumnHeaderText, Multiple Columns, ShowCloseButton, ShowGripper] -->
```