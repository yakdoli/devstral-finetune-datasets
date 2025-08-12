```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_088.jpeg
document_name: grid
page_number: 088
page_id: grid#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- The image shows the "Data Adapter Configuration Wizard" in the context of creating or configuring a grid in a Windows Forms application.
- It demonstrates the process of generating SQL statements, particularly focusing on the SELECT statement that will be used to create INSERT, UPDATE, and DELETE statements.
- The SQL query displayed is used to configure the grid's data load operations.

## Content

### Data Adapter Configuration Wizard

#### Generating SQL Statements
The wizard helps in generating SQL statements that will be used to create the INSERT, UPDATE, and DELETE operations in a dataset. Below is the SQL Select statement that is being used:

```sql
SELECT
    ProductName,
    ProductID,
    QuantityPerUnit,
    UnitPrice
FROM
    Products
```

This query specifies the `ProductName`, `ProductID`, `QuantityPerUnit`, and `UnitPrice` fields to be retrieved from the `Products` table.

**Buttons:**
- **Cancel**: Cancels the current operation and exits the wizard.
- **< Back**: Allows users to go back to the previous step in the wizard.
- **Next >**: Proceeds to the next step in the wizard.
- **Finish**: Completes the configuration process.

**Other Options:**
- **Advanced Options**: Allows users to access more advanced configuration options.
- **Query Builder**: Provides a graphical interface for designing and modifying the query.

#### Confirming the Query
Once the query is confirmed, the user can finalize the configuration by clicking the **Finish** button. The confirmation screen shown in the image ensures that the SQL query is correctly configured for the grid.

**Figure 54: Confirm the Query**
The visual confirmation screen includes the SQL query that will be used to populate the grid with data.

### Design Surface
After clicking **Finish**, the user's design surface will reflect the configuration made in the wizard. The design will resemble the configuration shown in Figure 54.

## Code Examples (Example Configuration)

Here is an example of how the SQL query might look in the context of configuring the grid:

```csharp
// Example of configuring the grid with the SQL query
using Syncfusion.WinForms.DataGrid;
using System.Data.SqlClient;

// SQL Connection and Command setup
SqlConnection connection = new SqlConnection("YourConnectionString");
SqlCommand command = new SqlCommand("SELECT ProductName, ProductID, QuantityPerUnit, UnitPrice FROM Products", connection);

// Configure Data Adapter
SqlDataAdapter adapter = new SqlDataAdapter(command);

// Configure DataSet
DataSet dataSet = new DataSet();
adapter.Fill(dataSet);

// Configure Grid
grid.DataSource = dataSet.Tables[0];
```

## API Reference

### Essential Grid Methods/Properties
- **Generate SQL Statement**: Configures data insertion, updates, and deletions.
- **Query Builder**: Graphical interface for modifying and designing queries.
- **Next/Back/Finish/Cancel**: Navigation controls within the wizard.

## Cross References

### Related Topics
- For more on configuring grids using SQL queries in Windows Forms, see the relevant sections in the Syncfusion WinForms documentation.
- For advanced options and customization, refer to the "Advanced Options" feature in the Data Adapter Configuration Wizard.

<!-- tags: [Syncfusion WinForms, Data Adapter Configuration Wizard, SQL Statements, Grid Configuration, Windows Forms] keywords: [Essential Grid, SQL Query, INSERT, UPDATE, DELETE, Query Builder, Windows Forms, Design Surface] -->
```