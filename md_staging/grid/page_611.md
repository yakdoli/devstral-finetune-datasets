```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_611.jpeg
document_name: grid
page_number: 611
page_id: grid#page_611
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:04Z
fidelity: lossless
-->

## Overview
- Describes the architecture of `GridEngine` and its relationship with `GridTableDescriptor` and `GridTable` for handling hierarchies in grid grouping controls.
- Explains how relations between tables are defined within the `GridTableDescriptor` and managed by `RelationDescriptor` objects.
- Details the role of the `GridTable` object in managing records and group elements from the `DataSource`.
- Introduces the `DisplayElements` and `NestedDisplayElements` collections for controlling display in the grid.
- Summarizes the functionality of the `Grouping Engine` and its integration with the grid grouping control.

## Content

### GridEngine and Grid Tables
There is only one `GridEngine` object for a Grid Grouping control. The `GridTableDescriptor` and `GridTable` objects on the other side can be more than one when hierarchies are displayed. For each hierarchy level, a `GridTableDescriptor` and `GridTable` are initialized. For example, if you have an ADO.NET `DataSet` with three tables: "Products", "Orders", and "OrderDetails", there will be three `GridTableDescriptors` and `GridTables`.

#### Relations between Tables
Relations between tables are defined with a `GridTableDescriptor.Relations` collection of a `TableDescriptor`. Each `TableDescriptor` can have one or multiple `RelationDescriptor` objects. A `RelationDescriptor` defines the foreign key columns in the parent table, a child with information about the related child table and the primary key columns in the child table.

### GridTable Object
The `GridTable` object is instantiated by the `GridEngine` class. The `Table` object manages the records from the engine's `DataSource` and provides access to records and grouped elements through several collection classes.

### Important Collections
The most important collection used by the Grid Table control is the `DisplayElements` collection. This collection provides the Grid Table control with information on which element to display at a row. It returns elements such as `CaptionSection`, `RecordRow`, `SummaryRow`, and others. Based on the elements returned by this collection, the Grid Table control will display a record, a summary, or a group caption bar.

There are several collections returned, such as:
- `Records`, which contains all records in the table.
- `FilterRecords`, which contains all visible records.

#### Nested Display Elements
Another related collection is the `NestedDisplayElements` collection. Similar to `DisplayElements`, this collection also returns all records, groups, and sections that are expanded and meet filter criteria. The only difference between these two collections is that the `NestedDisplayElements` collection steps into nested tables, where the `DisplayElements` collection will not.

### The Grouping Engine

#### Overview
The `Engine` is the main object of the grid grouping control. It contains the `TableDescriptor` with schema information, such as fields, relations, and the `Table` with runtime representation of the data source, including groups, records, data, and display elements. The engine lets you set the main `datasource` for the whole engine. The `TableDescriptor` will pick up the `ItemProperties` (schema information) from the `datasource`, and the `table` will be initialized at runtime with records from the list.

#### Design-Time Support
The `GridEngineBase` class adds design-time support for the engine class. It can be dropped as a component into the component tray of the designer. It can be initialized with a `BindingContext` so that the `CurrencyManager` can be kept synchronized.

## API Reference
- **Classes**
  - `GridEngine`
  - `GridTableDescriptor`
  - `GridTable`
  - `RelationDescriptor`
  - `GridEngineBase`

## Code Examples

### Example: Setting Up GridEngine with ADO.NET DataSet

```csharp
// Assume we have an ADO.NET DataSet with tables "Products", "Orders", and "OrderDetails"
DataSet dataSet = new DataSet();
dataGridView1.DataSource = dataSet;

// Configure GridEngine
var engine = new GridEngine();
engine.DataSource = dataSet;
```

### Example: Defining Relations between Tables

```csharp
// Define a relation between "Orders" and "OrderDetails"
var relationDescriptor = new RelationDescriptor
{
    ParentTable = "Orders",
    ChildTable = "OrderDetails",
    PrimaryKeyColumns = new[] { "OrderID" },
    ForeignKeyColumns = new[] { "OrderID" }
};

gridTableDescriptor.Relations.Add(relationDescriptor);
```

## Cross References
- See also: [ADO.NET DataSet Overview](#ado-net-dataset-overview)
- See also: [Design-Time Support in WinForms](#design-time-support-in-winforms)

<!-- tags: [grid, gridengine, tabledescriptor, gridtable, relation, adonet, design-time, displayelements, nesteddisplayelements] keywords: [grid grouping, hierarchy, table relations, relations between tables, record management, filter records, data source, runtime representation, display elements, nested tables, designer component] -->
```