```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_759.jpeg
document_name: grid
page_number: 759
page_id: grid#page_759
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:34Z
fidelity: lossless
-->

# SetGroupSummaryOrder Method

This method itself will set up a custom comparer for sorting groups if the groups should be sorted in a different order than the category. It can be defined for a given column say `Col1` by passing the summary name, a property in the summary and optionally the sort direction as the parameters. It makes use of these parameters to retrieve the summary values and then pass these values to a custom comparer which sets up a sort order based on these summary values. When the grid is grouped against the column `Col1`, then the groups are sorted in the order specified by the custom comparer instead of sorting in the default order. Here is a sample usage of this method.

## Example

This example uses an Orders Table bound to a grouping grid. Summaries are created for the column `Freight`. The group caption cells are made to display the group summaries for the `Freight` column. Now, our goal is to sort the table against the `ShipCountry` field with the data records get arranged based on the caption summaries i.e. the groups should get sorted against the summary values rather than the category.

Follow these steps to sort the groups by the summary values.

1. Define a Summary Column Descriptor for the column `Freight` and add it into a SummaryRow of the Orders table.

```csharp
GridSummaryColumnDescriptor summaryColumn1 = new GridSummaryColumnDescriptor("FreightAverage", 
    SummaryType.DoubleAggregate, "Freight", "{Average:###.00}");
GridSummaryRowDescriptor summaryRow1 = new GridSummaryRowDescriptor();
summaryRow1.Name = "Caption";
summaryRow1.SummaryColumns.Add(summaryColumn1);
this.gridGroupingControl1.TableDescriptor.SummaryRows.Add(summaryRow1);
```

```vb
Dim summaryColumn1 As New GridSummaryColumnDescriptor("FreightAverage", 
    SummaryType.DoubleAggregate, "Freight", "{Average:###.00}")
Dim summaryRow1 As New GridSummaryRowDescriptor()
summaryRow1.Name = "Caption"
summaryRow1.SummaryColumns.Add(summaryColumn1)
Me.gridGroupingControl1.TableDescriptor.SummaryRows.Add(summaryRow1)
```
```