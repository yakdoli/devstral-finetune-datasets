```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_174.jpeg
document_name: grid
page_number: 174
page_id: grid#page_174
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
imageList1.Images.Add(SystemIcons.Error.ToBitmap())

' Set the imagelist into the TableStyle.
gridControl1.TableStyle.ImageList = imageList1

' To use an image, set the ImageIndex in the cell GridInfoStyle.
gridControl1(rowIndex, colIndex + 1).CellType = "Static"
gridControl1(rowIndex, colIndex + 1).Text = "Static2"

' Show the third icon in the imagelist which, is inherited from TableStyle.
gridControl1(rowIndex, colIndex + 1).ImageIndex = 2
```

![Static Cells](https://example.com/static_cells.png)  
*Figure 92: Static Cells*

## 4.1.4.1.17 Text Box

A Text Box cell type displays text and images that can be edited in place.

The following code example illustrates how to set the cell type to TextBox.

### [C#]
```csharp
gridControl1[rowIndex, colIndex].Text = "TextBox";
gridControl1[rowIndex, colIndex].CellType = "TextBox";

// Text box with image - assumes Imagelist set the same Static sample code.
gridControl1[rowIndex, colIndex + 1].Text = "TextBox/Image";
gridControl1[rowIndex, colIndex].CellType = "TextBox";
gridControl1[rowIndex, colIndex + 1].ImageIndex = 1;
```

### [VB.NET]
```vb
gridControl1(rowIndex, colIndex).Text = "TextBox"
gridControl1(rowIndex, colIndex).CellType = "TextBox"

' Text box with image - assumes ImageList set the same Static sample code.
gridControl1(rowIndex, colIndex + 1).Text = "TextBox/Image"
```

## Page-level Navigation/TOC (if applicable)
- [C#]
- [VB.NET]

## Cross References
- [Essential Grid for Windows Forms]
- [Static Cells]
- [Text Box Cell Type]

### RAG Annotations
<!-- tags: [Essential Grid, Windows Forms, Text Box, Static Cells, Control, Property, Method] keywords: [imagelist, tablestyle, celltype, imageindex, textbox, static, image, place] -->

```