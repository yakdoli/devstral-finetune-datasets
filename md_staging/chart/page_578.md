```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_578.jpeg
document_name: chart
page_number: 578
page_id: chart#page_578
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:47Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
This page describes the process of exporting a chart to a grid using the Syncfusion WinForms library. It includes steps to set up the environment, drag a grid control, and import the necessary namespaces and code to display chart data in a grid.

## Content

### Exporting Chart to Grid
The following steps will guide you through the process of exporting a chart to a grid:

#### Steps to Export Chart to Grid
1. Add the `Syncfusion.Grid.Base` and `Syncfusion.Grid.Windows` assemblies.
2. Add a form (Form2) to hold the Grid control in which the chart is to be exported.
3. Drag a grid control onto the Form2.
4. Add the namespace `Syncfusion.Windows.Forms.Grid` in Form2.

[Code Examples]
```csharp
using Syncfusion.Windows.Forms.Grid;
```

```vb
Imports Syncfusion.Windows.Forms.Grid
```

5. Add the code snippet below in Form2 to get the chart data into the grid.

## API Reference

### Namespaces
- `Syncfusion.Windows.Forms.Grid`

### Classes
- Grid
- Form

## Code Examples

### C#
```csharp
using Syncfusion.Windows.Forms.Grid;
// Add code here to export chart data into the grid
```

### VB.NET
```vb
Imports Syncfusion.Windows.Forms.Grid
' Add code here to export chart data into the grid
```

## Cross References

See also:
- [Other related documentation on charting and grid controls in Syncfusion WinForms]

### Footnote
- The sample code snippets provided are intended to be used in the context of a Windows Forms application.

<!-- tags: [winforms, chart, grid, export, syncfusion, essential chart, essential grid, windows forms] keywords: [chart export, grid control, windows forms, syncfusion, essential chart, essential grid, export chart to grid] -->
```