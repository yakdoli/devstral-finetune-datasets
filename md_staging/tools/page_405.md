```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_405.jpeg
document_name: tools
page_number: 405
page_id: tools#page_405
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:23Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Guides users on retrieving the value of the Calculator control after '=' is pressed.
- Demonstrates code snippets in C# and VB.NET for handling the `ValueCalculated` event.
- Explains how to identify the `LastAction` using the `ValueCalculated` event.

## Content

### Properties of the Calculator Control

| **Property** | **Description** |
|--------------|------------------|
| Value        | Gets/Sets the `CalculatorValue` object that contains the value of the Calculator control. |

### Retrieving Calculator Control Value After '=' Button Press

We can retrieve the value of the Calculator control after '=' button is pressed using the following code snippet.

#### C#

```csharp
private void calcctrl_ValueCalculated(object sender, CalculatorValueCalculatedEventArgs arg)
{
    // Checks the final answer after '=' is pressed.
    if (!arg.ErrorCondition && arg.LastAction == CalcActions.CalcOperatorEquals)
    {
        MessageBox.Show(calcctrl.Value.ToString());
    }
}
```

#### VB.NET

```vb
Private Sub calcctrl_ValueCalculated(ByVal sender As Object, ByVal arg As CalculatorValueCalculatedEventArgs)
    If Not arg.ErrorCondition AndAlso arg.LastAction = CalcActions.CalcOperatorEquals Then
        ' Checks the final answer after '=' is pressed.
        MessageBox.Show(calcctrl.Value.ToString())
    End If
End Sub
```

#### Figure: LastAction Identified Using ValueCalculated Event

![LastAction Identified Using ValueCalculated Event](https://i.imgur.com/twoHrjS.png)

**Figure 205**: LastAction identified using ValueCalculated Event

## API Reference

### `CalculatorValueCalculatedEventArgs`

- **ErrorCondition**: Indicates whether an error condition exists.
- **LastAction**: Specifies the last action performed by the calculator control.
- **Value**: Represents the current value of the calculator control.

### Properties

- **Value**: Gets/Sets the `CalculatorValue` object containing the value of the Calculator control.

### Events

- **ValueCalculated**: Triggered when the calculator control completes a calculation.

## Code Examples

### C#

```csharp
private void calcctrl_ValueCalculated(object sender, CalculatorValueCalculatedEventArgs arg)
{
    if (!arg.ErrorCondition && arg.LastAction == CalcActions.CalcOperatorEquals)
    {
        MessageBox.Show(calcctrl.Value.ToString());
    }
}
```

### VB.NET

```vb
Private Sub calcctrl_ValueCalculated(ByVal sender As Object, ByVal arg As CalculatorValueCalculatedEventArgs)
    If Not arg.ErrorCondition AndAlso arg.LastAction = CalcActions.CalcOperatorEquals Then
        MessageBox.Show(calcctrl.Value.ToString())
    End If
End Sub
```

---

<!-- tags: [Syncfusion Winforms, Calculator, ValueCalculatedEvent, C#, VB.NET] keywords: [CalculatorValue, LastAction, ValueCalculated, ErrorCondition, CalcActions, MessageBox] -->
```