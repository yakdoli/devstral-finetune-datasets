```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_490.jpeg
document_name: grid
page_number: 490
page_id: grid#page_490
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the functionality of floating cells in the grid control.
- Explains how to prevent certain cells from being flooded.
- Introduces the TabBarSplitterControl feature.

## Content

### Floating Cells Feature

```[VB.NET]
' Enable Float Cells.
Me.gridControl1.FloatCellsMode = GridFloatCellsMode.OnDemandCalculation

' Specify Cell Text.
Me.gridControl1(1, 1).Text = "This is a text that floats over several cells."
Me.gridControl1(3, 1).Text = "This is a text that floats over several cells."
Me.gridControl1(5, 1).Text = "This is a text that floats over several cells."
Me.gridControl1(3, 3).Text = "3.14159"

' Code to prevent cell(5,2) from being flooded.
Me.gridControl1(5, 2).FloodCell = False
Me.gridControl1(2, 2).Font.Bold = True
```

![Figure 188: Floating Cells](https://i.imgur.com/UnZi5yS.png)

### 4.1.4.18 TabBarSplitterControl

#### Description

TabBarSplitterControl enables users to create Tab Pages with dynamic splitters; when used with a grid control, it gives a workbook like appearance. It comes with Office 2007 Style, by default, and supports all the three color schemes.

#### Code Example (C#)

```csharp
this.tabBarSplitterControl.Style = Syncfusion.Windows.Forms.TabBarSplitterStyle.Office2007;
```

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms
- **Class**: TabBarSplitterControl
- **Properties**:
  - **Style**: Sets the style for the TabBarSplitterControl.

## Code Examples (multi-language supported)

### VB.NET Example
```vb
' Enable Float Cells.
Me.gridControl1.FloatCellsMode = GridFloatCellsMode.OnDemandCalculation

' Specify Cell Text.
Me.gridControl1(1, 1).Text = "This is a text that floats over several cells."
Me.gridControl1(3, 1).Text = "This is a text that floats over several cells."
Me.gridControl1(5, 1).Text = "This is a text that floats over several cells."
Me.gridControl1(3, 3).Text = "3.14159"

' Code to prevent cell(5,2) from being flooded.
Me.gridControl1(5, 2).FloodCell = False
Me.gridControl1(2, 2).Font.Bold = True
```

### C# Example
```csharp
this.tabBarSplitterControl.Style = Syncfusion.Windows.Forms.TabBarSplitterStyle.Office2007;
```

## Page-level Navigation/TOC (if applicable)
- 4.1.4.18 TabBarSplitterControl

## Cross References
- Related features: GridControl, TabBarSplitterControl, Floated Cell Support

<!-- tags: [Syncfusion Winforms, TabBarSplitterControl, Grid, Office2007, GridFloatCellsMode] keywords: [FloatingCells, FloodCell, Font.Bold, TabPages, DynamicSplitters, WorkbookAppearance, TabBarSplitterStyle] -->
```