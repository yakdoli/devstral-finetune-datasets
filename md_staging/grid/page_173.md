```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_173.jpeg
document_name: grid
page_number: 173
page_id: grid#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:00:23Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the functionality and usage of Static cells in the Essential Grid control.
- Details how to set up Static cells and how they behave in a grid display.
- Includes examples in both C# and VB.NET for configuring Static cells with or without images.

## Static Cell Type in Essential Grid

**Static cell type** will display text that cannot be edited. You can select it to make it the current cell, but the cell cannot be activated for editing. Static cells can be deleted by the user if they are part of the selection when the DELETE key is pressed (To prevent this deletion behavior, set static cells to ReadOnly). Static cells may also include an image in addition to the text.

### Example Code: Setting Cell Type to Static

#### C#
```csharp
// Use a static cell.
gridControl[rowIndex, colIndex].CellType = "Static";
gridControl[rowIndex, colIndex].Text = "Static";

// Use a static cell with an image.
// Create an image list and add some images during the initialization.
ImageList imageList1 = new ImageList();
imageList1.Images.Add(SystemIcons.Warning.ToBitmap());
imageList1.Images.Add(SystemIcons.Application.ToBitmap());
imageList1.Images.Add(SystemIcons.Asterisk.ToBitmap());
imageList1.Images.Add(SystemIcons.Error.ToBitmap());

// Set the imagelist into the TableStyle.
gridControl.TableStyle.ImageList = imageList1;

// To use an image, set the ImageIndex in the cell GridInfoStyle.
gridControl[rowIndex, colIndex + 1].CellType = "Static";
gridControl[rowIndex, colIndex + 1].Text = "Static2";

// Show the third icon in the imagelist which is inherited from the TableStyle.
gridControl[rowIndex, colIndex + 1].ImageIndex = 2;
```

#### VB.NET
```vb.net
' Use a static cell.
gridControl(rowIndex, colIndex).CellType = "Static"
gridControl(rowIndex, colIndex).Text = "Static"

' Use a static cell with an image.
' Create an image list and add some images during the initialization.
Dim imageList1 As New ImageList()
imageList1.Images.Add(SystemIcons.Warning.ToBitmap())
imageList1.Images.Add(SystemIcons.Application.ToBitmap())
imageList1.Images.Add(SystemIcons.Asterisk.ToBitmap())
```

## API Reference
- **gridControl**: The main object representing the grid control.
- **CellType**: Property to set the type of the cell.
- **Text**: Property to set the textual content of the cell.
- **ImageList**: Class to manage a list of images for icons.
- **ImageIndex**: Property to specify which image from the list to display.

## Code Examples
- Demonstrates how to configure a Static cell with both text and image options.
- Includes the creation and assignment of an `ImageList` to the grid control.

## Cross References
- See also: Documentation on other cell types and grid customization options for more information.

<!-- tags: Syncfusion Windows Forms, Grid Control, Static Cell, Image List, CellType, ReadOnly, ImageIndex keywords: Static cell, Grid control, ImageList, readonly, imageindex -->
```