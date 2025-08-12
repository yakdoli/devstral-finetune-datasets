```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: Olap Common
page_number: 070
page_id: Olap Common#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:12Z
fidelity: lossless
-->

# Essential OlapCommon

| Property          | Description                              | Type | Data Type |
|-------------------|------------------------------------------|------|-----------|
| VirtualKpiElements | Gets or sets the collection of VirtualKpiElement. | CLR  | Items    |

## 4.3.17.2 Adding Virtual KPI Element to the OlapReport

### OLAP Report Definition with VirtualKpiElement

```csharp
public OlapReport VirtualKPIReport()
{
    OlapReport olapReport = new OlapReport("Virtual KPI Report");
    olapReport.CurrentCubeName = "Adventure Works";

    MeasureElements measureElements = new MeasureElements();
    measureElements.Add(new MeasureElement { Name = "Internet Sales Amount" });

    olapReport.CategoricalElements.Add(measureElements);

    VirtualKpiElement virtualKPIElement = new VirtualKpiElement();
    virtualKPIElement.Name = "Sample KPI";
    virtualKPIElement.KpiValueExpression = ""; //Value expression
    virtualKPIElement.KpiGoalExpression = ""; //Goal expression
    virtualKPIElement.KpiStatusExpression = ""; //Status expression
    virtualKPIElement.KpiTrendExpression = ""; //Trend expression
    virtualKPIElement.StatusGraphic = ""; //Status graphic
    virtualKPIElement.TrendGraphic = ""; //Trend graphic
    olapReport.VirtualKpiElements.Add(virtualKPIElement);
    olapReport.CategoricalElements.Add(virtualKPIElement);

    DimensionElement internalDimension = new DimensionElement();
    internalDimension.Name = "Product";
    internalDimension.AddLevel("Product Categories", "Category");
    olapReport.SeriesElements.Add(internalDimension);

    return olapReport;
}
```

<!-- tags: [product, module, control, api, version?] keywords: [OlapReport, VirtualKPIElement, MeasureElements, DimensionElement, KpiValueExpression, KpiGoalExpression, KpiStatusExpression, KpiTrendExpression, StatusGraphic, TrendGraphic, ProductCategories, Category] -->
```