```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_267.jpeg
document_name: DocIo
page_number: 267
page_id: DocIo#page_267
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:58Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Implements nested mail merge using the `WordDocument.MailMerge.ExecuteNestedGroup` method.
- Uses `DictionaryEntry` objects to map table names and commands for data retrieval.
- Retrieves the current value of a specified column in a table using the expression `"TableName.ColumnName"`.

## Content

### Nested Mail Merge with DocIO

Use `WordDocument.MailMerge.ExecuteNestedGroup` method to perform nested mail merge. Each item of the "command" `ArrayList` must contain 0 or more `DictionaryEntry` objects. Each `DictionaryEntry` object must contain the Table Name (DataTable name) and String Command with command, which must be applied to the table. Use the following expression for getting the current value of specified column in the table - `"%TableName.ColumnName%"`.

The following code snippet illustrates how a nested mail merge for a region or table is implemented by using DocIO.

### C# Implementation

```csharp
// Get Data from the Database
OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + dataBase);
conn.Open();

// ArrayList contains the list of commands
ArrayList commands = new ArrayList();

// DictionaryEntry contains "Source table" (KEY) and "Command" (VALUE)
DictionaryEntry entry = new DictionaryEntry("Employees", "Select TOP 10 * from Employees");
commands.Add(entry);

// To retrieve customer details
entry = new DictionaryEntry("Customers", "SELECT DISTINCT TOP 10 * FROM ((Orders INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID) INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID) WHERE Employees.EmployeeID = %Employees.EmployeeID%");
commands.Add(entry);

// To retrieve order details
entry = new DictionaryEntry("Orders", "SELECT DISTINCT TOP 10 * FROM Orders WHERE Orders.CustomerID = '%Customers.CustomerID%' AND Orders.EmployeeID = %Employees.EmployeeID%");
commands.Add(entry);

// Execute Mail merge
doc.MailMerge.ExecuteNestedGroup(conn, commands);
```

### VB Implementation

```vb
' Get Data from the Database.
Dim conn As New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + dataBase)
```

## Page-level Navigation/TOC (if applicable)
- This page focuses on implementing nested mail merge using DocIO in C# and VB, providing example code snippets for each language.

## Cross References
- Refer to the DocIO section in the Syncfusion Winforms documentation for more information on mail merge functionalities.

<!-- tags: DocIO, mail merge, nested mail merge, C#, VB, ArrayList, DictionaryEntry, OleDbConnection, version: 11.4.0.26 -->
```