```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_769.jpeg
document_name: tools
page_number: 769
page_id: tools#page_769
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:29Z
fidelity: lossless
-->

## Overview
- Describes the settings of the `PercentSymbol` property forpercentage display in Windows Forms.
- Explains how to configure the grouping size of percent digits using the `Int32 Collection Editor` for `PercentGroupSizes`.
- Demonstrates sample codes in C# and VB.NET for setting various display properties of the `PercentTextBox` control.
- Illustrates the settings in a screenshot and directs to a sample application for demonstration purposes.

## Content

### PercentSymbol Property

| Property             | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| PercentSymbol        | Gets / sets the percent symbol which represents the Percentage.           |

The grouping size of the percent digits can be set using the `Int32 Collection Editor`, which will be displayed on selecting the `PercentGroupSizes` property in the property grid.

#### Code Examples

##### C#
```csharp
this.percentTextBox1.PercentDecimalDigits = 3;
this.percentTextBox1.PercentDecimalSeparator = ".";
this.percentTextBox1.PercentGroupSeparator = ",";
this.percentTextBox1.PercentGroupSizes = new int[] {5};
this.percentTextBox1.PercentNegativePattern = 2;
this.percentTextBox1.NegativeSign = "-";
this.percentTextBox1.PercentPositivePattern = 2;
this.percentTextBox1.PercentSymbol = "%";
```

##### VB.NET
```vb
Me.percentTextBox1.PercentDecimalDigits = 3
Me.percentTextBox1.PercentDecimalSeparator = "."
Me.percentTextBox1.PercentGroupSeparator = ","
Me.percentTextBox1.PercentGroupSizes = New Integer () {5}
Me.percentTextBox1.PercentNegativePattern = 2
Me.percentTextBox1.NegativeSign = "-"
Me.percentTextBox1.PercentPositivePattern = 2
Me.percentTextBox1.PercentSymbol = "%"
```

### Display Settings

The following screenshot illustrates the above settings.

![Display Settings of PercentTextBox](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAAP0lEQVR42mNk+A8AAQMB42+fAITkAAAAASUVORK5CYII=)

**Figure 485: Display Settings of PercentTextBox**

### Sample Application

A sample which demonstrates the Display Settings of PercentTextBox control is available in the below sample installation path:

- `.My Documents\Syncfusion\EssentialStudio\<Version Number>\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls`

## API Reference

This section provides a brief reference to the `PercentTextBox` control's properties used in the examples:

- **PercentDecimalDigits**: Gets or sets the number of digits after the decimal point.
- **PercentDecimalSeparator**: Gets or sets the separator character used for decimals.
- **PercentGroupSeparator**: Gets or sets the separator character used for grouping digits.
- **PercentGroupSizes**: Gets or sets the size of each group of digits in the percent display.
- **PercentNegativePattern**: Gets or sets the format for negative percentages.
- **NegativeSign**: Gets or sets the character used for indicating negative values.
- **PercentPositivePattern**: Gets or sets the format for positive percentages.
- **PercentSymbol**: Gets or sets the percent symbol used to represent percentages.

## Code Examples

### C# Example
The above code snippet in C# demonstrates how to configure the `PercentTextBox` control with specific formatting settings.

### VB.NET Example
The VB.NET example mirrors the C# example, providing an equivalent configuration for the `PercentTextBox` control.

## Cross References

For more detailed information about configuring UI controls and working with percentage formatting, refer to the following:

- [Syncfusion Documentation: PercentTextBox](https://www.syncfusion.com/documentation/windowsforms/tools/percenttextbox)
- [Syncfusion Samples: PercentTextBox Demonstration](https://www.syncfusion.com/downloads/support/demos/windowsforms)

## Additional Notes

The `PercentTextBox` control in Syncfusion WinForms provides extensive customization options for displaying percentage values, catering to different regional and formatting requirements.

<!-- tags: [Syncfusion, Windows Forms, PercentTextBox, Display Settings, Percentage Formatting] keywords: [PercentSymbol, PercentGroupSizes, DecimalSeparator, GroupSeparator, NegativePattern, PositivePattern, PercentDecimalDigits, PercentSymbol, C#, VB.NET, Sample Application, Windows Forms, Display Settings] -->
```