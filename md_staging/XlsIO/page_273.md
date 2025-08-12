```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_273.jpeg
document_name: XlsIO
page_number: 273
page_id: XlsIO#page_273
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:38Z
fidelity: lossless
-->

## XlsIO

### Overview
- Accesses the first worksheet in the workbook to create a pivot table.
- Configures the pivot table by setting dimensions, adding fields, creating data caches, and applying filters.
- Demonstrates how to manipulate pivot table fields and subtotals programmatically.

## Content

### Creating and Configuring a Pivot Table

#### Accessing and Defining the Worksheet
```csharp
// The first worksheet object in the worksheets collection is accessed.
IWorksheet worksheet = workbook.Worksheets[0];

// Access the worksheet to draw pivot table.
IWorksheet pivotSheet = workbook.Worksheets[1];
```

#### Defining the Data Cache
```csharp
// Select the data to add in cache.
IPivotCache cache = workbook.PivotCaches.Add(worksheet["A1:H50"]);
```

#### Inserting and Configuring the Pivot Table
```csharp
// Insert the pivot table.
IPivotTable pivotTable = pivotSheet.PivotTables.Add("PivotTable1", pivotSheet["A1"], cache);

// Set field axis to page.
pivotTable.Fields[4].Axis = PivotAxisTypes.Page;

// Set field axis to row.
pivotTable.Fields[2].Axis = PivotAxisTypes.Row;
pivotTable.Fields[6].Axis = PivotAxisTypes.Row;

// Set field axis to column.
pivotTable.Fields[3].Axis = PivotAxisTypes.Column;
```

#### Adding Data Fields with Subtotals
```csharp
IPivotField field = pivotSheet.PivotTables[0].Fields[5];
pivotTable.DataFields.Add(field, "Sum of Units", PivotSubtotalTypes.Sum);
```

#### Applying Filters to the Pivot Table
```csharp
// Apply page field filter.
IPivotField pageField = pivotTable.Fields[4];

// Select multiple items in page field to filter.
pageField.Items[1].Visible = false;
pageField.Items[2].Visible = false;
```

<!-- tags: [xlsio, pivot table, worksheet, field axis, subtotals, filters, syncfusion, winforms] keywords: [pivot table configuration, data cache, axis settings, subtotal addition, filter application] -->
```