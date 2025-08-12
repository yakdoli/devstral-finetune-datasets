```html
<!--  
  source: image
  domain: syncfusion-sdk
  task: pdf-ocr-to-markdown
  language: en
  source_filename: page_754.jpeg
  document_name: grid
  page_number: 754
  page_id: grid#page_754
  product: Syncfusion Winforms
  version: 11.4.0.26
  timestamp: 2025-08-09T06:41:02Z
  fidelity: lossless
  -->

## Essential Grid for Windows Forms

### Overview
- Displays summaries for nested tables and groups within the Essential Grid control for Windows Forms.
- Focuses on calculating summaries for Orders and ShipCountry data.
- Includes references to a browser sample for more details.

### Content

#### Figure 302: Summaries for Nested Tables and Groups

The figure illustrates a grid view displaying Orders data grouped by ShipCountry. The grid includes CustomerID, EmployeeID, Freight, OrderDate, OrderID, and RequiredDate columns, structured to show summaries across different levels:

- **ShipCountry: Austria - 40 Items**
- **ShipCountry: Argentina - 16 Items**

Each ShipCountry group is expanded to reveal detailed orders, with entries for various customers (e.g., OCEAN, RANCH, CACTU). Each order includes specific details such as Freight, OrderDate, OrderID, and RequiredDate.

At the bottom of the grid, there are summary rows:
- **Child Table Summary**: Total details for individual orders.
- **Group Summary**: Summary for each ShipCountry group (e.g., total orders for Argentina).
- **Parent Table Summary**: Overall summary for all groups, showing total order value ($599) and total freight cost ($64943).

#### Note: For more details, refer the following browser sample:
- **Install Location**: `<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Calculate Summary\Nested-Table and Group Summary Demo`

### Summary In Caption

This section discusses the implementation and features of summary calculations in the Essential Grid for Windows Forms, emphasizing how nested tables and groups are utilized to present summary information effectively.

## API Reference

### Namespaces and Classes
- **Namespace**: `Syncfusion.Windows.Forms.Grid`
- **Class**: `GridGroupingControl`
- **Class**: `GridSummaryColumn`

### Properties
- **SummaryRowHeight**  
  **Description**: Gets or sets the height of the summary rows.
  **Type**: `int`
  **Default**: `20`

- **SummaryColumns**  
  **Description**: Represents a collection of summary columns.
  **Type**: `GridSummaryColumns`

### Methods
- **CalculateTotal**  
  - **Description**: Calculates the total of a specified column across all rows.
  - **Parameters**: 
    - `columnName`: The name of the column to calculate the total.
    - `rows`: Collection of rows to include in the calculation.
  - **Returns**: `decimal`

- **AddSummaryColumn**  
  - **Description**: Adds a new summary column to the grid.
  - **Parameters**: 
    - `summaryColumn`: The summary column to be added.

## Code Examples

### Adding Summary Columns in C#
```csharp
// Add a summary column for total freight
summaryColumn = new GridSummaryColumn();
summaryColumn.Name = "Total Freight";
summaryColumn.Format = "C2";
summaryColumn.Tag = "OrderDetails";
summaryColumn.Editor = new GridCellTextEditor();
summaryColumn.Aggregate = GridAggregate.Sum;
summaryColumn.HeaderText = "Total Freight";
gridSummaryColumns.Add(summaryColumn);
```

### Adding Summary Columns in VB.NET
```vb.net
' Add a summary column for total freight
Dim summaryColumn As New GridSummaryColumn()
summaryColumn.Name = "Total Freight"
summaryColumn.Format = "C2"
summaryColumn.Tag = "OrderDetails"
summaryColumn.Editor = New GridCellTextEditor()
summaryColumn.Aggregate = GridAggregate.Sum
summaryColumn.HeaderText = "Total Freight"
gridSummaryColumns.Add(summaryColumn)
```

## Page-level Navigation/TOC
- **Figure 302: Summaries for Nested Tables and Groups**
- **Summary In Caption**

## Cross References
- See also: Grid.Grouping Windows Documentation for more details on group summaries and nested tables.

<!-- tags: [grid, windows forms, summary, group summary, shipcountry, orders, freight, essential grid, syncfusion windows forms] keywords: [summarization, nested tables, group summary, shipcountry, order summary, freight calculation, grid control, data grouping, essential grid for windows forms] -->
```