```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_111.jpeg
document_name: diagram
page_number: 111
page_id: diagram#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:13:42Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to create and add shapes and connectors to a diagram using the Syncfusion.Windows.Forms.Diagram library in Windows Forms applications.
- Includes examples in both C# and VB.NET.
- Illustrates the use of `Ellipse`, `Rectangle`, and `LineConnector` classes to design a basic diagram.
- Provides an example of adding these elements to the diagram's model in the `Page_Load` event.

## Content

### Adding Elements to a Diagram

#### C#

```csharp
protected void Page_Load(object sender, EventArgs e)
{
    Syncfusion.Windows.Forms.Diagram.Ellipse ellipse = new Syncfusion.Windows.Forms.Diagram.Ellipse(10, 10, 110, 70);
    Syncfusion.Windows.Forms.Diagram.Rectangle rectangle = new Syncfusion.Windows.Forms.Diagram.Rectangle(250, 50, 50, 80);
    Syncfusion.Windows.Forms.Diagram.LineConnector lineconnector = new Syncfusion.Windows.Forms.Diagram.LineConnector(new System.Drawing.PointF(10, 200), new System.Drawing.PointF(300, 250));
    this.diagram1.Model.AppendChild(ellipse);
    this.diagram1.Model.AppendChild(rectangle);
    this.diagram1.Model.AppendChild(lineconnector);
}
```

#### VB

```vb
Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs)
    Dim ellipse As New Syncfusion.Windows.Forms.Diagram.Ellipse(10, 10, 110, 70)
    Dim rectangle As New Syncfusion.Windows.Forms.Diagram.Rectangle(250, 50, 50, 80)
    Dim lineconnector As New Syncfusion.Windows.Forms.Diagram.LineConnector(New System.Drawing.PointF(10, 200), New System.Drawing.PointF(300, 250))
    Me.diagram1.Model.AppendChild(ellipse)
    Me.diagram1.Model.AppendChild(rectangle)
    Me.diagram1.Model.AppendChild(lineconnector)
End Sub
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Diagram

#### Classes
- **Ellipse**:
  - Represents an ellipse shape in the diagram.
  - **Constructor**:
    ```csharp
    public Ellipse(float x, float y, float width, float height)
    ```
    - **Parameters**:
      - `x`: X-coordinate of the top-left corner.
      - `y`: Y-coordinate of the top-left corner.
      - `width`: Width of the ellipse.
      - `height`: Height of the ellipse.
    
- **Rectangle**:
  - Represents a rectangle shape in the diagram.
  - **Constructor**:
    ```csharp
    public Rectangle(float x, float y, float width, float height)
    ```
    - **Parameters**:
      - `x`: X-coordinate of the top-left corner.
      - `y`: Y-coordinate of the top-left corner.
      - `width`: Width of the rectangle.
      - `height`: Height of the rectangle.
    
- **LineConnector**:
  - Represents a line connector in the diagram.
  - **Constructor**:
    ```csharp
    public LineConnector(PointF sourcePoint, PointF targetPoint)
    ```
    - **Parameters**:
      - `sourcePoint`: Starting point of the line connector.
      - `targetPoint`: Ending point of the line connector.

### Method
- **Model.AppendChild**:
  - Adds a child node to the diagram model.
  - **Signature**:
    ```csharp
    public void AppendChild(Node node)
    ```
    - **Parameters**:
      - `node`: The node (shape or connector) to be added to the model.

## Code Examples

The examples above demonstrate how to create and add basic shapes and connectors to a Syncfusion Windows Forms diagram. The `Page_Load` event is used to initialize the diagram with these elements, ensuring they are displayed when the form is loaded.

### Example Breakdown
1. **Creating Shapes**:
   - An ellipse is created with coordinates and dimensions: `(10, 10, 110, 70)`.
   - A rectangle is created with coordinates and dimensions: `(250, 50, 50, 80)`.

2. **Creating a Line Connector**:
   - A line connector is created between two points: `(10, 200)` and `(300, 250)`.

3. **Adding to the Model**:
   - Each shape and connector is added to the diagram's model using the `AppendChild` method.

## See also
- [Syncfusion Diagram Library Documentation](https://help.syncfusion.com/windowsforms/diagram)
- [Windows Forms Diagram Overview](https://help.syncfusion.com/windowsforms/diagram/overview)

<!-- tags: [Syncfusion, Windows Forms, Diagram, Shapes, Connectors, Page_Load, VB.NET, C#] keywords: [Windows Forms, Diagram, Ellipse, Rectangle, LineConnector, Page_Load, AppendChild] -->
```