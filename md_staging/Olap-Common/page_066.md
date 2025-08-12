```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_066.jpeg
document_name: Olap Common
page_number: 066
page_id: Olap Common#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:59Z
fidelity: lossless
-->

Essential OlapCommon

## Overview

- Explains how to customize currentPage and pageSize settings in OlapReport.
- Demonstrates how to implement drill position and drill replace functionalities using MDX queries.
- Provides examples in both C# and VB.NET.

## Content

### 4.3.14 Drill Position

Drill position enables the user to drill into the current position of a selected member in the OlapReport. This excludes the drilled data of the selected member in other positions by using MDX queries.

The following code illustrates how to achieve drill position support in the current report:

**C#**

```csharp
olapDataManager.CurrentReport.PagerOptions.CategoricalCurrentPage = 1;
olapDataManager.CurrentReport.PagerOptions.SeriesCurrentPage = 2;
olapDataManager.CurrentReport.PagerOptions.CategoricalPageSize = 50;
olapDataManager.CurrentReport.PagerOptions.SeriesPageSize = 50;
```

**VB.NET**

```vb
olapDataManager.CurrentReport.PagerOptions.CategoricalCurrentPage = 1
olapDataManager.CurrentReport.PagerOptions.SeriesCurrentPage = 2
olapDataManager.CurrentReport.PagerOptions.CategoricalPageSize = 50
olapDataManager.CurrentReport.PagerOptions.SeriesPageSize = 50
```

### 4.3.15 Drill Replace

Drill Replace displays only the immediate child members and ancestors on drill-down and drill-up respectively.

The following code illustrates how to achieve drill replace support in a current report:

**C#**

```csharp
olapDataManager.CurrentReport.DrillType = DrillType.DrillReplace;
```

**VB.NET**

```vb
olapDataManager.CurrentReport.DrillType = DrillType.DrillReplace
```

<!-- tags: [product, module, control, api, version?] keywords: [OlapReport, PagerOptions, DrillPosition, DrillReplace, MDX, C#, VB.NET] -->
```