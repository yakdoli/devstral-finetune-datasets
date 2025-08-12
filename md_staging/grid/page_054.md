```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_054.jpeg
document_name: grid
page_number: 054
page_id: grid#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:20:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Use the Query Builder to select tables and columns.
- Highlight the "Suppliers" table in the Query Builder window.
- Select "All Columns" and confirm the selection.

## Content

### Query Builder

**Figure 17: Select the Suppliers Table**

- The Query Builder window provides an interface to build SQL queries visually.
- In the "Add Table" dialog, the list of available tables is shown, including "Suppliers."
- To proceed, select the "Suppliers" table and choose "All Columns."

#### Step-by-Step Instructions:

10. In this Query Builder window, select **All Columns**. Then click **OK**.

## API Reference
For more details on the Query Builder and associated features, refer to the Grid documentation.

## Code Examples

```csharp
// Example of selecting all columns from a table using Query Builder
// Assume a method to build a query with the Query Builder interface
QueryResult result = QueryBuilder.SelectAll(TableName).Execute();
```

## Page-level Navigation/TOC (if applicable)
- [Step 10: Selecting all columns in Query Builder] -> [Next Step: Applying filters or conditions]

## Cross References
- See also: documentation on "Handling Data Grid Queries" and "Grid Data Selection Techniques."

## RAG Annotations
<!-- tags: [syncfusion, windows forms, query builder, grid, data selection, suppliers, all columns, version 11.4.0.26] keywords: [query builder, suppliers table, all columns, essential grid, windows forms, data selection, syncfusion winforms, table binding] -->
```