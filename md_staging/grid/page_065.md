```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: grid
page_number: 065
page_id: grid#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:20:21Z
fidelity: lossless
-->

## Overview
- Demonstrates the process of choosing a data source using the Smart Tag in the GridGroupingControl.
- Walks through configuring a grid by selecting a data source and connecting it to the grid.

## Content

### Configuring Data Source in GridGroupingControl

The image illustrates the process of choosing a data source for a GridGroupingControl in a Windows Forms application. Here is the breakdown:

1. **UI Layout**:
   - **Form Design Area**: On the left, a UI design window labeled "Form1" is shown with a GridGroupingControl placed within it. The placeholder text indicates instructions for configuring the grid.
   - **Smart Tag Options**: On the right, the "GridGroupingControl Tasks" pane shows the "Choose DataSource" option, currently set to "(none)".

2. **Process Steps**:
   - **Step 1**: Right-click the GridGroupingControl to display the smart tag options.
   - **Step 2**: Navigate to the "Choose DataSource" section and select the "Add Project Data Source..." option.
   - **Step 3**: In the Data Source Configuration Wizard that appears, select "Database" and click "Next."

#### Visual Elements
- **Grid Configuration**: The grid is outlined in the design window, providing a visual reference for the grid setup.
- **Task Pane**: Displays options for configuring the grid's data source, including selecting a database as the source.

3. **Instructions in Text**
   - "Right click and choose the required menu options (or use smart tag in VS.NET 2005) to configure the Grid."
   - "Click the 'Add Project Data Source…' link to connect to data."

### Additional Resources
- **Documentation and Support**:
  - Online Documentation
  - Evaluation Center
  - Forums Support
  - Direct-Trac Support

## API Reference (if applicable)

### Smart Tag Configuration
- **Property**: `DataSource`
  - Type: `Object`
  - Description: Sets or gets the object that is the data source for this grid.
  - Default: `null`
  - Optional Parameters: None.

## Code Examples

```csharp
// Connecting to a Database
using System;
using System.Data;
using System.Data.SqlClient;

public void ConfigureGridDataSource() {
    // Create a new GridGroupingControl instance
    GridGroupingControl grid = new GridGroupingControl();

    // Configure the data source
    grid.DataSource = new DataTable();

    // Example: Connecting to a database and setting the data source
    using (SqlConnection connection = new SqlConnection("YourConnectionStringHere")) {
        SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM YourTable", connection);
        DataSet dataSet = new DataSet();
        adapter.Fill(dataSet);

        grid.DataSource = dataSet.Tables[0];
    }
}
```

### Notes
- **Database Connection**: Ensure that the connection string is correctly formatted and accessible.
- **Data Access**: The data source can be any `IEnumerable` or `DataTable` that supports the grid's data binding requirements.

## Page-level Navigation/TOC (if applicable)

### Local TOC
- [How to Connect a Data Source to GridGroupingControl]
  1. Configuring the Grid
  2. Using Smart Tag Options
  3. Database Connection Process

<!-- tags: [WinForms, GridGroupingControl, DataSource, Database, SmartTag, ConfigurationWizard] keywords: [Syncfusion, Grid, Windows Forms, data binding, smart tag, database connection] -->
```