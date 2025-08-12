<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: calculate
page_number: 042
page_id: calculate#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:02Z
fidelity: lossless
-->

# Essential Calculate

```csharp
if (key.Length > 0)
{
    // The value.
    this.cq[key] = this.textBox3.Text;

    // Just display it in the list box.
    this.listBox1.Items.Add(string.Format("[{0}] = {1}", key, this.textBox3.Text));
}
}
```

### [VB]

```vb
Imports Syncfusion.Calculate

...

Dim cq As CalcQuickBase
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    cq = New CalcQuickBase

    AddHandler Me.button1.Click, AddressOf button1_Click
    AddHandler Me.button2.Click, AddressOf button2_Click

    ' Form1_Load
End Sub

Private Sub button1_Click(ByVal sender As Object, ByVal e As EventArgs)

    ' Compute
    Me.label3.Text = Me.cq.ParseAndCompute(Me.textBox1.Text)

    ' Button1_Click
End Sub

Private Sub button2_Click(ByVal sender As Object, ByVal e As EventArgs)

    ' Register name.
    Dim key As String = Me.textBox2.Text
    If key.Length > 0 Then

        ' The value.
        Me.cq(key) = Me.textBox3.Text

        ' Just display it in the list box.
        Me.listBox1.Items.Add(String.Format("[{0}] = {1}", key,
```

## API Reference

### Namespaces & Classes

- **Syncfusion.Calculate**
  - **CalcQuickBase**: The main class for performing calculations.

### Methods

- **ParseAndCompute(String):**
  - **Description**: Parses and computes the mathematical expression provided in the string.
  - **Parameters**: 
    - `expression`: The mathematical expression to compute.
  - **Returns**: The result of the computation as a `String`.

## Code Examples

The code above demonstrates:
- Handling user input to compute mathematical expressions.
- Registering names and their corresponding values for use in calculations.
- Displaying results in a list box for user reference.

### References
- **Syncfusion Documentation**: Further details on `CalcQuickBase` and its features can be found in the official Syncfusion documentation.

<!-- tags: [syncfusion, calculate, calcquickbase, winforms, .net, api, 11.4.0.26] keywords: [formula calculation, user input, list box, textbox, event handling, parse and compute] -->