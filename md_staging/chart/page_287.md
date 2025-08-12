```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_287.jpeg
document_name: chart
page_number: 287
page_id: chart#page_287
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:47Z
fidelity: lossless
-->

## Overview

- Essential Chart for Windows Forms provides detailed configuration settings for PointWidth in Gantt Charts.
- The PointWidth property can be set for series with possible values ranging from 0.0F to 1.0F.
- By default, the PointWidth is set to 1.0F, and it can be applied to any series in a Gantt Chart.
- Code snippets are provided in both C# and VB.NET for setting the PointWidth.

## Content

### Details

| **Possible Values** | **0.0F to 1.0F** |
| **Default Value**   | **1.0F**         |
| **2D / 3D Limitations** | **No**         |
| **Applies to Chart Element** | **Any Series**              |
| **Applies to Chart Types**   | **Gantt Chart**             |

Here is a code snippet using `PointWidth` in a Gantt Chart:

#### Series Wide Setting

**[C#]**

```csharp
ganttSeries.Style.PointWidth = 0.25f;
```

**[VB.NET]**

```vb
Private ganttSeries.Style.PointWidth = 0.25f
```

#### Visual Illustration

The following chart illustrates a Gantt Chart with the default `PointWidth`.

![](Illustrates_PointWidth.png)

**Figure 176: Chart with default PointWidth**

## API Reference

The `PointWidth` property is a float value that can be configured for Gantt Charts in Windows Forms. It applies to series in the Gantt Chart and can be set from 0.0F to 1.0F.

### Parameters

- **Name**: PointWidth
- **Type**: Float
- **Description**: Specifies the width of points in the Gantt Chart.
- **Default**: 1.0F
- **Required**: No

## Code Examples

### C#

```csharp
ganttSeries.Style.PointWidth = 0.25f;
```

### VB.NET

```vb
Private ganttSeries.Style.PointWidth = 0.25f
```

<!-- tags: [Windows Forms, Gantt Chart, Chart, PointWidth, Syncfusion, C#, VB.NET] -->
```