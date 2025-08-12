<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_583.jpeg
document_name: grid
page_number: 583
page_id: grid#page_583
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:26:05Z
fidelity: lossless
-->

## Overview

- This page explains the functionality of adding extra row and column headers using code, specifically `VB.NET`, within the `Essential Grid` control for `Windows Forms`. 
- Demonstrates handling multiple headers in a grid data-bound grid.
- Highlights the performance capabilities of the `Grid Data Bound Grid`, emphasizing its ability to manage large datasets efficiently.

## Content

### Adding Extra Row and Column Headers

```vb
[VB.NET]

Dim extraRowHeaders As Integer = 1
Dim extraColHeaders As Integer = 1

' Initialize extra row and column headers.
Me.gridDataBoundGrid1.Model.Rows.HeaderCount = extraRowHeaders
Me.gridDataBoundGrid1.Model.Cols.HeaderCount = extraColHeaders
```

The resultant output is shown below.

![Multiple Headers](https://example.com/figure_234.png)
*Figure 234: Multiple Headers*

### Grid Data Bound Grid Performance

#### 4.2.2.16 Grid Data Bound Grid Performance

Essential Grid Data Bound Grid can handle large amounts of data without a performance hit.

## API Reference

- None explicitly mentioned in the provided content.

## Code Examples

```vb
[VB.NET]

Dim extraRowHeaders As Integer = 1
Dim extraColHeaders As Integer = 1

' Initialize extra row and column headers.
Me.gridDataBoundGrid1.Model.Rows.HeaderCount = extraRowHeaders
Me.gridDataBoundGrid1.Model.Cols.HeaderCount = extraColHeaders
```

## Page-level Navigation/TOC

- Adding Extra Row and Column Headers
- Grid Data Bound Grid Performance

## Cross References

Refer to the Grid Data Bound Grid documentation for detailed usage and performance benchmarks.

## RAG Annotations

<!-- tags: [Syncfusion, Winforms, Grid, DataBoundGrid, Windows Forms, Extra Headers, Performance, VB.NET] keywords: [Essential Grid, Grid Data Bound Grid, Multiple Headers, Performance, Windows Forms] -->