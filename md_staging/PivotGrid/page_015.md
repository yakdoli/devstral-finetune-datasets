```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: PivotGrid
page_number: 015
page_id: PivotGrid#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:11Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

```vb
With {.FieldMappingName = "Country", .TotalHeader = "Total"}
            Me.PivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldMappingName = "State", .TotalHeader = "Total"})
            ' Adding PivotCalculations to Grid
            Me.PivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Amount", .Format = "C", .SummaryType = SummaryType.DoubleTotalSum})
            Me.PivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,#0"})
End Sub
```

## Overview

- The `PivotGrid` control is demonstrated with data manipulation capabilities.
- The code example shows field mapping and computation information for pivot reporting.
- The output pivot grid includes totals and summaries for pivoted data.

## Content

When the code above runs, the following output will be generated.

### Pivoted Data Output

|  | Canada | Total |  |  |
| --- | --- | --- | --- | --- |
|  |  | Canada Total |  | Grand Total |
|  | Amount | Quantity | Amount | Quantity | Amount | Quantity | Amount | Quantity |
| Bike | FY 2005 | $5,409,300.00 | 34 | $4,605,600.00 | 29 | $5,583,000.00 | 32 | $15,597,900.00 | 95 | $15,597,900.00 | 95 |
| FY 2006 | $1,595,900.00 | 11 | $2,647,200.00 | 15 | $1,948,500.00 | 10 | $6,291,600.00 | 35 | $6,291,600.00 | 36 |
| FY 2007 | $1,126,500.00 | 6 | $1,349,200.00 | 8 | $812,700.00 | 6 | $3,488,400.00 | 20 | $3,488,400.00 | 20 |
| Bike Total |  | $8,231,700.00 | 51 | $8,802,000.00 | 52 | $8,344,200.00 | 48 | $25,377,900.00 | 151 | $25,377,900.00 | 151 |
| Car | FY 2005 | $1,410,300.00 | 8 | $1,482,900.00 | 10 | $958,500.00 | 5 | $3,851,700.00 | 23 | $3,851,700.00 | 23 |
| FY 2006 | $1,003,500.00 | 4 | $629,700.00 | 3 | $584,100.00 | 4 | $2,217,300.00 | 11 | $2,217,300.00 | 11 |
| FY 2007 |  |  | $87,300.00 | 1 | $660,000.00 | 3 | $747,300.00 | 4 | $747,300.00 | 4 |
| Car Total |  | $2,413,800.00 | 12 | $2,199,900.00 | 14 | $2,202,500.00 | 12 | $6,816,300.00 | 38 | $6,816,300.00 | 38 |
| Grand Total |  | $10,645,500.00 | 63 | $11,001,900.00 | 66 | $10,546,800.00 | 60 | $32,194,200.00 | 189 | $32,194,200.00 | 189 |

**Figure 6: Pivot Grid Control with Pivoted Data**

## Page-level Navigation/TOC (if applicable)

- [Top of Page](#PivotGrid)
- [Overview](#overview)
- [Content](#content)

## Cross References

- See also:
  - C# and VBNet Code Examples
  - Related Features and Properties in the `PivotGrid` Control

## RAG Annotations

<!-- tags: [PivotGrid, Windows Forms, Control, Data Reporting, Version: 11.4.0.26] keywords: [PivotGrid, PivotCalculations, FieldMapping, SummaryType, DoubleTotalSum, Quantity] -->
```