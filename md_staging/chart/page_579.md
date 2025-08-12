```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_579.jpeg
document_name: chart
page_number: 579
page_id: chart#page_579
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:08Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to use the ImageList control to display images in a Grid control.
- Explains setting up and configuring the ImageList for the Grid control.
- Provides sample code in C# and VB.NET for implementing image display.

## Content

### Code Example: C#
```csharp
// Creates a new instance of the Imagelist class.
ImageList img = new ImageList();

// Adds the image to the Image collection of the Imagelist.
img.Images.Add(Image.FromFile(this.Name));

// Specify the size of the image.
img.ImageSize = new Size(256, 256);

// Set the imagelist of the cell.
this.gridControl1[1,1].ImageList = img;

// Specify the index for the image to be displayed.
this.gridControl1[1, 1].ImageIndex = 0;

// Specify the row and column height of the cell.
this.gridControl1.RowHeights[1] = 300;
this.gridControl1.ColWidths[1] = 300;

// Specify the image size mode.
this.gridControl1[1, 1].ImageSizeMode = GridImageSizeMode.CenterImage;
```

### Code Example: VB.NET
```vb
' Creates a new instance of the Imagelist class.
Dim img As ImageList = New ImageList()

' Adds the image to the Image collection of the Imagelist.
img.Images.Add(Image.FromFile(Me.Name))

' Specify the size of the image.
img.ImageSize = New Size(256, 256)

' Set the imagelist of the cell.
Me.gridControl1(1, 1).ImageList = img

' Specify the index for the image to be displayed.
Me.gridControl1(1, 1).ImageIndex = 0

' Specify the row and column height of the cell.
Me.gridControl1.RowHeights(1) = 300
Me.gridControl1.ColWidths(1) = 300
```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, GridControl, ImageList, C#, VB.NET] keywords: [ImageList, GridControl, ImageMode, CellProperties, CodeExample, Chart Documentation] -->
```