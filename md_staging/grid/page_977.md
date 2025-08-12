```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_977.jpeg
document_name: grid
page_number: 977
page_id: grid#page_977
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- The page explains the usage of Grouping Grid displaying Summary and the functionality of Record Filters.
- Demonstrates how to add row filters to a grid table by specifying filter criteria.

## Content

### Grouping Grid displaying Summary

The Grouping Grid is shown with 29 records, displaying columns like SupplierID, CompanyName, and ContactName. The summary bar at the bottom highlights the total number of records.

#### Figure: Grouping Grid displaying Summary
![Grouping Grid displaying Summary](#figure-370)

**Note**: The grid shows the summary at the bottom indicating a total of **29 Records**.

### Record Filters

#### Overview
By using the `TableDescriptor.RecordFilters` property, you can add row filters for your grid table. This section explains how to apply and implement record filters.

#### Implementation
- **Property Usage**: Use the `TableDescriptor.RecordFilters` property to add row filters.
- **Filter Criteria**: Once the filter criteria and the column name are specified, the grouping grid will display only the subset of records that satisfy the given criteria.
  
Example of applying filters:
```csharp
GridSummaryRowDescriptorCollection SummaryRows = new GridSummaryRowDescriptorCollection(summaryRows);
```

## API Reference

### Properties
- **RecordFilters**
  - **Type**: `GridRecordFilterCollection`
  - **Description**: A collection of filter criteria to apply to rows in the grid.
  - **Usage**: This property allows adding and managing row filters dynamically.

## Code Examples

```csharp
using Syncfusion.Windows.Forms.Grid;
using Syncfusion.Windows.Forms.Grid.Grouping;

// Example of adding a record filter
GridRecordFilter filter = new GridRecordFilter();
filter.RecordFilterFormula = "SupplierID > 25";
gridGroupingControl1.TableDescriptor.RecordFilters.Add(filter);
```

### Cross References
- Refer to the documentation on `GridSummaryRowDescriptorCollection` for more details on summary rows.

## RAG Annotations
<!-- tags: [grid, grouping-grid, record-filters, summary-view] keywords: [TableDescriptor, RecordFilters, GridSummaryRowDescriptorCollection] -->
```