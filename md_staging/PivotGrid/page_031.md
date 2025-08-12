<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: PivotGrid
page_number: 031
page_id: PivotGrid#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:36Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Content

Here is the C# code snippet for setting up a PivotGrid control:

```csharp
"Country" }));
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "State" });

// Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName="Amount", Format="C"});
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Quantity", Format = "#,##0" });

// Enabling cell selection
this.pivotGridControl1.AllowSelection = false;
```

### VB

Here is the VB code snippet for setting up a PivotGrid control:

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
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName="Amount", .Format="C"})
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,##0"})
' Enabling cell selection
Me.pivotGridControl1.AllowSelection = False
```

## API Reference

### Properties
- `PivotRows`: Collection of PivotItem for rows.
- `PivotColumns`: Collection of PivotItem for columns.
- `PivotCalculations`: Collection of PivotComputationInfo for calculations.
- `AllowSelection`: Boolean property to enable or disable cell selection.

### Methods
- `Add(PivotItem)`: Adds a PivotItem to the specified collection.
- `Add(PivotComputationInfo)`: Adds a PivotComputationInfo to the calculations.

## Code Examples

### C#
```csharp
pivotGridControl1.PivotRows.Add(new PivotItem { FieldHeader = "Product" });
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "Date" });

// Adding PivotColumns
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "Country" });
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "State" });

// Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName="Amount", Format="C" });
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Quantity", Format = "#,##0" });
```

### VB
```vb
pivotGridControl1.PivotRows.Add(New PivotItem With {.FieldHeader = "Product"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Date"})

' Adding PivotColumns
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Country"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "State"})

' Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName="Amount", .Format="C"})
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,##0"})
```

### RAG Annotations
<!-- tags: [PivotGrid, WindowsForms, syncing data, display settings, cell selection] -->
<!-- keywords: [PivotGrid, PivotRows, PivotColumns, PivotItem, PivotComputationInfo, FieldName, Format, AllowSelection] -->