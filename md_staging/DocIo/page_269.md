```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_269.jpeg
document_name: DocIo
page_number: 269
page_id: DocIo#page_269
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:15Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates the implementation of a nested mail merge for a region or table using a Data Set.
- Explains the use of `ArrayList commands` and `bool isSqlConnection` for fetching specified data from the database.
- Highlights the process of querying data from multiple tables and executing nested group mail merge operations.

## Content

### Nested Mail Merge Implementation

The following code snippet illustrates how to implement a nested mail merge for a region or table by using a Data Set.

```csharp
[C#]

public void CreateDocument()
{
    WordDocument doc = new WordDocument();
    doc.Open( dataPath + "NestedMailMerge1.doc" );

    // Get Data from the Database.
    DataTable table1 = GetNestedDataTable( "select * from Table1" );
    table1.TableName = "Table1";

    DataTable table2 = GetNestedDataTable( "select * from Table2" );
    table2.TableName = "Table2";

    DataTable table3 = GetNestedDataTable( "select * from Table3" );
    table3.TableName = "Table3";

    DataSet dataSet = new DataSet( "Test dataset" );
    dataSet.Tables.Add( table1 );
    dataSet.Tables.Add( table2 );
    dataSet.Tables.Add( table3 );

    // Arraylist contains the list of commands.
    ArrayList commands = new ArrayList();
    DictionaryEntry entry = new DictionaryEntry( "Table1", string.Empty );
    commands.Add( entry );

    entry = new dictionaryentry("table2", "sellerid = %table1.sellerid%");
    commands.Add( entry );

    entry = new DictionaryEntry("Table3", "CustomerID = %Table2.CustomerID%");
    commands.Add( entry );

    doc.MailMerge.RemoveEmptyParagraphs = true;

    // Execute NestedGroup by passing the DataSet.
    doc.MailMerge.ExecuteNestedGroup(dataSet, commands );
}
```

## API Reference

### Parameters

- `commands`: An `ArrayList` containing the list of commands for the mail merge operations.
- `dataSet`: A `DataSet` object that holds the data retrieved from the database.
- `isSqlConnection`: A `bool` value indicating whether the connection is an SQL connection. If it is an SQL connection, set this value to `True`.

### Return Type

This method does not return a value but modifies the `WordDocument` object by executing the nested mail merge operations.

## Code Examples

The above example demonstrates how to:

1. Open a Word document for mail merge.
2. Retrieve data from multiple tables.
3. Create a `DataSet` and populate it with the retrieved tables.
4. Define `DictionaryEntry` objects to specify the merge conditions.
5. Execute the nested mail merge using the `ExecuteNestedGroup` method.

## Cross References

- See also: [Nested Mail Merge Documentation](#nested-mail-merge-documentation)

<!-- tags: [syncfusion, winforms, docio, mail merge, nested mail merge, dataset, arraylist, dictionaryentry] keywords: [worddocument, datatables, mailmerge, executenestedgroup, commands, dataset, dictionaryentry] -->
```