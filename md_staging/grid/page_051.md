```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: grid
page_number: 051
page_id: grid#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:19:02Z
fidelity: lossless
-->

## Setting the MDB File as the Data Connection

This section guides users through setting up a data connection using an MDB file in the context of Syncfusion's WinForms for Windows Forms.

---

### Data Adapter Configuration Wizard

The data adapter uses the selected data connection to execute queries for loading and updating data.

1. **Choose Your Data Connection:**
   - Select from the list of data connections available in Server Explorer.
   - Alternatively, add a new connection if the desired one is not listed.

2. **Connection Setup:**
   - The dialog box displays the following options:
     - **Connection Drop-down:** Lists available connections, e.g., `ACCESS.C:\Data\nwind.mdb.Admin`.
     - **New Connection Button:** Allows adding a new data connection.

3. **Navigation Buttons:**
   - **Cancel:** Exits the wizard without saving changes.
   - **Back:** Navigates to the previous step.
   - **Next:** Proceeds to the next step in the wizard.
   - **Finish:** Completes the configuration process.

**Example Configuration Window:**

```plaintext
Data Adapter Configuration Wizard

Choose Your Data Connection
The data adapter will execute queries using this connection to load
and update data.

Choose from the list of data connections currently in Server Explorer or add a new
connection if the one you want is not listed.

Which data connection should the data adapter use?
ACCESS.C:\Data\nwind.mdb.Admin

Cancel | < Back | Next > | Finish
```

---

### Steps to Configure the Data Connection

1. **Open Connection Options:**
   - Ensure the appropriate database file (e.g., `nwind.mdb`) is selected as the data source.

2. **Set Query Type:**
   - Select **Use SQL statements** as the query type.

3. **Proceed to Next Step:**
   - After setting up the data connection, click **Next** to continue.

---

## Additional Information

For detailed API references and code examples, refer to the relevant sections in the Syncfusion documentation.

---

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Data Adapter Configuration, Windows Forms] keywords: [Data Adapter, Query, Connection, MDB File, Wizard, SQL Statements] -->
```