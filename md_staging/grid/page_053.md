```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: grid
page_number: 053
page_id: grid#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:19:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates configuring a Data Adapter using the Query Builder.
- Focuses on generating SQL statements for Insert, Update, and Delete operations.
- Guides users on selecting the appropriate table to load into the dataset.

## Content

### Data Adapter Configuration Wizard
The Data Adapter Configuration Wizard is used to generate SQL statements for Insert, Update, and Delete operations based on a given SELECT statement. Here's a step-by-step guide:

1. **Generate the SQL Statements:**
   - The SELECT statement provided in the wizard will be used to create the Insert, Update, and Delete statements dynamically.

2. **Define the Query:**
   - You can either type in your SQL SELECT statement manually or use the Query Builder to graphically design your query.

3. **Specify the Data to Load:**
   - Decide what data should be loaded into the dataset by modifying the SELECT statement or using the Query Builder.

4. **Access Additional Options:**
   - Click on the "Advanced Options..." button to access more configuration settings.

5. **Choose the Query Builder:**
   - Click on the "Query Builder..." button to open the Query Builder interface for graphical query design.

6. **Navigation inside the Wizard:**
   - Use the "Back," "Next," and "Finish" buttons to navigate through the wizard.

   ![Figure 16: Select the Query Builder](#)

### Step-by-Step Instructions
9. **Selecting the 'Suppliers' Table:**
   - In the **Add Table** dialog box, select the 'Suppliers' table.
   - Click **Add**.
   - Click **Close** to finish adding the table.

## API Reference
- The wizard interacts with the `Data Adapter` class, providing an interface for configuring SQL operations.
- Users can leverage the `Query Builder` to dynamically create and edit SQL queries.

## Code Examples
- This section would contain examples of using the Data Adapter and Query Builder programmatically in C#.

## Page-level Navigation/TOC
- This example focuses on a specific step in the Data Adapter Configuration Wizard. Details from previous or subsequent steps are not included in this excerpt.

## Cross References
- Refer to the main documentation for a complete list of features and examples related to the Data Adapter and Query Builder.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Data Adapter, Query Builder, SQL Statements] keywords: [Essential Grid, Windows Forms, Select Statement, Insert, Update, Delete, Database Operations, Query Builder Interface, Advanced Options, Suppliers Table] -->
```