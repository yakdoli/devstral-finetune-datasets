```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: grid
page_number: 068
page_id: grid#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:20:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Configuring database connections for data source integration.
- Selecting the appropriate data source type from the options provided.
- Logging into the database with necessary credentials.

## Content

### Add Connection Dialog Box
The dialog box shown in Figure 31 is used to establish a connection to a selected data source or choose a different data source and/or provider. The user can enter the required information, including the type of data source, the database file name, and login credentials for accessing the database.

#### Figure: Add Connection Dialog Box
- **Data source:** Microsoft Access Database File (OLE DB)
- **Database file name:** (User must specify the file name or browse for the file location.)
- **Log on to the database:** 
  - **User name:** Admin
  - **Password:** (User must provide the password if required.)
  - **Save my password:** (Optional checkbox to save the password for future use.)
- The user can also test the connection before confirming the settings.

### Choosing the Data Source
In the Change Source dialog box, as shown in Figure 32, the Microsoft Access Database File option is selected. After selecting the appropriate data source, the user clicks OK to confirm the choice.

#### Figure: Choosing the Data Source
- **Data source:** 
  - Microsoft Access Database File
  - Microsoft ODBC Data Source
  - Microsoft SQL Server
  - Microsoft SQL Server Database File
  - Microsoft SQL Server Mobile Edition
  - Oracle Database
  - <other>
- **Description:** Use this selection to connect to a Microsoft Access database file using the native Jet provider through the .NET Framework Data Provider for OLE DB.
- **Data provider:** .NET Framework Data Provider for OLE DB
- The user can choose to always use this selection.

#### Instructions
6. In the Change Source dialog box, select the Microsoft Access Database File option, and then click OK.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** GridControl
- **Methods/Properties:**
  - Use the appropriate methods or properties to fetch and display database data in the grid control.

## Code Examples
```csharp
// C# Example
String connectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=mydatabase.mdb;";
GridConnection gridConnection = new GridConnection(connectionString);
gridControl.DataSource = gridConnection;
```

## Page-level Navigation/TOC
- Step 6: Select Microsoft Access Database File
- Configure Logon Details
- Confirm Connection

## Cross References
- See also: Chapter on Data Source Integration and Connection Management.

<!-- tags: [syncfusion, windows forms, data source, database integration, connection management, grid control] keywords: [essential grid, microsoft access, database file, oledb, login, password, connection, data provider] -->
```