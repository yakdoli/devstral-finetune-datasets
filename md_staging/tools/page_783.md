```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_783.jpeg
document_name: tools
page_number: 783
page_id: tools#page_783
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Configuring different foreground colors for a `PercentTextBox` control.
- Methods associated with foreground color settings.

## Content

### Foreground Settings of PercentTextBox

```csharp
Me.percentTextBox1.PositiveColor = System.Drawing.Color.ForestGreen
Me.percentTextBox1.NegativeColor = System.Drawing.Color.Orange
Me.percentTextBox1.ZeroColor = System.Drawing.Color.Orchid
```

![Foreground Settings of PercentTextBox](https://s3.example.com/3rd644.png "Figure 499: Foreground Settings of PercentTextBox")

### Methods Associated with Foreground Settings

| Methods                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Reset ForeColor          | Resets the forecolor of the control to its default value.                  |
| Reset Positive Color     | Resets the PositiveColor property to its default value.                    |
| Reset Negative Color     | Resets the NegativeColor property to its default value.                    |
| Reset Zero Color         | Resets the ZeroColor property to its default value.                       |
| SetControlColor          | Sets the forecolor of the control depending on whether the current value is negative. |
| ShouldSerializePositiveColor | Serializes the PositiveColor property.                              |
| ShouldSerializeNegativeColor | Serializes the NegativeColor property.                              |
| ShouldSerializeZeroColor | Serializes the ZeroColor property.                                    |

A sample which demonstrates the Foreground Settings of `PercentTextBox` control is available in the below sample installation path.

## API Reference

### PercetTextBox Properties

- **PercentTextBox.PositiveColor**:
  - Type: `System.Drawing.Color`
  - Description: Controls the color for positive values.
- **PercentTextBox.NegativeColor**:
  - Type: `System.Drawing.Color`
  - Description: Controls the color for negative values.
- **PercentTextBox.ZeroColor**:
  - Type: `System.Drawing.Color`
  - Description: Controls the color for zero values.

### Methods

- **ResetForeColor()**
  - Resets the forecolor of the control to its default value.
- **ResetPositiveColor()**
  - Resets the PositiveColor property to its default value.
- **ResetNegativeColor()**
  - Resets the NegativeColor property to its default value.
- **ResetZeroColor()**
  - Resets the ZeroColor property to its default value.
- **SetControlColor()**
  - Sets the forecolor of the control depending on whether the current value is negative.
- **ShouldSerializePositiveColor()**
  - Serializes the PositiveColor property.
- **ShouldSerializeNegativeColor()**
  - Serializes the NegativeColor property.
- **ShouldSerializeZeroColor()**
  - Serializes the ZeroColor property.

## Code Examples

#### Configuring Foreground Colors

```csharp
percentTextBox1.PositiveColor = System.Drawing.Color.ForestGreen;
percentTextBox1.NegativeColor = System.Drawing.Color.Orange;
percentTextBox1.ZeroColor = System.Drawing.Color.Orchid;
```

## Page-level Navigation/TOC

### Related Topics
- PercentTextBox Control Overview
- Customizing PercentTextBox Properties

<!-- tags: [Windows Forms, PercentTextBox, Color, UIComponent, Version11.4.0.26] keywords: [PercentTextBox, ForegroundColors,UI Customization, Syncfusion WinForms] -->
```