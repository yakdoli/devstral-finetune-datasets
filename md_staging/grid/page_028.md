```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: grid
page_number: 028
page_id: grid#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:17:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes sorting behavior options available in GridDataBoundGrid.
- Explains how to implement sorting in GridControl through customization.
- Details on sorting icon placement options in Grid.

## Content

### GridDataBoundGrid

GridDataBoundGrid allows you to arrange items in sequence, in different sets, or in both. The following is the list of sorting behavior options that are available in `GridDataBoundGrid`:

- **SingleClick:** Sort column on single click.
- **DoubleClick:** Sort column on double-click.
- **None:** Sorting is disabled.

Note: For more details, refer to the following section:  
**Sorting By Display Member**

#### Sample

A sample of this feature is available in the following location:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Data Bound\Sort By DisplayMember Demo
```

### GridControl

In `GridControl`, sorting is not directly supported. Sorting can be performed through customizing the `GridSortColumnHeaderCellModel`.

#### Sample

The sample in the following location illustrates how to implement header-click sorting for the GridControl based grids.

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\MS Excel-Style Features\Grid Control Sort Demo
```

#### 1.3.4.1 Sort Icon Placement

This feature is used to place the sort icon in different positions of the column header cell of the grid. The default position of the sort icon is to the right.

The position options include:

- **Right**
- **Top**
- **Left**

### Properties

| Property         | Description     | Type          | Data Type          |
|-------------------|------------------|---------------|--------------------|
|                   |                  |               |                    |

## API Reference

Not provided in the current content.

## Code Examples

Not provided in the current content.

## Cross References

- See also: Sorting By Display Member

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [GridDataBoundGrid, GridControl, sort behavior, sorting, sort icon placement, GridSortColumnHeaderCellModel, display member] -->
```