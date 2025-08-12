```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_264.jpeg
document_name: DocIo
page_number: 264
page_id: DocIo#page_264
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:18Z
fidelity: lossless
-->

# Essential DocIO

## ExecuteGroup

- **void ExecuteGroup(DataTable table):** performs replacements of merge fields, in which field names match the table column names, with the corresponding values of table cells.

These replacements are performed for every row contained in the table in the specified region. The region where the mail merge operations are to be performed must be marked by two MergeFields with the following names:

- **TableStart:TableName:** for the entry point of the region
- **TableEnd:TableName:** for the end point of the region

For example, consider you have a DataTable containing the same data as in the previous example, and you want to get the document with the following content:

```
Australia
USA
France
   are beautiful countries.
```

You have to insert three MergeFields in the document with the following field names:

- **TableStart:Geography:** marks the beginning of the mail merge region.
- **Country:** will be replaced by values from the table, "Geography".
- **TableEnd:Geography:** marks the end of the mail merge region.

- **void ExecuteGroup(DataView dataView):** works similarly to that with DataTable parameter.
- **void ExecuteGroup(IDataReader dataReader):** works similarly to that with DataTable parameter.

## Public Methods

| Name                 | Description                          |
|----------------------|--------------------------------------|
| Execute              | Executes mail merge.                |
| ExecuteGroup         | Executes mail merge for a group (region). |
| GetMergeFieldNames   | Returns a collection of mergefield names found in |

## References
- Copyright © 2013 Syncfusion. All rights reserved.

<!-- tags: [DocIo, mail merge, Databiew, IDareader, DataTable, executegroup, public methods, essential docio, syncfusion winforms] keywords: [mergefields, content replacement, table data, region, entry point, end point, countries, sample, execute mail merge, execute group, getmergefieldnames, datareader, dataview] -->
```