```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: grid
page_number: 084
page_id: grid#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:27Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Wizard-based setup for configuring data adapters using SQL statements or stored procedures.
- Option to generate Insert, Update, and Delete statements based on selected configurations.

## Content

### Data Adapter Configuration Wizard

This section describes how the Data Adapter Configuration Wizard provides options for accessing a database. The wizard allows users to configure the data adapter to use SQL statements or stored procedures for performing database operations.

**Figure 50: Select to Use SQL Statements**

#### Wizard Options

- **Use SQL statements**: Specifies a SELECT statement to load data, and the wizard will generate the `INSERT`, `UPDATE`, and `DELETE` statements to save data changes.
- **Create new stored procedures**: Specifies a SELECT statement, and the wizard will generate new stored procedures for `select`, `insert`, `update`, and `delete` operations.
- **Use existing stored procedures**: Chooses an existing stored procedure for each operation (`select`, `insert`, `update`, and `delete`).

#### Navigation Buttons

- **Cancel**: Cancels the wizard.
- **Back**: Navigates to the previous step.
- **Next >**: Proceeds to the next step.
- **Finish**: Completes the wizard configuration.

#### Usage Instructions

5. To generate the SQL statement, click the Query Builder button.

## API Reference

The Data Adapter Configuration Wizard is designed to streamline the configuration process for selecting SQL statements or stored procedures. Detailed API references for the wizard and related components are available in the Syncfusion Winforms documentation.

## Code Examples

Below is an example demonstrating the process of using the Query Builder to generate a SQL statement:

```csharp
// Example: Using Query Builder to generate a SQL statement
void GenerateSQLStatement()
{
    // Placeholder for actual code to generate SQL statement
    // The Query Builder dialog can be invoked through the wizard interface
}
```

## Cross References

- Refer to the detailed documentation on "Data Adapter Configuration Wizard" for more information on the configuration options.
- See the section on "Using Query Builder" for further guidance on generating SQL statements.

<!-- tags: grid, data adapter configuration, wizard, sql statements, stored procedures, syncfusion winforms, 11.4.0.26 -->
```