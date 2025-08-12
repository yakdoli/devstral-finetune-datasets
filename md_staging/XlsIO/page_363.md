```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_363.jpeg
document_name: XlsIO
page_number: 363
page_id: XlsIO#page_363
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:38Z
fidelity: lossless
-->

# Essential XlsIO

```vb
'Creates the Data sorter
Dim sorter As IDataSort = book.CreateDataSorter()
'Specifies the sort range.
sorter.SortRange = range

Dim field As ISortField
' Adds the sort field with column index, sort based on and order by attribute
field = sorter.SortFields.Add(2, SortOn.CellColor, OrderBy.OnTop)
'Sorts the data based on this color
field.Color = Color.Red
' Sorts the data with the sort field attribute
sorter.Sort()
```

## 4.5.4 Import/Export

XlsIO has some helper methods that enable working with the ADO.NET data sources very easily.

### Importing

It only takes one line of code to import an ADO.NET data table into a worksheet. There are similar methods for working with other data sources like Data View, Data Column, Arrays, and so on. A data table from another source can be imported inside a worksheet by using the `ImportDataTable` method. It has an option to select the record range (row start, row end, col start and col end). It also allows preserving the data type in the data source.

### Exporting

Similarly, it is simple to export the sheet data to a data table by using the `ExportDataTable` method of IWorksheet. This method allows to select the various data table options such as include column names, export formula calculated values, styles and types, through the `ExcelExportDataTableOption` enumeration. It has the following values.

---

© 2013 Syncfusion. All rights reserved. 363 | Page
```