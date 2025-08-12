```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_217.jpeg
document_name: grid
page_number: 217
page_id: grid#page_217
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The following code examples illustrate how to set the cell type to LinkLabelCell.

## Content

### Overview
- Demonstrates how to set a cell type to LinkLabelCell using both C# and VB.NET.
- Includes examples of configuring text, font style, and a link URL for the cell.

### Using C#
```csharp
RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.LinkLabelCell);
int rowIndex = 5;
gridControl1[rowIndex, 2].CellType = CustomCellTypes.LinkLabelCell.ToString();
gridControl1[rowIndex, 2].Text = "Syncfusion, Inc.";
gridControl1[rowIndex, 2].Font.Bold = true;
gridControl1[rowIndex, 2].Tag = "http://www.syncfusion.com";
```

### Using VB.NET
```vbnet
RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.LinkLabelCell)
Dim rowIndex As Integer = 5
gridControl1(rowIndex, 2).CellType = CustomCellTypes.LinkLabelCell.ToString()
gridControl1(rowIndex, 2).Text = "Syncfusion, Inc."
gridControl1(rowIndex, 2).Font.Bold = True
gridControl1(rowIndex, 2).Tag = "http://www.syncfusion.com"
```

#### Figure 114: "Link Label Cell" Cells
![Link Label Cell](https://example.com/link_label_cell_image.png)

Figure 114: "Link Label Cell" Cells

### 4.1.4.4.9 Picture Box

#### Overview
- Explains how to embed a Picture Box cell type into a grid.
- Details the process of calculating the picture's size and adjusting the cell dimensions.

### Content
The Picture Box cell type can be embedded into a cell by calculating the size of the picture, and extending the width and height of the cell accordingly. The `PictureBoxStyleProperties` class provides the style where it holds the information of the picture that has to be added.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** PictureBoxStyleProperties
  - Provides the style for a picture box cell type.
  - Contains properties to define the picture's dimensions and display options.

## Code Examples
### Embedding a Picture Box Cell
#### C#
```csharp
// Example of embedding a picture box cell
gridControl1[rowIndex, 2].CellType = "PictureBox";
gridControl1[rowIndex, 2].Style = new PictureBoxStyleProperties()
{
    Image = new Bitmap("path_to_image.png"),
    StretchToFit = true,
    ShowBorder = false
};
```

#### VB.NET
```vbnet
' Example of embedding a picture box cell
gridControl1(rowIndex, 2).CellType = "PictureBox"
gridControl1(rowIndex, 2).Style = New PictureBoxStyleProperties() With {
    .Image = New Bitmap("path_to_image.png"),
    .StretchToFit = True,
    .ShowBorder = False
}
```

## Cross References
- Refer to the "PictureBoxStyleProperties" class documentation for more information.

<!-- tags: [Syncfusion Winforms, Grid, LinkLabelCell, PictureBox, CellStyle, CustomCellTypes, RegisterCellModel] keywords: [LinkLabelCell, Picture Box, Grid, CellType, Tag, Font, Bold, Size, StyleProperties] -->
```