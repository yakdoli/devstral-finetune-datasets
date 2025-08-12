```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_715.jpeg
document_name: tools
page_number: 715
page_id: tools#page_715
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:04Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
MessageBox.Show("The calculated Value is" + e.FinalValue.ToString());
}
```

### `CalculatorClosing Event`

This event is raised before the calculator popup is displayed. The `Cancel` property of this `CancelEventArgs` lets you cancel the popup display as follows.

```csharp
private void currencyEdit1_CalculatorClosing(object sender, CancelEventArgs e)
{
    //This prints the final calculated value before closing.
    MessageBox.Show("The calculated Value is" + e.FinalValue.ToString());
}
```

### `CalculatorShowing Event`

This event is raised before the calculator popup is displayed. The `Cancel` property of this `CancelEvent`Args lets you cancel the popup display as follows.

```csharp
private void currencyEdit1_CalculatorShowing(object sender, CancelEventArgs e)
{
    //Cancels the calculator popup.
    e.Cancel = true;
}
```

```vb
Private Sub currencyEdit1_CalculatorShowing(ByVal sender As Object, ByVal e As CancelEventArgs)
    'Cancels the calculator popup.
    e.Cancel = True
End Sub
```

### `DecimalValueChanged Event`

This event is raised when `DecimalValue` property is changed.

```csharp
private void currencyEdit1_DecimalValueChanged(object sender, EventArgs e)
{
}
```

---

## API Reference (if applicable)

## Code Examples (multi-language supported)

### Visual Basic .NET

```vb
Private Sub currencyEdit1_CalculatorClosing(ByVal sender As Object, ByVal e As CalculatorClosingEventArgs)
    ' This prints the final calculated value before closing.
    MessageBox.Show("The calculated Value is" + e.FinalValue.ToString())
End Sub
```

### C#

```csharp
private void currencyEdit1_CalculatorClosing(object sender, CalculatorClosingEventArgs e)
{
    // This prints the final calculated value before closing.
    MessageBox.Show("The calculated Value is" + e.FinalValue.ToString());
}
```

### WinForms-specific conventions

- Events: `CalculatorClosing`, `CalculatorShowing`, `DecimalValueChanged`
- Parameters: `e` (EventArgs)

## Page-level Navigation/TOC (if applicable)

### Cross References

See also:  
- `CalculatorClosingEventArgs`
- `CancelEventArgs`
- `MessageBox`
- `EventArgs`

<!-- tags: [tools, calculator, decimalvalue, events, windows forms] keywords: [calculatorclosing, calculatorshowing, decimalvaluechanged, windows forms] -->
```