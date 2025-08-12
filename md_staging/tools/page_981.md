```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_981.jpeg
document_name: tools
page_number: 981
page_id: tools#page_981
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:46:06Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
using Syncfusion.Windows.Forms.Tools;
```

```vb
Imports Syncfusion.Windows.Forms.Tools
```

### Overview
- Create an instance of the `RadioButtonAdv` control class.
- Set the properties and add the `RadioButtonAdv` control to the form.

### Content

#### C# Code Example
```csharp
private Syncfusion.Windows.Forms.Tools.RadioButtonAdv radioButtonAdv1;
this.radioButtonAdv1 = new Syncfusion.Windows.Forms.Tools.RadioButtonAdv();
```

#### VB.NET Code Example
```vb
Private radioButtonAdv1 As Syncfusion.Windows.Forms.Tools.RadioButtonAdv
Me.radioButtonAdv1 = New Syncfusion.Windows.Forms.Tools.RadioButtonAdv()
```

#### Setting Properties and Adding to Form
##### C#
```csharp
this.radioButtonAdv1.Text = "radioButtonAdv1";
this.radioButtonAdv1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold,
    System.Drawing.GraphicsUnit.Point, ((byte)(0)));
this.radioButtonAdv1.ForeColor = System.Drawing.Color.MistyRose;
this.radioButtonAdv1.BackColor = System.Drawing.Color.RosyBrown;

// Add the RadioButtonAdv control to the Form.
this.Controls.Add(this.radioButtonAdv1);
```

##### VB.NET
```vb
Me.radioButtonAdv1.Text = "radioButtonAdv1"
Me.radioButtonAdv1.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold,
    System.Drawing.GraphicsUnit.Point, CByte((0)))
Me.radioButtonAdv1.ForeColor = System.Drawing.Color.MistyRose
Me.radioButtonAdv1.BackColor = System.Drawing.Color.RosyBrown
```

<!-- tags: [Syncfusion Winforms, RadioButtonAdv, Control, Tools, C#, VB.NET] keywords: [RadioButtonAdv, Text, Font, ForeColor, BackColor, Controls] -->
```