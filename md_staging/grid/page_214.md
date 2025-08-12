```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_214.jpeg
document_name: grid
page_number: 214
page_id: grid#page_214
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:48Z
fidelity: lossless
-->

## Content

### WinForms-specific conventions

This section details how to set up a FloatNumericUpDown cell in a Syncfusion Grid control, providing both C# and VB.NET examples of configuring its properties.

#### C# Example

```csharp
style.Text = "Allow Decimal Increment and Decrement(step by 0.2,0.01,0.001)";
style.TextColor = Color.MidnightBlue;

// Set up FNumericUpDown Cell.
style = gridControl1[2, 2];
style.CellType = CustomCellTypes.FloatNumericUpDown.ToString();
style.Text = "0.5";

// Assign the Style Properties of Up Down Control.
FloatNumericUpDownStyleProperties sp = new FloatNumericUpDownStyleProperties(style);
sp.StyleInfo.BackColor = SystemColors.Window;
sp.FloatNumericUpDownProperties.Maximum = 15.0;
sp.FloatNumericUpDownProperties.Minimum = 0.0;
sp.FloatNumericUpDownProperties.StartValue = 0.5;
sp.FloatNumericUpDownProperties.Step = 0.2;
sp.FloatNumericUpDownProperties.WrapValue = true;
sp.FloatNumericUpDownProperties.DecimalPlaces = 1;
```

#### VB.NET Example

```vb
RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.FloatNumericUpDown)
Dim style As GridStyleInfo = Me.gridControl1(1, 1)
style.Text = "Allow Decimal Increment and Decrement(step by 0.2,0.01,0.001)"
style.TextColor = Color.MidnightBlue

' Set up FNumericUpDown Cell.
style = gridControl1(2, 2)
style.CellType = CustomCellTypes.FloatNumericUpDown.ToString()
style.Text = "0.5"

' Assign the Style Properties of Up Down Control.
Dim sp As FloatNumericUpDownStyleProperties = New FloatNumericUpDownStyleProperties(style)
sp.StyleInfo.BackColor = SystemColors.Window
sp.FloatNumericUpDownProperties.Maximum = 15.0
sp.FloatNumericUpDownProperties.Minimum = 0.0
sp.FloatNumericUpDownProperties.StartValue = 0.5
sp.FloatNumericUpDownProperties.Step = 0.2
sp.FloatNumericUpDownProperties.WrapValue = True
sp.FloatNumericUpDownProperties.DecimalPlaces = 1
```

## API Reference

This section includes the API elements used in the above examples:

- `CustomCellTypes.FloatNumericUpDown`: Defines the custom cell type for FloatNumericUpDown control.
- `GridControl`: The main grid control from Syncfusion for WinForms.
- `GridStyleInfo`: Represents the style properties of a grid cell.
- `FloatNumericUpDownStyleProperties`: Represents the style information specific to FloatNumericUpDown controls in grids.
- `SystemColors.Window`: System-provided color for the background of the control.
- `FloatNumericUpDownProperties`: Contains properties for configuring the behavior of FloatNumericUpDown cells.
  - `Maximum`: Sets the maximum value the FloatNumericUpDown control can reach.
  - `Minimum`: Sets the minimum value the FloatNumericUpDown control can reach.
  - `StartValue`: Sets the initial value of the control.
  - `Step`: Defines the increment/decrement step value.
  - `WrapValue`: Determines whether the control wraps back to the start value after reaching the maximum.
  - `DecimalPlaces`: Specifies the number of decimal places displayed.

## Code Examples

The provided code examples demonstrate how to create and configure FloatNumericUpDown cells in a Syncfusion Grid. These samples show how to set up the cell type, define initial values, and adjust various properties such as maximum, minimum, step, and decimal precision.

<!-- tags: [product, module, control, api, version?] keywords: [syncfusion grid, floatnumericupdown, gridcontrol, winforms, numeric up/down, decimal places, maximum, minimum, step, wrap value, style properties] -->
```