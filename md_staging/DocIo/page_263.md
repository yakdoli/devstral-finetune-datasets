```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_263.jpeg
document_name: DocIo
page_number: 263
page_id: DocIo#page_263
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:41Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- This section describes the `Execute` method used for performing replacements in a document based on field names and values.
- Two main versions of the `Execute` method are covered: one using field names and values arrays, and the other using a `DataTable` object.

## Content

### Execute
- **void Execute(string[] fieldNames, string[] fieldValues):**
  - Performs replacements of every merge field in the document, where the field name matches one of the values from the `fieldNames` string array. The corresponding value from the `fieldValues` string array is used for replacement.
  
- **void Execute(DataTable table):**
  - Performs replacements of merge fields, where field names match the table column names, with the corresponding values of table cells. These replacements are performed for every row contained in the table.

#### Example
Consider you have a document containing a single page with a MergeField on it, whose field name is "Country", with the words: "is a beautiful country". Also, you have a `DataTable`, "Geography", containing the following data:

| Column | Continent    | Country  |
|--------|--------------|----------|
| 1      | Australia    | Australia|
| 2      | North America| USA      |
| 3      | Eurasia      | France   |

After performing mail merge operations, you will have a document containing three pages with the following text:

1 page: Australia is a beautiful country.  
2 page: USA is a beautiful country.  
3 page: France is a beautiful country.

#### Using the Next Field
You can also use the `Next` field if you want to display the values of some rows at the same place. For example, if you want to enumerate all the countries contained in the table, you have to insert the `Next` field before every MergeField, with field name "Country" beginning with the second MergeField.

### Additional Methods
- **void Execute(DataRow row):**
  - Works similarly to that with `DataTable` parameter for the only row.
  
- **void Execute(DataView dataView):**
  - Works similarly to that with `DataTable` parameter.
  
- **void Execute(IDataReader dataReader):**
  - Works similarly to that with `DataTable` parameter.

## API Reference
- **Namespace**: EssentialDocIO
- **Members**:
  - `void Execute(string[] fieldNames, string[] fieldValues)`
  - `void Execute(DataTable table)`
  - `void Execute(DataRow row)`
  - `void Execute(DataView dataView)`
  - `void Execute(IDataReader dataReader)`

## Code Examples
- The sample code demonstrates the usage of the `Execute` method for merging fields in a document using different parameters.

## Cross References
- For more information on creating and managing `DataTables`, refer to the specific section in the WinForms documentation.

<!-- tags: syncfusion, docio, mail merge, data handling, field replacements, datatable, dribbble, version: 11.4.0.26 -->
```