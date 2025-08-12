```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_299.jpeg
document_name: diagram
page_number: 299
page_id: diagram#page_299
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:45Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Provides detailed steps and guidelines for various tasks related to using the Essential Diagram control in Windows Forms.
- Covers topics such as adding ports to custom symbols, highlighting nodes, controlling connection limitations, and manipulating diagram nodes programmatically.
- Explains how to print diagrams, serialize custom properties, and customize user interactions like smoothing edges and protecting links.

## Content

### FAQ for Diagram Operations
- **5.19 How to Get the Nearest Grid Point on a Diagram**: 278
- **5.2 How To Add Ports To A Custom Symbol**: 254
- **5.20 How To Hide Handles Completely From the Nodes**: 279
- **5.21 How To Highlight a Particular Node At Run-time**: 278
- **5.22 How To Move / Place the Nodes Outside the Diagram Model's Bounds**: 282
- **5.23 How To Prevent the Nodes From Being Rotated**: 283
- **5.24 How To Print a Diagram In a Single Page**: 283
- **5.25 How To Programmatically Add a Symbol From the Palette**: 285
- **5.26 How To Programmatically Link Two Symbols**: 285
- **5.27 How To Retain the Custom Position Of the Label While Resizing the Node**: 286
- **5.28 How To Retrieve the Port Information Of a Particular Symbol**: 287
- **5.29 How To Serialize the Custom Property Of a Node**: 288
- **5.3 How To Change the Color Of the LineConnector When Activating the LineTool**: 255
- **5.30 How To Set the Custom Position For a Label**: 289
- **5.31 How To Protect Links From User Selection / Manipulation**: 289
- **5.32 How To Smooth-out the Edges Of the Shapes In a Diagram**: 290
- **5.33 How to Move Nodes on a Diagram Programmatically?**: 291
- **5.34 How to Remove the Gray Area around a Diagram?**: 291
- **5.35 How to Detect whether a Property Value is Changed in the Property Editor?**: 292
- **5.36 How to Add Dynamically Created Symbol Palette to PaletteGroupBar**: 292
- **5.37 How to Get the Undo/Redo Description?**: 293
- **5.38 How to Import Visio Stencil?**: 294
- **5.39 How to Get a Node at a Point or under a Mouse Location?**: 295
- **5.4 How to Change the Selection Mode of the SelectTool**: 257
- **5.5 How To Combine Different Actions Into One Atomic Action To Avoid the Undo Operation On Certain Actions**: 258
- **5.6 How To Control the Number Of Connections That Can Be Drawn From / To the Port**: 259
- **5.7 How To Convert Diagram Node To Any Image**: 259
- **5.8 How To Copy / Paste Nodes In Essential Diagram**: 261
- **5.9 How To Create a Connection Programmatically**: 261

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Diagram
    - **Members**: 
        - LineConnector
        - SelectTool
        - PropertyEditor
        - PaletteGroupBar

## Code Examples
### Example: Adding a Custom Symbol and Linking Nodes
```csharp
// Adding a custom symbol
Diagram diagram = new Diagram();
Node node1 = new Node() { Label = "Node 1" };
Symbol symbol = diagram.SymbolTable["CustomSymbol"];
Node newSymbolNode = diagram.Model.AddDiagramNode(symbol);
diagram.Model.Add(node1);

// Programmatically linking two nodes
Link link = new Link(node1, newSymbolNode);
diagram.Model.Add(link);
```

## Cross References
- See also: Chapter 6 for advanced interaction features.
- Refer to Section 7 for detailed rendering and printing options.

<!-- tags: [Syncfusion, Winforms, Diagram, Essential, Windows Forms, controls, version 11.4.0.26] keywords: [Diagram, Windows Forms, custom symbols, nodes, connections, serialization, property editor, line connector, undo, redo, stencils, palette, diagrams, nodes, links, nodes programmatic movement, user interaction] -->
```