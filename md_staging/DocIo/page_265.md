```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_265.jpeg
document_name: DocIo
page_number: 265
page_id: DocIo#page_265
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:53Z
fidelity: lossless
-->


## Overview
- Executes nested mail merge for a group (Region or tables).

## Content

### MailMerge Class Usage Example

The following example illustrates how to use the MailMerge class for different data sources.

```csharp
[C#]

IWordDocument document = new WordDocument("MailMergeDocument.doc");

// Mail merge operations with string arrays data sources
string[] fieldNames = new string[] { "Continent", "Country", "Region" };
string[] fieldValues = new string[] { "Eurasia", "Germany", "Bavaria" };
document.MailMerge.Execute(fieldNames, fieldValues);

// Mail merge operations with DataTable data source containing data from database.
DataTable table = GetDataTable("select * from Geography");
document.MailMerge.Execute(table);

// Mail merge operations with DataView data source, created basing on the DataTable
DataView dataView = new DataView(GetDataTable("select * from Geography"));
dataView.Sort = "CountryName ASC";
document.MailMerge.Execute(dataView);

// Mail merge operations with DataReader data source
IDataReader dataReader = GetDataReader("select * from Geography ");
document.MailMerge.Execute(dataReader);
dataReader.Close();

// Mail merge operations for the specified region
DataTable table = GetDataTable("select * from Employees");
table.TableName = "Geography";
document.MailMerge.ExecuteGroup(table);

document.Save("AfterMailMerge.doc");
// or
document.Save("AfterMailMerge.docx", FormatType.Docx);
```

### VB.NET

```vb.net
[Vb.NET]
```

## API Reference

### Methods
- `Execute(string[] fieldNames, string[] fieldValues)`: Executes mail merge operations with string arrays as the data source.
- `Execute(DataTable table)`: Executes mail merge operations with DataTable data source containing data from database.
- `Execute(DataView dataView)`: Executes mail merge operations with DataView data source, created basing on the DataTable.
- `Execute(IDataReader dataReader)`: Executes mail merge operations with DataReader data source.
- `ExecuteGroup(DataTable table)`: Executes nested mail merge for a group (Region or tables).

## Code Examples

### C# Example
```csharp
IWordDocument document = new WordDocument("MailMergeDocument.doc");

string[] fieldNames = new string[] { "Continent", "Country", "Region" };
string[] fieldValues = new string[] { "Eurasia", "Germany", "Bavaria" };
document.MailMerge.Execute(fieldNames, fieldValues);

DataTable table = GetDataTable("select * from Geography");
document.MailMerge.Execute(table);

DataView dataView = new DataView(GetDataTable("select * from Geography"));
dataView.Sort = "CountryName ASC";
document.MailMerge.Execute(dataView);

IDataReader dataReader = GetDataReader("select * from Geography ");
document.MailMerge.Execute(dataReader);
dataReader.Close();

DataTable table = GetDataTable("select * from Employees");
table.TableName = "Geography";
document.MailMerge.ExecuteGroup(table);

document.Save("AfterMailMerge.doc");
document.Save("AfterMailMerge.docx", FormatType.Docx);
```

### VB.NET Example
```vb.net
' VB.NET implementation will be similar to the C# example above but written in VB.NET syntax.
```

<!-- tags: [Syncfusion, Winforms, MailMerge, DataTable, DataView, DataReader, Region, nested mail merge, .doc, .docx] -->
```