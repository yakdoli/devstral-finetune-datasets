```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_757.jpeg
document_name: tools
page_number: 757
page_id: tools#page_757
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:52Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Case Keys.K
v = v * 1000
End Select
integerTextBox1.IntegerValue = v
End Sub
```

## Shortcut Keys

### Overview
- Sometimes there may be some situations for incrementing or decrementing the value in the IntegerTextBox.
- In such situations, it is better to use shortcut keys.
- The following implementation illustrates how this can be achieved.
- Using Up and Down keys for incrementing and decrementing respectively.
- Cannot use the '-' key because it is already reserved for entering the minus sign.

### Code Implementation

#### C#
```csharp
private void integerTextBox1_KeyDown(object sender, KeyEventArgs e)
{
    long v = integerTextBox1.IntegerValue;
    switch (e.KeyCode)
    {
        // Increments and decrements values.
        case Keys.Up: v++; break;
        case Keys.Down: v--; break;
    }
    integerTextBox1.IntegerValue = v;
}
```

#### VB.NET
```vb
Private Sub integerTextBox1_KeyDown(ByVal sender As Object, ByVal e As KeyEventArgs)
    Dim v As Long = integerTextBox1.IntegerValue
    Select e.KeyCode
        ' Increments and decrements values.
        Case Keys.Up
            v = v + 1
        Case Keys.Down
            v = v - 1
    End Select
    integerTextBox1.IntegerValue = v
End Sub
```

## API Reference
- `integerTextBox1_KeyDown`:
  - Parameters:
    - `sender` of type `Object`
    - `e` of type `KeyEventArgs`
  - Purpose: Handles the KeyDown event on the IntegerTextBox control.
  - Modifies the `IntegerValue` property of the IntegerTextBox based on the key pressed.

### Code Examples
- The provided examples demonstrate how to use shortcut keys to increment or decrement the value in the IntegerTextBox control.

<!-- tags: [syncfusion, winforms, integertextbox, shortcutkeys, windowsforms, tools] keywords: [integer, increment, decrement, keydown, keys.up, keys.down, control, event, integervalue, csharp, vb.net] -->
```