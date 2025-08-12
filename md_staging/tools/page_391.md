```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_391.jpeg
document_name: tools
page_number: 391
page_id: tools#page_391
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:32Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains border styling options for controls.
- Demonstrates code examples in C# and VB.NET for setting Border Style.
- Includes figure showing BorderStyle = "Etched".
- Describes button spacing adjustments using `UseVerticalAndHorizontalSpacing` property.

## Content

### Border Styles
The following options are available for configuring the Border Style of a control:

- SunkenInner
- Raised
- Sunken
- Etched
- Flat
- Adjust
- Bump

#### Code Examples for Setting Border Style
**C#**
```csharp
this.calculatorControl1.BorderStyle =
System.Windows.Forms.Border3DStyle.Etched;
```

**VB.NET**
```vb
this.calculatorControl1.BorderStyle =
System.Windows.Forms.Border3DStyle.Etched;
```

#### Figure: BorderStyle = "Etched"
![Calculator Control with Etched Border](#)
*Figure 196: BorderStyle = "Etched"*

#### Button Spacing
The default spacing between Calculator buttons can be modified by enabling the `UseVerticalAndHorizontalSpacing` property. The following properties control the horizontal and vertical spacing:

**Subsection: 3.5.2.3.3.2.4 Button Spacing**
The default spacing between the Calculator buttons can be modified by enabling the `UseVerticalAndHorizontalSpacing` property. The below properties controls the horizontal and vertical spacing.

## API Reference

### Properties
- **UseVerticalAndHorizontalSpacing**
  - Type: Boolean
  - Description: Enables or disables button spacing adjustments.
  - Default: `false`
  - Required: No

## Code Examples (multi-language supported)

### C#
```csharp
this.calculatorControl1.UseVerticalAndHorizontalSpacing = true;
```

### VB.NET
```vb
this.calculatorControl1.UseVerticalAndHorizontalSpacing = True
```

## Page-level Navigation/TOC (if applicable)
- Border Styles
- Code Examples for Setting Border Style
- Button Spacing

## Cross References
- See also: Syncfusion documentation on configuring control styles and spacing.

<!-- tags: [Syncfusion, WinForms, BorderStyles, ButtonSpacing, CalculatorControl] keywords: [BorderStyle, Etched, SunkenInner, Raised, Sunken, Flat, Adjust, Bump, UseVerticalAndHorizontalSpacing, C#, VB.NET] -->
```