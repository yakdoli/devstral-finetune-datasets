```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: grid
page_number: 046
page_id: grid#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:19:36Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Introduction to the Data Adapter Configuration Wizard.
- Step-by-step guide to creating a connection to the NWIND.mdb file using the wizard.

## Content

### Data Adapter Configuration Wizard
This guide demonstrates how to configure a data adapter using the Data Adapter Configuration Wizard. The wizard aids in specifying the connection details and database commands necessary for selecting and modifying records in the database.

#### Figure 9: Data Adapter Configuration Wizard
The wizard includes the following steps:

1. **Welcome Screen**:  
   The wizard welcomes users and provides an overview of the process. It explains that the wizard helps specify the connection and database commands used by the data adapter for interacting with the database. Users must provide connection information and decide how the database commands are stored and executed. Completing the wizard requires appropriate database permissions.

2. **Creating a Database Connection**:  
   Use this wizard to create a connection to the NWIND.mdb file. Click **Next** to proceed with the configuration.

```markdown
## API Reference (if applicable)

### Methods
- **CreateConnection()**
  - Establishes a connection to the NWIND.mdb file using the specified parameters.
  - Returns: `bool`
  - Parameters:
    - `connectionString`: string
    - `provider`: string
  - Exceptions:
    - InvalidOperationException: If required database permissions are missing.
```

### Code Examples
```csharp
// Example: Creating a connection using the Data Adapter Configuration Wizard
private void ConfigureDataAdapter()
{
    // Launch the Data Adapter Configuration Wizard to create a connection
    WizardForm wizardForm = new WizardForm();
    wizardForm.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=NWind.mdb;Persist Security Info=False;";
    wizardForm.ShowDialog();

    // Additional steps to configure the data adapter
    // ...
}
```

### Cross References
- Refer to the section on Database Connection Setup for more details on configuring database connectivity.
- See also the API documentation for additional methods and properties related to data adapter configuration.

<!-- tags: Windows Forms, Data Adapter, Configuration Wizard, NWIND.mdb, Data Editing, Database Interaction keywords: Syncfusion Windows Forms, Data Adapter Configuration, NWIND.mdb, Database Connection, Data Selection, Change Handling -->
```