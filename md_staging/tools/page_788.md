```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_788.jpeg
document_name: tools
page_number: 788
page_id: tools#page_788
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:38Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Implements features for handling value entry in PercentTextBox using keyboard shortcuts.
- Demonstrates use of `Keys` to enter values as multiples of thousand.
- Explains handling of increment and decrement operations using specific key combinations (`Up` and `Down` keys).

## Content

### Handling Multiples of Thousand
The following VB.NET code snippet shows how to handle value entry in the `PercentTextBox` using specific key combinations to enter values as multiples of thousand.

```vb
Private Sub percentTextBox1_KeyDown(ByVal sender As Object, ByVal e As KeyEventArgs)
    Dim v As Double = percentTextBox1.PercentValue
    Select Case e.KeyCode
        ' Enter the value as multiples of thousand.
        Case Keys.G
            v = v * 1000000000
        Case Keys.M
            v = v * 1000000
        Case Keys.K
            v = v * 1000
    End Select
    percentTextBox1.PercentValue = v
End Sub
```

### Handling Increment/Decrement using Shortcut Keys
#### Subsection: Incrementing and Decreasing Values
When it is necessary to increment or decrement the value in the `PercentTextBox`, shortcut keys can simplify the process. The following example demonstrates using the `Up` and `Down` keys to adjust the value in the `PercentTextBox`.

##### Implementation in C#
```csharp
private void percentTextBox1_KeyDown(object sender, KeyEventArgs e)
{
    // Increments the PercentTextBoxValue.
    double v = percentTextBox1.PercentValue;
    switch (e.KeyCode)
    {
        case Keys.Up : v++; break; // you can change by a step like v+=10;
        case Keys.Down : v--; break;
    }
    percentTextBox1.PercentValue = v;
}
```

##### Implementation in VB.NET
```vb
[VB.NET]
```

### Explanation of the Code
- **Handling Multiples**:
  - The `percentTextBox1_KeyDown` event listens for specific key presses (e.g., `Keys.G`, `Keys.M`, `Keys.K`) to modify the value by multiplying it with appropriate factors.
- **Increment/Decrement**:
  - The use of `Keys.Up` increases the value by one step, and `Keys.Down` decreases it. These can be customized to increment in steps of 10 or any other value as needed.

#### Cross References
- Refer to related documentation for advanced key handling in `PercentTextBox` for further customization.

## Page-level Navigation/TOC (if applicable)
- Essential Tools for Windows Forms
  - Handling Multiples of Thousand
  - Handling Increment/Decrement using Shortcut Keys

<!-- tags: [syncfusion, winforms, percenttextbox, keyhandling, shortcuts, valueentry] keywords: [keys.g, keys.m, keys.k, percenttextbox, up, down, increment, decrement, value, multiples] -->
```
