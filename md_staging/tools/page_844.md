```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_844.jpeg
document_name: tools
page_number: 844
page_id: tools#page_844
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:20Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Decimal Separator Set

![Figure: Decimal Separator Set](https://i.imgur.com/ExampleImage.png)

## Thousand Separator Set

![Figure: Thousand Separator Set](https://i.imgur.com/ExampleImage.png)

## Time Separator Set

![Figure: Time Separator Set](https://i.imgur.com/ExampleImage.png)

## Cursor Position

The cursor position of the MaskedEditBox control can be specified using the options provided by the following properties.

### MaskedEditBox Properties and Their Descriptions

| MaskedEditBox Properties         | Description                                                                                                                                                                                                                          |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PositionAt                      | Defines the control's cursor position behavior on getting the focus. The options included are as follows:<br>- Decimal<br>- FirstPosition<br>- FirstMaskPosition.<br>The default value is 'FirstPosition'. |
| PositionAtDecimal               | Indicates whether the cursor is to be positioned at the decimal separator (if any) when the control receives focus.                                                                                                                   |

### Code Example

```csharp
this.maskedEditBox1.PositionAt = 
    Syncfusion.Windows.Forms.Tools.SpecialCursorPosition.Decimal;
this.maskedEditBox1.PositionAtDecimal = true;
```

## References

See also:
- [C#] Documentation for Syncfusion.Windows.Forms.Tools.MaskedEditBox
- SpecialCursorPosition Enumeration

<!-- tags: [WinForms, MaskedEditBox, CursorPosition] keywords: [MaskedEditBox, DecimalSeparator, ThousandSeparator, TimeSeparator, PositionAt, PositionAtDecimal, Syncfusion] -->
``` 
