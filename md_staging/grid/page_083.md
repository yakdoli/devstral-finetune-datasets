```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: grid
page_number: 083
page_id: grid#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the selection of the Northwind database in the Data Adapter Configuration Wizard.
- Steps to configure data connections using the wizard.
- Guidance on selecting SQL statements for database operations.

## Content

### Data Adapter Configuration Wizard

The Data Adapter Configuration Wizard is used to configure data connections and query execution in the Essential Grid for Windows Forms. The wizard's interface is shown below:

#### Wizard Interface
- **Choose Your Data Connection**:
  - The data adapter uses this connection to load and update data.
  - Select from existing connections in Server Explorer or add a new connection if needed.

- **Data Connection Selection**:
  - The selected connection is `RTATHINK\NetSDK.Northwind.dbo`.

#### Figure: Select the NorthWind Database

```markdown
Figure 49: Select the NorthWind Database
![Data Adapter Configuration Wizard](image_of_wizard)
```

### Steps to Configure Data Connection

1. **Open the Data Adapter Configuration Wizard**: Navigate to the wizard through the project's properties or design interface.
2. **Choose Your Data Connection**:
   - Select the desired data connection from the dropdown list or create a new connection.
3. **Configure Data Operations**:
   - Ensure the selected connection is appropriate for the grid's data requirements.
4. **Select to Use SQL Statements**: Once the data connection is configured, select using SQL statements to perform data operations.

## API Reference

This section would typically cover the relevant APIs or methods used for configuring data connections and executing SQL statements in the grid. However, the provided content does not include specific API details.

## Code Examples

While no code examples are provided here, the configuration process involves setting up data adapters and executing SQL commands programmatically. Below is a general example of connecting to a SQL Server database:

```csharp
using System;
using System.Data;
using System.Data.SqlClient;

// Example connection string
string connectionString = @"Data Source=RTATHINK\NetSDK;Initial Catalog=Northwind;Integrated Security=True";

// Create and open a connection
SqlConnection connection = new SqlConnection(connectionString);
connection.Open();

// Example SQL query
string query = "SELECT * FROM Customers";
SqlCommand command = new SqlCommand(query, connection);

// Execute the query and process the results
SqlDataReader reader = command.ExecuteReader();
while (reader.Read())
{
    Console.WriteLine(reader["CustomerID"] + ": " + reader["ContactName"]);
}

connection.Close();
```

## Page-level Navigation/TOC
- [Select the NorthWind Database](#figure-49-select-the-northwind-database)
- [Steps to Configure Data Connection](#steps-to-configure-data-connection)

## Cross References
- Refer to the engine modules for database connection configurations.
- See also: [SQL Statement Execution in WinForms](#sql-statement-execution-in-winforms)

<!-- tags: [syncfusion, windowsforms, grid, dataadapter, northwind, connectionconfiguration, sqlstatements, databaseaccess] keywords: [dataadapter, connectionstring, northwind, datagrid, sqlstatement, windowsforms] -->
```