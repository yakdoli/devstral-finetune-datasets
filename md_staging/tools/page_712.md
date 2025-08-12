```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_712.jpeg
document_name: tools
page_number: 712
page_id: tools#page_712
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:58Z
fidelity: lossless
-->

## Calculator Controls in Windows Forms

### Overview
- Demonstrates setting up a calculator in a Windows Forms application.
- Includes configuration of calculator actions, layout, and interaction settings.

### Content

| **Calculator Actions** | **Descriptions** |
|-----------------------|------------------|
| CalcOperatorDivide,   | Division operator                    |
| CalcOperatorPercent,  | Percentage operator                   |
| CalcOperatorEquals (default), | Equals operator (default action) |
| CalcOperatorSqrt,     | Square root operator                  |
| CalcOperatorSign,     | Sign operator                         |
| CalcOperatorMemoryClear, | Clear memory                        |
| CalcOperatorMemoryRecall, | Recall from memory                  |
| CalcOperatorMemoryStore, | Store in memory                     |
| CalcOperatorMemoryPlus, | Add to memory                        |
| CalcSpecialClear,     | Clear special                        |
| CalcSpecialClearEntry, | Clear entry                          |
| CalcSpecialDecimal,   | Decimal operator                     |
| CalcSpecialBackspace, | Backspace operator                   |

#### Setting Up the Calculator Layout

```csharp
this.currencyEdit1.CalculatorLayoutType =
    Syncfusion.Windows.Forms.Tools.CalculatorLayoutTypes.WindowsStandard;
this.currencyEdit1.CloseAction =
    Syncfusion.Windows.Forms.Tools.CalcActions.CalcOperatorEquals;
this.currencyEdit1.PopupCalculatorAlignment =
    Syncfusion.Windows.Forms.Tools.CalculatorPopupAlignment.Left;
this.currencyEdit1.ShowCalculator = true;
this.currencyEdit1.TransferFromCalculator = true;
this.currencyEdit1.TransferToCalculator = true;
```

```vb
Me.currencyEdit1.CalculatorLayoutType =
    Syncfusion.Windows.Forms.Tools.CalculatorLayoutTypes.WindowsStandard
Me.currencyEdit1.CloseAction =
    Syncfusion.Windows.Forms.Tools.CalcActions.CalcOperatorEquals
Me.currencyEdit1.PopupCalculatorAlignment =
    Syncfusion.Windows.Forms.Tools.CalculatorPopupAlignment.Left
Me.currencyEdit1.ShowCalculator = True
Me.currencyEdit1.TransferFromCalculator = True
Me.currencyEdit1.TransferToCalculator = True
```

### Important Considerations
- The `CalculatorLayoutType` property determines the layout and functionality of the calculator.
- The `CloseAction` property specifies the action that occurs when the calculator is closed, with the default being `CalcOperatorEquals`.
- Alignment and interaction settings are also configurable to enhance the user experience.

### Conclusion
This section highlights the configuration of calculator controls in Windows Forms, providing examples in both C# and VB.NET.

<!-- tags: [syncfusion, windows forms, calculator controls, layout, actions, interaction, settings, version 11.4.0.26] keywords: [calculator, windows forms, operations, actions, layout types, memory, clear, decimal, backspace, alignment, show calculator] -->
```