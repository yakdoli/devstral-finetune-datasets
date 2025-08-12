```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_892.jpeg
document_name: grid
page_number: 892
page_id: grid#page_892
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:47:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Grouping grid offers different layouts to organize data display.
- With default layout, grouping grid combines column headers into a single row.
- This section discusses two features for customizing data views.

## Grid Layout

Grouping grid offers different layouts to organize the data display. With default layout, grouping grid combines the column headers into a single row docked to the top. Below the column headers are the rows of data records displayed with one record per row and only one record field per column.

This default arrangement can be modified to customize the data views. This section discusses two features offered by the grouping grid in this regard.

### Stacked MultiHeaders

Essential Grouping Grid Control offers in-built support for Stacked MultiHeaders. This feature allows you to create additional unbound header rows called **StackedHeaderRows** that span across visible grid columns. You can group some columns under each header row. It also supports Drag / Drop of these header rows. Grouped columns will also be rearranged along with the header.

#### The StackedHeaderRows Collection

Stacked Header rows for a given Grid Table are gathered under `TableDescriptor.StackedHeaderRows` collection. This contains the property definitions that controls the behavior and appearance of the Stacked Headers. A StackedHeaderRow collection can be viewed as a set of stacked header rows in which each header row contains a collection of stacked headers that span across multiple columns.

Every header in a Stacked Header Row is defined by a `GridStackedHeaderDescriptor`. All the headers for a given stacked header row is managed by `GridStackedHeaderRowDescriptor`. `GridStackedHeaderRowDescriptorCollection`, which is returned by `TableDescriptor.StackedHeaderRows` property, manages the collection of `GridStackedHeaderRowDescriptors` for a given table. It is the `GridStackedHeaderVisibleColumnDescriptor` that binds a `Column` or `ColumnSet` to the StackedHeaderCell.

## API Reference

#### Properties
- **TableDescriptor.StackedHeaderRows**
- **GridStackedHeaderDescriptor**
- **GridStackedHeaderRowDescriptor**
- **GridStackedHeaderRowDescriptorCollection**

#### Methods
- All the headers for a given stacked header row are managed using `GridStackedHeaderRowDescriptor`.

## Code Examples

```csharp
GridStackedHeaderRowDescriptorCollection stackedHeaderRows = tableDescriptor.StackedHeaderRows;

foreach (GridStackedHeaderRowDescriptor row in stackedHeaderRows)
{
    foreach (GridStackedHeaderDescriptor header in row.Headers)
    {
        // Perform operations on stacked headers
    }
}
```

## Page-level Navigation/TOC
- [4.3.4.6 Grid Layout](#grid-layout)
  - [4.3.4.6.1 Stacked MultiHeaders](#stacked-multiheaders)
    - [The StackedHeaderRows Collection](#the-stackedheaderrows-collection)

## Cross References
- Refer to related sections on grouping grid and data customization.

<!-- tags: [essentialgrid, windowsforms, groupinggrid, layout, multiviews, stackedheaders] keywords: [GridStackedHeaderRows, GridStackedHeaderDescriptor, TableDescriptor, GridStackedHeaderVisibleColumnDescriptor, StackedHeaderRows] -->
```