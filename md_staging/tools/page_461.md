```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_461.jpeg
document_name: tools
page_number: 461
page_id: tools#page_461
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:03Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Documents the `DateTimePickerAdv` control properties and their descriptions.
- Demonstrates setting dropdown colors for various modes using C# and VB.NET code examples.

## Content

### DateTimePickerAdv Properties

| DateTimePickerAdv Properties              | Description                                                                                     |
|-------------------------------------------|-------------------------------------------------------------------------------------------------|
| DropDownNormalColor                      | Gets or Sets the dropdown backcolor in Normal mode.                                             |
| DropDownPressedColor                     | Gets or Sets the dropdown backcolor in Pressed mode, i.e., when the date is selected in the text field. |
| DropDownSelectedColor                    | Gets or Sets the dropdown backcolor in Selected mode, i.e., when a date is selected using the popup calendar. |

### Code Examples

#### C#

```csharp
this.dateTimePickerAdv2.DropDownNormalColor = System.Drawing.Color.LightBlue;
this.dateTimePickerAdv2.DropDownPressedColor = System.Drawing.Color.Goldenrod;
this.dateTimePickerAdv2.DropDownSelectedColor = System.Drawing.Color.SteelBlue;
```

#### VB.NET

```vb
Me.dateTimePickerAdv2.DropDownNormalColor = System.Drawing.Color.LightBlue
Me.dateTimePickerAdv2.DropDownPressedColor = System.Drawing.Color.Goldenrod
Me.dateTimePickerAdv2.DropDownSelectedColor = System.Drawing.Color.SteelBlue
```

### Note

<blockquote>
These settings will be effective only when `DateTimePickerAdv.Style` is `Office2003`, `OfficeXP`, and `VS2005`.
</blockquote>

## Page-level Navigation/TOC (if applicable)

- DateTimePickerAdv Properties
  - DropDownNormalColor
  - DropDownPressedColor
  - DropDownSelectedColor

## Cross References

- **See also:**
  - [DateTimePickerAdv Class](#datetimepickeradv-class)
  - [Style Property](#style-property)

```html

<!-- tags: [syncfusion, windows forms, datetimepickeradv, dropdown colors, style] keywords: [datetimepickeradv, dropdownnormalcolor, dropdownpressedcolor, dropdownselectedcolor, office2003, officexp, vs2005] -->
```