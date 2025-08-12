```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_469.jpeg
document_name: tools
page_number: 469
page_id: tools#page_469
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

| Property            | Description                                                                                                                                                                                                                               |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NullString          | Specifies the text visible when there is no date selected. `EnableNullDate` must be set to `true` to make this setting effective.                                                                                                       |
| NullModeKeyReset    | Specifies what keys will toggle off null date. i.e., when null value is selected, by pressing the keys we can replace the null value with date selected. The keys are, <br> <br> - ArrowKeys (default), <br> - NumericKeys and <br> - Any. <br> <br> `EnableNullDate` must be set to `true` to make this setting effective. |
| IsNullDate          | Set this to `true`, if you want to display null value (String specified in `NullString`) instead of current value, specified using `DateTimePicker.value` property. <br> By default it is set to `false`.                                                                      |

## Code Examples

### C#

```csharp
this.dateTimePickerAdv1.EnableNullDate = true;
this.dateTimePickerAdv1.EnableNullKeys = true;
this.dateTimePickerAdv1.NullString = "Null Value";
this.dateTimePickerAdv1.NullModeKeyReset =
    Syncfusion.Windows.Forms.Tools.NullModeKeyReset.NumericKeys;
```

### VB.NET

```vb
Me.dateTimePickerAdv1.EnableNullDate = True
Me.dateTimePickerAdv1.EnableNullKeys = True
Me.dateTimePickerAdv1.NullString = "Null Value"
Me.dateTimePickerAdv1.NullModeKeyReset =
    Syncfusion.Windows.Forms.Tools.NullModeKeyReset.NumericKeys
```

## Screenshot

![CheckBox displaying "Null Value"](images/check-null-value.png)

<!-- tags: [winforms, tools, datetimepicker, nullstring, nullmodekeyreset, isnulldate] keywords: [syncfusion winforms, tools, datetimepickeradvice, enablenulldate, enablenullkeys, nullstring, nullmodekeys] -->
```