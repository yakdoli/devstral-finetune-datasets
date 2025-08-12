```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_032.jpeg
document_name: diagram
page_number: 032
page_id: diagram#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:08:55Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to add a label to a decision node and style it.
- Positions the decision node on the diagram.
- Creates and styles an orthogonal connector between two nodes.
- Connects a tail node to a head node using the orthogonal connector.

## Content

### Creating a Label for the Decision Node

```csharp
//Add a label to the decision node
label = new Syncfusion.Windows.Forms.Diagram.LabelControl();
label.Text = "Decision";
label.FontStyle.FontFamily = "Arial";
label.FontStyle.Color = Color.White;
decision.Labels.Add(label);
```

### Positioning the Decision Node

```csharp
//Position the decision node
decision.PinPoint = new PointF(250, 250);
//Add decision node to the Model
diagram.Model.AppendChild(decision);
```

### Creating an Orthogonal Connector

```csharp
//Create an orthogonal connector
OrthogonalConnector link =
    new OrthogonalConnector(process.PinPoint,
    decision.PinPoint);
```

### Styling the Link

```csharp
//Style the link
link.LineStyle.LineColor = Color.RosyBrown;
link.LineStyle.LineWidth = 2f;
```

### Configuring the Head Decorator

```csharp
//Head decorator style
link.HeadDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
link.HeadDecorator.Size = new SizeF(8, 8);
link.HeadDecorator.FillStyle.Color = Color.RosyBrown;
link.HeadDecorator.LineStyle.LineColor = Color.RosyBrown;
```

### Connecting Nodes

```csharp
//Connect a tail node to a head node
process.CentralPort.TryConnect(link.TailEndPoint);
//process is tail node
decision.CentralPort.TryConnect(link.HeadEndPoint);
//decision is head node
```

### Adding the Link to the Model

```csharp
//Add a link to the model
```

## API Reference

### Namespaces and Classes
- `Syncfusion.Windows.Forms.Diagram`
  - `Label`
  - `OrthogonalConnector`
  - `Diagram`
  - `PinPoint`
  - `CentralPort`

### Methods
- `AppendChild`: Adds a child node to the diagram model.
- `TryConnect`: Attempts to connect two ports.

## Code Examples

### Complete Example

```csharp
// Add a label to the decision node
Label label = new Label();
label.Text = "Decision";
label.FontStyle.FontFamily = "Arial";
label.FontStyle.Color = Color.White;
decision.Labels.Add(label);

// Position the decision node
decision.PinPoint = new PointF(250, 250);
diagram.Model.AppendChild(decision);

// Create an orthogonal connector
OrthogonalConnector link = new OrthogonalConnector(process.PinPoint, decision.PinPoint);

// Style the link
link.LineStyle.LineColor = Color.RosyBrown;
link.LineStyle.LineWidth = 2f;

// Head decorator style
link.HeadDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
link.HeadDecorator.Size = new SizeF(8, 8);
link.HeadDecorator.FillStyle.Color = Color.RosyBrown;
link.HeadDecorator.LineStyle.LineColor = Color.RosyBrown;

// Connect a tail node to a head node
process.CentralPort.TryConnect(link.TailEndPoint);
decision.CentralPort.TryConnect(link.HeadEndPoint);
```

<!-- tags: [Syncfusion, WinForms, Diagram, Node, Connector, Label, Style] keywords: [Decision node, Orthogonal connector, Tail, Head, LineStyle, DecoratorShape, RosyBrown, PinPoint] -->
```