```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_262.jpeg
document_name: XlsIO
page_number: 262
page_id: XlsIO#page_262
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:59Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
IPivotTable pivotTable = sheet1.PivotTables.Add("PivotTable1", sheet1["A1"], cache);
pivotTable.Fields[0].Axis = PivotAxisTypes.Row;
pivotTable.Fields[1].Axis = PivotAxisTypes.Row;
pivotTable.Fields[3].Axis = PivotAxisTypes.Column;

IPivotField field = pivotTable.Fields[2];
pivotTable.DataFields.Add(field, "sum", PivotSubtotalTypes.Sum);
```

## Properties

The following properties of the IPivotTable interface are used to fetch pivot table fields.

### Table 1: IPivotTable Properties Table

| Property         | Description                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------|
| Name             | Gets or sets pivot table name                                                                     |
| Location         | Returns pivot table location                                                                       |
| CacheIndex       | Gets Index of the pivot Cache. Read-only                                                          |
| Fields           | Gets collection of pivot fields. Read-only                                                        |
| DataFields       | Gets IDataField collection of pivot table data fields. Read-only                                 |
| ColumnFields     | Returns the collection of Column field for the specified pivot table. Read-only                   |
| RowFields        | Returns the collection of Row field for the specified pivot table. Read-only                      |
| PageFields       | Returns the collection of page field for the specified pivot table. Read-only                      |
| CalculatedFields | Returns the collection of calculated fields of the specified pivot table. Read-only                |
| ColumnsPerPage   | Specifies the number of columns per page for this PivotTable that the filter area will occupy      |
| RowsPerPage      | Specifies the number of rows per page for this PivotTable that the filter area will occupy         |
| Options          | Represents the pivot table options. Read-only                                                    |
```