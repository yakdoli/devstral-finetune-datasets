```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_202.jpeg
document_name: grid
page_number: 202
page_id: grid#page_202
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates various cell types and functionalities in the Essential Grid for Windows Forms.
- Provides examples of custom cell types, such as derived cells, tree node cells, and dropdown cells.
- Highlights integration with other controls, including LinkLabel, GridCell controls, and visual components like ImageBox, DateTimePicker, and Slider.

## Content

### Samples and Descriptions

| Sample                   | Description                                                                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ExcelSelectionMarker     | Has a derived celltype that displays in a cell a BMP that is stored in the GridStyleInfo.Tag for that cell.                                     |
| GridDataBoundImageCell   | Has two cell-derived cell types. Both display picture data stored in a database in a grid cell. One displays the picture directly in the grid cell with several choices regarding how the image is fit to the cell. The second celltype is a dropdown cell that displays a picture box when you click the cell. |
| VirtTreeGrid             | Has an expandable tree node cell with an indentation property. This celltype is used in this example to make the grid have collapsible rows, and generally functions as a multicolumn tree control. |
| 3. LinkLabelCells        | Has a LinkLabel-derived cell type. This cell type allows you to place a link in a GridCell, and then launch the link in a browser window by clicking the link.                                               |
| CellButtons              | Shows two different types of derived cell controls with buttons. The first is an ellipsis cell that displays further information when you click the button. This particular cell uses a bitmap button to display the ellipsis. The second custom cell type in this sample is a bar of three buttons that display different drag effects as you mouse down and drag. |
| Drop-down grid           | Shows how you can drop a new grid in a cell. This sample is useful as it shows how to pass keystrokes onto the control that is embedded in the grid. For example, you may want the dropped grid to handle the ARROW keys, but not have the ARROW keys move to another cell in the parent grid.            |
| CalendarCells            | Shows how you can drop a Windows Forms DateTimePicker in a cell.                                                                                     |
| SliderCells              | Shows how you can drop a Windows Forms                                                                                 |

## API Reference

### Grid-related Components

- **GridStyleInfo.Tag**: Used to store metadata for cells, such as BMP images for ExcelSelectionMarker.
- **GridCell**: A base class for all cell types, supporting link launching and integration with external controls.
- **GridDataBoundImageCell**: Serves to display and manage images derived from database sources.

## Code Examples

```csharp
// Example: Using LinkLabel in GridCell
GridCell linkCell = new GridLinkCell(
    url: "https://www.example.com",
    textDisplayInCell: "Click here"
);
linkCell.OnLinkClicked += (s, e) =>
{
    System.Diagnostics.Process.Start(e.Url);
};
``` 

## Cross References

- Refer to the documentation on [LinkLabel](#) for more information on integrating web links.
- For more details on Tree Grids, see [TreeGrid Documentation](#).

## RAG Annotations

<!-- tags: [syncfusion, windowsforms, grid, celltypes, linklabel, datetimepicker, slider, treenode] keywords: [cell, grid, dropdown, image, calendar, slider, clickable link, arrow keys, indentation, derived celltypes, database-bound image] -->
```