```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_265.jpeg
document_name: XlsIO
page_number: 265
page_id: XlsIO#page_265
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:14Z
fidelity: lossless
-->

# Essential XlsIO

It is also possible to insert multiple subtotals for a field by using the `Subtotal` property of `I PivotField`. This is demonstrated in the following code example.

## Subtotal Example in Code

```csharp
IPivotTable pivotTable = sheet1.PivotTables.Add("PivotTable1", sheet1["A1"], cache);
pivotTable.Fields[0].Axis = PivotAxisTypes.Row;
pivotTable.Fields[0].Subtotals = PivotSubtotalTypes.Sum |
                                 PivotSubtotalTypes.Average |
                                 PivotSubtotalTypes.Max |
                                 PivotSubtotalTypes.Min;
```

## Pivot Table Options

Excel provides various options through the `PivotTableOptions` dialog box to customize the appearance of the pivot table.

### PivotTable Options Dialog Box

The `PivotTableOptions` dialog box allows customization of various pivot table settings, including layout, totals, filters, display, printing, and data. Below is a brief description of the features available in each tab:

#### Layout & Format
- **Grand Totals**
  - Show grand totals for rows
  - Show grand totals for columns
- **Filters**
  - Subtotal filtered page items
  - Allow multiple filters per field
- **Sorting**
  - Use Custom Lists when sorting

---

### Figure 92: PivotTable Options Dialog Box

![PivotTable Options Dialog Box](attachment://PivotTable_Options_Dialog_Box.jpg)

## API Reference

- **IPivotField**
  - **Subtotal** property
    - Allows specification of types of subtotals to be applied to a pivot table field.
    - Types include `Sum`, `Average`, `Max`, and `Min`.

## Code Examples

The example provided demonstrates how to assign multiple subtotals (Sum, Average, Max, and Min) to a field in a pivot table using the C# code snippet.

```csharp
pivotTable.Fields[0].Subtotals = PivotSubtotalTypes.Sum |
                                 PivotSubtotalTypes.Average |
                                 PivotSubtotalTypes.Max |
                                 PivotSubtotalTypes.Min;
```

## Cross References

- See also:
  - [Creating Pivot Tables using XlsIO](#creating-pivot-tables-using-xslio)

<!-- tags: [pivotTable, subtotal, I PivotField, PivotTableOptions, Excel, customization] -->
<!-- keywords: [subtotal, pivotTables, pivotFields, grandTotals, filters, sorting, customization, XlsIO, programmatic, configuration] -->
```