```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_562.jpeg
document_name: grid
page_number: 562
page_id: grid#page_562
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:43Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the setup and behavior of a simple Master-Detail relation in a Windows Forms application.
- Explains the use of grids to display a Master table and a Details table, focusing on the interaction between the two.

## Content

### Master-Detail Relation

To define a simple Master-Detail relation, you must have two tables:
1. **Master Table**: This table contains a column whose values are also included in a second table.
2. **Details Table**: This table includes the column from the Master Table as its foreign key.

These two tables are displayed in two grids:
- **Master Grid**: Displays the Master table.
- **Details Grid**: Displays the Details table. The rows shown in the Details grid are restricted to only those rows whose common value matches the value in the selected Master grid row.

#### Example Demonstrating Master-Detail Interaction
A screenshot illustrates a Master-Detail grid pair using the NorthWind Customers table as the Master table and the NorthWind Orders table as the details table. When a customer is selected in the customers grid, the orders for that customer appear in the second grid.

![Master-Detail Grid Pair](https://placeholder.com)
*Figure 220: Top Grid is Master Listing All Customers, Bottom Table is Details, Displaying All Orders for Selected Customer*

### Implementation Details

The following code implements the Master-Detail form:

#### Designer Setup
1. Two `DataAdapters` (one for each table) are added to the form.
2. A `DataSet` is generated to hold the tables.
3. Two `Grid Data Bound Grids` are positioned on the form.
4. The `Form_Load` event sets up the data binding between the `DataSet` and the grids.

#### Code Implementation
Below is the `C#` code for the `Form_Load` event:

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    // Fill the Data Set with two tables.
}
```

### Summary
The Master-Detail relation allows users to interactively view related data in two grids, providing a flexible and intuitive way to manage and display complex data relationships.

## Page-level Navigation/TOC (if applicable)
- [Not applicable on this page]

## Cross References
- See also: Master-Detail grid setup, grid interaction events, and `DataSet` usage in Syncfusion WinForms.

## RAG Annotations
<!-- tags: [Essential Grid, Windows Forms, Master-Detail, Grid Data Bound Grids, DataSet, NorthWind Database] keywords: [master table, details table, grid interaction, customer orders, two table setup, grid data binding] -->
```