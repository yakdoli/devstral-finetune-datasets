```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_332.jpeg
document_name: DocIo
page_number: 332
page_id: DocIo#page_332
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:09Z
fidelity: lossless
-->

## Performing Mail Merge Using a Database in C#

### Overview
- Demonstrates how to perform a mail merge in C# using data from a database.
- Connects to a database, retrieves data, and merges it into a Word document template.
- Saves the merged document in DOC format.

### Content

#### Code Example: Mail Merge with Database in C#
```csharp
string dataBase = "Northwind.mdb";

// Open existing template
WordDocument doc = new WordDocument("EmployeesReportDemo.doc", FormatType.Doc);

// Get Data from the Database.
OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + dataBase);
conn.Open();

// Populate data table
DataTable table = new DataTable();
OleDbDataAdapter adapter = new OleDbDataAdapter("select * from employees", conn);
adapter.Fill(table);
adapter.Dispose();

// Perform Mail Merge
doc.MailMerge.Execute(table);

// Save the document
doc.Save("MailMerge.doc", FormatType.Doc);

// Close the document
doc.Close();
```

## API Reference
- **WordDocument**: Represents a document in Word format.
- **OleDbConnection**: Represents an Open Database Connectivity (ODBC) or a Microsoft Jet Database Engine (OLE DB) connection to a database.
- **OleDbDataAdapter**: Serves as a bridge between a DataSet and a data source for retrieving and saving data.
- **MailMerge.Execute**: Executes the mail merge operation using the specified data source.

## Cross References
- For more details on Syncfusion's DocIO library, refer to the official documentation.
- Additional examples and tutorials can be found in the Syncfusion WinForms user guide.

<!-- tags: DocIO, WinForms, mail merge, C# -->
```