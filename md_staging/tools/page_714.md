```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_714.jpeg
document_name: tools
page_number: 714
page_id: tools#page_714
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:23Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

![Figure 443](https://example.com/image_url)
**Figure 443:** Text = "\$400"; TextAlign = "Right"; TransferFromCalculator = "True"

### Note: Enabling ButtonEdit.UseVisualStyle property and by setting visual style for control using ButtonEdit.ButtonStyle property, we can change the appearance of the calculator button.

### 3.5.8.1.4 Frequently Asked Questions

#### 3.5.8.1.4.1 How to Change the Calculator layout using CalcPopup property

Sometimes we may be in need of a calculator with Windows standard layout. By changing the CalcPopup property, we can do the same. Include this code fragment in the FormLoad event.

#### [C#]

```csharp
// Changes the layout of the calculator.
PopupCalculator pc = new Populcalculator();
pc.LayoutType = CalculatorLayoutTypes.WindowsStandard;
pc.ParentControl = currencyEdit1;
currencyEdit1.CalcPopup = pc;
```

#### [VB.NET]

```vb
' Changes the layout of the calculator.
Dim pc As PopupCalculator = New Populcalculator()
pc.LayoutType = CalculatorLayoutTypes.WindowsStandard
pc.ParentControl = currencyEdit1
currencyEdit1.CalcPopup = pc
```

### 3.5.8.1.5 Events

#### 3.5.8.1.5.1 CalculatorClosing Event

**CalculatorClosing** event is handled when the calculator is closing after the specified button is clicked.

#### [C#]

```csharp
private void currencyEdit1_CalculatorClosing(object sender, CalculatorClosingEventArgs e)
{
    // This prints the final calculated value before closing.
}
```

---

> © 2013 Syncfusion. All rights reserved. 714
<!-- tags: [syncfusion winforms, buttonedit, calculator, visualstyle, controlappearance, calcpopup, calculatorclosingevent, formload] keywords: [Essential Tools, Windows Forms, ButtonEdit, Calculator, Visual Style, Control Appearance, CalcPopup, CalculatorClosing Event, FormLoad] -->
```