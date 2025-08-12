<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_762.jpeg
document_name: tools
page_number: 762
page_id: tools#page_762
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:16Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```vb
yncfusion.Windows.Forms.Tools.SetNullEventArgs
    Console.WriteLine(" SetNull event is raised ")
End Sub
```

### 3.5.8.4.4.6 ValidationError

This event occurs when the input text is invalid for the current state of the control.

The event handler receives an argument of type `ValidationEventArgs` containing data related to this event. The following `ValidationEventArgs` members provide information specific to this event.

| Members       | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| ErrorMessage  | Returns the error message.                                                  |
| InvalidText   | Returns the invalid text as it would have been if the error had not intercepted it. |
| StartPosition | Returns the location of the invalid input in the invalid text.            |

#### Code Examples

##### [C#]

```csharp
private void integerTextBox1_ValidationError(object sender, Syncfusion.Windows.Forms.Tools.ValidationEventArgs e)
{
    Console.WriteLine(" ValidationError event is raised ");
}
```

##### [VB.NET]

```vb
Private Sub integerTextBox1_ValidationError(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Tools.ValidationEventArgs)
    Console.WriteLine(" ValidationError event is raised ")
End Sub
```

### 3.5.8.4.5 Frequently Asked Questions

#### 3.5.8.4.5.1 How to display empty string in editor controls when databound value is null?

We can display empty string when data bound value is null. For this, we need to bind the editor controls (like `IntegerTextBox`, `DoubleTextBox`, etc.) to `BindableValue` property and also we need to set `AllowNull` to `true` and `NullString` property to empty string.

<!-- tags: [syncfusion, winforms, essential tools, validationerror, frequently asked questions, databinding, bindablevalue, allownull, nullstring] keywords: [validation event, error message, invalid text, location, c#, vb.net, editor control, databound value, empty string, frequently asked] -->