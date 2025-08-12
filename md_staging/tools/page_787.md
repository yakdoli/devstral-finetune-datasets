```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_787.jpeg
document_name: tools
page_number: 787
page_id: tools#page_787
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:50Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- MinimumSize property is used to get/set the minimum size for a control.
- Textbox control sizes can be specified programmatically using MaximumSize and MinimumSize properties.
- Enhancing user input in textboxes by supporting key shortcuts for large value entries, like 'K' for thousands.

## Content

| MinimumSize | Gets / sets the minimum size for the control. |
|-------------|-------------------------------------------------|

### Programmatically Setting Control Sizes

#### C#
```csharp
this.percentTextBox1.MaximumSize = new System.Drawing.Size(100, 25);
this.percentTextBox1.MinimumSize = new System.Drawing.Size(100, 25);
```

#### VB.NET
```vb
Me.percentTextBox1.MaximumSize = New System.Drawing.Size(100, 25)
Me.percentTextBox1.MinimumSize = New System.Drawing.Size(100, 25)
```

![Size of the PercentTextBox control Set](image.png)
*Figure 501: Size of the PercentTextBox control Set*

### Key Settings for Large Values

**3.5.8.5.3.9 Key Settings**
Sometimes there may occur some situations for entering large values, like in Mega, Kilo etc. In such situations if we add some sort of keyboard support, it will be very much useful for the users.

For example, if the user wants to enter 32000, he just needs to enter `32` and then press the `'K'`. The value will change to `32000` automatically. This is illustrated in the code snippet given below.

#### C#
```csharp
private void percentTextBox1_KeyDown(object sender, KeyEventArgs e)
{
    double v = percentTextBox1.PercentValue;
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
    percentTextBox1.PercentValue = v;
}
```

## API Reference
- **MinimumSize Property**: 
  - Type: Size
  - Description: Gets or sets the minimum size for the control.
  - Parameters: None
  - Returns: The minimum size of the control.
  - Exceptions: None

## Code Examples
- The provided C# and VB.NET code examples demonstrate setting the maximum and minimum sizes for a textbox control.
- The key handling logic illustrates the scenario of user-friendly input for large values using shortcuts.

## Cross References
- See also: Textbox Control in Syncfusion WinForms documentation.
- Key Handling in UI Controls for more information on programmatically managing user input.

<!-- tags: [Syncfusion WinForms, MinimumSize, PercentTextBox, KeySettings, SizeControl] keywords: [MinimumSize, MaximumSize, Control Sizes, Key Handling, Large Values, User Input] -->
``` 
