```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_404.jpeg
document_name: tools
page_number: 404
page_id: tools#page_404
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:58Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

![Calculator Control Using PopupCalculator Class](# "Figure 204: Calculator Control Using PopupCalculator Class")
*Figure 204: Calculator Control Using PopupCalculator Class*

### Calculator Events

The event for Calculator control and PopupCalculator control are discussed in this section.

#### ValueCalculated Event

The ValueCalculated event fires each time the value of the CalculatorControl is changed. That is, even if you just press any digit, this event will be handled.

The event handler receives an argument of type `CalculatorValueCalculatedEventArgs`. To get the final result, use the `LastAction` property of the `CalculatorValueCalculatedEventArgs` in the ValueCalculated event.

| Members          | Description                                   |
|------------------|-----------------------------------------------|
| ErrorCondition   | Specifies the error condition of the Calculator control if any. |
| LastAction       | Gets/Sets the last action that was performed. |
| MemoryValue      | Gets/Sets the MemoryValue of the Calculator control. |
| Message          | Gets/Sets the custom error message when in error mode. |

---

© 2013 Syncfusion. All rights reserved.
<!-- tags: [syncfusion, essential tools, windows forms, calculator control, popupcalculator class, valuecalculated event, calculatorvaluecalculatedeventargs, tools] keywords: [calculator control, popupcalculator, event handler, lastaction, memoryvalue, message, error condition, custom error message] -->
``` 
