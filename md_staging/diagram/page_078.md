```
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_078.jpeg
document_name: diagram
page_number: 078
page_id: diagram#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:13:27Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Provides an overview of working with Symbol Palettes in Diagram Builder.
- Demonstrates adding symbols and customizing their properties in a Windows Forms application.
- Explains the steps to place symbols into the diagram area and save the file with the appropriate extension.

## Content

### Symbol Palettes

The Symbol Palette tool offers a variety of shapes and symbols for designing floor plans and diagrams in Windows Forms applications. Here is a breakdown of the symbols available:

- **FloorPlan Shapes**
  - SquareT...
  - CircularT...
  - Bed
  - SmallPlant
  - HousePlant...
  - LargePlant
  - Sink
  - DoubleD...
  - SingleD...
  - KingSize...
  - SingleDi...
  - ThreeSe...
  - SingleSe...
  - TeaTable
  - Diningta...
  - SideTable
  - Television
  - Dressing...
  - Table
  - RedCar
  - BlueCar
  - FrenchD...
  - Curved...

**Figure 45: Symbol Palette**

### Steps to Use Symbol Palette

1. **Adding Symbols to Associated Palettes**:
   - On placing a symbol into the diagram area, the Diagram Builder displays a dialog for adding the symbol palette into the Associated Palettes.
   - To add the symbol palette, click **OK**.
   - If it is not required, click **Cancel**.

2. **Placing and Customizing Symbols**:
   - Place the symbols in the diagram area as needed.
   - Change their properties according to the requirements.
   - Finally, save the file with the **.edd** extension.

## Code Examples

The following example demonstrates how to programmatically add symbols from the Symbol Palette to a Diagram in a Windows Forms application:

```csharp
using Syncfusion.Windows.Forms.Diagram;

// Create a new Diagram instance
Diagram diagram = new Diagram();

// Load the symbol palette
SymbolPalette symbolPalette = new SymbolPalette();

// Add symbols to diagram
Symbol symbol = symbolPalette.GetSymbol(@"FloorPlanShapes\Bed");
DiagramNode node = diagram.Nodes.Add(new DiagramNode(symbol));

// Customize properties
node.Size = new SizeF(100, 100);
node.Location = new PointF(50, 50);

// Save the diagram
diagram.Save("diagram.edd");
```

## Cross References

- For more information on managing palettes, refer to the [Symbol Palette Management](#symbol-palette-management) section.
- For details on saving and loading diagrams, see the [Diagram File Handling](#diagram-file-handling) section.

## RAG Annotations

<!-- tags: Diagram, Windows Forms, Symbol Palette, FloorPlanShapes, DiagramBuilder keywords: symbol palette, floor plan shapes, associated palettes, property customization, file extension -->
```