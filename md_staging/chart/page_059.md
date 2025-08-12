```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: chart
page_number: 059
page_id: chart#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:52Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- A step-by-step guide to configuring a database connection for data source selection.
- Covers use of data providers, selection of database files, and connection testing.
- Demonstrates the process of setting up the connection via the Add Connection dialog box.

## Content

![Choose Data Source Dialog Box](https://raw.githubusercontent.com/user/repo/assets/dialog-box-1.png "Figure 32: Choose Data Source Dialog Box")
*Figure 32: Choose Data Source Dialog Box*

6. This opens the **Add Connection** dialog box. Click the **Browse** button and select the database file from any location. Click **OK** to make this connection available to the Data source Configuration Wizard.

### Database Connection Setup

![Selecting the Database File](https://raw.githubusercontent.com/user/repo/assets/dialog-box-2.png "Figure 33: Selecting the Database file by clicking on the Browse Button in the Add Connection Dialog Box")
*Figure 33: Selecting the Database file by clicking on the Browse Button in the Add Connection Dialog Box*

### Step-by-Step Process
- **Choose Data Source Dialog Box**:  
  - **Data source**: Provides options like `Microsoft Access Database File` and `Microsoft SQL Server Database File`.
  - **Data provider**: Lists available data providers, such as `.NET Framework Data Provider for OLE DB`.
  - **Always use this selection**: Ensures that the current selection is remembered.
  - **Description**: Guides the user on connecting to the selected database type.

- **Add Connection Dialog Box**:  
  - **Data source**: Displays the selected data source (e.g., `Microsoft Access Database File (OLE DB)`).
  - **Database file name**: Allows specifying or browsing for the database file path.
  - **Log on to the database**: Requires entering a valid `User name` and `Password` for database access.
  - **Advanced Options**: Provides further configuration options for database connections.
  - **Test Connection**: Allows the user to verify the connection before confirming.

- **Connection Confirmation**:  
  - Click the **OK** button to confirm the database connection settings.
  - Alternatively, click **Cancel** to abort the connection process.

### Key Features
- **Dynamic Data Source Selection**: Flexibility in selecting different types of database files.
- **User Authentication**: Ensures secure access by requiring valid credentials.
- **Connection Testing**: Validates the connection before it is saved.
- **Save My Password**: Option to retain user credentials for convenience.

## Page-level Navigation/TOC
- **Choose Data Source Dialog Box**
- **Add Connection Dialog Box**
- **Database Connection Setup**
- **Connection Confirmation**

## Cross References
- Refer to related sections on configuring data sources and handling database connections in the WinForms documentation.

<!-- tags: [syncfusion, winforms, chart, database, connection, data source] keywords: [Data Source, Add Connection, Database File, User Authentication, Connection Testing, Data provider] -->
```