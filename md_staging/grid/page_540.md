```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_540.jpeg
document_name: grid
page_number: 540
page_id: grid#page_540
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:42Z
fidelity: lossless
-->

## Overview

- This page explains how to configure a data source to populate a grid control in Windows Forms using Essential Grid.
- Provides steps for selecting a project data source through Smart Tags and configuring a database connection.
- Includes screenshots of the data source configuration wizard and the Smart Tag interface.

## Content

### Step-by-Step Data Source Configuration

1. **Smart Tag for Data Source Selection**:
   - The first step involves utilizing the Smart Tag feature to add a project data source.
   - **Figure 210**: Demonstrates the selection of the "Add Project Data Source" option through the Smart Tag interface.
     ```markdown
     Figure 210: Add Project Data Source Option selected through Smart Tag
     ```

2. **Data Source Configuration Wizard**:
   - After selecting the project data source option, the Data Source Configuration wizard appears.
   - The wizard allows you to choose the type of data source.

#### Wizard Interface
   - **Data Source Type**: The wizard provides options to select where the application will retrieve data from, including:
     - **Database**: Connects to a database and allows you to choose the database objects.
     - **Service**: Connects to services for retrieving data.
     - **Object**: Connects to objects as data sources.

     ![Data Source Type Selection](image-url)

   - **Instructions**: The wizard text reads:
     ```
     Where will the application get data from?
     Database Object
     Service
     Lets you connect to a database and choose the database objects for your application. This option creates a dataset.
     ```

3. **Step-by-Step Guide**:
   - **Step 4**:
     - In the **Data Source Configuration** wizard, select **Database** and click **Next**.
     ```markdown
     4. In the Data Source Configuration wizard, select Database and click Next.
     ```

## Code Examples (if applicable)

```csharp
// Example of setting up a data source programmatically
using System;
using System.Collections.Generic;
using System.Data;
using Syncfusion.Windows.Forms.Grid;

public class DataSourceSetup
{
    public void ConfigureDataSource()
    {
        // Add your data source configuration logic here
        // For example, connecting to a database:
        var connectionString = "Your Connection String Here";
        var connectionStringBuilder = new SqlConnectionStringBuilder(connectionString);
        var dataSource = new SqlConnection(connectionStringBuilder.ConnectionString);
        
        // Bind the data source to the grid
        gridControl.DataSource = dataSource;
    }
}
```

## API Reference

### Properties
- DataSource: Used to bind data to the grid control.
```markdown
Properties:
- DataSource: Type of object used to bind the grid to a data source.
```

### Methods
- ConfigureDataSource(): Sets up the data source connection for the grid.
```markdown
Methods:
- ConfigureDataSource: Configures the data source connection for the grid control.
```

### Events
- DataSourceChanged: Triggered when the data source for the grid changes.
```markdown
Events:
- DataSourceChanged: Event raised when the grid's data source is changed.
```

## RAG Annotations
<!-- tags: Essential Grid, Data Source, Windows Forms, Smart Tag, Database Connection, Data Source Configuration Wizard keywords: Windows Forms, Data Source, database, grid control, Smart Tag, DataSource, DataSourceChanged -->
```