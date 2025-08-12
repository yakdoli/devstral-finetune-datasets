```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_872.jpeg
document_name: tools
page_number: 872
page_id: tools#page_872
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
private Syncfusion.Windows.Forms.Tools.NumericUpDownExt numericUpDownExt1;
```

```vb
Private numericUpDownExt1 As Syncfusion.Windows.Forms.Tools.NumericUpDownExt
```

## Overview
- 1-3 bullets summarizing the page scope using only visible text.

### Steps to Initialize and Configure a Syncfusion Windows Forms Tool
- Declare the `numericUpDownExt1` control.
- Initialize the control.
- Set the properties of the `NumericUpDownExt` control.
- Add the control to the form.

---

### WinForms-specific conventions

#### Initializing the Control

##### C#
```csharp
this.numericUpDownExt1 = new Syncfusion.Windows.Forms.Tools.NumericUpDownExt();
```

##### VB.NET
```vb
Me.numericUpDownExt1 = New Syncfusion.Windows.Forms.Tools.NumericUpDownExt()
```

---

#### Setting Properties of the `NumericUpDownExt` Control

##### C#
```csharp
this.numericUpDownExt1.Location = new System.Drawing.Point(70, 29);
this.numericUpDownExt1.Name = "numericUpDownExt1";
this.numericUpDownExt1.Size = new System.Drawing.Size(84, 20);
```

##### VB.NET
```vb
Me.numericUpDownExt1.Location = New System.Drawing.Point(70, 29)
Me.numericUpDownExt1.Name = "numericUpDownExt1"
Me.numericUpDownExt1.Size = New System.Drawing.Size(84, 20)
```

---

## Adding the Control to the Form

##### C#
```csharp
this.Controls.Add(this.numericUpDownExt1);
```

##### VB.NET
```vb
Me.Controls.Add(Me.numericUpDownExt1)
```
```