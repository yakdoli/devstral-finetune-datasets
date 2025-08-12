```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_542.jpeg
document_name: tools
page_number: 542
page_id: tools#page_542
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:19:47Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates custom color selection using the ColorPickerUIAdv control in Windows Forms.
- Explains runtime selection of colors through the Color dialog.
- Provides insights into adding colors to color groups.

## Content

### Custom Color Selection

#### Figure 330: Custom Color = "Orange"

![](https://via.placeholder.com/300x200?text=Figure+330)

This figure illustrates the use of the ColorPickerUIAdv control, showing a selection of the custom color "Orange."

#### Runtime Selection
**3.5.4.5.3.3 Runtime Selection**

The ColorPickerUIAdv control at runtime provides a Color dialog, enabling users to select and add colors to the color groups.

#### Figure 331: Adding Color Through Color Dialog at Run Time

![](https://via.placeholder.com/300x200?text=Figure+331)

This figure demonstrates the addition of a color through the Color dialog at runtime, showing the interface for selecting and confirming the new color.

## API Reference

### Namespaces and Classes
- `Syncfusion.Windows.Forms.Tools`
- `ColorPickerUIAdv`

### Methods and Properties
- `ShowColorDialog()`: Displays the Color dialog for runtime color selection.
- `SelectedColor`: Gets or sets the currently selected color.
- `ColorGroups`: Allows adding and managing color groups.

## Code Examples

### C# Example

```csharp
using Syncfusion.Windows.Forms.Tools;

public class CustomColorPickerForm : Form
{
    private ColorPickerUIAdv colorPicker;

    public CustomColorPickerForm()
    {
        InitializeComponent();

        // Initialize ColorPickerUIAdv
        colorPicker = new ColorPickerUIAdv();
        colorPicker.Dock = DockStyle.Fill;
        colorPicker.ColorGroups.Add(new ColorGroup("Custom", CustomColors));
        this.Controls.Add(colorPicker);
    }

    private void SelectCustomColor()
    {
        if (colorPicker.ShowDialog() == DialogResult.OK)
        {
            MessageBox.Show($"Selected Color: {colorPicker.SelectedColor}");
        }
    }
}
```

## Cross References
- See also:
  - ColorPickerUIAdv documentation
  - Managing Color Groups in Windows Forms
  - Runtime Interactivity in Windows Forms Applications

<!-- tags: [Syncfusion Winforms, ColorPickerUIAdv, Runtime Selection, Color Dialog, Custom Colors] keywords: [Custom Color, Color Groups, Windows Forms, UI Dialog, Runtime Addition, Color Selection] -->
```