```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: Olap Common
page_number: 123
page_id: Olap Common#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:09Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Demonstrates the use of OlapGrid Control with OLAP Data.
- Describes how to integrate and manipulate OLAP data within the OlapGrid.
- Highlights features and functionalities specific to displaying OLAP data.

## Content

### Figure 19: OlapGrid Control with OLAP Data

This figure showcases the OlapGrid Control applied to display OLAP (On-Line Analytical Processing) data. The OlapGrid Control is capable of handling multidimensional data structures typically found in OLAP cubes, providing a user-friendly interface for data analysis.

#### Key Features
- **Multidimensional Data Support**: The OlapGrid can display data from OLAP cubes, slicing and dicing data as needed.
- **Interactive Exploration**: Users can interactively explore the data by drilling down into categories or dimensions.
- **Customization Options**: The grid provides options to customize views, such as hiding or showing dimensions, rearranging them, and applying filters.

#### Usage Example

The following is a sample setup for integrating the OlapGrid with OLAP data:

```csharp
using Syncfusion.Olap.Controllers;
using Syncfusion.Olap.Grid;

// Create OLAP data controller
OlapController controller = new OlapController();

// Load OLAP data (example: from an XMLA data source)
controller.LoadXmla("http://localhost/olap/mondrian", "AdventureWorks");

// Create OlapGrid and bind it to the controller
OlapGrid grid = new OlapGrid();
grid.Controller = controller;

// Initialize the grid with initial dimensions and measures
grid.ShowDimension("Product", "Category");
grid.ShowMeasure("Sales Amount", "Product");

// Display the grid
this.Controls.Add(grid);
grid.Dock = DockStyle.Fill;
```

### WinForms-specific Notes

- **OlapGrid Properties**:
  - `Controller`: This property allows you to specify the OLAP data controller to be used for binding the grid.
  - `ShowDimension`: This method is used to display dimensions within the grid.
  - `ShowMeasure`: This method adds measures to the grid for aggregation and display.

- **Event Handling**:
  - `CellClick`: This event is triggered when a cell is clicked, useful for handling user interactions such as drilling down or filtering.

### API Reference

#### Methods

- **ShowDimension**
  - Displays a specific dimension in the grid.
  - **Parameters**:
    - `string dimensionName`: The name of the dimension to display.
- **ShowMeasure**
  - Adds a specific measure to the grid for display.
  - **Parameters**:
    - `string measureName`: The name of the measure to display.

#### Exceptions

- `OlapGridException`: Thrown when there are errors related to OLAP data manipulation or binding.

## Code Examples

### C#

```csharp
using Syncfusion.Olap.Grid;
using Syncfusion.Olap.Controllers;

OlapGrid grid = new OlapGrid();
OlapController controller = new OlapController();
controller.LoadXmla("http://localhost/olap/mondrian", "AdventureWorks");
grid.Controller = controller;
grid.ShowDimension("Product", "Category");
grid.ShowMeasure("Sales Amount", "Product");
this.Controls.Add(grid);
grid.Dock = DockStyle.Fill;
```

### VB.NET

```vb
Imports Syncfusion.Olap.Grid
Imports Syncfusion.Olap.Controllers

Dim grid As New OlapGrid()
Dim controller As New OlapController()
controller.LoadXmla("http://localhost/olap/mondrian", "AdventureWorks")
grid.Controller = controller
grid.ShowDimension("Product", "Category")
grid.ShowMeasure("Sales Amount", "Product")
Me.Controls.Add(grid)
grid.Dock = DockStyle.Fill
```

## Page-level Navigation/TOC
- Overview
- Content
  - Figure 19: OlapGrid Control with OLAP Data
  - Key Features
  - Usage Example
  - WinForms-specific Notes
    - Methods
    - Event Handling
  - API Reference
    - Methods
    - Exceptions

## Cross References
- See also: `OlapController`, `OLAP`, `Drill-Down`, `DataGrid`, `MultidimensionalDataAnalysis`

<!-- tags: [OlapGrid, OLAP, OnLineAnalyticalProcessing, OLAPData, DataGrid, WinForms, Syncfusion] keywords: [OlapGrid, OLAP, OLAPData, Dimensions, Measures, DataGrid, Grid, DrillDown, MultidimensionalData, OnLineAnalyticalProcessing] -->
```
