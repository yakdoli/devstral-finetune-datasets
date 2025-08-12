```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_588.jpeg
document_name: grid
page_number: 588
page_id: grid#page_588
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:26:23Z
fidelity: lossless
 -->

## Overview

- This page details the properties and behaviors of the `Grid` control in SyncfusionWinForms, focusing on customization options for rows, columns, headers, and overall appearance.
- It introduces various properties that control user interaction, display, and customization of grid elements.
- Key functionalities include enabling row addition, deletion, resizing of rows and columns, and setting visual properties like grid colors and header visibility.

## Content

### Grid Control Properties

The `Grid` control in SyncfusionWinForms allows extensive customization through various properties. Below is a summary of key properties and their functionalities:

| Property Name                      | Property Name (Alternative/Mapping) | Description                                                                                                                                                      |
|------------------------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                   |                                      | whether the control can accept data that<br/>the user drags into it.                                                                                              |
| AllowUserToAddRows                | EnableAddNew                         | Gets or sets a value indicating whether the option to add rows is displayed.                                                                                  |
| AllowUserToDeleteRows             | EnableRemove                          | Gets or sets a value indicating whether it allows deletion of rows.                                                                                               |
| AllowUserToResizeColumns          | ResizeRowsBehavior                   | Gets or sets a value indicating whether it allows dragging of selected columns for rearranging.                                                                    |
| AllowUserToResizeRows             | ResizeRowsBehavior                   | Gets or sets a value indicating whether row resizing is allowed.                                                                                                  |
| ColumnCount                       | Model.ColCount                       | Gets or sets the number of columns displayed.                                                                                                                  |
| ColumnHeadersHeight               | Model.RowHeights[0]                  | Gets or sets the width of the row (interpreted as height of the headers).                                                                                     |
| ColumnHeadersVisible              | Properties.ColHeaders                 | Gets or sets a value indicating whether the column header row is displayed.                                                                               |
| HorizontalScrollingOffset          | HScrollIncrement                     | Gets or sets the number of pixels by which the control is scrolled horizontally.                                                                            |
| GridColor                          | Properties.GridLineColor             | Gets or sets the color of the grid lines separating the cells.                                                                                              |
| MultiSelect                       | AllowSelection                       | Gets or sets a value indicating whether more than one cell, row, or column can be selected.                                                              |
| RowCount                          | Model.RowCount                       | Gets or sets the number of rows.                                                                                                                             |

### Description of Key Properties

- **AllowUserTo** properties: These properties enhance user interaction by enabling or disabling specific actions such as adding or deleting rows, and adding or removing features.
- **Grid Color and Headers**: Customizing grid lines and headers enhances the visual presentation to suit application requirements.
- **Scrolling and Resizing**: These properties manage how rows and columns are displayed dynamically, especially useful for large datasets.
- **Column and Row Count**: Management of displayed data size through setting number of columns and rows.

### Property-Mapping Notes

The grid provides alternative property names for several functionalities. For example:
- `AllowUserToResizeColumns` and `AllowUserToResizeRows` are both mapped to `ResizeRowsBehavior`, but they control different aspects of resizing.
- `HelperMethods 적용`: `HorizontalScrollingOffset` can be adjusted via `HScrollIncrement` to manage horizontal scrolling in fine detail.

### Example Usage in Code

Here's a sample code snippet demonstrating how to configure some of these properties programmatically:

```csharp
// Setting properties for a Syncfusion Grid
grid.AllowUserToAddRows = true;
grid.EnableAddNew = true;

grid.ColumnHeaderHeight = 40;
grid.ColumnHeadersVisible = false;

grid.MultiSelect = true;
grid.AllowSelection = true;

// Customizing grid appearance
grid.GridColor = Color.LightGray;
grid.HScrollIncrement = 20;
```

## API Reference

### Properties

| Property Name                   | Type                  | Description                                                                                           |
|---------------------------------|-----------------------|-------------------------------------------------------------------------------------------------------|
| AllowUserToAddRows              | boolean               | Enables or disables the option for users to add rows in the grid.                                    |
| AllowUserToDeleteRows           | boolean               | Enables or disables the option for users to delete rows in the grid.                                  |
| AllowUserToResizeColumns        | boolean               | Enables or disables the option for users to resize columns in the grid.                               |
| ColumnCount                     | int                  | Specifies the number of displayed columns in the grid.                                              |
| ColumnHeadersHeight             | int                  | Specifies the height of column headers in pixels.                                                   |
| ColumnHeadersVisible            | boolean               | Determines whether column headers are displayed or hidden.                                         |
| HorizontalScrollingOffset        | int                  | Specifies the number of pixels the control is horizontally scrolled.                                |
| GridColor                       | Color                | Specifies the color of lines between grid cells.                                                    |
| MultiSelect                     | boolean               | Determines whether users can select multiple cells, rows, or columns.                                |
| RowCount                        | int                  | Specifies the number of rows in the grid.                                                                 |

### Methods and Events

The grid control provides methods and events for various interactions, such as `BeginUpdate()` and `EndUpdate()` for batch operations to improve performance, and events like `SelectionChanged` for detecting changes in user selections.

## Code Examples

### Configuring the Grid Control

The following example demonstrates configuring several grid properties:

```csharp
Syncfusion.Windows.Forms.Grid.GridControl grid1 = new Syncfusion.Windows.Forms.Grid.GridControl();
grid1.AllowUserToAddRows = true;
grid1.EnableAddNew = true;
grid1.ColumnHeadersVisible = true;
grid1.GridColor = System.Drawing.Color.Gray;
grid1.ColumnCount = 5;
grid1.RowCount = 10;
```

## Cross References

See also:
- [Syncfusion GridControl Documentation](https://docs.syncfusion.com/windowsforms/) for detailed information on all available properties and methods.
- [Manipulating Grid Layout Programmatically](#programmatic-grid-layout) for how to dynamically adjust grid elements.

<!-- tags: Grid, SyncfusionWinForms, customization, properties, events, methods keywords: AllowUserToAddRows, AllowUserToDeleteRows, AllowUserToResizeColumns, ColumnCount, ColumnHeadersHeight, ColumnHeadersVisible, HorizontalScrollingOffset, GridColor, MultiSelect, RowCount -->
```