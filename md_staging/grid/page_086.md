```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: grid
page_number: 086
page_id: grid#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Add Table selection dialog to choose tables, views, or functions for querying in the grid.
- Walkthrough on selecting the "Products" table and specifying relevant columns for data retrieval.
- Focus on building queries for grid data display.

## Content

### Selecting the Products Table
#### Figure 52: Select the Products Table
- **Window Title:** Add Table
- **Tabs:** Tables, Views, Functions

The "Add Table" dialog box displays a list of tables under the "Tables" tab:
- Categories
- CustomerCustomerDemo
- CustomerDemographics
- Customers
- Employees
- EmployeeTerritories
- Order Details
- Orders
- **Products** (selected)
- Region
- Shippers
- Suppliers
- Territories

### Query Build Instructions
7. In this Query Build window, select the ProductName, ProductID, QuantityPerUnit, and UnitPrice. Then press OK.

## API Reference (if applicable)
- Refer to the [Grid API](#grid-api-reference) for more information on building custom queries.

### Code Examples (multi-language supported)

```csharp
// Assuming a connection to a database is established
grid.Query.CustomSql = "SELECT ProductName, ProductID, QuantityPerUnit, UnitPrice FROM Products";
grid.Refresh();
```

## Page-level Navigation/TOC (if applicable)
- **Adding and Configuring Tables**  
  - Selecting Tables, Views, and Functions
  - Query Building and Customization

## Cross References
See also:
- [Grid API Reference](#grid-api-reference)
- [Building Custom Queries in Essential Grid](#building-custom-queries)

<!-- tags: [Essential Grid, Windows Forms, Query Build, Products Table, SQL, API, Syncfusion] keywords: [Windows Forms, Syncfusion, Essential Grid, Query Build, Products Table, SQL, Custom Queries, Table selection] -->
```