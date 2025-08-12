```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_177.jpeg
document_name: grid
page_number: 177
page_id: grid#page_177
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:00:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Figure 95: Removing BackColor from the Cell Specific Style

This figure demonstrates the precedence of different style settings in a grid. The grid displays various style objects, and their effects on the grid's appearance can be observed. The style objects listed include:

- **Standard GridStyleInfo**
- **Table GridStyleInfo**
- **Column2 GridStyleInfo**
- **Row3 GridStyleInfo**
- **Cell 3,2 GridStyleInfo**

The grid is colored as follows:
- Row 1: Blue (Standard GridStyleInfo)
- Row 3, Column B: Red (Table GridStyleInfo)
- Row : Yellow (Column2 GridStyleInfo)
- Row 3: Green (Row3 GridStyleInfo)
- Individual cell (Cell 3,2): Pink (Cell 3,2 GridStyleInfo)

### See Also

### 4.1.4.2.1.1 Properties

#### Overview
- Important details about GridStyleInfo properties are provided here.
- Control the appearance and behavior of grid cells using various properties.

#### Content

GridStyleInfo provides many properties to control the appearance and behavior of grid cells. The following table lists some of the properties.

| GridStyleInfo Property     | Description                      |
|----------------------------|-----------------------------------|
| String GridStyleInfo.Text | Formatted string value of the cell. |
| Object GridStyleInfo.CellValue | Value of the object stored in the cell. |
| BrushInfo GridStyleInfo.BackColor | Back color of the cell. |
| Color GridStyleInfo.TextColor | Color of the displayed text. |
| GridFontInfo GridStyleInfo.Font | Font used to display the text. |

## Code Examples

Example snippet demonstrating the usage of GridStyleInfo properties:

```csharp
// Example of setting GridStyleInfo properties
GridStyleInfo style = new GridStyleInfo();
style.BackColor = Color.Red;
style.TextColor = Color.White;
style.Font = new Font("Arial", 12, FontStyle.Bold);
```

### Notes
- Ensure that the properties are applied correctly to achieve the desired visual effect.
- The precedence of styles can be observed in the grid by checking the color of individual cells.

<!-- tags: [grid, gridstyleinfo, properties, backcolor, textcolor, font, windowsforms] keywords: [Essential Grid, GridStyleInfo, Properties, BackColor, TextColor, Font, Windows Forms, precedence] -->
```