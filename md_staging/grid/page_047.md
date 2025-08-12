```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: grid
page_number: 047
page_id: grid#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:18:45Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Data Adapter Configuration Wizard

### Setting up the Data Connection

The image illustrates the "Data Adapter Configuration Wizard," where users set up their data connection for the Essential Grid in Windows Forms. The wizard helps configure the data adapter to execute queries using the specified connection to load and update data. Key elements from the image are as follows:

### Figure 10: Setting up the Data Connection

- **Choose Your Data Connection**
  - The data adapter will execute queries using this connection to load and update data.
  - Users can either choose from the list of existing data connections in Server Explorer or add a new connection if the desired one is not listed.

- **Which data connection should the data adapter use?**
  - A dropdown menu allows users to select an existing connection or create a new one using the "New Connection..." button.

### Navigation Buttons
- **Cancel**: Exits the wizard without saving changes.
- **< Back**: Returns to the previous step.
- **Next >**: Moves to the next step in the wizard.
- **Finish**: Completes the configuration and saves the settings.

### Instructions for Setting Up the Connection

1. Click **New Connection**. The Data Link Properties dialog box will be displayed.
2. In the **Provider** tab, select **Microsoft Jet 4.0 OLE DB Provider** option as shown in the following screenshot.

## Summary

This section provides a step-by-step guide for configuring a data connection using the Data Adapter Configuration Wizard in the Syncfusion Grid for Windows Forms. The process involves selecting or creating a data connection, ensuring the data adapter is set up correctly for executing queries and managing data.

## API Reference

### Properties
- **DataConnection**
  - Type: String
  - Description: Specifies the data connection to be used by the data adapter.

### Methods
- **ConfigureDataConnection**
  - Parameters:
    - `connectionString`: String - The connection string for the data source.
  - Returns: None
  - Description: Configures the data connection based on the provided connection string.

### Events
- **ConnectionChanged**
  - Triggered when the data connection is changed.

## Code Examples

### C#

```csharp
// Example of configuring a data connection
string connectionString = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\pathToDatabase\MyDatabase.mdb";
grid.ConfigDataConnection(connectionString);
```

### Important Notes

- Always ensure that the data source is accessible and that the connection string is correctly formatted to avoid runtime errors.
- For more detailed configuration options, refer to the Data Link Properties dialog box and the Provider tab settings.

## RAG Annotations
<!-- tags: grid, data adapter, windows forms, data connection, provider, configuration, essential grid, syncfusion sdk, jet OleDb, version 11.4.0.26 keywords: data adapter configuration wizard, microsoft jet 4.0 ole db provider, setting up data connection, data connection, c#, essential grid, windows forms, data source, connection string -->
```