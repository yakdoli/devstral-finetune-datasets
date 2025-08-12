```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_209.jpeg
document_name: grid
page_number: 209
page_id: grid#page_209
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:59Z
fidelity: lossless
-->

## Overview

- Demonstrates how to configure and useOLEContainerCell in a GridControl.
- Explains how to display file previews in grid cells.
- Highlightsthe CalculatorTextBox feature with integrated calculator functionality for numerical input.

## Content

### OLEContainer Cell Configuration

The following code snippets illustrate how to configure an OLEContainerCell in a GridControl.

#### C# Implementation

```csharp
OleContainerCell.ToString();
this.gridControl1[rowIndex, colIndex].Description = 
GetIconFile(@"common\Data\DocIO\SalesInvoiceDemo.doc");
```

#### VB.NET Implementation

```vb
RegisterCellModel.GridCellType(this.gridControl1,
CustomCellTypes.OleContainerCell);
Me.gridControl(rowIndex, colIndex).CellType = CustomCellTypes.
OleContainerCell.ToString()
Me.gridControl(rowIndex, colIndex).Description = 
GetIconFile("common\Data\DocIO\SalesInvoiceDemo.doc")
```

#### OLEContainer Cell Example

The following figure depicts the OLEContainerCell in action, showing various icon representations for different file types:

![](https://raw.githubusercontent.com/ColeshawG/article-images/main/syncfusion_sdk/figure_108_grid_ole_container_cell.png)

**Figure 108 Grid OLE Container Cell**

### 4.1.4.4.3 Calculator Text Box

#### Overview

The Calculator Text Box cell type is designed as a drop-down container embedded within a grid cell. This feature provides an integrated calculator for numerical input, which updates the displayed value in the cell.

#### Code Examples for Configuring CalculatorTextBox

The following code examples demonstrate how to set the cell type to `CalculatorTextBox`.

##### Using C#

```csharp
[C#]
```

## API Reference (if applicable)

Details on methods, properties, and events related to `CalculatorTextBox` and `OLEContainerCell` can be found in the Syncfusion GridControl API documentation.

## Code Examples (multi-language supported)

Refer to the preceding sections for code examples in C# and VB.NET regarding the configuration and use of `OLEContainerCell` and `CalculatorTextBox`.

<!-- tags: [OLEContainerCell, GridControl, CalculatorTextBox, Windows Forms, Syncfusion Winforms, 11.4.0.26] keywords: [OLEContainerCell, CalculatorTextBox, GridControl, numerical input, file previews, drop-down container, integrated calculator] -->
```