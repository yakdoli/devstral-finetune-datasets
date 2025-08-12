```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_955.jpeg
document_name: tools
page_number: 955
page_id: tools#page_955
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:35Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Create a C# or VB.NET application though Visual Studio.
- Add the required assembly references.
- Include the required namespace.

### Using Syncfusion.Windows.Forms.Tools Namespace
```csharp
using Syncfusion.Windows.Forms.Tools;
```

```vbnet
Imports Syncfusion.Windows.Forms.Tools
```

### Creating an Instance of the CheckBoxAdv Control

- **Create an instance of the CheckBoxAdv control class.**

```csharp
private Syncfusion.Windows.Forms.Tools.CheckBoxAdv checkBoxAdv1;
this.checkBoxAdv1 = new Syncfusion.Windows.Forms.Tools.CheckBoxAdv();
```

```vbnet
Private checkBoxAdv1 As Syncfusion.Windows.Forms.Tools.CheckBoxAdv
Me.checkBoxAdv1 = New Syncfusion.Windows.Forms.Tools.CheckBoxAdv()
```

- **Set the properties and add the CheckBoxAdv control to the form.**

```csharp
this.checkBoxAdv1.Text = "checkBoxAdv1";
this.checkBoxAdv1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
this.checkBoxAdv1.ForeColor = System.Drawing.Color.OliveDrab;
this.checkBoxAdv1.BackColor = System.Drawing.Color.Beige;

// Add the CheckBoxAdv control to the Form.
this.Controls.Add(this.radioButtonAdv1);
```

```vbnet
Me.checkBoxAdv1.Text = "checkBoxAdv1"
Me.checkBoxAdv1.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CByte((0)))
```

## API Reference

### CheckBoxAdv Class
- Used to create advanced checkbox controls with customizable properties.

### Properties
- **Text**: Sets the text displayed next to the checkbox.
- **Font**: Defines the font style, size, and other attributes for the text.
- **ForeColor**: Sets the foreground color of the text.
- **BackColor**: Sets the background color of the checkbox.

- Include other relevant properties, methods, and events based on the Syncfusion documentation for comprehensive reference.

## Code Examples

The examples above demonstrate how to:
1. Import the necessary namespace.
2. Instantiate a `CheckBoxAdv` control.
3. Customize its properties.
4. Add the control to the form.

## See also

- Refer to the Syncfusion official documentation and resources for more examples and detailed explanations.

<!-- tags: [Syncfusion, WinForms, CheckBoxAdv, Tools] keywords: [CheckBoxAdv, Controls, C#, VB.NET, properties, design time, runtime] -->
```