<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_759.jpeg
document_name: tools
page_number: 759
page_id: tools#page_759
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Events Overview

The following table lists some common events related to Windows Forms controls:

| Event Name             | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| ClipTextChanged        | This event occurs when the ClipText property is changed.                     |
| FormattedTextChanged   | This event occurs when the FormattedText property is changed.                |
| IntegerValueChanged    | This event occurs when the IntegerValue property is changed.                  |
| SetNull                | This event occurs when the NULL state is to be set based on a value.          |
| ValidationError        | This event occurs when the input text is invalid for the current state of the control. |

### 3.5.8.4.4.1 BindableValueChanged

This event occurs when the `BindableValue` property is changed. The `BindableValue` property is a wrapper property that indicates the value. This property can be used to set the value of the control to 'Null'.

#### Event Handler Example

```csharp
[C#]
private void integerTextBox1_BindableValueChanged(object sender, EventArgs e)
{
    Console.WriteLine("BindableValueChanged event is raised");
}
```

```vb.net
[VB.NET]
Private Sub integerTextBox1_BindableValueChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("BindableValueChanged event is raised")
End Sub
```

### 3.5.8.4.4.2 ClipTextChanged

This event occurs when the `ClipText` property is changed. The `ClipText` property returns the clipped text without the formatting.

---

<!-- tags: [syncfusion, windowsforms, events, bindablevaluechanged, cliptextchanged] keywords: [event handler, bindablevalue, cliptext, windows forms, formatting, null, input validation, csharp, vb.net] -->