```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_801.jpeg
document_name: tools
page_number: 801
page_id: tools#page_801
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:51Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

The event handler receives an argument of type `ValidationEventArgs` containing data related to this event. The following `ValidationEventArgs` members provide information specific to this event.

| Members          | Description                                                             |
|------------------|-------------------------------------------------------------------------|
| ErrorMessage     | Returns the error message.                                              |
| InvalidText      | Returns the invalid text as it would have been if the error had not intercepted it. |
| StartPosition    | Returns the location of the invalid input in the invalid text.       |

### Error Handling Code Examples

[C#]

```csharp
private void percentTextBox1_ValidationError(object sender, Syncfusion.Windows.Forms.Tools.ValidationEventArgs e)
{
    Console.WriteLine("ValidationError event is raised ");
}
```

[VB.NET]

```vb
Private Sub percentTextBox1_ValidationError(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Tools.ValidationEventArgs)
    Console.WriteLine("ValidationError event is raised ")
End Sub
```

### 3.5.8.6 CurrencyTextBox

#### Overview
- Implements currency-specific behavior for editing controls.
- Inherits from `System.Windows.Forms.TextBox`.
- Enhances functionality for formatting and validating currency input.

#### Implementation Details
- `CurrencyTextBox` provides specialized features for handling currency values.
- Example usage for formatting currency:
  - Input: `125678.13000`
  - Output: `$125,678.13000`

#### Example

![$125,678.13000](image.png)

**Figure 503: CurrencyTextBox**

#### Text Box Control Enhancements
- Standard `TextBox` controls can display and edit string values.
- Custom enhancements for numeric data collection:
  - Restricting input to currency values requires adding specific validation logic.

#### Conclusion
- The `CurrencyTextBox` is a specialized control for handling monetary data, providing necessary enhancements over a standard `TextBox`.

### Page-level Navigation/TOC
- [Essential Tools for Windows Forms]
  - [Error Handling with ValidationEventArgs]
  - [CurrencyTextBox Implementation]

### Cross References
- See also:
  - [System.Windows.Forms.TextBox]
  - [ValidationEventArgs]

<!-- tags: [syncfusion, windows forms, validationeventargs, currencytextbox, textboxes, tool controls, error handling, formatting, numeric data] keywords: [validation, textbox, currency, error handling, string input, numeric validation, winforms, tools, essential, events] -->
```