```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_884.jpeg
document_name: grid
page_number: 884
page_id: grid#page_884
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates a visual comparison of the Grid Grouping Control in Office 2007 Black and Silver themes.
- Shows how visual styles affect user interactions such as hovering and clicking on cells.

## Content
### Figure 347: Grid Grouping Control with Office 2007 Black Visual Style

<p>Here is the image showcasing the Grid Grouping Control with an Office 2007 Black visual style.</p>
- The figure highlights the different visual elements such as the DockStyle, Boolean, and Font settings.

<p><img alt="Figure 347: Grid Grouping Control with Office 2007 Black Visual Style" /></p>
### Figure 348: Grid Grouping Control with Office 2007 Silver Visual Style

<p>Here is the image showcasing the Grid Grouping Control with an Office 2007 Silver visual style.</p>
- The figure demonstrates a variation in visual elements and highlights how selection indicators change.
- The grid showcases changes in the appearance of cells when different styles are applied.

<p><img alt="Figure 348: Grid Grouping Control with Office 2007 Silver Visual Style" /></p>

<p>Since visual styles also affect how the cells behave, the cell controls are painted with a different gradient when users interact with them either by clicking or by hovering the mouse over them. Below is the image that exposes these cases.</p>
#### Figure 349: Highlighting Cells in the Grid when the Mouse Pointer moves or rests over the Cells

<p>Here is the image demonstrating the behavior and highlighting of cells in the Grid.</p>
- The figure shows how cells change appearance when the mouse hovers over them and when the user clicks.
- Two scenarios are depicted:
  - "When Mouse Hovers": This shows the cell appearance when the mouse pointer is over a cell.
  - "On Mouse Down": This shows the cell appearance when the mouse is clicked on a cell.

<p><img alt="Figure 349: Highlighting Cells in the Grid when the Mouse Pointer moves or rests over the Cells" /></p>

### Explanation of Visual Effects
- The images illustrate the hover and mouse-down states, showcasing the interactive features of the Grid Grouping Control.
- These visual cues provide feedback to the user and enhance the usability of the grid.

## Code Examples

### Example of Basic Grid Setup
```csharp
using Syncfusion.Windows.Forms;
using Syncfusion.Windows.Forms.Grid;

// Create a new Grid control
GridControl grid = new GridControl();

// Add mock data or set up the grid
grid.DataSource = yourData;

// Apply Office 2007 Black style
grid.SetStyle("Standard", new GridOffice2007BlackTheme());

// Apply Office 2007 Silver style
grid.SetStyle("Standard", new GridOffice2007SilverTheme());
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Grid
#### Properties
- `DockStyle`: Sets the docking style for the grid.
- `Boolean`: Represents a Boolean value for any grid-specific functionality.

#### Methods
- `SetStyle`: Method to apply predefined styles such as Office 2007 Black or Silver.

#### Events
- `MouseHover`: Triggered when the mouse pointer hovers over a cell.
- `MouseDown`: Triggered when the mouse is clicked on a cell.

## Issue Resolution Tips
- Ensure that the appropriate theme assemblies are referenced in the project.
- Test different themes to confirm they work as expected and provide visual feedback.

## Related Documentation
- See also: Syncfusion documentation for Grid Controls, themes, and styling.

<!-- tags: [essentials, grid, winforms, controls, visual styles, mouse interactions, office themes] keywords: [DockStyle, Boolean, Font, mouse hover, click, Office 2007 Black, Office 2007 Silver, highlighting, GridGroupingControl] -->
```