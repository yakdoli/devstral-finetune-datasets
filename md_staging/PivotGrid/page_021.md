```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: PivotGrid
page_number: 021
page_id: PivotGrid#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:36Z
fidelity: lossless
-->

## Understanding SummaryType and Summary Properties

### Overview
- The SummaryType and Summary properties are crucial for defining calculation types in PivotGrid.
- SummaryType allows selection from predefined calculation options such as Sum, Average, etc., and can also be customized.
- Summary is automatically set for non-custom SummaryType values, requiring a custom SummaryBase-derived object for Custom.

### Detailed Description

| Property         | Description                                                                                                                                                                                                                                                                                                                                 | Enumerations                                                    | Value        |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------------|
| SummaryType      | Gets or sets the SummaryType enumeration for this calculation. Setting it to any value other than Custom will also properly set Summary.                                                                                                                                                                      | DoubleTotal Sum<br>DoubleAverage<br>DoubleMaximum<br>DoubleMinimum<br>DoubleStandardDeviation<br>DoubleVariance<br>Count<br>DecimalTotalSum<br>IntTotalSum<br>Custom | -          |
| Summary          | The Summary property is used to perform specific calculations. This value is automatically set when you specify any non-custom value of SummaryType; if you specify SummaryType.Custom, then you are required to set Summary to be an instance of your custom SummaryBase-derived object. |

## Defining PivotComputationInfo and Code-Behind

### Overview
- The PivotComputationInfo can be defined in C# or VB code.

### 4.2.1 Defining PivotComputationInfo and Code-Behind

#### The PivotComputationInfo can be defined in C# or VB code.

##### C#
```csharp
// Defining PivotComputationInfo
PivotComputationInfo m_PivotComputationInfo = new PivotComputationInfo() { CalculationName="Amount", FieldName="Amount", };
```

### API Reference

#### Naming Properties
- **CalculationName**: Specifies the calculation name to be displayed in the PivotGrid. Example value: "Amount".
- **FieldName**: Specifies the field name to be used in the calculation. Example value: "Amount".

### Code Examples (C#)

```csharp
// Example: Defining a PivotComputationInfo
PivotComputationInfo m_PivotComputationInfo = new PivotComputationInfo() {
    CalculationName = "Amount",
    FieldName = "Amount"
};
```

<!-- tags: [PivotGrid, SummaryType, Summary, PivotComputationInfo, WinForms] keywords: [SummaryType, Summary, Calculation, Custom, DoubleTotalSum, DoubleAverage, DoubleMaximum, DoubleMinimum, DoubleStandardDeviation, DoubleVariance, Count, DecimalTotalSum, IntTotalSum, Custom] -->
```