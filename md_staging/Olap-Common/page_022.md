```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: Olap Common
page_number: 022
page_id: Olap Common#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:03Z
fidelity: lossless
-->

## Overview
- Explains the `UseWhereClauseForSlicing` property in MDX queries and how it affects slicing operations.
- Demonstrates using the `Drill Through` feature to explore data within the cube.
- Introduces the `OlapReport` object, which contains information about cube elements for processing with filters and sorting constraints.

## Content

### UseWhereClauseForSlicing
| Property Name          | Description                                                                                                                                 | Server side | Type    | Default |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------|---------|
| UseWhereClauseForSlicing | Enables the user to decide whether the MDX Query Parser Engine should consider the 'Where' or 'Select' clause for slicing operation. | Server side | Boolean | ----    |

#### Adding UseWhereClauseForSlicing property to an Application:
Refer to 5.22

### 4.2.3 Drill Through
This feature enables the user to drill through any value and see the data which formed the value.

The following code snippet illustrates how to drill through using MDX Query in OlapDataManager:

#### C# Implementation:
```csharp
string query = @"drillthrough Select { [Customer].[Customer Geography].[Country].[Australia] } on 0, { [Date].[Fiscal].[Fiscal Year].[2002] } on 1 from [Adventure Works] Where [Internet Sales Amount]";
// executing the drill-through operation.
olapDataManager.Execute(query);
```

#### VB Implementation:
```vb
Dim query As String = "drillthrough Select { [Customer].[Customer Geography].[Country].[Australia] } on 0, { [Date].[Fiscal].[Fiscal Year].[2002] } on 1 from [Adventure Works] Where [Internet Sales Amount]"
' Executing the drill-through operation.
olapDataManager.Execute(query)
```

### 4.3 OlapReport
**OlapReport** is an object that contains information about the cube element that has to be included for processing along its axis position and filter and sorting constraints. OlapReport has categorized the elements based on their characteristics as below:
- **Dimension Element**
  - Hierarchy Element
  - Level Element
  - Member Elements
- **Measure Element**
- **KPI Element**
- **NamedSet Element**

## Page-level Navigation/TOC (if applicable)
- Adding UseWhereClauseForSlicing property to an Application
- 4.2.3 Drill Through
- 4.3 OlapReport

## Cross References
- Refer to 5.22 for more details on the `UseWhereClauseForSlicing` property.

<!-- tags: [OlapCommon, MDX Queries, Drill Through, OlapReport, Filters, Sorting Constraints, Dimension Elements, Measure Elements, KPI Elements, NamedSet Elements, Syncfusion Winforms, 11.4.0.26] keywords: [MDX, Cube, Drill Through, OlapDataManager, OlapReport, Dimension Element, Measure Element, KPI, NamedSet Element] -->
```