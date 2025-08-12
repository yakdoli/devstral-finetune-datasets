```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_766.jpeg
document_name: tools
page_number: 766
page_id: tools#page_766
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:29Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The document discusses the use of the PercentTextBox control in Windows Forms.
- It explains how to add and configure the PercentTextBox control both through the designer and programmatically.
- The example provided demonstrates displaying a percent value.

## Content

### Designer Approach

1. **Adding PercentTextBox to Toolbox**
   - Open the toolbox to access various controls.
   - Locate the PercentTextBox control as shown in Figure 482.

   ![Figure 482: PercentTextBox in Toolbox](image1)

2. **Running the Application**
   - After adding the PercentTextBox control to the form using the designer:
     - Run the application.
     - The PercentTextBox will allow you to enter a percent value, which is displayed as shown in Figure 483.

   ![Figure 483: PercentTextBox created Through Designer](image2)

### Programmatical Approach

#### Declaring an instance of the PercentTextBox control

1. **C#**
   ```csharp
   private Syncfusion.Windows.Forms.Tools.PercentTextBox percentTextBox1;
   ```

2. **VB.NET**
   ```vb
   Private percentTextBox1 As Syncfusion.Windows.Forms.Tools.PercentTextBox
   ```

## API Reference

### Syncfusion.Windows.Forms.Tools.PercentTextBox

#### Properties
- `Text`: Gets or sets the text displayed in the PercentTextBox.

## Code Examples

### Using PercentTextBox in C#

```csharp
private void Form_Load(object sender, EventArgs e)
{
    // Initialize PercentTextBox
    PercentTextBox percentTextBox1 = new PercentTextBox();

    // Add to form
    this.Controls.Add(percentTextBox1);

    // Set initial value
    percentTextBox1.Text = "50.00%";
}
```

### Using PercentTextBox in VB.NET

```vb
Private Sub Form_Load(sender As Object, e As EventArgs)
    ' Initialize PercentTextBox
    Dim percentTextBox1 As New PercentTextBox()

    ' Add to form
    Me.Controls.Add(percentTextBox1)

    ' Set initial value
    percentTextBox1.Text = "50.00%"
End Sub
```

## Cross References

- For more information on controls in the Toolbox, see the "Toolbox Overview" section in the documentation.
- To explore additional custom text boxes, refer to the "CustomTextBox" section.

<!-- tags: [Syncfusion Winforms, PercentTextBox, Toolbox, Designer, Programmatical Approach, Percent value, C#, VB.NET] keywords: [PercentTextBox, Windows Forms, Designer, вш, programmatic, percent value, C#, VB.NET] -->
```