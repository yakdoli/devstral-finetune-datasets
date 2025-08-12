```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_893.jpeg
document_name: grid
page_number: 893
page_id: grid#page_893
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:49Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- The order of StackedHeaders is determined by the VisibleColumns collection.
- The layout of GridStackedHeaderRow is based on the VisibleColumns.
- StackedHeaderDescriptors reference VisibleColumns, influencing header drawing.
- If not specified, StackedHeaders span across all visible columns.
- Columns can be rearranged via dragging stacked headers, affecting the VisibleColumns collection.
- Display of StackedHeaders can be toggled for groups and sub-tables.

## Content

### StackedHeader Display and Arrangement

The order in which the StackedHeaders will appear is determined by the VisibleColumns collection. When the layout of the GridStackedHeaderRow is calculated, the grid will loop through the VisibleColumns collection and find the StackedHeader Descriptor that references the VisibleColumn. If the same StackedHeader references multiple neighboring VisibleColumns, then the header for these columns will be drawn as one cell. If there are no visible columns specified for a StackedHeader, then it will span across all the visible columns similar to a Caption.

You could be able to rearrange the columns by dragging the stacked headers. While doing so, it is the Visible Columns collection that is being affected. Since the order of stacked headers is dependent on Visible Columns, the GridStackedHeaderCollections itself does not need to be modified.

It is possible to add Stacked Headers for nested tables and groups too. You can enable the display of the StackedHeaders by setting the **ShowStackedHeaders** property to true.

#### Toggling StackedHeaders

- **TopLevelGroupOptions.ShowStackedHeaders** - Toggles the display of StackedHeaders for the topmost group.
- **ChildGroupOptions.ShowStackedHeaders** - Toggles the display of StackedHeaders for child groups.
- **NestedTableGroupOptions.ShowStackedHeaders** - Toggles the display of StackedHeaders for child tables and its groups.

### Through Designer

#### Creating Stacked Headers

Creating Stacked Headers is a two-step process.

1. **Step 1: Defining Stacked Header Rows**
   As a first step, you must define the Stacked Header Rows by accessing the **TableDescriptor.StackedHeaderRows** property. This will open the GridStackedHeaderRowDescriptor Collection Editor wherein you can add as many header rows as you want, by specifying the different attributes like HeaderText, VisibleColumns, Appearance, and so on, for each header in the header row.
``` 

 <!-- tags: [grid, stackedheaders, visiblerow, visiblerows, syncfusionwinforms, windowforms, gridstackedheaderrow, caption, groups, nestedtables, designer, tabledescriptor] keywords: [grid, stackedheaders, visiblerow, visiblerows, gridstackedheaderrow, caption, groups, nestedtables, designer, tabledescriptor] -->
 ```