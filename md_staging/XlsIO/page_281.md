```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_281.jpeg
document_name: XlsIO
page_number: 281
page_id: XlsIO#page_281
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:27Z
fidelity: lossless
-->

## Overview
- This page demonstrates how to apply row field filters in an Excel PivotTable using Excel Interop (XlsIO).
- The Focus is on filtering data based on specific criteria, such as selecting regions in a PivotTable.

## Content

### Applying Row Field Filter

The image illustrates the process of applying a row field filter to a PivotTable in Excel using the XlsIO library. Below is a detailed breakdown:

#### Interface Description
- **Row Labels**: The PivotTable's row labels have been configured to show different regions.
- **Region Filter Panel**: A filter panel is visible where the user can select which regions to include in the PivotTable view.
- **Label Filters**: Options to filter the row labels based on specific criteria, such as "Select All," "Central," "East," and "West."

#### Filter Options
- The user can apply advanced filtering using the "Label Filters" section:
  - **Value Filters**: Includes options like "Does Not Equal," "Begins With," "Does Not Begin With," among others.
  - **Equality and Comparison Filters**: Users can use equality (`Equals`, `Not Equal`) as well as comparison operators (`Greater Than`, `Less Than`) to filter the rows.

#### Grand Total
- The "Grand Total" column displays the sum of units for the regions selected in the filter, totaling 69.

### Figure Explanation
#### Figure 96: Applying Row Field Filter
The figure shows a pivot table setup where:
- The pivot table header includes "Sum of Units," "Column Labels," and "Row Labels."
- The "Select field" dropdown is set to "Region."
- The filter options are categorized under "Value Filters," including selections like "Central," "East," and "West."
- The "Equals..." option is highlighted, suggesting the user can filter rows based on specific equality conditions.

## API Reference

### Methods and Properties
This section elaborates on the API methods used for applying row field filters in a PivotTable.

#### Methods
- **FilterPivotRows**:
  - **Description**: Applies a filter to the rows of a PivotTable based on specified criteria.
  - **Parameters**:
    - `region`: Defines the field on which the rows are to be filtered.
    - `criteria`: Specifies the filtering criteria (e.g., "Equal," "Greater Than").
    - `value`: The value against which the filtering is applied.

#### Properties
- **SelectedRegions**:
  - **Type**: IEnumerable<string>
  - **Description**: Lists the selected regions to be included in the PivotTable view.

## Code Examples

### Example: Filtering PivotTable Rows

```csharp
// Assuming 'pivotTable' is the reference to the PivotTable object
// Apply Filter based on Region
pivotTable.PivotFilters.SetFilter(PivotFilterType.Equal, "Region", "Central");

// Alternatively, to select multiple regions
pivotTable.PivotFilters.SetFilter(PivotFilterType.SelectMultiple, "Region", new string[] { "East", "West" });
```

## Cross References
- See also: [Creating PivotTables in Excel](#creating-pivot-tables-in-excel)
- See also: [Advanced Filtering Options in Excel Interop](#advanced-filtering-options-in-excel-interop)

## RAG Annotations
<!-- tags: [XlsIO, PivotTable, ExcelInterop, Filter, Region, WinForms] keywords: [pivot, filter, region, excelinterop, rowfield, grand total] -->
```