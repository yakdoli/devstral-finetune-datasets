```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_822.jpeg
document_name: tools
page_number: 822
page_id: tools#page_822
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:59Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```vb
Select Case e.KeyCode
    Case Keys.G
        v = v * 1000000000
    Case Keys.M
        v = v * 1000000
    Case Keys.K
        v = v * 1000
End Select
currencyTextBox1.DecimalValue = v
End Sub
```

So if the user wants to enter 32000, he just needs to enter 32 and then press 'K'. The value will change to 32000.

### 3.5.8.6.7.2 Error Validation

When invalid text is entered by the user, we can handle the `Validation.Error` event to raise an alarm. Follow the steps below.

- Drag the `CurrencyTextBox`, `ErrorProvider` control, and `TextBox` onto the form.
- Handle the `Validation.Error` event of `CurrencyTextBox`.

#### [C#]

```csharp
string item = e.StartPosition.ToString();
string eventlogmessage = String.Format("Event: {0} InvalidText: {1} Position: {2}\r\n", "Validation.Error", e.InvalidText, item);
textBox1.Text = textBox1.Text + eventlogmessage;
this.errorProvider1.SetError((Control) sender, eventlogmessage);
```

#### [VB.NET]

```vb
Private item As String = e.StartPosition.ToString()
Private eventlogmessage As String = String.Format("Event: {0} InvalidText: {1} Position: {2}" & Constants.vbCrLf, "Validation.Error", e.InvalidText, item)
Private textBox1.Text = textBox1.Text & eventlogmessage
Me.errorProvider1.SetError(CType(sender, Control), eventlogmessage)
```

<!-- tags: [product, module, control, api, version?] keywords: [filesystem, validation, error, text, enter, value, change, handle, validation.error, string, textbox, eventlogmessage, csharp, vb, net] -->
```