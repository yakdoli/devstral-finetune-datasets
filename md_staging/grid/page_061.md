```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: grid
page_number: 061
page_id: grid#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:19:57Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains how to add the Group Drop Area to a Grid Grouping control.
- Demonstrates configuring properties to enable grouping functionality.
- Guides through binding the grid to data sources using `OleDbDataAdapter`.

## Content

### Configuring Grid Grouping Control

The image shows the Windows Forms Designer interface. The form named `Form1` contains a **Grid Grouping Control** with the following components:
- **gridGroupingControl1**: The primary control for displaying the grid with grouping functionality.
- **Binding components**: Includes `OleDbDataAdapter1`, `OleDbConnection1`, and `DataSet1`, which are used to bind the grid to a data source.

#### Properties of `gridGroupingControl1`
Properties for the `gridGroupingControl1` control are visible in the **Properties Window** on the right side:
- **ShowGroupDropArea**: Set to True to enable dragging column headers to group by a specific column.
- Other relevant properties include:
  - **HorizontalScrollTips**: False
  - **HorizontalThumbTrack**: True
  - **IntelliMousePanning**: False
  - **InvalidAllWhenListC**: True
  - **RightToLeft**: No
  - **ShowNavigationBar**: False
  - **ShowNestingProperties**: True
  - **ShowRelationFields**: ShowDisplayFieldsOnly
  - **ThemesEnabled**: True
  - **UseInvariantCulture**: False
  - **VerticalScrollTips**: False
  - **VerticalThumbTrack**: True
  - **WantTabKey**: True

#### User Interface
The grid displays a table with the following columns:
- **Address**
- **City**
- **CompanyName**
- **ContactName**
- **ContactTitle**
The header bar contains a placeholder text: **"Drag a column header here to group by that column."**

### Running the Project

After configuring the Grid Grouping Control and binding it to the data source:
- **Run the project** to see the basic Grid Grouping Control with the data as shown in the example.

## API Reference

### gridGroupingControl1 Properties
- **ShowGroupDropArea**: Allows or disallows grouping by dragging column headers.
- **HorizontalScrollTips**: Enables tips for horizontal scrolling.
- **HorizontalThumbTrack**: Enables track scrolling.
- **IntelliMousePanning**: Enables intelligent mouse panning.
- **RightToLeft**: Sets the layout direction for the grid to right-to-left.
- **ShowNavigationBar**: Enables or disables the navigation bar.
- **ShowNestingProperties**: Enables or disables nesting properties.
- **ShowRelationFields**: Controls how related fields are displayed.

### DataSet Binding
- **OleDbDataAdapter1**: Used to fill the `DataSet` with data from a data source.
- **OleDbConnection1**: Establishes a connection to the database.
- **DataSet1**: Acts as the data source for the grid.

## Code Examples

```csharp
// C# Example: Binding GridGroupingControl to OleDbDataAdapter
using Syncfusion.Windows.Forms.Grid.Grouping;

// Initialize data components
OleDbDataAdapter1.Fill(DataSet1);

// Bind DataSet to GridGroupingControl
gridGroupingControl1.DataSource = DataSet1;
gridGroupingControl1.ShowGroupDropArea = true;

// Enable grouping functionality
gridGroupingControl1.Properties.AllowDragDropGrouping = true;
```

## Page-level Navigation/TOC
- Figure 24: Adding the Group Drop Area
- Configuring Grid Grouping Control

## Cross References
- See also:
  - [Creating and Customizing Grid Grouping Control](grid#customizing-grid-grouping-control).
  - [Data Binding in Windows Forms](grid#data-binding-in-windows-forms).

<!-- tags: [syncfusion, winforms, gridgroupingcontrol, datagrid, databinding, api, 11.4.0.26] keywords: [grid grouping, group drop area, drag and drop, data binding, windows forms, essential grid] -->
```
