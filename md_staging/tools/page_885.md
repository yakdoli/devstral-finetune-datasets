```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_885.jpeg
document_name: tools
page_number: 885
page_id: tools#page_885
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:40:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Covers the properties and functionalities of the `NumericUpDownExt` control.
- Demonstrates how to set the size of the `NumericUpDownExt` control.
- Explains the implementation of keyboard support for easier input of large values.

## Content

### Setting the Size of the `NumericUpDownExt` Control

The following code snippets show how to set the `MaximumSize` and `MinimumSize` properties of the `NumericUpDownExt` control to ensure it maintains a fixed size.

#### [C#]
```csharp
this.numericUpDownExt1.MaximumSize = new System.Drawing.Size(60, 50);
this.numericUpDownExt1.MinimumSize = new System.Drawing.Size(60, 50);
```

#### [VB.NET]
```vb
Me.numericUpDownExt1.MaximumSize = New System.Drawing.Size(60, 50)
Me.numericUpDownExt1.MinimumSize = New System.Drawing.Size(60, 50)
```

**Figure 561: Size of the `NumericUpDownExt` control Set**

![NumericUpDownExt Size](https://i.imgur.com/example_image.jpg)

### Adding Keyboard Support for Entering Large Values

In situations where you need to enter large values (e.g., Mega, Kilo), adding keyboard support can be very useful. For example, if you want to enter 22000, you can simply enter `22` and then press `'K'`. The value will automatically change to 22000.

#### Implementation Example

The following code snippet demonstrates how to handle keyboard input for multiplying the entered value by appropriate factors (e.g., K for 1000, M for 1000000, G for 1000000000).

#### [C#]
```csharp
private void numericUpDownExt1_KeyDown(object sender, KeyEventArgs e)
{
    decimal v = integerTextBox1.Value;
    
    switch (e.KeyCode)
    {
        // Entering the value as multiples of thousand.
        case Keys.G: v = v * 1000000000; break;
        case Keys.M: v = v * 1000000; break;
        case Keys.K: v = v * 1000; break;
    }
    
    integerTextBox.Value = v;
}
```

#### [VB.NET]
```vb
Private Sub numericUpDownExt1_KeyDown(ByVal sender As Object, ByVal e As KeyEventArgs)
    Dim v As Decimal = integerTextBox1.Value
    
    Select Case e.KeyCode
        ' Entering the value as multiples of thousand.
        Case Keys.G: v = v * 1000000000 : Exit Select
        Case Keys.M: v = v * 1000000 : Exit Select
        Case Keys.K: v = v * 1000 : Exit Select
    End Select
    
    integerTextBox.Value = v
End Sub
```

## API Reference

### Properties
- `MaximumSize`: Defines the maximum size of the control.
- `MinimumSize`: Defines the minimum size of the control.

### Methods
- `numericUpDownExt1_KeyDown`: Handles the `Key Down` event for the `NumericUpDownExt` control.

## Code Examples

#### Example: Setting Fixed Size
```csharp
// C#
this.numericUpDownExt1.MaximumSize = new System.Drawing.Size(60, 50);
this.numericUpDownExt1.MinimumSize = new System.Drawing.Size(60, 50);
```

```vb
' VB.NET
Me.numericUpDownExt1.MaximumSize = New System.Drawing.Size(60, 50)
Me.numericUpDownExt1.MinimumSize = New System.Drawing.Size(60, 50)
```

#### Example: Adding Keyboard Support
```csharp
// C#
private void numericUpDownExt1_KeyDown(object sender, KeyEventArgs e)
{
    decimal v = integerTextBox1.Value;
    
    switch (e.KeyCode)
    {
        case Keys.G: v = v * 1000000000; break;
        case Keys.M: v = v * 1000000; break;
        case Keys.K: v = v * 1000; break;
    }
    
    integerTextBox.Value = v;
}
```

```vb
' VB.NET
Private Sub numericUpDownExt1_KeyDown(ByVal sender As Object, ByVal e As KeyEventArgs)
    Dim v As Decimal = integerTextBox1.Value
    
    Select Case e.KeyCode
        Case Keys.G: v = v * 1000000000 : Exit Select
        Case Keys.M: v = v * 1000000 : Exit Select
        Case Keys.K: v = v * 1000 : Exit Select
    End Select
    
    integerTextBox.Value = v
End Sub
```

<!-- tags: [NumericUpDownExt, Windows Forms, size, keyboard support] keywords: [maximumsize, minimumsize, keydown, large values, useful, example] -->
```