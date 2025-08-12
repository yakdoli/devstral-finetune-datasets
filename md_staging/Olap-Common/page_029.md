```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: Olap Common
page_number: 029
page_id: Olap Common#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:40Z
fidelity: lossless
-->

## Key Performance Indicator (KPI) Element

### Overview
- Key Performance Indicators (KPIs) are collections of calculations associated with a measure group in a cube, used to evaluate business success.
- KPIs typically use MDX expressions or calculated members.
- Metadata is included to guide client application display of KPI results.
- Types include KPI Goal, Status, Trend, and Value.
- KPI elements are created by specifying details like name and the indicators included.

### Content

#### Key Performance Indicator (KPI) Element
Key Performance Indicator (KPI) is a collection of calculations that are associated with a measure group in a cube that are used to evaluate business success. Typically, these calculations are a combination of Multidimensional Expressions (MDX) or calculated members. The KPIs also have an additional metadata that provides information about how client applications should display the results of the KPI's calculations.

The different types of KPI Indicators are:

- KPI Goal
- KPI Status
- KPI Trend
- KPI Value

We can create a KPI element by specifying its name and giving details of the indicator that are included in the element.

#### Code Example in C#

```csharp
KpiElements kpiElement = new KpiElements();

// Specifying the KPI Element name and configuring its Indicators
kpiElement.Elements.Add(new KpiElement { Name = "Internet Revenue", ShowKPIGoal = true, ShowKPIStatus = true, ShowKPIValue = true, ShowKPITrend = true });
```

#### Code Example in VB

```vb
Dim kpiElement As KpiElements = New KpiElements()

' Specifying the KPI Element name and configuring its Indicators
kpiElement.Elements.Add(New KpiElement With { .Name = "Internet Revenue", .ShowKPIGoal = True, .ShowKPIStatus = True, .ShowKPIValue = True, .ShowKPITrend = True })
```

### NamedSet Element

#### Overview
- A named set is a collection of tuples and members defined and saved as part of the cube definition.
- Named sets reside inside the sets folder under a dimension.
- They can be dragged to Categories/Series/Slicer axes in Axes Element Builder.
- MDX allows defining named sets for easier handling of complex expressions.

### Content

#### NamedSet Element
A named set is a collection of tuples and members, which can be defined and saved as a part of the cube definition. Named set records reside inside the sets folder, which is under a dimension element. These elements can be dragged to Categories/Series/Slicer axis of Axes Element Builder. To help make working with a lengthy, complex, or commonly used expression easier, Multidimensional Expressions (MDX) lets you to define a named set.

The following code will describe the creation of a Named set Element:

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- If other pages or sections are referenced in the text, maintain those links or anchor text.
- If cross-referencing is not possible, note explicit links or text references.

## RAG Annotations
<!-- tags: [syncfusion, olap, namedset, kpi, mdx, cubes, winforms, 11.4.0.26] keywords: [key performance indicators, named set, multidimensional expressions, cube, kpi goal, kpi status, kpi trend, kpi value, axes element builder] -->
```