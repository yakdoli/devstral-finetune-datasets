```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_408.jpeg
document_name: tools
page_number: 408
page_id: tools#page_408
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:09Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Content

#### Code Example: Creating a Calculator Display Box

```csharp
Public Sub New()
End Sub

Protected Overloads Overrides Sub CreateCalculatorDisplayBox()
    Dim dtb As New Syncfusion.Windows.Forms.Tools.DoubleTextBox()

    dtb.NumberGroupSeparator = ","
    Me.textCalculatorBox = dtb
    ' Changing the TextBox to DoubleTextBox
End Sub
End Class
```

#### Figure: Calculator Displaying NumberGroupSeparator with the Help of DoubleTextBox

![Calculator Displaying NumberGroupSeparator with the Help of DoubleTextBox](https://i.imgur.com/example_image.png)

**Figure 208**: Calculator displaying **NumberGroupSeparator** with the help of **DoubleTextBox**

### 3.5.2.3.5.2 How to Simulate a Particular button in the Calculator?

We can use **Calculator.ButtonAction()** method for this. When the user clicks the button, the **ButtonAction** method of the Calculator control will call back the action of the particular button (in this example it is "=" button) and displays the result in the textbox area, using **CalcActions** Enumerator. This enumerator has all the actions that can be assigned to the calculator buttons, including digits and arithmetic operators also.

#### Code Example: Simulating the "=" Button Action

```csharp
[C#]
private void buttonAdv1_Click(object sender, EventArgs e)
{
    // Performing the "=" button action
    this.calculatorControl1.ButtonAction(Syncfusion.Windows.Forms.Tools.CalcActions.CalcOperatorEquals);
}
```

### API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Tools`
  - **Class**: `CalculatorControl`
    - **Methods**:
      - `ButtonAction(CalcActions calcAction)`
        - **Description**: Executes the specified calculator action.
        - **Parameters**:
          - `calcAction`: `CalcActions` - The type of action to be executed.
        - **Returns**: `void`
- **Enums**:
  - **CalcActions**
    - **Members**: Includes all actions like digits and operators.

### Code Examples

The provided code examples demonstrate how to use the **CalculatorControl** to perform specific actions, such as simulating the "=" button.

## Page-level Navigation/TOC (if applicable)
- Essential Tools for Windows Forms
  - Creating a Calculator Display Box
  - Simulating a Particular button in the Calculator

## Cross References
- **See also**: CalculatorControl, DoubleTextBox, CalcActions

<!-- tags: [syncfusion, windows forms, calculator, controls, numbergroupseparator, doubletextbox, buttons, actions] keywords: [calculatorcontrol, buttonaction, calcactions, simulating buttons, number formatting] -->
```
