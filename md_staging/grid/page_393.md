```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_393.jpeg
document_name: grid
page_number: 393
page_id: grid#page_393
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explanation of how to edit cell styles through the designer.
- Instructions on creating a Grid object by adding a Grid control to a form.

## Content

### 4.1.4.7.3.1.2 Through Designer
To edit cell styles from the designer, you must select the grid on the design surface and then click the **Toggle Interactive Mode** verb shown at the bottom of the **PropertyGrid**. This will allow you to select the cells that are within the Grid control on the design surface. To change any of the style settings of the selected cells, you must first click the Cell Settings tool bar button at the top of the PropertyGrid. This will display the cell style settings that are within the PropertyGrid and will allow you to change them. The changes will affect the currently selected range or the current cell if no range is selected.

![Toggle Interactive Mode Verb and CellSettings Button](https://example.com/image-url)

### 4.1.4.7.3.2 Creating a Grid Object
To add a Grid control to a form, you must create an instance of the Grid control, set the row and column count, then position it on your form.

It comprises the following sections:

#### Sections
1. Creating an instance of the Grid control.
2. Setting the row and column count.
3. Positioning the Grid control on the form.

## Code Examples
Example of adding a Grid control to a form:

```csharp
// Create an instance of the Grid control
Syncfusion.Windows.Forms.Grid.GridControl grid1 = new Syncfusion.Windows.Forms.Grid.GridControl();

// Set the row and column count
grid1.RowCount = 10;
grid1.ColCount = 5;

// Position the Grid control on the form
grid1.Location = new System.Drawing.Point(10, 10);
grid1.Size = new System.Drawing.Size(400, 200);

// Add the Grid control to the form
this.Controls.Add(grid1);
```

## RAG Annotations
<!-- tags: [WinForms, Syncfusion, Grid, Designer, Cell Styles] keywords: [PropertyGrid, Toggle Interactive Mode, Cell Settings, GridControl, row count, column count] -->
```