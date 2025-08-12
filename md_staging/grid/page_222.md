```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_222.jpeg
document_name: grid
page_number: 222
page_id: grid#page_222
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Integrates a Chart control into grid cells by creating a custom Chart Cell type.
- Utilizes the CellModel class for serialization and renderer association.
- Demonstrates implementation using both C# and VB.NET examples.

## Content

### 4.1.4.4.12 Chart Cell

 Essential Chart control can be embedded in grid cells by creating and registering a custom Chart Cell cell type. The **CellModel** class handles any serialization that a cell type requires, and also creates the CellRenderer class associated with the cell type.

The actions mentioned can be performed by using the following code example.

#### 1. Using C#

```csharp
[CSHARP]
ChartStyleProperties csp;
this.gridControl1.CellModels.Add("ChartCell", new GridChartCellModel(this.gridControl1.Model));
style = this.gridControl1[8, 2];
style.CellType = "ChartCell";
csp = new ChartStyleProperties(style);
csp.ChartType = ChartSeriesType.Column;
csp.TitleText = "Chart Cell";
csp.Series3D = false;
csp.TitleAlignment = StringAlignment.Center;
```

#### 2. Using VB.NET

```vbnet
[VB.NET]
Dim csp As ChartStyleProperties
Me.gridControl1.CellModels.Add("ChartCell", New GridChartCellModel(Me.gridControl1.Model))
style = Me.gridControl1(8, 2)
style.CellType = "ChartCell"
csp = New ChartStyleProperties(style)
csp.ChartType = ChartSeriesType.Column
csp.TitleText = "Chart Cell"
csp.Series3D = False
csp.TitleAlignment = StringAlignment.Center
```

## API Reference

- **Methods**
  - `CellModels.Add(string, object)` – Adds a custom cell model to the grid.
  - `ChartStyleProperties` – Initializes a new instance of ChartStyleProperties for configuring cell appearance.
  - `GridChartCellModel` – Represents a model for embedding chart controls in grid cells.

## Code Examples (multi-language supported)

The examples provided demonstrate embedding a Chart control in a grid cell using both C# and VB.NET. These examples include setting the cell type, configuring chart properties, and adjusting the chart's appearance.

## Cross References

See also:
- [4.1.4.4.0 GridModel](#)
- [4.1.4.4.1 Cell Type](#)
- [4.1.4.4.2 CellRenderer](#)

<!-- tags: grid, chart, cellmodel, winforms, syncfusion, version:11.4.0.26 -->
```