```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: diagram
page_number: 085
page_id: diagram#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:08Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This page explains how to create and manage symbols in the Symbol Palette using Flow Diagram Symbols in Syncfusion Winforms.

## Content

### Symbol Palette with New Symbol

#### Figure: Symbol Palette With New Symbol

The image displays a window with two sections:
1. **Left Section (Symbol Palette):**
   - Title: "Symbol Palettes"
   - Category: "Flow Diagram Symbols*"
   - New Symbol: "New Symbol1" is shown with a small yellow-green triangular shape.

2. **Right Section (New Symbol Design Area):**
   - Title: "New Symbol1"
   - Design Area: A grid layout where a new symbol is being created. The symbol consists of:
     - A green triangular shape at the top.
     - A yellow rectangular shape below the triangle.

### Instructions for Creating More Symbols
- **Repeat Steps 3 to 7:** This suggests that users should follow specific steps outlined in the documentation (not visible on this page) to create more symbols.
- **Grouping Multiple Shapes:** If a symbol is created using more than one shape, all the shapes need to be grouped into a single symbol using the "Group" option available in the symbol designer.

### Notes
- The process of creating symbols involves selecting shapes from the palette and combining them into a single design.
- Grouping ensures that all the component shapes are treated as one unit, simplifying management in flow diagrams.

## Code Examples
```csharp
// Example code for creating a grouped symbol in C#
// This is hypothetical and not directly sourced from the image

Diagram d = new Diagram();
d.Option("GroupShapes");

// Add shapes
Shape shape1 = new Shape("Triangle", "Green");
Shape shape2 = new Shape("Rectangle", "Yellow");

// Group shapes
d.GroupShapes("New Symbol1", shape1, shape2);

// Add grouped symbol to palette
SymbolPalette sp = new SymbolPalette();
sp.Add("New Symbol1");
```

## API Reference
### Methods
- `Option("GroupShapes")`: Enables grouping of multiple shapes into a single symbol.
- `GroupShapes(string symbolName, params Shape[] shapes)`: Groups multiple shapes into a single named symbol.

### Properties
- `SymbolPalette.SymbolItems`: Contains all the symbols available in the palette.

## Page-level Navigation/TOC
- [Symbol Palette with New Symbol](#symbol-palette-with-new-symbol)
- [Instructions for Creating More Symbols](#instructions-for-creating-more-symbols)

## Cross References
- Refer to the full documentation for detailed steps on creating and grouping shapes (steps 3 to 7).
- For more on `SymbolPalette` and `Shape` classes, see the API Reference.

<!-- tags: [WinForms, Syncfusion, Symbol Palette, Flow Diagram Symbols, Group Shapes] keywords: [SymbolPalette, Shape, GroupShapes, Diagram, New Symbol] -->
```