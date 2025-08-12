```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_093.jpeg
document_name: grid
page_number: 093
page_id: grid#page_093
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:22:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

This page explains how to configure the GridBoundColumns collection in the Grid Data Bound Grid control using the property grid. It provides detailed steps to open the GridBoundColumns editor and add grid bound columns with mappings to specific data fields.

## Content

### GridBoundColumns Collection in the Grid Data Bound Grid's PropertyGrid

![Figure 58: GridBoundColumns Collection in the Grid Data Bound Grid's PropertyGrid](image_for_Figure_58)

Figure 58: GridBoundColumns Collection in the Grid Data Bound Grid's PropertyGrid

The GridBoundColumns collection is a crucial feature of the Grid Data Bound Grid control. It allows you to define columns in the grid that are bound to specific data fields. Here are the steps to configure the GridBoundColumns collection:

1. **Open the GridBoundColumns collection editor by using the property grid.**
   - Locate the `GridBoundColumns` property in the PropertyGrid for the `gridDataBoundGrid1` control.
   - Click on the collection editor (the icon next to the property) to open the GridBoundColumns editor.

2. **Click the Add button to add a grid bound column, and then set MappingName property of that grid bound column to ProductName.**
   - In the GridBoundColumns editor, click the `Add` button to create a new grid bound column.
   - Set the `MappingName` property of the newly added column to `ProductName`. This links the column to the `ProductName` field in the underlying data source.

## API Reference

### Control Properties

- **GridBoundColumns**
  - Type: Collection
  - Description: A collection of GridBoundColumn objects.

- **MappingName**
  - Type: string
  - Description: Specifies the name of the field in the data source that the grid column is bound to.

## Code Examples

Here is an example of how to programmatically add a GridBoundColumn with a `MappingName` property set to `ProductName`:

```csharp
// Assuming gridDataBoundGrid1 is an instance of GridDataBoundGrid
GridDataBoundGrid gridDataBoundGrid1 = new GridDataBoundGrid();

// Create a new GridBoundColumn
GridBoundColumn column = new GridBoundColumn();

// Set the MappingName property
column.MappingName = "ProductName";

// Add the column to the GridBoundColumns collection
gridDataBoundGrid1.Model.Bands[0].Columns.Add(column);
```

## Page-level Navigation/TOC (if applicable)

**Steps to configure GridBoundColumns:**
1. Open the GridBoundColumns editor.
2. Add a grid bound column and set its MappingName property.

## Cross References

See also: Data Binding, Grid Data Bound Grid Control, GridBoundColumn, MappingName Property.

<!-- tags: [Syncfusion, WinForms, Grid, GridBoundColumns, MappingName, PropertyGrid, Data Binding] keywords: [GridBoundColumns, MappingName, PropertyGrid, Data Source, Windows Forms, PropertyGrid] -->
```