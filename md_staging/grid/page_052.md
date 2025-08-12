```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: grid
page_number: 052
page_id: grid#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:19:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This page guides users through configuring a data adapter by choosing a query type.
- It provides options for accessing the database using SQL statements or stored procedures.
- The page includes steps to generate SQL statements, including the use of the Query Builder.

## Content

### Data Adapter Configuration Wizard

#### Choose a Query Type
The data adapter uses SQL statements or stored procedures.

**How should the data adapter access the database?**

1. **Use SQL statements**
   - Specify a `Select` statement to load data, and the wizard will generate the `Insert`, `Update`, and `Delete` statements to save data changes.

2. **Create new stored procedures**
   - Specify a `Select` statement, and the wizard will generate new stored procedures to select, insert, update, and delete records.

3. **Use existing stored procedures**
   - Choose an existing stored procedure for each operation (select, insert, update, and delete).

#### Figure 15: Select to Use SQL Statements

To generate the SQL statement, click **Query Builder**.

## Code Examples

No code examples are provided in this section, as the page focuses on guiding users through the configuration process.

## API Reference

**Methods/Properties**
- **QueryBuilder**: Constructs SQL statements for CRUD operations based on the selected options.

<!-- tags: [syncfusion, windows forms, data adapter configuration, sql statements, stored procedures, query builder] keywords: [data access, sql, stored procedures, configuration wizard, crud operations, insert, update, delete] -->
```