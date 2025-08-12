```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_841.jpeg
document_name: tools
page_number: 841
page_id: tools#page_841
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

|  | Normal.\<br>The default value is 'OvertypeOnly'. |
| --- | --- |
| UsageMode | Specifies if the MaskedEditBox control is to behave as a numeric control. |

## Clip mode

At runtime, we can copy / paste the entries of MaskedEditBox. The entries that are copied can be specified whether to include literals using the `ClipMode` property.

Setting the `ClipMode` property of the MaskedEditBox to 'ExcludeLiterals', will get rid of the literals from the text that is returned by the control. The default value is set to 'IncludeLiterals'.

## InputMode

The different modes of the input can be determined by the `InputMode` property.

Setting the `InputMode` to 'Normal', allows the user to work in insert mode and the INSERT key is not allowed. In OvertureOnly mode, the INSERT key will not have any effect.

## UsageMode

The `UsageMode` property modifies the behavior of the MaskedEditBox as detailed below.

### Normal mode

When the `UsageMode` is set to 'Normal', there is no change in the behavior. This is the default mode for a MaskedEditBox control.

### Numeric Mode

When the `UsageMode` is set to 'Numeric', the control creates internally two data groups and one decimal separator character in the mask. These groups are created such that the first group holds the mask value before the decimal separator and the second group holds the mask value after the decimal separator. For example, let us specify the mask as follows:

```
####.#####
```

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: MaskedEditBox
- **Properties**:
  - `ClipMode`: Specifies whether to include literals in the copied entries.
  - `InputMode`: Determines different modes of input ('Normal', 'OvertypeOnly').
  - `UsageMode`: Modifies the behavior of the MaskedEditBox control.

## Code Examples (multi-language supported)
- **C# Example**:
  ```csharp
  MaskedEditBox maskedEditBox = new MaskedEditBox();
  maskedEditBox.UsageMode = MaskedEditBoxUsage.Numeric;
  maskedEditBox.Mask = "####.####";
  maskedEditBox.ClipMode = MaskedEditBoxClipMode.ExcludeLiterals;
  maskedEditBox.InputMode = MaskedEditBoxInputMode.Normal;
  ```

<!-- tags: [Syncfusion Winforms, MaskedEditBox, UsageMode, InputMode, ClipMode, Numeric Mode, Normal Mode] keywords: [maskededitbox, inputmode, usagemode, clipmode, numeric, normal, overtypeonly, literals, default behavior] -->
```