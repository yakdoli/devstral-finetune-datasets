```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_165.jpeg
document_name: diagram
page_number: 165
page_id: diagram#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:00Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Explains the use of the ConnectionPoint Collection Editor in managing visual and behavioral properties for connecting elements in a Windows Forms Diagram.
- Demonstrates how to configure ConnectionPoints for shapes to allow for incoming and outgoing connections.

## Content

### ConnectionPoint Collection Editor
The ConnectionPoint Collection Editor is a tool for defining and customizing properties related to connection points in a Windows Forms Diagram. This helps in designing visually appealing and interactive diagrams by specifying how elements connect to each other.

#### Properties
- **Appearance**:
  - **FillStyle**: Specifies the fill color and type (Transparent, Solid, etc.).
  - **LineStyle**: Defines the color, width, and style of the lines.
- **Behavior**:
  - **InheritContainerMeasureUnits**: Indicates whether the connection point inherits the container's measurement units.
  - **MeasureUnit**: Sets the unit of measurement (Pixel, Point, etc.).
- **Misc**:
  - **ConnectionPointSize**: Determines the size of the connection point (Large, Medium, Small).
  - **ConnectionPointType**: Specifies the type of connections (Incoming, Outgoing, or IncomingOutgoing).
  - **ConnectionsLimit**: Limits the number of connections for a connection point.
  - **Name**: Assigns a name to the connection point.
  - **OffsetX**, **OffsetY**: Controls the offset position of the connection point.
  - **Position**: Defines the position within the element (Center, Top, Bottom, Left, Right).
  - **VisualType**: Specifies the visual style of the connection point (XPort, etc.).

#### Sample Diagram
A sample diagram illustrating a rectangle with a connection point is shown below:

```plaintext
+---------------------------------------------+
|                     X                       |
|                                             |
|                   ConnectionPoint            |
|                                             |
+---------------------------------------------+
```

**Figure 99: Rectangle with ConnectionPoint**

### Figure 98: ConnectionPoint Collection Editor
The ConnectionPoint Collection Editor window is shown in the image above, detailing the UI layout and options available for configuring connection points.

## API Reference

### Namespace: `Syncfusion.Windows.Forms.Diagram`

#### Class: `ConnectionPoint`

##### Properties

- **Appearance**
  - **FillStyle**: Determines the fill style for the connection point.
  - **LineStyle**: Defines the line style, including color and width.
  
- **Behavior**
  - **InheritContainerMeasureUnits**: Boolean indicating whether the connection point inherits measure units from its container.
  - **MeasureUnit**: Enumeration specifying the unit of measurement (e.g., Pixel, Point).

- **Misc**
  - **ConnectionPointSize**: Enum to specify the size of the connection point.
  - **ConnectionPointType**: Enum indicating the type of connections allowed (Incoming, Outgoing, or both).
  - **ConnectionsLimit**: Integer specifying the maximum number of connections allowed.
  - **Name**: String for assigning a name to the connection point.
  - **OffsetX**, **OffsetY**: Offset values in X and Y directions for positioning.
  - **Position**: Enum indicating the position within the connected element.
  - **VisualType**: Enum defining the visual style of the connection point.

##### Methods

- **AddConnection()**: Adds a new connection to the connection point.
- **RemoveConnection()**: Removes a specific connection from the connection point.

### Figure 99: Rectangle with ConnectionPoint
This figure illustrates a rectangle containing a connection point with a sample visual representation.

## Code Examples

### Example: Configuring Connection Point Properties

```csharp
using Syncfusion.Windows.Forms.Diagram;

// Create a connection point.
ConnectionPoint connectionPoint = new ConnectionPoint();

// Configure appearance properties.
connectionPoint.FillStyle = new FillStyle(Color.Blue, FillType.Solid);
connectionPoint.LineStyle = new LineStyle(2, Color.Black);

// Configure behavior properties.
connectionPoint.InheritContainerMeasureUnits = true;
connectionPoint.MeasureUnit = UnitType.Pixel;

// Configure miscellaneous properties.
connectionPoint.ConnectionPointSize = Size.Large;
connectionPoint.ConnectionPointType = ConnectionPointType.IncomingOutgoing;
connectionPoint.ConnectionsLimit = 5;
connectionPoint.Name = "ConnectionPoint1";
connectionPoint.OffsetX = 10;
connectionPoint.OffsetY = 10;
connectionPoint.Position = Position.Center;
connectionPoint.VisualType = ConnectionPointVisualType.XPort;
```

### Example: Adding a Connection Point to a Diagram Shape
```csharp
// Assuming a Shape object named 'rectangle' is already created.
rectangle.ConnectionPoints.Add(connectionPoint);
```

## Cross References
See also:
- Diagram Shape Customization
- Working with Diagram Connections

<!-- tags: [Windows Forms, Diagram, ConnectionPoint, ConnectionPointCollectionEditor, VisualStyle, Behavior, Appearance, connections, measureunits] keywords: [ConnectionPoint, LineStyle, FillStyle, ConnectionPointSize, ConnectionPointType, MeasureUnit, InheritContainerMeasureUnits, VisualType, Stroke] -->
```