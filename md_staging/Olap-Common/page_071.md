```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_071.jpeg
document_name: Olap Common
page_number: 071
page_id: Olap Common#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:49Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Public Function VirtualKPIReport() As OlapReport
    Dim olapReport As New OlapReport("Virtual KPI Report")
    
    olapReport.CurrentCubeName = "Adventure Works"
    
    Dim measureElements As New MeasureElements()
    measureElements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
    olapReport.CategoricalElements.Add(measureElements)
    
    Dim virtualKPIElement As New VirtualKpiElement()
    virtualKPIElement.Name = "Sample KPI"
    virtualKPIElement.KpiValueExpression = "'Value expression"
    virtualKPIElement.KpiGoalExpression = "'Goal expression"
    virtualKPIElement.KpiStatusExpression = "'Status expression"
    virtualKPIElement.KpiTrendExpression = "'Trend expression"
    virtualKPIElement.StatusGraphic = "'Status graphic"
    virtualKPIElement.TrendGraphic = "'Trend graphic"
    olapReport.VirtualKpiElements.Add(virtualKPIElement)
    olapReport.CategoricalElements.Add(virtualKPIElement)
    
    Dim internalDimension As New DimensionElement()
    internalDimension.Name = "Product"
    internalDimension.AddLevel("Product Categories", "Category")
    olapReport.SeriesElements.Add(internalDimension)
    
    Return olapReport
End Function
```

## Content

The above code snippet demonstrates the creation of a virtual KPI report using the `OlapReport` class in VB. The report is configured to use the "Adventure Works" cube and includes the following elements:

1. **Measure Elements**:
   - A `MeasureElement` named "Internet Sales Amount" is added to the `MeasureElements` collection, which is then added to the `CategoricalElements` of the `OlapReport`.

2. **Virtual KPI Element**:
   - A `VirtualKpiElement` is created and configured with:
     - `Name` set to "Sample KPI".
     - Expressions for `KpiValueExpression`, `KpiGoalExpression`, `KpiStatusExpression`, and `KpiTrendExpression` placeholder expressions.
     - Placeholder expressions for `StatusGraphic` and `TrendGraphic`.
   - The `VirtualKPIElement` is added to both the `VirtualKpiElements` and `CategoricalElements` collections of the `OlapReport`.

3. **Internal Dimension**:
   - A `DimensionElement` named "Product" is created with a level `"Product Categories"` labeled as `"Category"`.
   - The `DimensionElement` is added to the `SeriesElements` collection of the `OlapReport`.

The function returns the configured `OlapReport` object, ready for further processing or display.

## API Reference

### Namespace: `Syncfusion` (Implied)
- **Class**: `OlapReport`
- **Methods**:
  - `Add()`: Used to add elements to the report.
- **Properties**:
  - `CurrentCubeName`: Specifies the name of the current cube.
  - `CategoricalElements`: Collection of categorical elements.
  - `VirtualKpiElements`: Collection of virtual KPI elements.
  - `SeriesElements`: Collection of series elements.
- **Types**:
  - `MeasureElement`
  - `VirtualKpiElement`
  - `DimensionElement`

## Code Examples

The provided VB code snippet is a complete example of how to construct a `VirtualKPIReport` with all necessary elements, including:
- Measure elements.
- Virtual KPI elements.
- Dimension elements.

This structure can be used as a template for creating similar reports.

<!-- tags: [OlapReport, VirtualKPIReport, MeasureElements, VirtualKpiElement, DimensionElement, Syncfusion] keywords: [OlapReport, VirtualKPIReport, MeasureElements, KPI, VirtualKPI, DimensionElement, SeriesElements, CategoricalElements, .NET] -->
```