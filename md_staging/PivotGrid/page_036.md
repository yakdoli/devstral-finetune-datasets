```html
<!-- {{page_id}} -->
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: PivotGrid
page_number: 036
page_id: PivotGrid#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:55:08Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Cell-by-Cell Export

**Overview**
- In cell-by-cell export, the contents are exported cell by cell with applied formatting.
- The formatting includes all styles applied to the data.

### Implementation Details
The following image shows the cell-by-cell export:

| A    | B    | C      | D      | E       | F       | G       | H       | I       | J      | K      | L      | M      | N      | O      |
|------|------|--------|--------|---------|---------|---------|---------|---------|--------|--------|--------|--------|--------|--------|
| 1    |      | Canada  |        |         |         |         |         |         |        |        |        |        |        |        |
| 2    |      | Alberta |        |         |         |         |         |         |        |        |        |        |        |        |
| 3    |      | 1       |        | 11      |         | 2       |         | 3       |        | 4      |        | 5      |        |        |
| 4    |      | Quantity | Year   | Quantity | Year     | Quantity | Year     | Quantity | Year   | Quantity | Year   | Quantity |        |        |
| 5    | Bike | FY 2005 | 25     | 25      | 28      | 39      | 39      | 32      | 32     | 38     | 38     | 47     | 47     | 43     |
| 6    |      | FY 2006 | 9      | 11      | 11      | 8       | 8       | 14      | 14     | 15     | 15     | 8      | 8      | 15     |
| 7    |      | FY 2007 | 4      | 4       | 4       | 2       | 2       | 6       | 6      | 6      | 6      | 4      | 4      | 5      |
| 8    | Bike Total | 38 | 38  | 43  | 43  | 49  | 49  | 52  | 52  | 59  | 59  | 59  | 59  | 63 |
| 9    | Car | FY 2005 | 6      | 6       | 4      | 10      | 10      | 9       | 9      | 4      | 4      | 9      | 9      | 8      |
| 10   |      | FY 2006 | 1      | 1       | 1      | 2       | 2      | 1       | 1      | 4      | 4      | 1      | 1      | 1      |
| 11   |      | FY 2007 | 1      | 1       | 2      | 2       | 1       | 1       |        | 1      | 1      |        |        | 1      |
| 12   | Car Total | 8     | 8      | 7      | 7      | 13      | 13      | 10      | 10     | 9      | 9      | 10     | 10     | 10     |
| 13   | Grand Total | 46   | 46  | 50  | 50  | 62  | 62  | 62  | 62  | 68  | 68  | 68  | 69  | 69 |

## Pivot Table Export

**Overview**
- In PivotTable export, users can export the entire PivotGrid with its functionalities, including sorting and filtering.
- The PivotGrid allows data manipulation via drag-and-drop to organize data into a cross-tabulated format.

### Features
- Extract desired information quickly.
- Summarizes and groups data.
- Primary application in the financial domain for organizing and analyzing business data.

### Implementation Details
The following image depicts the exported PivotTable:

| A | B    | C       | D       | E       | F       | G       | H       | I       | J     |
|---|------|---------|---------|---------|---------|---------|---------|---------|-------|
| 1 |      | Country | State   | Quantity | Values  |         |         |         |       |
| 2 |      | Canada  |         | Quantity | Values  |         |         |         |       |
| 3 |      | Alberta |         | Quantity | Values  |         |         |         |       |
| 4 |      | Product | Year    | Quantity | Year    | Quantity | Year    | Quantity | Year  |
| 5 |      | Bike    | FY 2005 | 25      | 25      | 32      | 32      | 38      | 38    |
| 6 |      | FY 2006 | 9       | 14      | 14      | 15      | 15      | 8       | 8     |
| 7 |      | FY 2007 | 4       | 6       | 6       | 6       | 6       | 4       | 4     |
| 8 | Bike Total | 38  | 38  | 52  | 52  | 59  | 59  | 59  | 59 |
| 9 |      | Car | FY 2005 | 6       | 9       | 4       | 4       | 9       | 9     |
| 10 |       | FY 2006 | 1       | 1       | 4       | 4       | 1       | 1       | 1     |
| 11 |       | FY 2007 | 1       | 1       | 1       | 1       |        |        | 1     |
| 12 | Car Total | 8      | 8      | 10      | 10      | 9       | 9       | 10      | 10    |
| 13 | Grand Total | 46  | 46  | 62  | 62  | 62  | 62  | 68  | 69 |

## Export to Word

**Overview**
- Essential Grid provides built-in support to export data to Word.
- Users can download data from the PivotGrid into a Word document for offline verification and computation.
- Achieved using the `PivotWordExport` class.

### Code Example
The following code snippet demonstrates exporting PivotGrid to Word:

```csharp
[PivotWordExport]
```

## API Reference

- **PivotWordExport**: Exports PivotGrid data to Word.

## RAG Annotations
<!-- tags: [essential-pivotgrid, synchronization-api, cell-by-cell-export, pivottable-export, data-export, windowsforms] keywords: [pivotgrid, cell-by-cell, pivottable, data-export, word-export, syncfusion, windowsforms] -->
```