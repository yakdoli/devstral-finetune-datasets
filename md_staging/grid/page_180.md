```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_180.jpeg
document_name: grid
page_number: 180
page_id: grid#page_180
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to display images in grid cells using the `ImageList` and `ImageIndex` properties.
- Explains the relationship between the `Text` and `CellValue` properties in grid controls.

## Content

### Displaying an Image in a Cell

The following code snippet shows how to display an image in a grid cell using the `ImageList` and `ImageIndex` properties:

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    this.gridControl1.TableStyle.ImageList = this.imageList1;
    this.gridControl1[2, 1].ImageIndex = 0;
}
```

**Figure 98: Displaying an Image in a Cell by using ImageList and ImageIndex Properties**

![](https://i.imgur.com/undefined.png)

### 4.1.4.2.1.1.4 Text and CellValue

The `Text` and `CellValue` properties are closely related. You can set the value of either by using the other. The major difference is that the `Text` property is a string and the `CellValue` property is an object. This means, for example, that you can assign a `DateTime` object to a cell value, but you cannot assign it to a text. Grid control generally sets the `Text` property by using the `CultureInfo` formatting on the `CellValue` property. The `Text` property can also be set directly through code.

## API Reference

- **Properties**
  - `ImageList`: Specifies the `ImageList` control used for displaying images in grid cells.
  - `ImageIndex`: Specifies the index of the image to display in a specific cell.
  - `Text`: Specifies the text displayed in the cell.
  - `CellValue`: Specifies the value stored in the cell.

## Code Examples

### Displaying an Image in a Grid Cell

```csharp
// Assign the ImageList to the grid's TableStyle property
this.gridControl1.TableStyle.ImageList = this.imageList1;

// Set the ImageIndex for a specific cell
this.gridControl1[2, 1].ImageIndex = 0;
```

### Setting Text and CellValue

```csharp
// Setting the CellValue
this.gridControl1[2, 1].CellValue = DateTime.Now;

// Setting the Text directly
this.gridControl1[2, 1].Text = "Custom Text";
```

## Cross References

- Refer to the documentation on `ImageList` and `ImageIndex` for more details on how to manage images in grid controls.
- For information on `CultureInfo` formatting, see the section on globalization and localization in the grid control documentation.

<!-- tags: [Syncfusion Winforms, Grid, ImageList, ImageIndex, Text, CellValue] keywords: [grid, imageList, imageIndex, text, cellValue, datetime, cultureInfo, formatting] -->
```