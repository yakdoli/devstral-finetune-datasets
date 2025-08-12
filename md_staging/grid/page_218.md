```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_218.jpeg
document_name: grid
page_number: 218
page_id: grid#page_218
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:08Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to set the cell type to PictureBox in a Windows Forms application.
- Provides code examples in both C# and VB.NET.
- Explains the process of assigning images to PictureBox cells.

## Content

The following code examples illustrate how to set the cell type to PictureBox.

### Using C#

```csharp
RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.PictureBox);
PictureBoxStyleProperties sp;
style = gridControl1[2, 2];
style.CellType = CustomCellTypes.PictureBox.ToString();
sp = new PictureBoxStyleProperties(style);
sp.Image = GetImage("one.jpg");
```

### Using VB.NET

```vbnet
RegisterCellModel.GridCellType(Me.gridControl1, CustomCellTypes.PictureBox)
Dim sp As PictureBoxStyleProperties
style = gridControl1(2, 2)
style.CellType = CustomCellTypes.PictureBox.ToString()
sp = New PictureBoxStyleProperties(style)
sp.Image = GetImage("one.jpg")
```

![Figure 115: Picture Box Cell](https://example.com/image-url)

### 4.1.4.4.10 Slider

## API Reference

### Methods

- `RegisterCellModel.GridCellType`
- `CustomCellTypes.PictureBox`
- `PictureBoxStyleProperties`
- `GetImage`

### Parameters

| Name       | Type                          | Description                           |
|------------|-------------------------------|---------------------------------------|
| gridControl1 | object | The grid control object to which the cell type is assigned. |
| CustomCellTypes.PictureBox | object | Specifies the PictureBox type for the cells. |
| sp | PictureBoxStyleProperties | The style properties for the PictureBox cell. |
| "one.jpg" | string | The path to the image file to be displayed in the PictureBox. |

## Code Examples

### C# Example

```csharp
RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.PictureBox);
PictureBoxStyleProperties sp;
style = gridControl1[2, 2];
style.CellType = CustomCellTypes.PictureBox.ToString();
sp = new PictureBoxStyleProperties(style);
sp.Image = GetImage("one.jpg");
```

### VB.NET Example

```vbnet
RegisterCellModel.GridCellType(Me.gridControl1, CustomCellTypes.PictureBox)
Dim sp As PictureBoxStyleProperties
style = gridControl1(2, 2)
style.CellType = CustomCellTypes.PictureBox.ToString()
sp = New PictureBoxStyleProperties(style)
sp.Image = GetImage("one.jpg")
```

## Page-level Navigation/TOC

- Using C#
- Using VB.NET
- 4.1.4.4.10 Slider

<!-- tags: [syncfusion, grid, windows forms, picturebox, c#, vb.net, api] keywords: [cell type, picture box, image, grid control, .net, windows forms, programming, code examples] -->
```