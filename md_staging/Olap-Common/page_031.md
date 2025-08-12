```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: Olap Common
page_number: 031
page_id: Olap Common#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:14Z
fidelity: lossless
-->

# Essential OlapCommon

Calculated Member to be defined in OlapReport requires the following definitions:

- **Name** – Name of the calculated member
- **Expression** – Expression to form the calculated member
- **Measure/Dimension Element** – You should add a measure or dimension element from which the calculated member should be created.

The following steps will explain how to create and add a calculated member in an OlapReport:

1. **Create the dimension measure or dimension element** from which the calculated member has to be created.
2. **Create the calculated member** by giving the name and expression.
3. **Add the element created in Step 1** to the calculated member.
4. **Once the calculated member is defined**, add that member to the calculated member collection in an OlapReport.
5. **Add the newly created calculated members** in the categorical or series axis of an OlapReport.

The following code snippet will describe the creation and addition of a calculated member in OlapReport:

## Calculated Measure

### C#

```csharp
MeasureElement measureElement = new MeasureElement();
measureElement.Name = "Order Quantity";

CalculatedMember calculatedMeasure = new CalculatedMember();
calculatedMeasure.Name = "Order on Discount";
calculatedMeasure.Expression = "[Measures].[Order Quantity] + ([Measures].[Order Quantity] * 0.10)";
calculatedMeasure.AddElement(measureElement);
olapReport.CalculatedMembers.Add(calculatedMeasure);
```

### VB

```vb
Private measureElement As MeasureElement = New MeasureElement()
measureElement.Name = " Order Quantity "

Dim calculatedMeasure As CalculatedMember = New CalculatedMember()
calculatedMeasure.Name = " Order on Discount "
calculatedMeasure.Expression = "[Measures].[Order Quantity] + ([Measures].[Order Quantity] * 0.10)"
calculatedMeasure.AddElement(measureElement)
olapReport.CalculatedMembers.Add(calculatedMeasure)
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown.

## Cross References
- See also: bullet list of explicit links/texts present on the page.

## RAG Annotations
- Made up of tags and keywords like {OlapReport, CalculatedMember, OLAP, Expression, MeasureElement, DimensionElement, WinForms, Syncfusion}.
```