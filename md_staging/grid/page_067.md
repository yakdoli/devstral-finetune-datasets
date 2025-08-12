```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: grid
page_number: 067
page_id: grid#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:20:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- **Choose Your Data Connection**: Select the appropriate data connection for your application to interact with the database.
- **Handling Sensitive Data**: Decide whether to include sensitive data, such as passwords, in the connection string, avoiding potential security risks.
- **Connection String Setup**: Configure the connection string, ensuring all necessary credentials and details are included or managed securely.

## Content

### Data Source Configuration Wizard

The **Data Source Configuration Wizard** assists in setting up the necessary configuration for connecting your application to a database. Below are the steps to guide you through this process:

#### Step 5: Modify Existing Data Connection

1. **Open the Add Connection Dialog Box**:
   - If you have an existing connection that you wish to modify, use the **Add Connection** dialog box.
   - Click the **Change** button to initiate the process of modifying the current data connection.

2. **Choose the Change Data Source Option**:
   - Clicking the **Change** button will open the **Change Data Source** dialog box. This dialog box allows you to alter the existing data source settings.

#### Choosing the Data Connection

The dialog presents options for managing the connection string, focusing on the inclusion of sensitive data such as passwords. Here's a brief overview of the choices provided:

- **No, exclude sensitive data**: This option allows you to exclude sensitive data from the connection string. Instead, you will manage this information within your application code, enhancing security.
- **Yes, include sensitive data**: If you choose this option, sensitive data will be included in the connection string, which might pose a security risk.

#### Configuration Wizard Interface

The interface displays:
- Dropdown selection for existing connections.
- An option to create a **New Connection**.
- Clear instructions and considerations about embedding sensitive data in the connection string.

## Figure: Choosing the Data Connection

### WinForms-specific Conventions

Ensure to follow these conventions when setting up and managing data connections within a Windows Forms application using Syncfusion controls:
- Utilize the **Data Source Configuration Wizard** properly to integrate with your application.
- Always prioritize security by managing sensitive data appropriately.
- Ensure your connection strings are accurate and up-to-date.

## Page-level Navigation/TOC

- **Step 5**: Modify Existing Data Connection
  - Open the Add Connection dialog box
  - Choose the Change Data Source option

## Cross References

- Refer to **Step 4** for setting up a new data connection using the New Connection option. 

<!-- tags: [data-source-configuration, windows-forms, syncfusion, sensitive-data-handling, data-connections] keywords: [Choose Your Data Connection, sensitive data, connection string, Data Source Configuration Wizard] -->
```