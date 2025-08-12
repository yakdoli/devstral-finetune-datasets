```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_616.jpeg
document_name: tools
page_number: 616
page_id: tools#page_616
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:16Z
fidelity: lossless
-->

## Overview

The page provides detailed information about the events and functionalities related to essential tools for Windows Forms. It highlights different behaviors of events such as `DropDown` closing by `Escape` key and `Click`, handling focus loss, and modifying properties like text through code. It also includes code examples to set text according to the selection in a `MultiColumnComboBox`.

## Content

### Event Behavior Summary

The following table outlines the behavior of various events for different control modes:

| Event Description                  | No   | Yes:2 | Yes:3 | Yes:1 |
|------------------------------------|------|-------|-------|-------|
| Drop-Down Close by Escape Key      | No   | No    | No    | No    |
| Drop-Down Close by Click          | Yes:1| Yes:2 | Yes:3 | No    |
| Losing Focus                       | Yes:2 (in DropDownStyle.DropDown (editable) mode only) | No    | No    | Yes:1 |
| Changing Text Property in Code     | Yes:1| No    | No    | No    |

### References for Implementation

You can refer to the following topics to gain an idea of implementing the above events:

- How to display multiple members in a `MultiColumnComboBox`?
- How to retrieve the columns other than `Display` and `Value` members in a `MultiColumnComboBox`?

#### 3.5.5.4.4.1 `SelectedValueChanged` Event

This event is handled when the selected value is changed in the combobox. This section discusses a use case illustrating the event.

##### Setting Text According to Selection

The process of accessing the selected item is complex. We need to access `DataRowView` from the control and then get the values. Include the below code in the `SelectedValueChanged` event handler to set the text of `MultiColumnComboBox` to the text in the first column of the selected row.

```csharp
[C#]

private void multiColumnComboBox1_SelectedValueChanged(object sender, System.EventArgs e)
{
    ComboBoxBaseDataBound c = multiColumnComboBox1 as ComboBoxBaseDataBound;
    if (c.SelectedIndex != -1)
    {
        // Sets the text of MultiColumnComboBox to the text in the first column of selected row.
        DataRowView drv = c.Items[c.SelectedIndex] as DataRowView;
        c.Text = drv.Row[1].ToString();
    }
}
```

### API References (if applicable)

This section is not explicitly provided in the image but could include detailed API references related to the controls and events discussed.

### Code Examples

The code snippet above is included to demonstrate how to set the text of a `MultiColumnComboBox` based on the selected row's first column.

### Page-level Navigation/TOC

The document provides step-by-step guidance and implementation details for handling specific events and functionalities in Windows Forms, focusing on `MultiColumnComboBox`.

### Cross References

See also:
- Related topics and references for handling multiple members and retrieving columns in a `MultiColumnComboBox`.

<!-- tags: Syncfusion, Winforms, MultiColumnComboBox, Events, SelectedValueChanged, C# code examples, version: 11.4.0.26 -->
```