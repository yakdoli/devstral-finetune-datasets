```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: diagram
page_number: 123
page_id: diagram#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:37Z
fidelity: lossless
-->

## Overview

- This page explains how to create and group nodes using the Syncfusion Windows Forms Diagram.
- Demonstrates the creation of two nodes (`nodeRect` and `nodeRect1`) with custom properties and labels.
- Includes grouping nodes (`grp`) and adding them to the diagram model.

## Content

The following examples showcase how to create and group nodes in a Syncfusion Windows Forms Diagram.

### C#

```csharp
//Node 1
Syncfusion.Windows.Forms.Diagram.Rectangle nodeRect = new Syncfusion.Windows.Forms.Diagram.Rectangle(50, 100, 125, 75);
nodeRect.FillStyle.Color = Color.FromArgb(255, 223, 189);
nodeRect.LineStyle.LineColor = Color.Orange;
Syncfusion.Windows.Forms.Diagram.Label lbl = new Syncfusion.Windows.Forms.Diagram.Label(nodeRect, "Rectangle");
lbl.FontStyle.Size = 12;
lbl.FontStyle.Bold = true;
nodeRect.Labels.Add(lbl);

//Node 2
Syncfusion.Windows.Forms.Diagram.Rectangle nodeRect1 = new Syncfusion.Windows.Forms.Diagram.Rectangle(150, 100, 125, 75);
nodeRect1.FillStyle.Color = Color.FromArgb(255, 223, 189);
nodeRect1.LineStyle.LineColor = Color.Orange;
Syncfusion.Windows.Forms.Diagram.Label lbl1 = new Syncfusion.Windows.Forms.Diagram.Label(nodeRect1, "Rectangle1");
lbl1.FontStyle.Size = 12;
lbl1.FontStyle.Bold = true;
nodeRect1.Labels.Add(lbl1);

//Grouping Nodes
Syncfusion.Windows.Forms.Diagram.Group grp = new Group();
grp.AppendChild(nodeRect);
grp.AppendChild(nodeRect1);
this.diagramControl1.Model.AppendChild(grp);
```

### VB.NET

```vb
'Node 1
Dim nodeRect As Syncfusion.Windows.Forms.Diagram.Rectangle = New Syncfusion.Windows.Forms.Diagram.Rectangle(50, 100, 125, 75)
nodeRect.FillStyle.Color = Color.FromArgb(255, 223, 189)
nodeRect.LineStyle.LineColor = Color.Orange
Dim lbl As Syncfusion.Windows.Forms.Diagram.Label = New Syncfusion.Windows.Forms.Diagram.Label(nodeRect, "Rectangle")
lbl.FontStyle.Size = 12
lbl.FontStyle.Bold = True
nodeRect.Labels.Add(lbl)

'Node 2
Dim nodeRect1 As Syncfusion.Windows.Forms.Diagram.Rectangle = New Syncfusion.Windows.Forms.Diagram.Rectangle(150, 100, 125, 75)
nodeRect1.FillStyle.Color = Color.FromArgb(255, 223, 189)
nodeRect1.LineStyle.LineColor = Color.Orange
```

## Cross References

- See also: [Syncfusion Windows Forms Diagram Documentation](https://www.syncfusion.com/documentation/windowsforms-diagram/)

<!-- tags: [Syncfusion Winforms, Diagram, Nodes, Grouping] keywords: [Syncfusion.Windows.Forms.Diagram, Rectangle, Group, Label] -->
```