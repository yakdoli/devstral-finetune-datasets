```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_468.jpeg
document_name: tools
page_number: 468
page_id: tools#page_468
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:36Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Configuration of spacing for date fields in a Windows Forms application.
- Explanation of programmatically refreshing textField functionality.
- Overview of Null Value settings and their properties.

## Content

### Setting Spacing in DateTimePickerAdv

```vb
Me.dateTimePickerAdv1.Spacing = 5
```

#### Figure 267: Spacing Applied to TextField
![](Spacing Applied to TextField.png)

**Note:** The text field can be refreshed programmatically by calling `DateTimePickerAdv.RefreshFields()` method.

#### See Also
- [Navigating between Fields, UpDown and DropDown Buttons](https://link-to-documentation)
- 3.5.3.2.3.1.3.1 Null Value Settings

### Null Value Settings

At run time, on clicking the "None" button of the popup calendar, "No date is selected" string will be displayed in the text field like the below image.

#### Figure 268: NullValue Selected
![](NullValue Selected.png)

This default string can be changed using `NullString` property. Below table describes the properties which controls the Null value behavior.

| DateTimePickerAdv Properties     | Description                                                                                                                                                                              |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EnableNullDate                    | Specifies whether null date support is enabled. If it is set to false, DateTimePickerAdv will always have a selected date instead of null string. i.e., text field displays the selected date even when None button is selected. By default it is true. |
| EnableNullKeys                    | Specifies Backspace or Delete keys makes the date null. EnableNullDate must be set to true to make this setting effective.                                                                    |

---

*Page 468 | © 2013 Syncfusion. All rights reserved.*

## Page-level Navigation/TOC

- [Essential Tools for Windows Forms](#essential-tools-for-windows-forms)
  - [Setting Spacing in DateTimePickerAdv](#setting-spacing-in-datetimepickeradv)
  - [Null Value Settings](#null-value-settings)

## Cross References

- **See Also**:
  - [Navigating between Fields, UpDown and DropDown Buttons](https://link-to-documentation)
  - [3.5.3.2.3.1.3.1 Null Value Settings](https://link-to-documentation)

<!-- tags: [windows forms, datetimepicker, null value settings, spacing, refresh fields] keywords: [date picker, text field, null string, enable null date, enable null keys] -->
```