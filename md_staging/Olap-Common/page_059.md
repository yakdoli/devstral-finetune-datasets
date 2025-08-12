```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: Olap Common
page_number: 059
page_id: Olap Common#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:09Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
'''Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)
olapReport.CategoricalElements.Add(calculatedMeasure1)
olapReport.CategoricalElements.Add(calculatedMeasure2)

'''Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

## 4.3.11.1.11 Report with KPI Element

### [C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Products Sales Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the name for Dimension Element for Column
dimensionElementColumn.Name = "Product";
dimensionElementColumn.AddLevel("Product Categories", "Category");
dimensionElementColumn.Hierarchy.LevelElements["Category"].Add(this.productName);
dimensionElementColumn.Hierarchy.LevelElements["Category"].IncludeAvail
ableMembers = true;

MeasureElements measureElementColumn = new MeasureElements();
// Specifying the name for Measure Element
measureElementColumn.Elements.Add(new MeasureElement { Name = "Gross Pr
ofit" });

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the Name for Row Dimension Element
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

KpiElements kpiElement = new KpiElements();
kpiElement.Elements.Add(new KpiElement { Name = "Revenue", ShowKPIStatu
s = true, ShowKPIGOal = false, ShowKPITrend = true, ShowKPIValue = true
});

// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.CategoricalElements.Add(kpiElement);
```
```