```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_392.jpeg
document_name: tools
page_number: 392
page_id: tools#page_392
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:05Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Introduces essential tools for configuring and customizing Windows Forms controls.
- Focuses on advanced spacing customization in a Calculator control using properties like `UseVerticalAndHorizontalSpacing`, `HorizontalSpacing`, and `VerticalSpacing`.

## Content

### CalculatorControl Properties

The following table explains the properties and their descriptions for customizing spacing in a Calculator control:

| CalculatorControl Properties         | Description                                                                                                                                                                                                 |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UseVerticalAndHorizontalSpacing       | Specifies whether horizontal and vertical spacing can be set using HorizontalSpacing and VerticalSpacing properties. By default it is false.                                                             |
| HorizontalSpacing                     | Sets horizontal spacing between buttons. The default value is 10. UseVerticalAndHorizontalSpacing must be set to true.                                                                                 |
| VerticalSpacing                       | Sets vertical spacing between buttons. The default value is 10. UseVerticalAndHorizontalSpacing must be set to true.                                                                                 |

### Code Examples

#### C#
```csharp
this.calculatorControl1.UseVerticalAndHorizontalSpacing = true;
this.calculatorControl1.HorizontalSpacing = 5;
this.calculatorControl1.VerticalSpacing = 5;
```

#### VB.NET
```vb
Me.calculatorControl1.UseVerticalAndHorizontalSpacing = True
Me.calculatorControl1.HorizontalSpacing = 5
Me.calculatorControl1.VerticalSpacing = 5
```

### Visual Example

The following image demonstrates the effect of setting `HorizontalSpacing` and `VerticalSpacing` to "5":

![HorizontalSpacing = "5"; VerticalSpacing = "5"](image.png)

**Figure 197: HorizontalSpacing = "5"; VerticalSpacing = "5"**

## API Reference

### Properties
- **UseVerticalAndHorizontalSpacing**
  - Type: `bool`
  - Description: Enables or disables the ability to set `HorizontalSpacing` and `VerticalSpacing`. Defaults to `false`.
- **HorizontalSpacing**
  - Type: `int`
  - Description: Sets the horizontal spacing between buttons. Requires `UseVerticalAndHorizontalSpacing` to be `true`. Defaults to `10`.
- **VerticalSpacing**
  - Type: `int`
  - Description: Sets the vertical spacing between buttons. Requires `UseVerticalAndHorizontalSpacing` to be `true`. Defaults to `10`.

## Code Examples

The above code examples demonstrate how to configure these properties in both C# and VB.NET.

## Page-level Navigation/TOC (if applicable)
- [Getting Started](#getting-started)
- [Customizing Spacing](#customizing-spacing)
- [Code Examples](#code-examples)
- [API Reference](#api-reference)

### Getting Started
- Explore the basic setup for customizing spacing in a CalculatorControl.

### Customizing Spacing
- Learn how to adjust `HorizontalSpacing` and `VerticalSpacing` to modify the layout of buttons.

### Code Examples
- View sample code in both C# and VB.NET to apply the spacing configurations.

### API Reference
- Access detailed descriptions of the properties involved in spacing customization.

<!-- tags: [Syncfusion Winforms, CalculatorControl, Spacing, Controls] keywords: [UseVerticalAndHorizontalSpacing, HorizontalSpacing, VerticalSpacing, C#, VB.NET, Windows Forms, Customization] -->
```