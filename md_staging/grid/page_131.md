<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: grid
page_number: 131
page_id: grid#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:45:34Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The ControlStyle properties are similar to the System.Windows.Forms.DataGridColumnStyle class. It is this property that allows Grid Data Bound Grid to be described as a column-oriented grid.

## Overview
- This document outlines the various grid controls available in the Syncfusion WinForms library.
- The grid controls provide advanced features for data presentation and manipulation, such as grouping, sorting, and hierarchical support.

## Grid Grouping Control
- **Description:** This grouping control is derived from the control class and implements several interfaces to add grouping support.
- **Features:**
  - Grouping support
  - Multi-column sort support
  - True nested-table hierarchical support
- **Customization:** You can easily add:
  - Expression columns
  - Filter columns
  - Summary rows
- **Data Binding:** It can be bound to any IList data source.
- **Design:** It can be fully designed using Visual Studio.

## Grid List Control
- **Description:** This class is derived from System.Windows.Forms.ListControl and can display multiple columns in its list.
- **Key Features:**
  - Contains a GridControl object as its property.
  - Provides grid-like access to a ListControl.
  - Supports both data and formatting.
- **Usage:** Easy to use with the exact data displayed.
- **Customization:** Can be customized by hiding columns or changing column names.
- **Use Case:** Serves as the drop list object for the combo box that acts as a cell control.

## Grid Record Navigation Control
- **Description:** This class provides MS Access-like navigation support.
- **Common Use:** Used in conjunction with the Grid Data Bound Grid to display record numbers and allow record scrolling.
- **Features:**
  - Displays record numbers.
  - Enables record scrolling through a record information window in the lower-left corner of the grid.
- **Flexibility:** Can also be used with a Grid control.

## Grid Aware Text Box
- **Description:** This class is derived from System.Windows.Forms.TextBox.
- **Functionality:**
  - Allows binding to the CurrentCell of a Grid control or Grid Data Bound Grid.
  - Provides a special edit bar for editing grid cells or serves as a formula bar in a formula grid.
- **Purpose:** Ideal for advanced editing and formula management within grid controls.

## API Reference
- **Classes:**
  - GridControl
  - GridGroupingControl
  - GridListControl
  - GridRecordNavigationControl
  - GridAwareTextBox

## Code Examples
```csharp
// Example of using GridGroupingControl
GridGroupingControl gridGrouping = new GridGroupingControl();
gridGrouping.DataSource = data;
```

## Cross References
- See also: DataGrid, ListControl, TextBox, Grid Navigation

## RAG Annotations
<!-- tags: [grid, grouping, list control, navigation, text box] keywords: [data bound grid, grid control, list control, record navigation, text box, grid aware, grid grouping] -->
