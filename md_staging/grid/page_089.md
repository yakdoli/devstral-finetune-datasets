```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_089.jpeg
document_name: grid
page_number: 089
page_id: grid#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:51Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of SqlDataAdapter and SqlConnection in a Windows Forms application.
- Explains the process of generating a DataSet from a SQLDataAdapter.
- Guides users through creating and configuring database connections and data adapters.

## Generating a Dataset from SQLDataAdapter

### Design Surface Setup
The design surface includes:
- **Form1.cs [Design]** showing the main form where you can drag and drop SQL components.
- **sqlDataAdapter1** and **sqlConnection1** components added to the design surface for database interaction.

**Figure 55: Adapter and Connection**

![](image.png)

#### Step-by-Step Instructions
1. **Open the Design Surface**:
   - Ensure you have the necessary components (`sqlDataAdapter1` and `sqlConnection1`) added to your form design surface.
2. **Prepare to Generate the DataSet**:
   - You are ready to generate a dataset from the `sqlDataAdapter1`. Right-click on `sqlDataAdapter1` under the design surface.

3. **Generate the DataSet**:
   - Right-click the `sqlDataAdapter1` under the design surface and select **Generate DataSet**.
   - This operation will lead you to the next stage: a configuration window for generating the dataset.

### Notes:
- **DataSet Generation**: This step is crucial for enabling the application to interact with the database using strongly typed datasets.
- **Data Interaction**: Generated datasets allow easier and more efficient manipulation of data within your Windows Forms application.

## API Reference
- **sqlDataAdapter1**: Used for filling a DataSet or DataTable with data from a database.
- **sqlConnection1**: Manages the connection to the database, providing a way to specify the server, database, username, and password.

## Code Examples
```csharp
// Example: Configuring the SqlDataAdapter and SqlConnection
using System.Data.SqlClient;

public void ConfigureDataAccess()
{
    string connectionString = "Data Source=servername;Initial Catalog=databasename;User ID=username;Password=password;";

    using (SqlConnection connection = new SqlConnection(connectionString))
    {
        SqlDataAdapter adapter = new SqlDataAdapter();
        adapter.SelectCommand = new SqlCommand("SELECT * FROM TableName", connection);

        // Generate DataSet
        DataSet dataSet = new DataSet();
        adapter.Fill(dataSet);

        // Use the DataSet to populate a Grid or any other component
    }
}
```

### See also:
- [Using DataAdapters in Windows Forms](link)
- [DataSet Documentation](link)

<!-- tags: [grid, winforms, Syncfusion, dataset, sqladapter, sqlconnection] keywords: [database interaction, dataset generation, windows forms, data manipulation] -->
```