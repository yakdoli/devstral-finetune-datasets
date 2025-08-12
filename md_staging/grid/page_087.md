```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: grid
page_number: 087
page_id: grid#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Creating Queries with Query Builder

### Selecting Fields for your Query

#### Figure 53: Select the Fields for your Query

The Query Builder interface allows you to create and configure SQL queries visually. The interface is divided into several sections:

1. **Available Columns**: On the left side, you can see a list of available columns from the `Products` table. Checked columns like `ProductID`, `ProductName`, and `QuantityPerUnit` are selected for inclusion in the query.

2. **Query Design Grid**: The central area displays a grid where the selected columns are listed under `ColumnName`, with their respective tables (e.g., `Products`). The `Output` column indicates which columns will be included in the query result. In this example, `ProductName`, `ProductID`, and `QuantityPerUnit` are marked for output.

3. **SQL Query Preview**: Below the design grid, the SQL query is generated automatically based on the selections. For this example, the query is:
   ```sql
   SELECT ProductName, ProductID, QuantityPerUnit, UnitPrice
   FROM Products
   ```

### Confirming the Query

Once you have selected the fields for your query, you can proceed to confirm your selections. The next step involves confirming the query you have configured.

#### Step 8: Confirm the Query

- Click **Next** to confirm the Query you selected.

## Summary

This section of the guide focuses on using the Query Builder in the Essential Grid for Windows Forms to select fields for your query. By leveraging the Query Builder interface, users can visually configure SQL queries, ensuring they include the desired fields from the database table. Once the fields are selected, confirming the query by clicking **Next** allows users to proceed to the next configuration step.

<!-- tags: [query builder, essential grid, windows forms, sql queries, query selections] keywords: [query design, product fields, unit price, quantity per unit, product id, product name] -->
```