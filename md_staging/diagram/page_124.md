```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_124.jpeg
document_name: diagram
page_number: 124
page_id: diagram#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:25Z
fidelity: lossless
--> 

# Essential Diagram for Windows Forms

```vb
Dim lbl1 As Syncfusion.Windows.Forms.Diagram.Label = New Syncfusion.Windows.Forms.Diagram.Label(nodeRect1, "Rectangle1")
lbl1.FontStyle.Size = 12
lbl1.FontStyle.Bold = True
nodeRect1.Labels.Add(lbl1)

' Grouping Nodes
Dim grp As Syncfusion.Windows.Forms.Diagram.Group = New Syncfusion.Windows.Forms.Diagram.Group()
grp.AppendChild(nodeRect)
grp.AppendChild(nodeRect1)
Me.diagramWebControl1.Model.AppendChild(grp)
```

![Selecting a Group in a Diagram](https://i.imgur.com/on0MuBw.png)

*Figure 71: Selecting a Group in a Diagram*

The grouping of nodes can be performed using ready-made API.

```csharp
// Method to Group the nodes
this.diagram1.Controller.Group();

// Method to UnGroup the nodes
this.diagram1.Controller.UnGroup();
```


```vb
' Method to Group the nodes
Me.diagram1.Controller.Group()
```


## API Reference (if applicable)

### Methods
- **Group()**
- **Ungroup()**

## Code Examples

### Grouping Nodes in a Diagram

#### C#

```csharp
this.diagram1.Controller.Group();
```

#### VB

```vb
Me.diagram1.Controller.Group()
```

### UnGrouping Nodes in a Diagram

#### C#

```csharp
this.diagram1.Controller.UnGroup();
```

### Cross References

- See also:
  - [Diagram Operations](#diagram-operations)

### Notes

- Grouping provides a convenient way to manage multiple nodes as a single unit.

<!-- tags: [Syncfusion, Windows Forms, Diagram, Grouping, API] keywords: [Grouping, Ungrouping, Diagram, Nodes, API, Operations] -->
```