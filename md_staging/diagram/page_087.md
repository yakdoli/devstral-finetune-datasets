```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: diagram
page_number: 087
page_id: diagram#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:12:08Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

The image in the document shows a symbolic representation of a Symbol Palette with various symbols labeled as Symbol1, Symbol2, etc., under the heading "Flow Diagram Symbols."

### Overview
- The figure depicts a Symbol Palette with predefined symbols for creating flow diagrams.
- The symbols are visually distinct, indicating their purpose in diagramming tasks.

### Content

#### Symbol Palette Overview
- **Figure 55: Symbol Palette with New Symbols**
  - This figure illustrates a palette containing a set of flow diagram symbols.
    - **Symbol1**: Represented by a green and white triangle.
    - **Symbol2**: Represented by a pink and white cylinder.
    - **Symbol3**: Represented by a pair of yellow and orange directional arrows.
    - **Symbol4**: Represented by a blue and white rectangular block.

#### Saving the Symbol Palette
- **Final Step:** Save the Flow Diagram Symbol Palette.
- **File Format:** The symbols are saved in `.edp` file format.
- **Reusability:** These can be reused in applications and in the Diagram Builder.

## Code Examples

### Example: Creating a Diagram with Custom Symbols
```csharp
// Example usage of the saved symbols in a C# code snippet
Diagram diagram = new Diagram();

// Adding symbols from the saved palette
foreach (var symbol in SymbolPalette.GetAllSymbols())
{
    diagram.Add(symbol);
}

// Saving the diagram for future use
diagram.Save("PathToSave.edp");
```

## Page-level Navigation/TOC (if applicable)
- This section provides a local table of contents or navigational elements for this page, but no such elements are present in the current document.

## Cross References
- See also:
  - "Diagram Builder" for more information on how to use custom symbols.
  - "Flow Diagram Symbols" for additional details on predefined symbols and their usage.

## RAG Annotations
<!-- tags: [Essential Diagram, Windows Forms, Flow Diagram Symbols, Symbol Palette] keywords: [save, reuse, applications, Diagram Builder, edp file format, symbols] -->
```