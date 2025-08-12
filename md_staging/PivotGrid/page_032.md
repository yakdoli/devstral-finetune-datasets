```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: PivotGrid
page_number: 032
page_id: PivotGrid#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:26Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

## Overview

- The PivotGrid control with detailed cell selection and subtotal hiding functionality.
- Data visualization and manipulation in PivotGrid using cells and subtotals.
- Example scenarios demonstrating the use of PivotGrid features.

## Content

### PivotGrid Cell Selection

**Figure 12: PivotGrid Cell Selection**

The PivotGrid control displays financial data for different countries and fiscal years. The data is organized into rows for "Bike" and "Car" categories, with columns for Canada, France, Germany, the United Kingdom, the United States, and a Grand Total.

#### Bike Category

| Year   | Canada         | France         | Germany         | United Kingdom | United States | Grand Total    |
|--------|----------------|----------------|----------------|----------------|----------------|----------------|
| FY 2005 | $28,042,200.00 | $26,531,700.00 | $28,022,100.00 | $29,365,200.00 | $33,896,700.00 | $145,857,900.00 |
| FY 2006 | $13,699,800.00 | $13,812,300.00 | $13,020,300.00 | $9,955,500.00  | $12,009,300.00 | $62,497,200.00  |
| FY 2007 | $6,795,000.00  | $7,396,800.00  | $8,487,600.00  | $6,083,400.00  | $7,078,500.00  | $35,841,300.00  |
| FY 2008 | $3,612,600.00  | $3,812,100.00  | $3,933,000.00  | $3,421,500.00  | $3,315,300.00  | $18,094,500.00  |
| FY 2009 | $1,490,400.00  | $2,655,900.00  | $2,169,000.00  | $2,543,700.00  | $1,161,300.00  | $10,020,300.00  |
| Bike Total | $53,640,000.00 | $54,208,800.00 | $55,632,000.00 | $51,369,300.00 | $57,461,100.00 | $272,311,200.00 |

#### Car Category

| Year   | Canada         | France         | Germany         | United Kingdom | United States | Grand Total    |
|--------|----------------|----------------|----------------|----------------|----------------|----------------|
| FY 2005 | $5,514,600.00  | $6,982,200.00  | $5,710,800.00  | $5,500,800.00  | $6,949,800.00  | $30,658,200.00  |
| FY 2006 | $2,439,900.00  | $2,606,700.00  | $1,287,000.00  | $2,762,400.00  | $2,304,900.00  | $11,400,900.00  |
| FY 2007 | $1,137,900.00  | $2,750,100.00  | $1,619,100.00  | $1,176,300.00  | $2,483,400.00  | $9,166,800.00   |
| FY 2008 | $1,151,400.00  | $767,400.00    | $408,900.00    | $740,700.00    | $777,600.00    | $3,846,000.00   |
| FY 2009 | $58,800.00     | $270,000.00    | $404,400.00    | $293,700.00    | $1,026,900.00  | $1,026,900.00   |
| Car Total | $10,302,600.00 | $13,106,400.00 | $9,295,800.00  | $10,584,600.00 | $12,809,400.00 | $56,098,800.00  |
| Grand Total | $63,942,600.00 | $67,315,200.00 | $64,927,800.00 | $61,953,900.00 | $70,270,500.00 | $328,410,000.00 |

### 4.8 Subtotal Hiding

#### Overview

The subtotal hiding feature is used to show or hide the subtotals in the PivotGrid. In the case of larger data tables, this feature enables the user to have an abstract view of the data by hiding subtotals using the `ShowSubTotals` property.

#### Use Case Scenarios

When the user has more computational fields with subtotals in each group of their PivotGrid, the user might find it difficult to view all the data. In that case, the user can hide the subtotals and make it visible when required.

The following screenshots show the PivotGrid with shown and hidden subtotals.

## API Reference

- **`ShowSubTotals`** property: Controls whether subtotals are shown or hidden in the PivotGrid.

## Code Examples

```csharp
using Syncfusion.Windows.Forms.PivotGrid;
// Example to hide subtotals
pivotGridControl1.ShowSubTotals = false;
```

## Page-level Navigation/TOC

- [Subtotal Hiding](#4.8-subtotal-hiding)

## Cross References

- See also: [PivotGrid Overview](#overview), [PivotGrid Cell Selection](#pivotgrid-cell-selection)

<!-- tags: [syncfusion-windowsforms, pivotgrid, subtotalhiding, showsubtotals, datavisualization, financialdata] keywords: [subtotal, hiding, subtotals, pivotgrid, data, visualization, financial, cell selection, grand total] -->
```