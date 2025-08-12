<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_935.jpeg
document_name: tools
page_number: 935
page_id: tools#page_935
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:44:21Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Declares and initializes the AutoLabel control.
- Sets properties for the AutoLabel control and adds it to the form.

## Content

### Using AutoLabel

- **Declare the AutoLabel control.**
  ```csharp
  private Syncfusion.Windows.Forms.Tools.AutoLabel autoLabel1;
  ```
  ```vb
  Private autoLabel1 As Syncfusion.Windows.Forms.Tools.AutoLabel
  ```

- **Initialize the control.**
  ```csharp
  this.autoLabel1 = new Syncfusion.Windows.Forms.Tools.AutoLabel();
  ```
  ```vb
  Me.autoLabel1 = New Syncfusion.Windows.Forms.Tools.AutoLabel()
  ```

- **Set the properties for the AutoLabel control and add it to your form.**
  ```csharp
  this.autoLabel1.Text = "autoLabel1";
  this.autoLabel1.BackColor = System.Drawing.Color.BurlyWood;
  this.autoLabel1.ForeColor = System.Drawing.Color.SaddleBrown;
  this.autoLabel1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
  this.autoLabel1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;

  // Add the AutoLabel control to the Form.
  this.Controls.Add(this.autoLabel1);
  ```
  ```vb
  ' Code for VB.NET will be similar to the C# example provided above.
  ' Unlike the C# version, the VB.NET code is not shown here but can be derived from the C# example.
  ```

## API Reference

### AutoLabel Properties
- **Text**: The text displayed by the label.
- **BackColor**: The background color of the label.
- **ForeColor**: The foreground color of the label.
- **Font**: The font used to display the text.
- **TextAlign**: The alignment of the text within the label.

## Code Examples

### C# Example
```csharp
using Syncfusion.Windows.Forms.Tools;

public class MainForm : Form
{
    private AutoLabel autoLabel1;

    public MainForm()
    {
        InitializeComponent();
    }

    private void InitializeComponent()
    {
        autoLabel1 = new AutoLabel();

        // Set properties
        autoLabel1.Text = "autoLabel1";
        autoLabel1.BackColor = System.Drawing.Color.BurlyWood;
        autoLabel1.ForeColor = System.Drawing.Color.SaddleBrown;
        autoLabel1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        autoLabel1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;

        // Add to the form
        this.Controls.Add(autoLabel1);
    }
}
```

### VB.NET Example
```vb
Imports Syncfusion.Windows.Forms.Tools

Public Class MainForm
    Inherits Form

    Private autoLabel1 As AutoLabel

    Public Sub New()
        InitializeComponent()
    End Sub

    Private Sub InitializeComponent()
        autoLabel1 = New AutoLabel()

        ' Set properties
        autoLabel1.Text = "autoLabel1"
        autoLabel1.BackColor = System.Drawing.Color.BurlyWood
        autoLabel1.ForeColor = System.Drawing.Color.SaddleBrown
        autoLabel1.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((Byte)(0)))
        autoLabel1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter

        ' Add to the form
        Me.Controls.Add(autoLabel1)
    End Sub
End Class
```

## Cross References
- For more information on other tools and controls in WinForms, refer to the Syncfusion WinForms documentation.

<!-- tags: [Syncfusion WinForms, AutoLabel, control, Windows Forms, UI design] keywords: [AutoLabel properties, text alignment, color settings, font styling, control initialization] -->