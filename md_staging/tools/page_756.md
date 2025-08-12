```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_756.jpeg
document_name: tools
page_number: 756
page_id: tools#page_756
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:40Z
fidelity: lossless
-->

## Overview
- Demonstrates the Border Settings of IntegerTextBox control.
- Provides a code snippet example for handling key settings to enter large values as multiples of thousands, megas, kilos, etc.

## Content

### IntegerTextBox Border Settings

A sample demonstrating the Border Settings of IntegerTextBox control is available at the following installation path:

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls
```

#### Key Settings

In scenarios where users need to enter large values, such as in suffixes like Mega, Kilo, etc., adding keyboard support for these values can greatly enhance usability for the users.

For example, if the user wants to enter 32,000, they can simply enter `32` and press the `'K'` key. The value will then automatically change to `32,000`. This functionality is illustrated in the code snippet provided below.

##### C# Code Snippet

```csharp
private void integerTextBox1_KeyDown(object sender, KeyEventArgs e)
{
    long v = integerTextBox1.IntegerValue;
    switch (e.KeyCode)
    {
        // Enter the value as multiples of thousand.
        case Keys.G : v = v * 1000000000;
            break;
        case Keys.M : v = v * 1000000;
            break;
        case Keys.K : v = v * 1000;
            break;
    }
    integerTextBox1.IntegerValue = v;
}
```

##### VB.NET Code Snippet

```vbnet
Private Sub integerTextBox1_KeyDown(ByVal sender As Object, ByVal e As KeyEventArgs)
    Dim v As Long = integerTextBox1.IntegerValue
    Select e.KeyCode
        ' Enter the value as multiples of thousand.
        Case Keys.G
            v = v * 1000000000
        Case Keys.M
            v = v * 1000000
    End Select
    integerTextBox1.IntegerValue = v
End Sub
```

### Conclusion

This feature enhances user experience by allowing quick and efficient entry of large values using keyboard shortcuts, making it easier for users to handle massive numeric inputs.

---

<!-- tags: [Syncfusion, Winforms, IntegerTextBox, Border Settings, Key Settings, Large Values] keywords: [IntegerTextBox, Border Settings, keyboard shortcuts, large values, user experience] -->
```