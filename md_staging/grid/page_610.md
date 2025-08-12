```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_610.jpeg
document_name: grid
page_number: 610
page_id: grid#page_610
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- An in-depth look at the Serializaton feature of the Essential Grid for Windows Forms.
- Detailed explanation of the Major Control Classes in the Essential Grid, focusing on `GridGroupingControl`.
- Provides insights into grouping, sorting, and hierarchical table support.

## Content

### GridGroupingControl Class

#### Overview
The GridGroupingControl class is derived from the `Control` class and implements several interfaces that add grouping support to this class. Provides support for displaying ADO.NET data and other data sources in a grid. Data will be loaded from the given datasources and changes will be written back to the datasource.

#### Key Features
- Provides grouping support, multi-column sort support, or true nested-table hierarchical support in a grid.
- Can be bound to any `IList` datasources.
- Allows easy addition of expression columns, filter columns, and summary rows.
- Fully designable using Visual Studio and customizable from code.

#### Implementation Details
The `GridTableControl` is the main element in the Grid Grouping control. The Grid Table control displays the rows from the `Syncfusion.Grouping.Table.DisplayElements` collection of the Grid Grouping control.Table using schema information stored in the `TableDescriptor`.

#### TableDescriptor
The `TableDescriptor` gives access to the table schema information of the root table in the datasource. The `TableDescriptor` object is instantiated by the `GridEngine` class and initialized with default schema information from the list assigned to the `DataSource`.

#### Example Usage
The GridGroupingControl is ideal for scenarios where grouping, sorting, and hierarchical table support are required. It offers a flexible and customizable way to display and interact with data in a grid format.

---

## API Reference
### GridGroupingControl
- Inherits from: `Control`
- Key Interfaces Implemented:
  - Grouping functionality
  - ADO.NET data support
  - Hierarchical table support
- Properties:
  - `DataBound`: Manages binding to data sources.
  - `GroupOptions`: Configures grouping options.
  - `SortOptions`: Configures sorting options.
- Methods:
  - `BeginGroupOperation`: Starts a grouping operation.
  - `EndGroupOperation`: Completes a grouping operation.

### TableDescriptor
- Accesses: Table schema information
- Instantiated by: `GridEngine`
- Initialized with: Default schema information

---

## Code Examples

```csharp
// Binding GridGroupingControl to a datasources
GridGroupingControl grid = new GridGroupingControl();
var dataSource = GetDataSource(); // Assume this method returns the data list.
grid.DataSource = dataSource;

// Example of adding expression column
grid.TableModels.AddNewExpressionColumn("FullName", "FirstName + ' ' + LastName");

// Setting up grouping
GroupDescription groupDescription = new GroupDescription();
groupDescription.CaseSensitive = false;
groupDescription.GroupSettings.ShowCaption = true;
grid.GroupDescriptions.Add(groupDescription);
```

---

## RAG Annotations
<!-- tags: [GridGroupingControl, TableDescriptor, GridEngine, ADO.NET, HierarchicalTableSupport] keywords: [grouping, sorting, expression columns, filter columns, summary rows, Visual Studio customization, Design-time Features, Runtime Features] -->
```