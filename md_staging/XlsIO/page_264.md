```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_264.jpeg
document_name: XlsIO
page_number: 264
page_id: XlsIO#page_264
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:19Z
fidelity: lossless
-->

## PivotTable Report Properties

### Overview
- The PivotTable report properties allow users to customize the layout, formatting, and display settings of a PivotTable.
- These properties specify how fields are arranged, how null values are displayed, and how formatting is preserved during operations.

| Property            | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| PageFieldsOrder     | Returns or sets the order in which page fields are added to the PivotTable report's layout. |
| DisplayNullString   | True, if the PivotTable report displays a custom string in cells that contain null values. The default value is True. |
| NullString          | Returns or sets the string displayed in cells that contain null values when the DisplayNullString property is True. |
| PreserveFormatting  | True, if formatting is preserved when the report is refreshed or recalculated by operations such as pivoting, sorting, or changing page field items. |
| ShowTooltips        | True, if tooltips displayed for the pivot table cell. |
| DisplayFieldCaptions | Gets/sets value controlling whether or not filter buttons and PivotField captions for rows and columns are displayed in the grid. |
| PrintTitles         | True, if the print titles for the worksheet are set based on the PivotTable report. <br> False, if the print titles for the worksheet are used. |
| RowLayout           | This property specifies the pivot table row layout settings. |

### IPivotCache Interface Properties

#### Overview
- The properties of the IPivotCache interface provide read-only access to information about the PivotTable cache.

### Table 3: IPivotCache Properties Table

| Property    | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| Index       | Gets zero-based cache index. Read-only.                                   |
| SourceType  | Specifies the pivot table cache source type. Read-only.                  |
| SourceRange | Returns the data source for the PivotTable report. Read-only.            |

### SubTotals

#### Overview
- The PivotSubtotalTypes enum allows users to insert various subtotal types for the pivot table.

### SubTotals

You can also insert various subtotal types for the pivot table through the PivotSubtotalTypes enum.

<!-- tags: [XlsIO, PivotTable, report properties, IPivotCache, SubTotals, PivotSubtotalTypes, fields, formatting] keywords: [PivotTable report, null values, subtitles, formatting,逐行垂直扫描原文] -->
```