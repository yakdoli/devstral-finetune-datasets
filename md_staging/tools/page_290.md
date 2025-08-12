```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_290.jpeg
document_name: tools
page_number: 290
page_id: tools#page_290
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section covers behavior settings related to AutoComplete controls in Windows Forms.
- Properties like `ShowCloseButton` and `ShowGripper` are detailed, along with their default values.
- Case sensitivity is explained through properties like `IgnoreCase` and `CaseSensitive`.

## Content

### Behavior Settings

#### Case Sensitivity
At run time, the string entered in a textbox (for example), can be made case sensitive using the below properties.

| **AutoComplete Properties** | **Description**                                                                 |
|-------------------------------|---------------------------------------------------------------------------------|
| IgnoreCase                   | Specifies whether to ignore case sensitivity for string comparison. Default value is true. |
| CaseSensitive                | Specifies if the replacement of the matching entry is to be case sensitive.                  |

The behavior of the AutoComplete dropdown can be customized by adjusting properties such as `ShowCloseButton` and `ShowGripper`.

#### Property: ShowGripper
- **Description**: Specifies whether to show a gripper at the bottom right of a DropDownContainer.
- **Default Value**: `true`

#### Note
The AutoComplete dropdown can be closed by calling `AutoComplete.CloseDropDown()` method.

```csharp
this.autoComplete1.ShowCloseButton = true;
this.autoComplete1.ShowGripper = true;
```

```vb
Me.autoComplete1.ShowCloseButton = True
Me.autoComplete1.ShowGripper = True
```

#### Case Sensitivity Settings
To adjust case sensitivity, the following properties can be used:

```csharp
this.autoComplete1.IgnoreCase = false;
this.autoComplete1.CaseSensitive = true;
```

```vb
Me.autoComplete1.IgnoreCase = False
```

## Footer
© 2013 Syncfusion. All rights reserved.

<!-- tags: [syncfusion, winforms, tools, autocomplete, behavior settings, case sensitivity, showclosebutton, showgripper, closedropdown, ignorecase, casesensitive] keywords: [autocompletetool, dropdowncontainer, casemismatch, runtimeoptions, caseinsensitivity, propertysettings, synced, winformscontrols] -->
```