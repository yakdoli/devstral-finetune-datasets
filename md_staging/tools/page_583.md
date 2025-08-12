```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_583.jpeg
document_name: tools
page_number: 583
page_id: tools#page_583
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:32Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Explains how to set the height of the ComboBoxAdv control in VB.NET using a code example.
- Discusses event handling in the ComboBoxAdv control, specifically focusing on selection events and their respective behaviors.

## Content

### Event Handling

#### Selection Events

The events present in the ComboBox can be applied for the ComboBoxAdv control.

| ComboBoxAdv Events                     | Description                                                                |
|-----------------------------------------|-----------------------------------------------------------------------------|
| SelectedIndexChanged                    | Handled when the SelectedIndex property is changed.                       |
| SelectedIndexChanging                   | Handled when the SelectedIndex property is changing.                      |
| SelectedValueChanged                    | Handled when the SelectedValue property is changed.                       |
| SelectionChangeCommitted                | Handled when the user selects a new text for the combo.                   |
| DropDown Event                          | Handled before the dropdown is shown.                                    |

The ComboBoxAdv handles different events for various user interaction scenarios. The occurrence and order of these events are detailed in the following table.

| Scenarios                               | SelectionChangeCommitted Event | SelectedValueChanged | SelectedIndexChanged | Validating/Validated |
|-----------------------------------------|----------------------------------|-----------------------|----------------------|----------------------|
| TextArea-Change Selection by Keys       | Yes:1                           | Yes:2                | Yes:3               | No                   |
| TextArea-On AutoComplete                | No                              | No                   | No                  | No                   |
| Drop-Down List-Change Selection by Keys | No                              | Yes:1                | Yes:2               | No                   |
| Drop-Down List-Change Selection by Mouse Move | No                          | No                   | No                  | No                   |
| Drop-Down Close by Enter Key            | Yes:1                           | No                   | No                  | No                   |

## Code Examples

```vb
' Sets the height of the ComboBox.
Me.comboBoxAdv1.TextBoxHeight = 80
```

## RAG Annotations

<!-- tags: [ComboBoxAdv, Events, SelectionEvents, .NET, VB.NET, Windows Forms, EventHandling] keywords: [ComboBoxAdv, SelectedIndexChanged, SelectedIndexChanging, SelectedValueChanged, SelectionChangeCommitted, DropDown Event, AutoComplete, TextArea, Drop-Down List, UserInteraction, CodeExample] -->
```