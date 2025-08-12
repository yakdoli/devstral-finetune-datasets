```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_644.jpeg
document_name: grid
page_number: 644
page_id: grid#page_644
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:30:42Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section explains how to handle summary columns and display summaries in cells for a `GridGroupingControl` in WinForms applications.
- Demonstrates using `GridColumnDescriptor` and `ManualTotalSummary` to manage summary calculations and styling.

## Content

### Understanding Summary Columns in GridGroupingControl

The `TableCellIdentity.SummaryColumn` will be `null`, indicating that the column is not a summary column. You can retrieve the summary column using the following steps:

```csharp
GridColumnDescriptor column = 
gridGroupingControl1.TableModel.GetHeaderColumnDescriptorAt(e.TableCellIdentity.ColIndex);

if (column != null &&
    table.TotalSummaries.IndexOf(column.MappingName) != -1)
{
    int index = column.TableDescriptor.Fields.IndexOf(column.FieldDescriptor);
    IManualTotalSummaryArraySource tsa = (el is Group ? el : el.ParentGroup) as IManualTotalSummaryArraySource;
    ManualTotalSummary tm = tsa.GetManualTotalSummaryArray()[index];
    e.Style.CellValue = tm.Total;
    e.Style.CellValueType = typeof(double);
    e.Style.Format = "0.00";
}

// By using that column you could try and identify the summary that should be displayed in this cell.
}
```

### Handling Summary Rows

For summary rows identified as `GridSummaryRow`, you can similarly retrieve the column and display the summary value:

```csharp
GridColumnDescriptor column = 
this.gridGroupingControl1.TableModel.GetHeaderColumnDescriptorAt(e.TableCellIdentity.ColIndex);

if (column != null &&
    table.TotalSummaries.IndexOf(column.MappingName) != -1)
{
    int index = column.TableDescriptor.Fields.IndexOf(column.FieldDescriptor);
    IManualTotalSummaryArraySource tsa = (el is Group ? el : el.ParentGroup) as IManualTotalSummaryArraySource;
    ManualTotalSummary tm = tsa.GetManualTotalSummaryArray()[index];
    e.Style.CellValue = tm.Total;
    e.Style.CellValueType = typeof(double);
    e.Style.Format = "0.00";
}

// By using that column you could try and identify the summary that should be displayed in this cell.
}
```

### Key Concepts

- **SummaryColumns**: Columns used to display summary values in the grid.
- **Manual Total Summary**: Custom summary calculations implemented using `IManualTotalSummaryArraySource`.
- **Format**: Specifies how summary values are displayed in the grid.

## Code Examples (VB.NET)

```vb
' [VB.NET]
```

<!-- tags: [Essential Grid, GridGroupingControl, SummaryColumn, ManualTotalSummary, WinForms, TableModel, GridColumnDescriptor] keywords: [summary columns, summary values, GridColumnDescriptor, ManualTotalSummary, GridGroupingControl, Windows Forms, format, mappingName, TableCellIdentity] -->
```