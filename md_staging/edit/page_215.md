```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_215.jpeg
document_name: edit
page_number: 215
page_id: edit#page_215
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:54Z
fidelity: lossless
-->
# Essential Edit for Windows Forms

## Overview
- Exploring the various pattern styles available for use in Windows Forms.
- Detailed list of pattern options to customize the appearance of controls.
- Understanding and applying different patterns to enhance the visual appeal and functionality of forms.

## Content

### Pattern Styles
The following list outlines the available pattern styles that can be applied using the `Edit` control in Windows Forms. These styles are categorized based on their visual characteristics, such as diagonal lines, horizontal/vertical lines, and decorative patterns.

#### Diagonal Patterns
- DiagonalCross
- Percent05
- Percent10
- Percent20
- Percent25
- Percent30
- Percent40
- Percent50
- Percent60
- Percent70
- Percent75
- Percent80
- Percent90

#### Light/Dark Diagonal Patterns
- LightDownwardDiagonal
- LightUpwardDiagonal
- DarkDownwardDiagonal
- DarkUpwardDiagonal

#### Wide Diagonal Patterns
- WideDownwardDiagonal
- WideUpwardDiagonal

#### Vertical Patterns
- LightVertical
- NarrowVertical
- DarkVertical

#### Horizontal Patterns
- LightHorizontal
- NarrowHorizontal
- DarkHorizontal

#### Dashed Patterns
- DashedDownwardDiagonal
- DashedUpwardDiagonal
- DashedHorizontal
- DashedVertical

#### Confetti Patterns
- SmallConfetti
- LargeConfetti

#### Decorative Patterns
- ZigZag
- Wave

#### Brick Patterns
- DiagonalBrick
- HorizontalBrick

#### Weave and Plaid Patterns
- Weave
- Plaid

#### Other Patterns
- Divot
- DottedGrid
- DottedDiamond
- Shingle
- Trellis
- Sphere
- SmallGrid

## Code Examples
To apply these patterns programmatically, you can use the following C# code snippet as an example:

```csharp
// Import necessary namespaces
using Syncfusion.Windows.Forms.Edit.Printing;

// Example: Applying a specific pattern to the Edit control
Edit editControl = new Edit();
editControl.Pattern = ThemeStylePattern.DiagonalCross; // Select a pattern from the list above

// Additional customization (optional)
editControl.PatternForeground = System.Drawing.Color.Gray;
editControl.PatternBackground = System.Drawing.Color.White;
```

### API Reference
- **Namespace:** Syncfusion.Windows.Forms.Edit
- **Class:** Edit
- **Property:** `Pattern`
  - Type: `ThemeStylePattern`
  - Description: Sets or gets the pattern style for the control.
- **Enum:** `ThemeStylePattern`
  - Lists all the available pattern styles.

## Cross References
- Refer to theofficial Syncfusion documentation for more details on setting and customizing patterns in Windows Forms.
- See the example section for practical applications of these patterns.

<!-- tags: [Syncfusion, Windows Forms, ThemeStylePattern, Edit control, pattern styles, version 11.4.0.26] keywords: [pattern, diagonal, horizontal, vertical, dashed, confetti, brick, weave, plaid, dotted, sphere, grid] -->
```