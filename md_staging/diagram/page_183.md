```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_183.jpeg
document_name: diagram
page_number: 183
page_id: diagram#page_183
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:28Z
fidelity: lossless
-->

### Essential Diagram for Windows Forms

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
this.DiagramWebControl1.Model.AppendChild(grp);
```

### 2. Diagram Control Support Two Direct Methods for Grouping and Ungrouping as Follows.

```csharp
// C#
this.diagram1.Controller.Group();  // Method to Group the nodes
this.diagram1.Controller.UnGroup(); // Method to UnGroup the nodes
```

#### How to Access the Child Nodes in a Group, and How to Delete/Remove the Node

- **The First Step is to Check Whether the Node is a Group.**

```csharp
// C#
if (node is Group)
{
    // Your code here
}
```

<!-- tags: [Syncfusion Windows Forms, Diagram, Grouping, Ungrouping, Nodes, Child Nodes, Accessing Nodes, Node Manipulation] keywords: [Syncfusion, Diagram, Group, Ungroup, Child Nodes, Access, Remove, Node] -->
```