```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_261.jpeg
document_name: XlsIO
page_number: 261
page_id: XlsIO#page_261
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:58Z
fidelity: lossless
-->

# Essential XlsIO

## Adding Fields to the Pivot Table

### Figure 91: Adding Fields to the Pivot Table
![Figure 91: Adding Fields to the Pivot Table](https://example.com/image_url)

To filter by a field, open its drop-down list and select the value by which to filter. The table now displays data only for the filtered criterion (in this case, the Central region).

You can also sort by a field by opening its drop-down list and selecting one of the sort orders.

## PivotTable Creation Manipulation Using XlsIO

XlsIO provides support for creation and manipulation of Pivot Table by using simple APIs. IPivotCache interface caches the data that needs to be summarized. IPivotTable represents a pivot table in object, and has properties that allow customizing it. IPivotTable interface returns the collection of Pivot Tables present in a worksheet. IPivotField represents the field in the pivot table. This includes row, column and data field axis. IPivotDataFields gets collection of data field.

**Note**: Pivot Table is currently not supported for .xls format.

### Example: Creating a Pivot Table Using XlsIO

The following code example illustrates how to create a pivot table by using XlsIO.

```csharp
IPivotCache cache = book.PivotCaches.Add(sheet["A1:D136"]);
```

## Summary

This section explains how to add fields to a Pivot Table, filter and sort data, and manipulate Pivot Tables using the XlsIO library in Syncfusion Winforms. It also provides a code example demonstrating the creation of a Pivot Table.

## API Reference

### Classes
- **IPivotCache**: Caches the data needed for summarization.
- **IPivotTable**: Represents and customizes a pivot table.
- **IPivotField**: Represents a field in the pivot table.
- **IPivotDataFields**: Represents the collection of data fields.

### Methods
- **Add**: Adds a new pivot cache.
- **Update**: Updates the pivot table layout.

## Code Examples

```csharp
// Example: Creating a Pivot Table
IPivotCache cache = book.PivotCaches.Add(sheet["A1:D136"]);

// Example: Adding Fields to the Pivot Table
var pivotTable = cache.CreatePivotTable();
pivotTable.RowLabels.Add("Region");
pivotTable.ColumnLabels.Add("Employee");
pivotTable.DataFields.Add("Units");
pivotTable.DataFields.Add("Total");
// Additional configuration as needed
```

<!-- tags: [XlsIO, PivotTable, WindowsForms, Syncfusion, XlsIO API] keywords: [PivotTable, IPivotCache, IPivotTable, IPivotField, IPivotDataFields, filter, sort, creation, manipulation, XlsIO] -->
```