```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_292.jpeg
document_name: tools
page_number: 292
page_id: tools#page_292
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:03:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the size settings of the AutoCompletePopup control.
- Explains how to control the height and width of the AutoCompletePopup.
- Provides details on the properties affecting the AutoComplete control's display.

## Content

### Size Settings

The properties which can control the height and width of the AutoCompletePopup are as follows.

| AutoComplete Properties             | Description                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| AdjustHeightToltemCount            | Specifies if the height of the drop down should be adjusted automatically, based on the number of items.                               |
| AutoPersistentDropDownSize          | The Dropdown size of Autocomplete control is automatically persistent when this property is set to true.                             |
| PreferredHeight                    | Specifies preferred height for the drop down displayed by the AutoComplete control when `AdjustHeightToltemCount` property is false.<br>Default value is 200. |
| PreferredWidth                     | Specifies preferred width for the drop down displayed by the AutoComplete control when `AdjustHeightToltemCount` property is false.<br>Default value is -1. |

#### Examples

**[C#]**
```csharp
this.autoComplete1.AdjustHeightToItemCount = false;
this.autoComplete1.AutoPersistentDropDownSize = true;
this.autoComplete1.PreferredHeight = 100;
this.autoComplete1.PreferredWidth = 300;
```

**[VB.NET]**
```vb
Me.autoComplete1.AdjustHeightToItemCount = False
Me.autoComplete1.AutoPersistentDropDownSize = True
Me.autoComplete1.PreferredHeight = 100
Me.autoComplete1.PreferredWidth = 300
```

### Notes on Usage

- When `AdjustHeightToltemCount` is false, the `PreferredHeight` and `PreferredWidth` properties will determine the size of the drop-down.
- Setting `AutoPersistentDropDownSize` to true ensures that the dropdown size is consistently preserved.

## Cross References
- **See Also**
  - Source for AutoComplete Control, External Datasource

<!-- tags: [tools, windows forms, autocomplete, size settings, auto-complete, dropdown, dimensions] keywords: [AutoCompleteControl, AdjustHeight, PreferredHeight, AutoPersistent, PreferredWidth] -->
```