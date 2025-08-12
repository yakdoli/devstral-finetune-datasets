```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_391.jpeg
document_name: grid
page_number: 391
page_id: grid#page_391
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:11Z
fidelity: lossless
-->


## Overview
- Demonstrates how to change the back color of a grid using the `TableStyle` property.
- Explains setting row and column styles programmatically in both C# and VB.NET.
- Includes visual representation of modified grid appearance.

## Content

### Changing Grid BackColor Using TableStyle

The `TableStyle` property allows setting the background color for the entire grid, impacting cells whose backcolor is not explicitly set.

#### Code Example: C#
```csharp
// Change the back color of the grid by using TableStyle.
this.gridControl1.TableStyle.BackColor = Color.FromArgb(255, 192, 192);
```

#### Code Example: VB.NET
```vb
' Change the back color of the grid using TableStyle.
Me.gridControl1.TableStyle.BackColor = Color.FromArgb(255, 192, 192)
```

**Figure 141: Changing the TableStyle BackColor Property Adds a Rose Background for Cells Whose BackColor Was Not Explicitly Set**

![Grid with Rose Background](https://...)

### Modifying Row and Column Styles

Individual row and column styles can be customized to alter appearance, such as text color and cell values.

#### Code Example: C#
```csharp
// Change a row style and a column style.
this.gridControl1.RowStyles[3].TextColor = Color.Blue;
this.gridControl1.RowStyles[3].CellValue = "Blue";
this.gridControl1.ColStyles[3].TextColor = Color.Red;
this.gridControl1.ColStyles[3].CellValue = "Red";
```

#### Code Example: VB.NET
```vb
' Change a row style and a column style.
Me.gridControl1.RowStyles(3).TextColor = Color.Blue
Me.gridControl1.RowStyles(3).CellValue = "Blue"
Me.gridControl1.ColStyles(3).TextColor = Color.Red
Me.gridControl1.ColStyles(3).CellValue = "Red"
```

### Summary

This section demonstrates programmatically altering the appearance of a Syncfusion grid control by:
- Setting the background color using `TableStyle`.
- Customizing row and column styles to meet specific design requirements.

<!-- tags: grid, tablestyle, rowstyles, colstyles, windowsforms keywords: background color, row style, column style, programmatically, syncfusion -->
```