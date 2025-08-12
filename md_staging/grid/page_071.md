```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_071.jpeg
document_name: grid
page_number: 071
page_id: grid#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:20:19Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Walkthrough of configuring connection strings for data sources in a Windows Forms application.
- Saving connection strings to the application configuration file for easier maintenance and deployment.
- Selection of database tables for use in the application.

## Content

### Figure 36: Connection String Dialog

**Figure 36: Connection String Dialog**

This figure illustrates the "Data Source Configuration Wizard" dialog, specifically the step where users are prompted to save the connection string to the application configuration file. The dialog provides the following information and options:

#### Prompt
- **Message**: Storing connection strings in your application configuration file eases maintenance and deployment. To save the connection string in the application configuration file, enter a name in the box and then click Next.
- **Checkbox**: "Yes, save the connection as:"
  - **Input Box**: Contains the default name `NWindConnectionString`.

#### Navigation Buttons
- **Previous**: To go back to the previous step.
- **Next**: To proceed to the next step.
- **Finish**: To complete the wizard configuration.
- **Cancel**: To exit the wizard without saving changes.

### Instructions for Database Object Selection
10. Click **Next** to choose your Database Objects. Select the Tables that you want. Click **Finish**.

## API Reference
- **Connection String Configuration**: 
  - The dialog suggests saving connection strings in the application configuration file for easier maintenance and deployment.
  - The connection string can be saved with a custom name, default being `NWindConnectionString`.

## Code Examples
```csharp
// Example of configuring connection strings in the application's configuration file.
<connectionStrings>
  <add name="NWindConnectionString"
       connectionString="server=your_server;database=your_database;uid=your_username;pwd=your_password;"
       providerName="System.Data.SqlClient" />
</connectionStrings>
```

## RAG Annotations
<!-- tags: [Essential Grid for Windows Forms, Windows Forms, Data Source Configuration Wizard, Connection Strings] keywords: [connection string dialog, database objects, tables, configuration file, application maintenance, deployment] -->
```