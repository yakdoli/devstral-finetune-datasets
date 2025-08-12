```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_190.jpeg
document_name: grid
page_number: 190
page_id: grid#page_190
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The below table provides an overview of various styling options in GridStyleInfo properties.

| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| 2 | Interior |  |  |  |  |  |
| 3 | ■ | ■ | ■ | ■ | ■ | ■ |
| 4 | ■ | ■ | ■ | ■ | ■ | ■ |
| 5 | ■ | ■ | ■ | ■ | ■ | ■ |
| 6 | ■ | ■ | ■ | ■ | ■ | ■ |
| 8 | Font |  |  |  |  |  |
| 9 | Bold | Italic | Regular | Strikeout | Underline | Bold, Italic |
| 12 | TextColor |  |  |  |  |  |
| 13 | Black | Red | Blue | Green | Yellow | DimGray |
| 15 | Borders |  |  |  |  |  |
| 16 | Solid; Black | ■ | ■ | ■ | ■ | ■ |
| 17 | Dashed; Black | ■ | ■ | ■ | ■ | ■ |
| 19 | Orientation |  |  |  |  |  |
| 20 | Angle = 0 | Angle = 45 | Angle = 60 | Angle = 90 | Angle = 180 | Angle = 270 |

## Overview

- **Interior**: Allows you to specify a solid, gradient, or pattern style for a cell's background.
- **Font**: Includes style options such as Bold, Italic, Underline, etc., for cell text.
- **TextColor**: Supports various text colors for cell content.
- **Borders**: Offers multiple border styles including Solid, Dashed, Dotted, etc., with color options.
- **Orientation**: Allows cell content to be oriented at different angles.

## Content

### Interior Property

The `Interior` property lets you specify a solid, gradient, or pattern style for a cell's background.

#### Underlying API Class

The grid cells can be painted using the `Interior` property under the `Syncfusion.Drawing.BrushInfo` class. The `BrushInfo` class holds information about filling the background of a grid cell. 

- **PatternStyle**: Specifies the pattern style to be used.
- **GradientStyle**: Specifies the gradient style to be used.

#### Example Using C#

```csharp
[C#]
```

### Font Property

The `Font` property allows you to specify various text formatting options such as Bold, Italic, Underline, etc., for the cell content.

### TextColor Property

The `TextColor` property enables you to specify the color of the text within the cell.

### Borders Property

The `Borders` property provides options to customize the border style of the cell, including different patterns like solid, dashed, dotted, etc., along with color specifications.

### Orientation Property

The `Orientation` property allows you to set the orientation of the cell content at specific angles, such as 0, 45, 90, 180, or 270 degrees.

## API Reference

### Classes and Properties

- **Syncfusion.Drawing.BrushInfo**
  - **PatternStyle**: Specifies the pattern style to be used.
  - **GradientStyle**: Specifies the gradient style to be used.

### Methods
- **Solid; Black**: Returns a solid black border style.
- **Dotted; Red**: Returns a dotted red border style.
- **Dashed; Black**: Returns a dashed black border style.
- **DashDot**: Returns a dash-dot border style.
- **DashDotDot**: Returns a dash-dot-dot border style.

### Events
- **OrientationChanged**: Triggered when the orientation of the cell content changes.

## Code Examples

### C# Example

```csharp
[C#]
```

## Page-level Navigation/TOC (if applicable)

- Interior Property
- Font Property
- TextColor Property
- Borders Property
- Orientation Property

## Cross References

- See also: [Syncfusion Grid Documentation](#syncfusion-grid-documentation)

<!-- tags: [Syncfusion, Grid, Windows Forms, Interior, Font, TextColor, Borders, Orientation] keywords: [GridStyleInfo, font styles, text color, border styles, cell orientation, c#, documentation] -->
```