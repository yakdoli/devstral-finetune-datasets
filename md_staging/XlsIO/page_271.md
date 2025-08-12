```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_271.jpeg
document_name: XlsIO
page_number: 271
page_id: XlsIO#page_271
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:12Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates creating and configuring a PivotTable using XlsIO.
- Focuses on setting up filters, axes, and layout options to align with MS Excel.

## Content

### Adding and Configuring a PivotTable in C#

```csharp
// C#
IPivotCache cache = book.PivotCaches.Add(sheet["A1:D136"]);
IPivotTable pivotTable = sheet1.PivotTables.Add("PivotTable1", sheet1["A1"], cache);

IPivotField field = pivotTable.Fields[0];
Field.Axis = PivotAxisTypes.Page;
// Setting the Filter to Page field of Pivot table
IPivotFilter filter = field.PivotFilters.Add();
filter.Value1 = "East";

pivotTable.Fields[0].FilterValue = "Binder";
pivotTable.Fields[1].Axis = PivotAxisTypes.Row;
pivotTable.Fields[3].Axis = PivotAxisTypes.Column;

IPivotField field = pivotTable.Fields[2];
pivotTable.DataFields.Add(field, "sum", PivotSubtotalTypes.Sum);
// The following code sample must be included to XlsIO layout the pivot
// table like MS Excel.
pivotTable.Layout();
```

### Adding and Configuring a PivotTable in VB.Net

```vb
' VB.Net

Dim cache As IPivotCache = book.PivotCaches.Add(sheet("A1:D136"))
Dim pivotTable As IPivotTable = sheet1.PivotTables.Add("PivotTable1", sheet1("A1"), cache)

Dim field As IPivotField = pivotTable.Fields(0)
Field.Axis = PivotAxisTypes.Page
' Setting the Filter to Page field of Pivot table
Dim filter As IPivotFilter = field.PivotFilters.Add()
```

## API Reference

- **Namespace**: Syncfusion.XlsIO
- **Class**: PivotTable
  - **Methods**:
    - `PivotTables.Add`: Adds a new PivotTable to the worksheet.
    - `PivotFilters.Add`: Adds a new filter to the PivotTable field.
    - `PivotAxes`: Sets the axes for the PivotTable fields.
    - `Layout`: Adjusts the layout of the PivotTable to mimic the Excel-like layout.

## Code Examples

### C# Example

```csharp
// Adding a pivot table and configuring its fields
IPivotCache cache = book.PivotCaches.Add(sheet["A1:D136"]);
IPivotTable pivotTable = sheet1.PivotTables.Add("PivotTable1", sheet1["A1"], cache);

// Configuring the fields
foreach (IPivotField field in pivotTable.Fields)
{
    if (field.Name == "PageField")
    {
        field.Axis = PivotAxisTypes.Page;
        IPivotFilter filter = field.PivotFilters.Add();
        filter.Value1 = "East";
    }
    else if (field.Name == "RowField")
    {
        field.Axis = PivotAxisTypes.Row;
    }
    else if (field.Name == "ColumnField")
    {
        field.Axis = PivotAxisTypes.Column;
    }
    else
    {
        pivotTable.DataFields.Add(field, "sum", PivotSubtotalTypes.Sum);
    }
}

pivotTable.Layout(); // Lays out the PivotTable similar to how Excel does
```

### VB.Net Example

```vb
' Adding a pivot table and configuring its fields
Dim cache As IPivotCache = book.PivotCaches.Add(sheet("A1:D136"))
Dim pivotTable As IPivotTable = sheet1.PivotTables.Add("PivotTable1", sheet1("A1"), cache)

' Configuring the fields
For Each field As IPivotField In pivotTable.Fields
    If field.Name = "PageField" Then
        field.Axis = PivotAxisTypes.Page
        Dim filter As IPivotFilter = field.PivotFilters.Add()
        filter.Value1 = "East"
    ElseIf field.Name = "RowField" Then
        field.Axis = PivotAxisTypes.Row
    ElseIf field.Name = "ColumnField" Then
        field.Axis = PivotAxisTypes.Column
    Else
        pivotTable.DataFields.Add(field, "sum", PivotSubtotalTypes.Sum)
    End If
Next

pivotTable.Layout() ' Lays out the PivotTable similar to how Excel does
```

## Conclusion

This code guides users through the process of creating a PivotTable using XlsIO, focusing on setting up filters, axes, and configuring the PivotTable layout to match the behavior of MS Excel. The examples demonstrate C# and VB.Net implementations, enabling developers to integrate PivotTables into their applications effectively.

<!-- tags: [XlsIO, PivotTable, data analysis, Excel, filter configuration, layout, MS Excel, C#, VB.Net] keywords: [PivotTable, PivotCache, PivotFilter] -->
```