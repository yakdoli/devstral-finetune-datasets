```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_895.jpeg
document_name: tools
page_number: 895
page_id: tools#page_895
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes how to create a `TextBoxExt` control using both designer and programmatic approaches in Windows Forms.
- Provides step-by-step instructions for initializing and adding the control to a form.

## Content

### Through Designer
4. Run the application. The `TextBoxExt` displayed will allow you to enter text.

![Figure 568: TextBoxExt created Through Designer](https://image.png)

### Through Programmatical Approach

#### Declaring an Instance of the TextBoxExt Control
1. Declare an instance of the `TextBoxExt` control.

##### C#
```csharp
private Syncfusion.Windows.Forms.Tools.TextBoxExt textBoxExt1;
```

##### VB.NET
```vbnet
Private textBoxExt1 As Syncfusion.Windows.Forms.Tools.TextBoxExt
```

#### Initializing the Control
2. Initialize the control.

##### C#
```csharp
this.textBoxExt1 = new Syncfusion.Windows.Forms.Tools.TextBoxExt();
```

##### VB.NET
```vbnet
Me.textBoxExt1 = New Syncfusion.Windows.Forms.Tools.TextBoxExt()
```

#### Adding the Control to the Form
3. Add the control to the form.

##### C#
```csharp
this.Controls.Add(this.textBoxExt1);
```

##### VB.NET
```vbnet
Me.Controls.Add(Me.textBoxExt1)
```

## API Reference

### Namespace
- `Syncfusion.Windows.Forms.Tools`

### Class
- `TextBoxExt`

### Methods/Properties/Events
- `TextBoxExt()` - Constructor for creating a new instance of the `TextBoxExt` control.

## Code Examples

#### C# Example
```csharp
private Syncfusion.Windows.Forms.Tools.TextBoxExt textBoxExt1;

this.textBoxExt1 = new Syncfusion.Windows.Forms.Tools.TextBoxExt();
this.Controls.Add(this.textBoxExt1);
```

#### VB.NET Example
```vbnet
Private textBoxExt1 As Syncfusion.Windows.Forms.Tools.TextBoxExt

Me.textBoxExt1 = New Syncfusion.Windows.Forms.Tools.TextBoxExt()
Me.Controls.Add(Me.textBoxExt1)
```

## Tags and Keywords
<!-- tags: [Syncfusion, WinForms, TextBoxExt, Control, Designer, Programmatic, Initialization, Form, C#, VB.NET] keywords: [TextBoxExt, Windows Forms, Designer, Programmatic, Initialization, Control, Application, C#, VB.NET, Syncfusion] -->
```