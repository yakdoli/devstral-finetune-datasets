<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_027.jpeg
document_name: PivotGrid
page_number: 027
page_id: PivotGrid#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:20Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

## Overview
- Filter button - end-users can use it to filter field values

## Content

### Header Areas

The headers of all visible fields are contained within header areas. The headers of row and column fields are displayed within the row header and column header areas, respectively. The headers of data fields are displayed within the data header area.

### Use Case Scenarios

At times, you may expect the Grid to perform sorting and filtering at run-time.

### Adding Grouping Bar

By default, Grouping Bar is enabled. It can be disabled by setting the `ShowGroupBar` property of `PivotGrid` to `False`.

#### Code Examples

##### C#

```csharp
// Instantiating PivotGridControl
PivotGridControl pivotGridControl1 = new PivotGridControl();

// Adding PivotRows
pivotGridControl1.PivotRows.Add(new PivotItem { FieldHeader = "Product" });
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "Date" });

// Adding PivotColumns
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "Country" });
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "State" });

// Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName="Amount", Format="C" });
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Quantity", Format = "#,##0" });
```

##### VB

```vb
' Instantiating PivotGridControl
Dim pivotGridControl1 As PivotGridControl = New PivotGridControl()

' Adding PivotRows
pivotGridControl1.PivotRows.Add(New PivotItem With {.FieldHeader = "Product"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Date"})

' Adding PivotColumns
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Country"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "State"})

' Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Amount", .Format = "C"})
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,##0"})
```

## Page-level Navigation/TOC (if applicable)

This section is not present on the page.

## Cross References

This section is not present on the page.

<!-- tags: [pivotgrid, windowsforms, filterbutton, groupingbar, usecasescenario] keywords: [pivotgrid, windowsforms, filterbutton, groupingbar, sorting, filtering] -->