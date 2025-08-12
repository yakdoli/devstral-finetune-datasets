```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_735.jpeg
document_name: tools
page_number: 735
page_id: tools#page_735
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:17Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```vb
Dim v As Decimal = doubleTextBox1.DoubleValue
Select e.KeyCode

    ' Up and Down keys are used for incrementing and decrementing respectively.
    Case Keys.Up
        v = v + 1
    Case Keys.Down
        v = v - 1
End Select
doubleTextBox1.DoubleValue = v
End Sub
```

### 3.5.8.3.4.2 DoubleValueChanged Event

This event is handled when the double value in the text field is changed.

#### [C#]

```csharp
private void doubleTextBox1_DoubleValueChanged(object sender, EventArgs e)
{
    MessageBox.Show("Double Value is changed");
}
```

#### [VB.NET]

```vb
Private Sub doubleTextBox1_DoubleValueChanged(ByVal sender As Object, ByVal e As EventArgs)
    MessageBox.Show("Double Value is changed")
End Sub
```

## 3.5.8.4 IntegerTextBox

The **IntegerTextBox** is derived from the Windows Forms framework TextBox control and can display integer data type values. It exhibits properties similar to that of the **CurrencyTextBox**.

![Figure 463: IntegerTextBox Control](image.svg)

### Figure 463: IntegerTextBox Control

## API Reference

## Code Examples

## Page-level Navigation/TOC

## Cross References

<!-- tags: [product, module, control, api, version?] keywords: [Windows Forms, Essential Tools, DoubleTextBox, IntegerTextBox, CurrencyTextBox] -->
``` 
