```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_169.jpeg
document_name: grid
page_number: 169
page_id: grid#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Provides details on configuring and handling push button cells in the Syncfusion Grid control for Windows Forms.
- Demonstrates how to set up push buttons with different appearances.
- Explains the event handling for push button clicks.

## Content

### Configuring Push Button Cells

The following examples demonstrate how to create and manage push button cells in the grid. The code snippets include configurations for setting the cell type, appearance, and handling click events.

#### Example in C#

```csharp
gridControl1[rowIndex, colIndex].Description = "PushButton1";
gridControl1[rowIndex, colIndex].CellType = "PushButton";
gridControl1[rowIndex, colIndex].CellAppearance = GridCellAppearance.Raised;

// To catch a click, hook up a CellButtonClicked handler.
gridControl1.CellButtonClicked += new GridCellButtonClickedEventHandler(gridControl1_CellButtonClicked);

// Add a handler.
private void gridControl1_CellButtonClicked(object sender, GridCellButtonClickedEventArgs e)
{
    MessageBox.Show("You clicked row " + e.RowIndex.ToString() + " col " + e.ColIndex.ToString());
}
```

#### Example in VB.NET

```vb
gridControl1(rowIndex, colIndex).Description = "PushButton1"
gridControl1(rowIndex, colIndex).CellType = "PushButton"
gridControl1(rowIndex, colIndex).CellAppearance = GridCellAppearance.Raised

' To catch a click, hook up a CellButtonClicked handler.
AddHandler gridControl1.CellButtonClicked, AddressOf gridControl1_CellButtonClicked

' Add a handler.
Private Sub gridControl1_CellButtonClicked(ByVal sender As Object, ByVal e As GridCellButtonClickedEventArgs)
    MessageBox.Show("You clicked row " + e.RowIndex.ToString() + " col " + e.ColIndex.ToString())
End Sub
```

### Push Button Cells: Flat, Raised or Sunken

The following figure illustrates the appearance of different types of push buttons in grid cells:

![Push Button Cells](./push_button_cells.png)

**Figure 89: Push Button Cells**

This example shows how to configure and handle push button cells, allowing users to interact with the grid in a more intuitive and customized manner.

## API Reference

### Properties
- `Description`: A string property used to set the display text of the push button.
- `CellType`: A property used to specify the type of cell, in this case `"PushButton"`.
- `CellAppearance`: Enum used to define the appearance of the push button, such as `Raised`, `Flat`, or `Sunken`.

### Events
- `CellButtonClicked`: An event triggered when a push button cell is clicked.

### Enumerations
- `GridCellAppearance`: Defines the appearance of the push button cells.

## Code Examples

### C# Example

```csharp
// Set up the push button cell
gridControl1[0, 0].Description = "PushButton1";
gridControl1[0, 0].CellType = "PushButton";
gridControl1[0, 0].CellAppearance = GridCellAppearance.Raised;

// Handle the click event
gridControl1.CellButtonClicked += new GridCellButtonClickedEventHandler(gridControl1_CellButtonClicked);

private void gridControl1_CellButtonClicked(object sender, GridCellButtonClickedEventArgs e)
{
    MessageBox.Show($"You clicked row {e.RowIndex}, column {e.ColIndex}");
}
```

### VB.NET Example

```vb
' Set up the push button cell
gridControl1(0, 0).Description = "PushButton1"
gridControl1(0, 0).CellType = "PushButton"
gridControl1(0, 0).CellAppearance = GridCellAppearance.Raised

' Handle the click event
AddHandler gridControl1.CellButtonClicked, AddressOf gridControl1_CellButtonClicked

Private Sub gridControl1_CellButtonClicked(ByVal sender As Object, ByVal e As GridCellButtonClickedEventArgs)
    MessageBox.Show($"You clicked row {e.RowIndex}, column {e.ColIndex}")
End Sub
```

## Cross References

- "Configuring Cell Types in the Grid"
- "Handling Grid Events"

<!-- tags: [Essential Grid, Windows Forms, Grid Control, Push Button, Cell Type, Cell Appearance, Button Click Event, C#, VB.NET, Syncfusion, Windows Forms] keywords: [grid, push button, cell type, cell appearance, button click event, cellButtonClicked, gridCellAppearance, raised, flat, sunken, grid control] -->
```