<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_523.jpeg
document_name: tools
page_number: 523
page_id: tools#page_523
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Learn how to use the `ColorPickerButton` control to display a `ColorUIControl` for selecting colors.

## Adding the ColorPickerButton Control

### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Tools
```

### C#

1. Create an instance of the `ColorPickerButton` class and add it to the form.

```csharp
private Syncfusion.Windows.Forms.ColorPickerButton colorPickerButton1;
this.colorPickerButton2 = new
Syncfusion.Windows.Forms.ColorPickerButton();
this.colorPickerButton1.Text = "Select a Color";
this.Controls.Add(this.colorPickerButton1);
```

### VB.NET

```vb
Private colorPickerButton1 As Syncfusion.Windows.Forms.ColorPickerButton
Me.colorPickerButton2 = New
Syncfusion.Windows.Forms.ColorPickerButton()
Me.colorPickerButton1.Text = "Select a Color"
Me.Controls.Add(Me.colorPickerButton1)
```

### Clicking the Button at Runtime

2. Clicking this button at runtime will display the `ColorUIControl`.

![The ColorPickerButton Control Displaying the ColorUIControl](image.png)

## API Reference

### Namespaces and Classes
- `Syncfusion.Windows.Forms.Tools`

### Members
- `ColorPickerButton` - Provides a button that opens a `ColorUIControl` for color selection.
- `ColorUIControl` - Defines the UI for selecting colors.

## Code Examples

### Example: Adding a ColorPickerButton

- **C#**
  ```csharp
  private void Form_Load(object sender, EventArgs e)
  {
      ColorPickerButton colorPicker = new ColorPickerButton();
      colorPicker.Text = "Select a Color";
      colorPicker.Location = new Point(50, 50);
      this.Controls.Add(colorPicker);
  }
  ```

- **VB.NET**
  ```vb
  Private Sub Form_Load(ByVal sender As Object, ByVal e As EventArgs)
      Dim colorPicker As New ColorPickerButton()
      colorPicker.Text = "Select a Color"
      colorPicker.Location = New Point(50, 50)
      Me.Controls.Add(colorPicker)
  End Sub
  ```

## RAG Annotations

<!-- tags: [Syncfusion, WinForms, ColorPickerButton, ColorUIControl] keywords: [Color selection, Windows Forms, Control, UI, VB.NET, C#] -->