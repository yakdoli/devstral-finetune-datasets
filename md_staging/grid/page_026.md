```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: grid
page_number: 026
page_id: grid#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:18:19Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Note: For more details, refer to the following section:

- [Performance](Performance)

### GridControl and GridDataBoundGrid

GridControl has an extremely high performance standard. It can handle high frequency updates and work with large amounts of data without affecting the performance. Similarly, GridDataBoundGrid can also handle large amounts of data without affecting the performance.

Note: For more details, refer to the following section:

- [Grid Data Bound Grid Performance](Grid Data Bound Grid Performance) and [Performance](Performance)

## 1.3.2 Grouping

### GridGroupingControl

The GridGroupingControl alone supports grouping. This control is exclusively designed for grouping. This control supports grouping data at design time too. Grouping at design time displays the grid as a tree view. For non-nested data tables, you can use this control to quickly provide custom views of data.

The Grid Grouping control allows you to group the data based on one or more columns. When grouping is applied, the data will be organized into a hierarchical structure based on the matching field values. This control enables you to combine identical value to form a group. Each group is identified by its GroupCaptionSection. You can expand this to view the records in the group. The GroupCaptionSection provides the information about a particular group such as the group name, number of items in the group, and so on. The Grid Grouping control also provides Expand/Collapse button for every group.

> **Note:** For more details, refer to the following section:
>
> [Grouping](Grouping)

### Sample

A sample of this feature is available in the following location:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping\Grouping Demo
```

## API Reference

### Overview

- GridControl supports high performance standards.
- GridDataBoundGrid can handle large amounts of data without performance degradation.
- GridGroupingControl enables data grouping at both runtime and design time.
- GroupCaptionSection provides details about each group.

### Features

- The Grid Control handles high frequency updates efficiently.
- The Grouping feature organizes data into hierarchical structures based on matching field values.
- Group Caption Section provides summary-information for each group.
- Expand/Collapse functionality is provided for every group.

### Usage

To use the GridGroupingControl:

1. Add the GridGroupingControl to your form.
2. Bind the control to your data source.
3. Enable grouping by setting the appropriate properties.
4. Customize the GroupCaptionSection to display relevant group information.

### Installation Location

To access the sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping\Grouping Demo
```

<!-- tags: [Syncfusion, Winforms, GridGroupingControl, Grouping, Performance, GridDataBoundGrid] keywords: [GridControl, GridDataBoundGrid, Grouping, GroupCaptionSection, High Performance, Large Data, Nested Data Tables, Expand/Collapse] -->
```