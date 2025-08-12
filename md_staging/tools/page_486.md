<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_486.jpeg
document_name: tools
page_number: 486
page_id: tools#page_486
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:25Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of DateTimePickerAdv and its child controls.
- Explains how to apply themes and styles to enhance the appearance.
- Lists details about the Style property and its functionality.

## Content

### DateTimePickerAdv Controls
#### Child Controls Without Themes
![Figure 281: DateTimePicker and Child Controls Without Themes](#)

#### Child Controls With Themes
![Figure 282: DateTimePicker and Child Controls With Themes](#)

### Styles
Visual Styles for the DateTimePickerAdv and its child controls can be applied using the Style property.

| DateTimePickerAdv Properties | Description |
| --- | --- |
| Style | Specifies the Office style of the picker. The options are: <br> • OfficeXP |

## API Reference

### DateTimePickerAdv
- **Style Property:** Specifies the Office style of the picker. The available option is:
  - OfficeXP

## Code Examples

```csharp
// Example: Applying the Style Property
using Syncfusion.WinForms.Input;
using Syncfusion.WinForms.Input.Extensions;

DateTimePickerAdv dateTimePicker = new DateTimePickerAdv();
dateTimePicker.Style = DatePickerAdvStyle.OfficeXP;
```

<!-- tags: [syncfusion winforms, datetimepickeradv, styles, officexp, visual styles] keywords: [datetimepickeradv, child controls, themes, style, office XP, windows forms] -->