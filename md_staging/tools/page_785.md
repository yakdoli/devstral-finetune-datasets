```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_785.jpeg
document_name: tools
page_number: 785
page_id: tools#page_785
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:46Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- The page describes PercentTextBox Properties in Windows Forms applications.
- It details various properties and their descriptions relevant to defining and customizing the appearance of borders for controls.
- The examples provided include Border3DStyle, BorderColor, BorderSides, and BorderStyle, with their respective options and default settings.

## PercentTextBox Properties

### Border3DStyle

- **Description**: Indicates the style of the 3D border. The options included are:
  - RaisedOuter
  - SunkenOuter
  - RaisedInner
  - SunkenInner
  - Raised
  - Etched
  - Bump
  - Sunken
  - Adjust
  - Flat

  The default value is set to `'Sunken'`.

### BorderColor

- **Description**: Specifies the color of the 2D border.

### BorderSides

- **Description**: Indicates the border sides of the panel. The options included are:
  - Left
  - Top
  - Right
  - Bottom
  - Middle
  - All

### BorderStyle

- **Description**: Indicates whether the edit control should have a border. The options included are:
  - FixedSingle

## API Reference (if applicable)

- The exact members and their properties would be detailed in the API Reference section, including:
  - Namespace: `Syncfusion.Windows.Forms.Tools`
  - Class: `PercentTextBox`
  - Properties:
    - `Border3DStyle`
    - `BorderColor`
    - `BorderSides`
    - `BorderStyle`

## Code Examples (multi-language supported)

- Relevant code examples demonstrating the usage of these properties in a Windows Forms application would be provided using C# and other relevant languages.

### Example: Setting Border Style

```csharp
// Setting Border3DStyle to 'RaisedInner'
PercentTextBox.percentTextBox.Border3DStyle = Border3DStyle.RaisedInner;

// Setting BorderColor to Color.Red
PercentTextBox.percentTextBox.BorderColor = Color.Red;

// Setting BorderSides to include Top and Bottom sides
PercentTextBox.percentTextBox.BorderSides = BorderSides.Top | BorderSides.Bottom;

// Setting BorderStyle to FixedSingle
PercentTextBox.percentTextBox.BorderStyle = BorderStyle.FixedSingle;
```

## Tags and Keywords

<!-- tags: WindowsForms, PercentTextBox, BorderStyle, Border3DStyle, BorderColor, BorderSides keywords: PercentTextBox properties, Border styles, Windows Forms controls, Syncfusion WinForms -->
```