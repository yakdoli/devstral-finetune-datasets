```python
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_081.jpeg
document_name: diagram
page_number: 081
page_id: diagram#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:13:49Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This section demonstrates how to create and customize new flow diagram symbols using the Symbol Designer in Windows Forms.

## Content

### Symbol Designer Overview

#### Figure 49: Symbol Designer With New Symbol
The image depicts the Symbol Designer interface in Windows Forms. The interface includes:
- A **Symbol Palettes** pane on the left, displaying the **Flow Diagram Symbol** category, which contains a symbol named **New Symbol1**.
- A central workspace area showing a grid where shapes can be drawn and customized.
- A rich set of tools and options at the top for drawing, formatting, and editing symbols.
- The toolbar includes options for customization such as color, size, and shape properties.

#### Instructions for Customizing Symbols
- **Draw Shapes**: Use the grid area to draw the desired shapes for your flow diagram symbol.
- **Customize Properties**: Utilize the **Property window** to change the properties of the shapes (Example: Color, Size, etc.).

### Steps to Create and Customize a Symbol

1. **Open Symbol Designer**: Launch the Symbol Designer from within the Windows Forms application.
2. **Select Symbol Palette**: Navigate to the **Symbol Palettes** pane and choose the appropriate category, such as **Flow Diagram Symbol**.
3. **Create New Symbol**: Click to create a new symbol, such as **New Symbol1**.
4. **Draw Shapes**: Use the tools available in the toolbar to draw the desired shapes in the grid area.
5. **Customize Properties**: Use the **Property window** to adjust characteristics like color, size, and other properties of the drawn shapes.

## Code Examples

### Example: Programmatically Creating a New Symbol
```csharp
// Code example demonstrating the creation of a new symbol programmatically.
using Syncfusion.Windows.Forms.Diagram;

// Create a new Symbol instance
Symbol newSymbol = new Symbol();

// Add shapes to the symbol
Shape shape1 = new Shape();
shape1.AddPath(new System.Drawing.Drawing2D.GraphPath());
newSymbol.Shapes.Add(shape1);

// Modify properties of the shape
shape1.FillColor = Color.Blue;
shape1.StrokeColor = Color.Black;
shape1.Size = new Size(50, 50);

// Add the symbol to the document
Diagram diagram = new Diagram();
diagram.Symbols.Add(newSymbol);
```

### Example: Loading a Custom Symbol from File
```csharp
// Code example demonstrating how to load a custom symbol from a file.
using Syncfusion.Windows.Forms.Diagram;

// Load the symbol from a file
Symbol newSymbol = Symbol.LoadFromXml("path_to_symbol_file.xml");

// Add the symbol to the document
Diagram diagram = new Diagram();
diagram.Symbols.Add(newSymbol);
```

## API Reference

### Classes and Methods
- **Symbol**: Represents a symbol in the diagram.
  - **AddPath**: Adds a graph path to the shape.
  - **FillColor**: Sets the fill color of the shape.
  - **StrokeColor**: Sets the stroke color of the shape.
  - **Size**: Sets the size of the shape.
  
- **Diagram**: Represents the main diagram control.
  - **Symbols**: Collection of symbols in the diagram.
  - **Add**: Adds a new symbol to the diagram.

## Cross References
- See also: [Diagram Control Overview](#diagram-control-overview)
- See also: [Symbol Properties and Methods](#symbol-properties-and-methods)

### HTML Comment for Tags and Keywords
<!-- tags: [diagram, windows forms, custom symbols, symbol designer, shape properties] keywords: [draw, customize, properties, shapes, symbol creation, flow diagrams, windows forms] -->
```