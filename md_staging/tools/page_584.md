```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_584.jpeg
document_name: tools
page_number: 584
page_id: tools#page_584
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:25Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section covers essential tools and controls for Windows Forms, focusing on ComboBoxAdv.
- Compares behaviors such as handling dropdowns, losing focus, and text property changes.
- Details selection events for ComboBoxAdv.

## Content

### Key Behaviors Comparison

| Feature                       | No | Yes:1 | Yes:2 | Yes:3 |
|-------------------------------|----|-------|-------|-------|
| Drop-Down Close by Escape Key | No | No    | No    | No    |
| Drop-Down Close by Click     | Yes:1 | Yes:2 | Yes:3 | No    |
| Losing Focus                  | Yes:2 (in DropDownStyle.DropDown mode only) | No    | No    | Yes:1 |
| Changing Text Property in Code | Yes:1 | No    | No    | No    |

### Selection Events

#### Overview
The events present in the ComboBox can be applied for ComboBoxAdv control.

#### ComboBoxAdv Events and Descriptions

| ComboBoxAdv Events             | Description                                       |
|---------------------------------|---------------------------------------------------|
| SelectedIndexChanged            |Handled when SelectedIndex property is changed. |
| SelectedIndexChanging          |Handled when SelectedIndex property is changing. |
| SelectedValueChanged            |Handled when SelectedValue property is changed.  |
| SelectionChangeCommitted       |Handled when the user selects a new text for the combo. |
| DropDown Event                 |Handled before the dropdown is shown.             |

#### Event Scenarios

The ComboBoxAdv handles different events for the different user interaction scenarios. The occurrence and order of the events are tabulated below.

| Scenarios                     | SelectionChangedCommitted Event | SelectedValueChanged | SelectedIndexChanged | Validating/Validated |
|-------------------------------|-------------------------------|-----------------------|-----------------------|----------------------|
| TextArea-Change Selection by Keys | Yes:1                     | Yes:2                | Yes:3                | No                 |
| TextArea-On                    | No                         | No                   | No                   | No                 |

---

<!-- tags: [syncfusion, winforms, combobox, events, design-time] keywords: [SelectedIndexChanged, SelectedValue, DropDownStyle, user interaction, TabArea] -->
```