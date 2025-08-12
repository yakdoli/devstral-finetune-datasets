```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_821.jpeg
document_name: tools
page_number: 821
page_id: tools#page_821
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:13Z
fidelity: lossless
-->

## Review of Event Properties Associated with ValidationErrorArgs

### Event Properties Associated with ValidationErrorArgs

The properties of the `ValidationEventArgs` class are essential for handling validation errors in Windows Forms applications. These properties provide detailed information about the error encountered during the validation process:

| **Members**        | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| `ErrorMessage`     | Returns the error message.                                                      |
| `InvalidText`      | Returns the invalid text as it would have been if the error had not interrupted it. |
| `StartPosition`    | Returns the location of the invalid input within the invalid text.            |

This mechanism can be utilized to alert users when they enter invalid text, enhancing the user experience by providing clear feedback.

## Handling Error Validation

The following section provides a detailed explanation of the `KeyDown` event and how it can be used to add key support in scenarios where users need to enter large values, such as in Mega, Kilo, etc. This key support can be very useful for users who frequently handle such data inputs.

### Adding Key Support Using `Key flaskEvent`

#### Using `Key down Event` for Multiplier Support

In situations where users need to enter large values like Mega, Kilo, etc., adding key support can be very useful. For example, if users want to enter values as multiples of thousands, the following method can be used:

##### Implementation Details

This section provides the C# and VB.NET code snippets to handle the `Key down Event` for multiplying values.

#### C# Implementation

```csharp
private void currencyTextBox1_KeyDown(object sender, KeyEventArgs e)
{
    // Multiplies the Key value with multiples of 1000.
    decimal v = currencyTextBox1.DecimalValue;
    switch (e.KeyCode)
    {
        case Keys.G : v = v * 1000000000; break;
        case Keys.M : v = v * 1000000; break;
        case Keys.K : v = v * 1000; break;
    }
    currencyTextBox1.DecimalValue = v;
}
```

#### VB.NET Implementation

```vb.net
Private Sub currencyTextBox1_KeyDown(ByVal sender As Object, ByVal e As KeyEventArgs)

    ' Multiplies the Key value with multiples of 1000.
    Dim v As Decimal = currencyTextBox1.DecimalValue

End Sub
```

### Cross References

- Refer to **Error Validation** for additional details on handling validation errors.

<!-- tags: [syncfusion winforms, event properties, validationerrorargs, keydown event, validation, error handling] keywords: [validation, error message, key support, large values, user experience, event handling, validationargs, keyeventargs] -->
```