```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: PivotGrid
page_number: 022
page_id: PivotGrid#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:57Z
fidelity: lossless
-->

## Content

### Adding PivotComputationInfo to PivotCalculations

```csharp
SummaryType = SummaryType.Count;
// Adding PivotComputationInfo to PivotCalculations
this.pivotGrid1.PivotCalculations.Add(m_PivotComputationInfo);
```

```vb
' Defining PivotComputationInfo
Dim m_PivotComputationInfo As PivotComputationInfo = New PivotComputationInfo() With {.CalculationName="Amount", .FieldName="Amount", .SummaryType= SummaryType.Count}
' Adding PivotComputationInfo to PivotCalculations
Me.pivotGrid1.PivotCalculations.Add(m_PivotComputationInfo)
```

### 4.2.2 Format String in PivotComputationInfo

The `PivotComputationInfo` property replaces each format specification in a specified string with the textual equivalent of a corresponding value.

#### Decimal Format

```csharp
// Decimal Format
PivotComputationInfo m_PivotComputationInfo = new PivotComputationInfo() { CalculationName="Total", FieldName="Quantity", SummaryType= SummaryType.Count, Format="0.00"};
```

```vb
' Decimal Format
Dim m_PivotComputationInfo As PivotComputationInfo = New PivotComputationInfo() With {.CalculationName="Total", .FieldName="Quantity", .SummaryType= SummaryType.Count, .Format="0.00"}
```

## Page-level Navigation/TOC (if applicable)
- 4.2.2 Format String in PivotComputationInfo

## Cross References
- See also: [PivotGrid calculations, format strings, value conversion]

<!-- tags: [Syncfusion Winforms, PivotGrid, calculations, format strings, PivotComputationInfo, SummaryType, value conversion] keywords: [C#, VB, decimal format, textual equivalent, calculation name, field name, summary type, format string, value replacement] -->
```