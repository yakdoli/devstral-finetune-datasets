```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_479.jpeg
document_name: tools
page_number: 479
page_id: tools#page_479
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:15:38Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page describes various border options for controls in Windows Forms.
- Includes details on border styles, sides, colors, and border thickness.
- Focuses on configuring the look and feel of controls like `DateTimePickerAdv`.

## Content

### Border Styles
The border styles allow customization of the visual appearance of controls. Here are the options:

- **Raised**
- **RaisedOuter**
- **RaisedInner**
- **Sunken (Default)**
- **SunkenOuter**
- **SunkenInner**
- **Etched**
- **Bump**
- **Adjust**
- **Flat**

### BorderSingle
Specifies the 2D border style of the DateTimePickerAdv. The options are:

- **None**
- **Dotted**
- **Dashed**
- **Solid (default)**
- **Inset**
- **Outset**

### BorderSides
Specifies the sides of the control which should have a border. The sides are:

- **Left**
- **Top**
- **Right**
- **Bottom**
- **Middle**
- **All (Default)**

### BorderColor
Specifies the color of the 2D border when `BorderStyle` is set to `FixedSingle`.

### Example Usage

```csharp
DateTimePickerAdv dateTimePicker = new DateTimePickerAdv();
dateTimePicker.BorderStyle = BorderStyles.Sunken; // Example of setting a border style
dateTimePicker.BorderSingle = BorderStyles.Solid; // Example of setting a 2D border style
dateTimePicker.BorderSides = BorderSides.All; // Example of setting all sides for the border
dateTimePicker.Border.Color = Color.Blue; // Example of setting the border color
```

## API Reference

### Namespace: Syncfusion.Windows.Forms

#### Properties
- **BorderStyle**: Gets or sets the border style of the control.
- **BorderSingle**: Gets or sets the 2D border style of the control.
- **BorderSides**: Gets or sets the sides of the control which should have a border.
- **BorderColor**: Gets or sets the color of the 2D border when BorderStyle is set FixedSingle.

### Parameters

| Name           | Type               | Description                                                                 | Default             | Required |
|----------------|--------------------|-----------------------------------------------------------------------------|---------------------|----------|
| BorderStyle    | BorderStyles       | Specifies the border style of the control.                                 | Sunken              | No       |
| BorderSingle   | BorderStyles       | Specifies the 2D border style of the control.                              | Solid               | No       |
| BorderSides    | BorderSides        | Specifies the sides of the control which should have a border.             | All                 | No       |
| BorderColor    | Color              | Specifies the color of the 2D border when BorderStyle is set FixedSingle. | Default Color       | No       |

## Code Examples

### Setting Border Properties in C#

```csharp
using Syncfusion.Windows.Forms;

DateTimePickerAdv dateTimePicker = new DateTimePickerAdv();
dateTimePicker.BorderStyle = BorderStyles.RaisedOuter;
dateTimePicker.BorderSingle = BorderStyles.Dashed;
dateTimePicker.BorderSides = BorderSides.Middle;
dateTimePicker.Border.Color = Color.Red;
```

### Setting Border Properties in VB.NET

```vb
Imports Syncfusion.Windows.Forms

Dim dateTimePicker As New DateTimePickerAdv()
dateTimePicker.BorderStyle = BorderStyles.RaisedOuter
dateTimePicker.BorderSingle = BorderStyles.Dashed
dateTimePicker.BorderSides = BorderSides.Middle
dateTimePicker.Border.Color = Color.Red
```

## Page-level Navigation/TOC

- Border Styles
- BorderSingle
- BorderSides
- BorderColor

## Cross References

See also:
- `BorderStyle` documentation for detailed explanations.
- `DateTimePickerAdv` control properties and methods.

## RAG Annotations
<!-- tags: Border Styles, BorderSingle, BorderSides, BorderColor, Windows Forms, DateTimePickerAdv, Syncfusion WinForms keywords: border, control, customization, appearance, datetimepicker, Windows Forms -->
```