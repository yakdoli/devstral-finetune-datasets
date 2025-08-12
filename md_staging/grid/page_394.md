```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_394.jpeg
document_name: grid
page_number: 394
page_id: grid#page_394
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:53Z
fidelity: lossless
-->

## Overview

- Drag-and-drop grid control to design the UI.
- Set properties like `RowCount` and `ColCount` either through the designer or by coding.

## Content

### 4.1.4.7.3.2.1 Through Designer

With the designer, you can drag-and-drop the control, size it, and then set a couple of properties.

- Drag a Grid control object from your toolbox and drop it on the form.
- Size and position it.
- Change the `RowCount` and `ColCount` values in the `PropertyGrid` for this control.

---

### 4.1.4.7.3.2.2 Through Code

Given below is the code to help you create a grid.

#### C#

```csharp
using Syncfusion.Windows.Forms.Grid;
....
// Create the Essential Grid.
private GridControl gridControl1;
....
this.gridControl1 = new GridControl();
....
// Set the number of rows and columns.
this.gridControl1.ColCount = 10;
this.gridControl1.RowCount = 100;
....
// Position it on the form.
this.gridControl1.Location = new System.Drawing.Point(20, 20);
this.gridControl1.Size = new System.Drawing.Size(344, 200);
....
// Add it to the forms' controls.
this.Controls.Add(this.gridControl1);
```

#### VB.NET

```vb
imports Syncfusion.Windows.Forms.Grid
....
' Create the Essential Grid.
Private WithEvents gridControl1 As GridControl
....
Me.gridControl1 = New GridControl()
....
' Set the number of rows and columns.
....
```

## API Reference (if applicable)

- **Namespace**: `Syncfusion.Windows.Forms.Grid`
- **Class**: `GridControl`
  - **Properties**:
    - `RowCount`: Gets or sets the number of rows in the grid.
    - `ColCount`: Gets or sets the number of columns in the grid.
    - `Location`: Gets or sets the location of the control.
    - `Size`: Gets or sets the size of the control.

## Code Examples (multi-language supported)

The above sections provide examples in both C# and VB.NET for setting up a grid control.

## RAG Annotations

This section is related to the usage of grid controls in Windows Forms applications using the Syncfusion library.

<!-- tags: [Syncfusion, Windows Forms, GridControl, Designer, Code] keywords: [Grid, RowCount, ColCount, PropertyGrid, ControlPosition, ControlSize, C#, VB.NET] -->
```