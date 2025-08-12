```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: calculate
page_number: 074
page_id: calculate#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:28Z
fidelity: lossless
-->

# Essential Calculate

## Event Handlers and CalcQuickBase

9. These four event handlers signal when the user leaves a modified text box. At that point, the `CalcQuickBase` object is updated to reflect the new value that has been entered by the user.

## Using RegisterControlArray

### Overview

- **Purpose:** Streamlining the management of auto-calculation in `CalcQuickBase` for controls on a form.
- **Method:** `CalcQuickBase.RegisterControlArray` simplifies handling multiple events and removes the need to subscribe to individual events and write explicit handlers.
- **Assumptions:** 
  - The control is either a text box or a combo box.
  - The variable name for the control value in formulas is `Control.Name`.

### Content

#### Explicit Event Management

Using explicit events to manage auto-calculation in `CalcQuickBase` is straightforward but requires handling multiple events and writing event handlers. The `CalcQuickBase.RegisterControlArray` method automates this process, making it easier to add calculation support to a form or `UserControl`. 

There are two assumptions about the controls to which you want to bind the calculations:
1. The control is either a text box or a combo box.
2. The variable name used to represent the control value in formulas is `Control.Name`.

Here is the code that replicates the functionality of our previous example using explicit events to support auto-calculation. Notice that all the event handling has been removed. The process involves three steps:
1. Instantiating the `CalcQuickBase` object.
2. Calling the `RegisterControlArray` method.
3. Calling the `RefreshAllCalculations` method.

#### Code Example

```csharp
CalcQuickBase calculator = null;

private void Form1_Load(object sender, System.EventArgs e)
{
    // 1) Ensure controls have the names you want to use as variables.
    // These names can be set either from code or the designer.
    this.textBoxA.Name = "A";
    this.textBoxB.Name = "B";
    this.textBoxC.Name = "C";
    this.textBoxD.Name = "D";

    // 2) Initially populate the controls. Values can also be set in the designer.
    this.textBoxA.Text = "12";
    this.textBoxB.Text = "3";
    this.textBoxC.Text = "= [A] + 2 * [B]";

    // 3) Instantiate a CalcQuickBase object.
    calculator = new CalcQuickBase();

    // 4) Register the controls used in calculations. The formula variables are the Control.Name strings.
    this.calculator.RegisterControlArray(new Control[]
    {
    }
```

### Notes

- To support other controls beyond text boxes and combo boxes, you will need to derive `CalcQuickBase` and override `RegisterControl`.
- Ensure that all controls involved in the calculations have appropriate names to be used as variables in formulas.

## Conclusion

By utilizing `CalcQuickBase.RegisterControlArray`, developers can streamline the process of adding auto-calculation support to their WinForms applications, reducing the need for explicit event handling and simplifying the management of control-related calculations.

<!-- tags: [syncfusion, winforms, calcquickbase, auto-calculation, event-handling, registercontrolarray] keywords: [event handlers, text box, combo box, control names, explicit events, auto-calculation, formula variables, registercontrolarray] -->
```