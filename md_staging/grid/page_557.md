```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_557.jpeg
document_name: grid
page_number: 557
page_id: grid#page_557
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates filtering data records in a Grid using the `GridDataBoundGridFilterBarExt`.
- Explains adding `GridBoundColumns` to control the column format in a Grid Data Bound Grid.

## Content

### GridDataBoundGridFilterBarExt

The following VB.NET code snippet illustrates how to filter data records in a Grid using the `GridDataBoundGridFilterBarExt`:

```vb
Dim filterBar As GridDataBoundGridFilterBarExt = New GridDataBoundGridFilterBarExt()
filterBar.WireGrid(gridDataBoundGrid1)
```

#### Figure: Filtering Data Records in the Grid by the Display Member

![Filtering Data Records in the Grid by the Display Member](./filtering-data-records-demo.png)

*Figure 219: Filtering Data Records in the Grid by the Display Member*

**Note:** For more details, refer to the following browser sample:

- `<Install Location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Grid.Windows\Samples\2.0\Data Bound\Filter By DisplayMember Demo`

### 4.2.2.6 GridBoundColumns and Controlling the Column Format

To control the properties of a column in your Grid Data Bound Grid, you must use a `GridBoundColumn` class object. You can also explicitly add a `GridBoundColumn` object to the `GridDataBoundGrid.GridBoundColumns` collection for each column that you want to see in the grid or you can let the `GridDataBoundGrid.Binder` class generate these columns for you.

**Here are the code samples that will explicitly add GridBoundColumns. Note that you can add these GridBoundColumns at design-time provided that you properly set the `MappingName` property for each column.**

```html
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [Grid, DataBoundGrid, FilterBar, GridBoundColumns, Columns format control, DisplayMember, GridDataBoundGridFilterBarExt, SyncfusionWinforms] keywords: [Filtering, Grid, DisplayMember, GridBoundColumns, MappingName, Column format, Design-time, DataBoundGrid, FilterBar] -->
``` 
