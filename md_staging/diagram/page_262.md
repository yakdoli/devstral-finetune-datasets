```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_262.jpeg
document_name: diagram
page_number: 262
page_id: diagram#page_262
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:36Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Typically, symbols and links are connected using the interactive `LinkTool` UI tool or the `LinkCmd` command class.
- Programmatic connection creation is sometimes useful, such as generating diagrams from database data or using custom link tools.
- Direct connections between symbols without intermediate links can also be created.

## Content

### Connecting Symbols with Links

The following code creates a link and connects it to the center ports of two symbols.

```csharp
public Link LinkSymbols(Symbol sym1, Symbol sym2)
{
    Link link = new Link(Link.Shapes.Line);
    sym1.Connect(sym1.CenterPort, link.TailPort);
    sym2.Connect(link.HeadPort, sym2.CenterPort);
    return link;
}
```

```vb.net
Public Function LinkSymbols(ByVal sym1 As Syncfusion.Windows.Forms.Diagram.Symbol, ByVal sym2 As Syncfusion.Windows.Forms.Diagram.Symbol) As LinkLabel.Link
    Dim link As LinkLabel.Link = New LinkLabel.Link(Link.Shapes.Line)
    sym1.Connect(sym1.CenterPort, link.TailPort)
    sym2.Connect(link.HeadPort, sym2.CenterPort)
    Return link
End Function
```

### How To Create a Custom Symbol

#### Section: How To Create a Custom Symbol

The following code sample demonstrates how you can create a custom symbol and use it in Essential Diagram.

1.  Create the custom symbol.

```csharp
// Custom Symbol (MySymbol.cs)
public class MySymbol : Symbol
{
    private Syncfusion.Windows.Forms.Diagram.Rectangle outerRect =
```

## API Reference (if applicable)
<!-- Placeholder for API reference section -->

## Code Examples (multi-language supported)
<!-- Placeholder for code examples -->

## Page-level Navigation/TOC (if applicable)
<!-- Placeholder for page-level TOC -->

## Cross References
<!-- Placeholder for cross references -->

## RAG Annotations
电子产品, November, leverage, comebacks to memo, distanced themselves, colored edit coalition, null, treatment, Chapter 3 and Iran, identified, implemented events and clauses, bit, resolution, debate, MVC 3, like to achieve Gold Manga, St Quint Lincolnshire, since he was figure that functions have very User Diagram, CRL IBM, modal À ses, operating accordingly in, infrastructure apply querycommandvalue API tofu-enabled content that waiting life working list content type, Duration are specified robust that applies momentary dependencies sets, Example (NoteEndNote), services, Core winfsform different bits per word showefts port query different work, navigate DropTreeView1 alpha field video search TeamActivity,
```

```markdown
<!-- tags: [windows-forms, essential-diagram, custom-symbol, linking-symbols, custom-link-tool, diagramming, syncfusion] keywords: [symbols, links, LinkTool, LinkCmd, programmatic connection, custom symbols, custom link tool] -->
```