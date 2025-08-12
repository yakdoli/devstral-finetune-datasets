```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_020.jpeg
document_name: PivotGrid
page_number: 020
page_id: PivotGrid#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:36Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

```vb
Return 1
ElseIf x Is Nothing Then
    Return -1
Else
    Return -x.ToString().CompareTo(y.ToString())
End If
' #End Region
```

## 4.2 PivotComputationInfo

This class holds the information needed for calculations that appear in PivotGrid. For each calculation, there is an associated `PivotComputationInfo` object that is added to the `PivotCalculations` collection. The properties available in the `PivotComputationInfo` are listed in the following table.

### Table 6: Properties Table for PivotComputationInfo

| Property Name | Description | Type | Value it Accepts | Reference link |
|---------------|-------------|------|------------------|----------------|
| CalculationName | Gets or sets what is displayed in the pivot table if more than one calculation is included in the PivotGrid. | string | - | - |
| Description | Gets or sets a description of the calculation. | string | - | - |
| FieldName | Gets or sets the name of the property to be used in this calculation. | string | - | - |
| Format | Gets or sets the format string to be used to format the calculation results in the PivotGrid. | string | - | - |
| Summary | Gets or sets the SummaryBase object that is used to define this | SummaryBase | - | - |

## API Reference (if applicable)

### System.ComponentModel.ISupportInitialize

This section can be added if specific API references are provided in the actual documentation.

## Code Examples (multi-language supported)

### C# Example
```csharp
// Example usage of PivotComputationInfo
PivotComputationInfo computationInfo = new PivotComputationInfo();
computationInfo.CalculationName = "Total Sales";
computationInfo.Description = "Calculates the total sales for each item.";
computationInfo.FieldName = "SalesAmount";
computationInfo.Format = "C2";
computationInfo.Summary = new SummaryBase(); // Initialize appropriate summary type

pivotGridModel.PivotCalculations.Add(computationInfo);
```

### VB.NET Example
```vb.net
' Example usage of PivotComputationInfo
Dim computationInfo As New PivotComputationInfo()
computationInfo.CalculationName = "Total Sales"
computationInfo.Description = "Calculates the total sales for each item."
computationInfo.FieldName = "SalesAmount"
computationInfo.Format = "C2"
computationInfo.Summary = New SummaryBase() ' Initialize appropriate summary type

pivotGridModel.PivotCalculations.Add(computationInfo)
```

## Page-level Navigation/TOC (if applicable)
- [4.2 PivotComputationInfo](#4.2-pivotcomputationinfo)

## Cross References
- See also: Related sections or pages can be added here if they exist in the documentation.

<!-- tags: [pivotgrid, calculation, pivotgridcalculations, winforms, computationinfo] keywords: [pivotgrid, computation, pivot, sum, aggregation, calculation, data] -->
```