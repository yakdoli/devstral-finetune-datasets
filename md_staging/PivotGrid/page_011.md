```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: PivotGrid
page_number: 011
page_id: PivotGrid#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:57Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

## 2.4 Properties Table for PivotGrid

### Table 4: Properties Table

| Property Name          | Type          | Description                                                                                                                                                     |
|------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DeferLayoutUpdate      | bool          | Gets or sets a value to specify whether the layout should be updated immediately after updating the pivoting info, or if it should wait for a Refresh() call. |
| FreezeHeaders          | bool          | Gets or sets a value to specify whether headers of a grid has to be frozen or not.                                                                            |
| DataSource             | object        | Gets or sets the source of data for a pivot table. This object should be an IEnumerable or IQueryable list.                                                 |
| PivotCalculations       | Hashtable     | Gets the collection of Pivot Calculations.                                                                                                                    |
| PivotColumns           | Hashtable     | Gets the collection of pivot columns.                                                                                                                          |
| PivotEngine            | PivotEngine   | Gets or sets the pivot engine for a grid.                                                                                                                      |
| PivotRows              | Hashtable     | Gets the collection of pivot rows.                                                                                                                              |
| ShowCalculationsAsColumns | bool       | Gets or sets a value to specify whether calculations should appear as rows or columns. The default behavior is for calculations to appear as columns.        |
| ShowGrandTotals        | bool          | Gets or sets a value to specify whether grand total calculations should be computed by the engine.                                                       |
| PivotCellInfo          | PivotCellInfo | Gets or sets the PivotCellInfo in order to check the cell type.                                                                                               |

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/texts as shown.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

<!-- tags: [PivotGrid, Windows Forms, properties, table, Syncfusion, version] keywords: [Property Name, Type, Description, DeferLayoutUpdate, FreezeHeaders, DataSource, PivotCalculations, PivotColumns, PivotEngine, PivotRows, ShowCalculationsAsColumns, ShowGrandTotals, PivotCellInfo] -->
```