```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: diagram
page_number: 065
page_id: diagram#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:37Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Alignment Tool

### Overview
- The Alignment Tool provides multiple options to align selected nodes within a diagram.
- AlignLeft, AlignCenter, AlignRight, AlignTop, AlignMiddle, and AlignBottom are key alignment methods.
- Each method aligns the selected nodes relative to the first node's edges or center.

### Content

#### Alignment Tool Diagram
- The diagram below illustrates the alignment tools and their respective alignment directions.
```markdown
Align Center      Align Top
↑                 ↑
Align Left ← → Align Right → Align Bottom
↑                 ↓
Align Right      Align Middle
```

#### Alignment Tool Description Table
| Tool Name     | Description                                                        | Code Snippet            |
|---------------|--------------------------------------------------------------------|-------------------------|
| AlignLeft     | Aligns the selected nodes along the left edge of the first node. | diagram1.AlignLeft();  |
| AlignCenter   | Aligns the selected nodes along the vertical center of the first node. | diagram1.AlignCenter(); |
| AlignRight    | Aligns the selected nodes along the right edge of the first node. | diagram1.AlignRight(); |
| AlignTop      | Aligns the selected nodes along the top edge of the first node. | diagram1.AlignTop();   |
| AlignMiddle   | Aligns the selected nodes along the horizontal center of the first node. | diagram1.AlignMiddle(); |
| AlignBottom   | Aligns the selected nodes along the bottom edge of the first node. | diagram1.AlignBottom(); |

#### Rotate Tool
- The following screenshot illustrates the Rotate tools. (Screenshot not provided here.)

## Rotating Nodes
- Rotate tools allow transformation of nodes within the diagram. Details about the Rotate tools will be covered in subsequent sections.

## Page-level Navigation/TOC (if applicable)
- Overview
  - Alignment Tool
    - Overview
    - Content
- API Reference (if applicable)
- Code Examples (multi-language supported)
- Cross References

## Cross References
- See also: Node Alignment, DiagramTools, Rotate Tools

<!-- tags: [WinForms, Diagram, Alignment, Rotation] keywords: [diagram, alignment tool, rotate tool, nodes, center, edges, first node] -->
```