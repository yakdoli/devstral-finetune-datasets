```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_259.jpeg
document_name: diagram
page_number: 259
page_id: diagram#page_259
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:18Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

```csharp
this.diagram1.Model.HistoryManager.StartAtomicAction("Custom Action");
this.diagram1.Model.HistoryManager.EndAtomicAction();
```

**[VB.NET]**

```vb.net
Me.diagram1.Model.HistoryManager.StartAtomicAction("Custom Action")
Me.diagram1.Model.HistoryManager.EndAtomicAction()
```

### 5.6 How To Control the Number Of Connections That Can Be Drawn From / To the Port

This can be done using the port's **ConnectionsLimit** property. ConnectionsLimit specifies the number of connections to be allowed. Default value is **10**.

**[C#]**

```csharp
Syncfusion.Windows.Forms.Diagram.ConnectionPoint cp = new
Syncfusion.Windows.Forms.Diagram.ConnectionPoint();
cp.ConnectionsLimit = 12;
```

**[VB.NET]**

```vb.net
Dim cp As New Syncfusion.Windows.Forms.Diagram.ConnectionPoint()
cp.ConnectionsLimit = 12
```

### 5.7 How To Convert Diagram Node To Any Image

To export a single node as an image, use the below code snippet.

**[C#]**

```csharp
Node selectedNode = this.diagram1.Controller.SelectionList[0];
if (selectedNode != null)
{
    //Node size depends on the border line. So we have to calculate the
    //Line width also.
    Bitmap bmp = new Bitmap(Convert.ToInt32(selectedNode.Size.Width +
```

## Page-level Navigation/TOC (if applicable)
- 5.6 How To Control the Number Of Connections That Can Be Drawn From / To the Port
- 5.7 How To Convert Diagram Node To Any Image

### WinForms-specific conventions
- The code examples provided demonstrate how to control the number of connections to/from a port and how to convert a diagram node to an image using C# and VB.NET.

<!-- tags: [Syncfusion Winforms, Diagram, ConnectionsLimit, Node Export, Version 11.4.0.26] keywords: [ConnectionsLimit, Diagram Node Export, WinForms] -->
```