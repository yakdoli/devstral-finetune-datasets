<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: PivotGrid
page_number: 028
page_id: PivotGrid#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:07Z
fidelity: lossless
-->

## Essential PivotGrid Windows Forms

### Setting Up the PivotGrid

Here is a code snippet demonstrating how to set up the PivotGrid:

```csharp
"Product"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Date"})
' Adding PivotColumns
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Country"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "State"})
' Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName="Amount", .Format="C"})
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,#0"})
```

### PivotGrid Grouping Bar

The PivotGrid Grouping Bar is a feature that allows users to group data by specific fields. Here is an explanation of the key areas in the Grouping Bar:

- **Filter Button**: Indicates the option to filter data.
- **Filter Header Area**: Displays the fields that can be filtered.
- **Sort Indicator**: Shown when data is sorted by a specific field.
- **Column Header Area**: Lists the fields in the columns.
- **Data Area**: Displays the actual data grouped by the specified fields.
- **Row Header Area**: Lists the fields in the rows.

### Figure 9: PivotGrid Grouping Bar

![Figure 9: PivotGrid Grouping Bar](https://example.com/figure9.png)

### 4.6.1 Filtering in Grouping Bar

#### Overview
- Filtering allows users to display only a subset of data that meets specified criteria, hiding irrelevant data.
- Runtime filtering is a key feature, represented by a funnel symbol.
- Clicking the funnel opens a filter popup, allowing users to select specific elements to filter by.

#### Detailed Explanation
Data filtering displays only a subset of data that meets criteria specified by you and hides data that you don't want to be displayed. The items present in the filter header area, column header area, and row header area provide the option of runtime filtering, which is represented as a funnel symbol on it. On clicking the symbol, it opens a filter popup which displays a list of elements through which filtering can be applied.

## References

- **Syncfusion WinForms Documentation**: [Syncfusion WinForms PivotGrid Documentation](https://www.syncfusion.com/documentation/windowsforms/pivotgrid/)

### Figure 9: PivotGrid Grouping Bar
This figure illustrates the layout of the PivotGrid Grouping Bar, highlighting key interactive elements such as the filter button, sort indicators, and headers/rows.

## Additional Notes
- The PivotGrid control supports various calculations and formatting options, which are configured using `PivotComputationInfo`.
- Filtering enhances the user experience by allowing them to focus on relevant data subsets.

<!-- tags: [syncfusion, pivotgrid, filtering, winforms, data grouping, runtime filtering] keywords: [pivotgrid, grouping, filtering, runtime filtering, filter button, filter header, filter popup, data area, row header, column header] -->