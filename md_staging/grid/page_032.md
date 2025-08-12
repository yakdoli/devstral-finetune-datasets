```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_032.jpeg
document_name: grid
page_number: 032
page_id: grid#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:18:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

You can enable filtering for the grid based on GridDataBoundGrid, by adding a row of drop-down cells at the top of a simple (non-hierarchical) Grid Data Bound Grid. This allows you to filter match values from the drop-down. This control also supports filter by DisplayMember.

**Note:** For more details, refer to the following section:

[Filtering a Grid Data Bound Grid](Filtering a Grid Data Bound Grid)

## Sample

A sample of this feature is available in the following location:

`<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Data Bound\Filter By DisplayMember Demo`

### 1.3.6.1 Filter for Specific Columns

When a filter is wired to a grid, it is wired to the entire grid. This makes it difficult to use different filters (e.g., dynamic filter, Excel-style filter, and filter by display member) in a single grid.

Here is a short description of each filter:

- **Dynamic Filter**—Filters the content using a list of comparison operators.
- **Ordinary Filter**—Filters the content based on the selected text and index.
- **Excel-Style Filter**—Filters the content based on multiple values and can sort the results, similar to Microsoft Excel filtering.
- **Filter by Display Member**—Filters the content by displaying the member instead of the value member of a combo-box column.

This feature enhances the use of different filters within a single grid. The filters are wired to each column by changing the cell type of the corresponding column, which enables users to apply many filters.

A filter can be applied to an individual column by setting the `AllowIndividualColumnWiring` property of the filter to `true`.

## Properties

| Property                      | Description                                                                       | Type     | Data Type |
|-------------------------------|-----------------------------------------------------------------------------------|----------|-----------|
| AllowIndividualColumnWiring   | Gets or sets whether the filters can be wired to an individual column.           | Bool     | Bool      |

## RAG Annotations

This page discusses the filtering feature in the Essential Grid for Windows Forms, focusing on enabling filtering for specific columns using various filter types. It provides details on wiring filters to individual columns, descriptions of filter types, and a sample location.

<!-- tags: [Syncfusion, Essential Grid, WinForms, Filtering, GridDataBoundGrid] keywords: [filter, display member, dynamic filter, Excel-style filter, ordinary filter, grid, Windows Forms] -->
```