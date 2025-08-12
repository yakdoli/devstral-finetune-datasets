```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_459.jpeg
document_name: tools
page_number: 459
page_id: tools#page_459
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:29Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The following topics will help you become more familiar with using the DateTimePickerAdv control.

## DateTimePickerAdv Child Controls

### Overview

- DateTimePickerAdv has child controls like DropDown, Updown arrows, checkbox.
- This section discusses the properties which control the appearance and behavior of these controls.

### Child Controls in DateTimePickerAdv

#### Figure 255: Child Controls in DateTimePickerAdv

\[Image Description: The diagram shows the child controls of DateTimePickerAdv, including a CheckBox, DropDown Button, UpDown Button, and Text Field.\]

### UpDown and DropDown Buttons

#### Overview

- This section discusses the properties of DateTimePickerAdv control which customizes the UpDown and DropDown buttons.

#### UpDown Buttons

- The below properties control the appearance and behavior of the UpDown buttons.

| DateTimePickerAdv Properties      | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| ShowUpDown                        | Shows or hides the UpDown buttons.                                          |
| ShowUpDownOnFocus                 | Shows or hides the UpDown button when focussed. By default it is set to false. |
| VSLikeUpDown                      | Specifies whether the UpDown button will have a VS-like look.                 |

#### Code Example (C\#)

```csharp
this.dateTimePickerAdv2.ShowUpDown = true;
```

## API Reference

### Properties

- `ShowUpDown`: Boolean value to show or hide the UpDown buttons.
- `ShowUpDownOnFocus`: Boolean value to show or hide the UpDown button when focussed.
- `VSLikeUpDown`: Boolean value to specify whether the UpDown button will have a VS-like look.

## Code Examples

- C\# Example to show UpDown buttons:
  ```csharp
  this.dateTimePickerAdv2.ShowUpDown = true;
  ```

### Cross References

- [Unclear] (If any references or related topics are mentioned, include them here.)

### RAG Annotations

<!-- tags: [datetimepickeradv, windows forms, controls, child controls, updown buttons, dropdown buttons] keywords: [datetimepickeradv, syncfusion, windows forms, controls, appearance, behavior, updown, dropdown, properties, code example] -->
```