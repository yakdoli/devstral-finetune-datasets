```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_407.jpeg
document_name: tools
page_number: 407
page_id: tools#page_407
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:22Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Provides solutions for various task-based queries about the control.
- Focuses on customizing the calculator display text area to use NumberGroupSeparator.

## Content

### 3.5.2.3.5 Frequently Asked Questions

This section illustrates the solutions for various task-based queries about the control.

#### 3.5.2.3.5.1 How to customize the calculator display text area to use NumberGroupSeparator?

The calculator control by default does not allow the use of NumberGroupSeparator like in DoubleTextBox.

![](attachment:https://via.placeholder.com/300x200.png)

*Figure 207: DoubleTextBox*

So to achieve this, we need to derive the CalculatorControl and override the CreateCalculatorDisplayBox() method.

#### C#

```csharp
private CalculatorAdv calculatorControl1;
this.calculatorControl1 = new CalculatorAdv();
public class CalculatorAdv : Syncfusion.Windows.Forms.Tools.CalculatorControl
{
    public CalculatorAdv()
    {
    }
    protected override void CreateCalculatorDisplayBox()
    {
        Syncfusion.Windows.Forms.Tools.DoubleTextBox dtb = new Syncfusion.Windows.Forms.Tools.DoubleTextBox();
        dtb.NumberGroupSeparator = ",";
        this.textCalculatorBox = dtb; //Changing the TextBox to DoubleTextBox
    }
}
```

#### VB.NET

```vb
Private calculatorControl1 As CalculatorAdv
Me.calculatorControl1 = New CalculatorAdv()
Public Class CalculatorAdv
    Inherits Syncfusion.Windows.Forms.Tools.CalculatorControl
```

## API Reference (if applicable)
- Namespace: `Syncfusion.Windows.Forms.Tools`
- Class: `CalculatorControl`
- Methods:
  - `CreateCalculatorDisplayBox()`: Override method to customize the calculator display text area.

## Code Examples (multi-language supported)
- **C# Example**: Demonstrates how to customize the calculator display text area to use `NumberGroupSeparator`.
- **VB.NET Example**: Provides an equivalent approach in VB.NET for the same customization.

## Page-level Navigation/TOC (if applicable)
- 3.5.2.3.5 Frequently Asked Questions
  - 3.5.2.3.5.1 How to customize the calculator display text area to use NumberGroupSeparator?

## Cross References
- Refer to the version-specific documentation for detailed implementation guidelines: Syncfusion Winforms version 11.4.0.26.

<!-- tags: [Syncfusion Winforms, CalculatorControl, NumberGroupSeparator, Manual, C#, VB.NET] keywords: [CalculatorControl, DoubleTextBox, NumberGroupSeparator, Customization, C#, VB.NET, Version 11.4.0.26] -->
```