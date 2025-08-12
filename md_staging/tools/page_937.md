```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_937.jpeg
document_name: tools
page_number: 937
page_id: tools#page_937
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:20Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- An introduction to the Syncfusion.Windows.Forms.Tools namespace and its usage in Visual Studio Properties window.
- Demonstrates the configuration of the "LabeledControl" property using the AutoLabel control.
- Includes C# and VB.NET code examples for implementing AutoLabel with a textbox.

## Content

### Design-Time Example

Figure 599: "LabeledControl" property in the Properties Grid

![Properties Grid Screenshot](https://i.imgur.com/SpaceX.png)

1. **Property Setup**:
   - `LabeledControl` specified in the Properties Grid to associate the textbox with the AutoLabel.

### C# Code Example

```csharp
private Syncfusion.Windows.Forms.Tools.AutoLabel autoLabel1;
this.autoLabel1 = new Syncfusion.Windows.Forms.Tools.AutoLabel();
this.autoLabel1.LabeledControl = this.textBox1;

this.Controls.Add(this.autoLabel1);
```

### VB.NET Code Example

```vb
Private autoLabel1 As Syncfusion.Windows.Forms.Tools.AutoLabel
Me.autoLabel1 = New Syncfusion.Windows.Forms.Tools.AutoLabel()
Me.autoLabel1.LabeledControl = Me.textBox1

Me.Controls.Add(Me.autoLabel1)
```

### Application Execution

- **Run the application**.
  
Figure 600: TextBox labeled using AutoLabel

![TextBox Labeling Example](https://i.imgur.com/SpaceX.png)

### Output and Expected Result

- The textbox is displayed with the associated AutoLabel in the form, as shown in Figure 600.

## API Reference

### Namespace: Syncfusion.Windows.Forms.Tools
- **Class**: `AutoLabel`
  - Properties:
    - `LabeledControl`: Specifies the control that is being labeled.

### Methods
- `AutoLabel()`: Constructor to initialize a new instance of the `AutoLabel` class.
- `SetLabeledControl(Control control)`: Method to set the labeled control explicitly.

## Code Examples

### Adding AutoLabel to a Form

1. **Design-Time**:
   - Drag an `AutoLabel` control from the Toolbox into the Windows Forms designer.
   - Assign the desired control (e.g., `textBox1`) to the `LabeledControl` property using the Properties window.

2. **Run-Time**:
   - Use C# or VB.NET code as shown above to programmatically add and configure the `AutoLabel`.

## Cross References

- Refer to the Syncfusion WinForms documentation on [LabeledControls](link-to-doc) for more details.
- Documentation on [AutoLabel](link-to-doc) for advanced usage and additional properties.

<!-- tags: Windows Forms, AutoLabel, LabeledControl, Syncfusion, Windows Forms Tools keywords: Syncfusion.Windows.Forms.Tools, AutoLabel, LabeledControl, Visual Studio, Properties Grid -->
```