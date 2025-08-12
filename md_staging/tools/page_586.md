```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_586.jpeg
document_name: tools
page_number: 586
page_id: tools#page_586
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Syncfusion.Windows.Forms.Tools.PercentTextBox ();
    return ptb as TextBox;
}
```

## Deriving a New Class from Syncfusion ComboBoxAdv

The following example demonstrates how to derive a new class from the existing Syncfusion ComboBoxAdv and override the internal TextBox:

### C#

```csharp
public new Syncfusion.Windows.Forms.Tools.PercentTextBox TextBox
{
    get
    {
        return (Syncfusion.Windows.Forms.Tools.PercentTextBox)
        base.TextBox;
    }
}
```

### VB.NET

```vb
' Derive a new class from the existing Syncfusion ComboBoxAdv.
Public Class PercentComboBoxAdv : Inherits Syncfusion.Windows.Forms.Tools.ComboBoxAdv
    ' Overrides the internal TextBox.
    Protected Overrides Function CreateTextBox() As TextBox
        Dim ptb As Syncfusion.Windows.Forms.Tools.PercentTextBox = New Syncfusion.Windows.Forms.Tools.PercentTextBox ()
        Return CType(IIf(TypeOf ptb Is TextBox, ptb, Nothing), TextBox)
    End Function

    Public Shadows ReadOnly Property TextBox() As Syncfusion.Windows.Forms.Tools.PercentTextBox
        Get
            Return CType(MyBase.TextBox, Syncfusion.Windows.Forms.Tools.PercentTextBox)
        End Get
    End Property
End Class
```

### Creating an Instance for the Derived Class and Initializing

#### C#

```csharp
// Do the initialization.
private PercentComboBoxAdv PercentComboBoxAdv1;
this.PercentComboBoxAdv1 = new PercentComboBoxAdv();
this.PercentComboBoxAdv1.Location = new System.Drawing.Point(this.Width / 4, this.Height / 3);
this.Controls.Add(this.PercentComboBoxAdv1);
this.PercentComboBoxAdv1.SelectedValueChanged += new
```

## API Reference

### Method Overriding

- **CreateTextBox()**: Overrides the internal TextBox property of the Syncfusion ComboBoxAdv to use a PercentTextBox.

### Property

- **TextBox**: A new property that casts the internal TextBox of the derived class to a PercentTextBox.

## Code Examples

### Initialization and Event Handling

#### C#

```csharp
private PercentComboBoxAdv PercentComboBoxAdv1;

this.PercentComboBoxAdv1 = new PercentComboBoxAdv();
this.PercentComboBoxAdv1.Location = new System.Drawing.Point(this.Width / 4, this.Height / 3);
this.Controls.Add(this.PercentComboBoxAdv1);
this.PercentComboBoxAdv1.SelectedValueChanged += new
```

<!-- tags: [Syncfusion Winforms, PercentTextBox, ComboBoxAdv, Tool, Control, Version 11.4.0.26] keywords: [PercentTextBox, ComboBoxAdv, WinForms, Tool, Control, Derivation, Override, TextBox, Initialization, Event Handling] -->
```